"""
    Admin App For XSSTra
        - arush15june 2019/01/24

    - Blind DOM XSS on Admin Panel.

    - Admin App
        - Port: 8000

"""
import json
from flask import Flask, render_template, url_for, redirect, session
from flask_security import Security, login_required, \
     SQLAlchemySessionUserDatastore, LoginForm, \
     url_for_security, current_user, roles_required
from flask_security.signals import user_registered
from database import db_session, init_db
from models import User, Role

# Create app
app = Flask(__name__, static_url_path='')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_HASH'] = 'plaintext'
app.config['SECURITY_PASSWORD_SALT'] = 'somethingsomething'
app.config['SECURITY_REGISTERABLE'] = False
app.config['SECURITY_CONFIRMABLE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = False

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session,
                                                User, Role)
security = Security(app, user_datastore)

def check_if_exists(MODEL, **kwargs):
    return db_session.query(MODEL.query.filter_by(**kwargs).exists()).first()[0]

# Create a user to test with
@app.before_first_request
def create_user():
    init_db()
    if not check_if_exists(Role, name='admin'): 
        user_datastore.create_role(
            name='admin',
            description='Admin Role'
        )

        user_datastore.create_role(
            name='user',
            description='User Role'
        )
        db_session.commit()

    if not check_if_exists(User, email='admin@admin.com'):
        user = user_datastore.create_user(
            email='admin@admin.com',
            password='3f55af31',
            roles=['admin']
            )
        user_datastore.create_user(
            email='<script>console.log("testscript")</script>@gmail.com',
            password='asdas',
            roles=['user']
        )
        for fake_id in range(1, 50):
            user_datastore.create_user(
                email='user_1{}@gaml.com'.format(fake_id),
                password='asdasd',
                roles=['user']
            )
        db_session.commit()

@user_registered.connect_via(app)
def user_registered_sighandler(app, user, confirm_token):
    default_role = user_datastore.find_role('user')
    user_datastore.add_role_to_user(user, default_role)
    db_session.commit()

@app.context_processor
def login_context():
    return {
        'current_user': current_user
    }

# Views
@app.route('/')
def home():
    return render_template('index.html',
                        url_for_security= url_for_security, 
                        login_form= LoginForm(next=url_for('dashboard')))

@app.route('/dashboard')
@roles_required('admin')
def dashboard():
    user_list = User.query.all()
    return render_template('dashboard.html', user_list=user_list, )

if __name__ == '__main__':
    app.run(port=8000)
