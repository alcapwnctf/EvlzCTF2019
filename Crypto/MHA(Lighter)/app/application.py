import os
import helpers
from flask import Flask, flash, redirect, render_template, request, url_for, jsonify, abort, Response, make_response, send_from_directory
from werkzeug.utils import secure_filename

"""
Flask Config
"""
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['DEBUG'] = False
app.secret_key="somethingsomethign"
app.config['DOWNLOAD_FOLDER'] = 'downloads'

@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

FLAG = "evlz{md5_is_lub}ctf"
# Prevent caching
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

"""
    API ROUTES
"""

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/result', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file1' not in request.files and 'file2' not in request.files:
            flash('No Files')
            return redirect(url_for('index'))
        file1 = request.files['file1']
        file2 = request.files['file2']
        # if user does not select a file, browser also
        # submit a empty part without filename
        if file1.filename == '' or file2.filename == '':
            flash('No file selected')
            return redirect(url_for('index'))
        if file1 and file2 and allowed_file(file1.filename) and allowed_file(file2.filename):

            file1.save(os.path.join(app.config['DOWNLOAD_FOLDER'], secure_filename(file1.filename)))
            file2.save(os.path.join(app.config['DOWNLOAD_FOLDER'], secure_filename(file2.filename)))
            
            filename1 = os.path.join(app.config['DOWNLOAD_FOLDER'], secure_filename(file1.filename))
            filename2 = os.path.join(app.config['DOWNLOAD_FOLDER'], secure_filename(file2.filename))          
            
            comparisonResult = helpers.compareImages(secure_filename(file1.filename), secure_filename(file2.filename))

            if(os.path.isfile(filename1)):
            	os.remove(filename1)
            if(os.path.isfile(filename1)):
                os.remove(filename2)
            
            if comparisonResult is True:
                flash(FLAG)
                return redirect(url_for("index"))
            elif comparisonResult == '-1':
                flash("Similar Images")
                return redirect(url_for("index"))

            elif comparisonResult is None:
                flash("Incorrect Input")
                return redirect(url_for("index"))
            else:
                flash("Images Uploaded Successfully")
                flash("Incorrect Result")
                return redirect(url_for('index'))
        else:
            flash("Error!")
            return redirect(url_for('index'))

if __name__ == '__main__':
    # Heroku has a DATABASE_URL environment var for the Database URL
    if os.environ.get('DATABASE_URL') is not None:
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(host='0.0.0.0', port=5000)
