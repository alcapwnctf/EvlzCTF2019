from flask import Flask, request, make_response
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS

"""
    Flask Config
"""

app = Flask(__name__)
app.config['DEBUG'] = False
app.secret_key = "@@@H4CKTOBERFEST_DSC_BVP@@@"

cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

"""
    Resources
"""

class EnumerationResource(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('help', type=str, required=True)

    def get(self):
        args = self.get_parser.parse_args()
        help_arg =  args['help']

        response = 'NOPE'

        if(help_arg == 'Ǒ'):
            response = 'evlz{enumeration_args}ctf'
            response = make_response(response, 200)
            return response

        response = make_response(response, 202)
        return response


api.add_resource(EnumerationResource, "/enumerate")

if __name__ == "__main__":
    app.run(debug=True)
        
        
