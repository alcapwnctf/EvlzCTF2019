"""
    Yararara REST API
    REST API to scan files in pwd using received Yara rule.
"""

import os, glob
from base64 import b64encode, b64decode

from flask import Flask, request, make_response, render_template
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful_swagger import swagger

import yara

SCAN_DIRECTORY = './files'

"""
    Flask Config
"""
app = Flask(__name__)
app.config.from_object(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = swagger.docs(Api(app), apiVersion='0.1')
limiter = Limiter(
    app,
    key_func=get_remote_address,
)

"""
    Helpersglob.glob(os.path.join(directory, '*'))
"""

class InvalidYaraRuleError(Exception):
    pass

class InvalidDirectoryError(Exception):
    pass

class InvalidFileError(Exception):
    pass

class YaraDirectoryScanner(object):
    """
        Scan a directory with a provided yara rule source.
        Append matches as file names to self.matches.
    """
    def __init__(self, rule, *args, **kwargs):
        # Check if rule is valid
        try:
            self.rule = yara.compile(source=rule)
        except:
            raise InvalidYaraRuleError()

        self.directory = kwargs.get('directory', SCAN_DIRECTORY)
        self.matches = []

    @staticmethod
    def read_file(file_path):
        """
            Read file from file_path
        """
        try:
            with open(file_path) as f:
                data = f.read()
        except:
            raise InvalidFileError()
        return data

    @staticmethod
    def list_files(directory):
        """
            Return all files in directory as a list.
        """
        try:
            file_list = glob.glob(os.path.join(directory, '*'))
            return file_list
        except:
            raise InvalidDirectoryError()

    def scan_directory(self, *args, **kwargs):
        """
            Scan self.directory with compiled YARA rule self.rule
            and return matched files.
        """
        file_list = self.list_files(self.directory)
        match_list = []
        
        for file in file_list:
            try:
                file_data = self.read_file(file)
            except InvalidFileError:
                continue

            yara_match = self.rule.match(data=file_data)

            if len(yara_match):
                match_list.append(os.path.basename(file))
        
        self.matches = match_list
        return match_list

"""
    Resources
"""

class YaraScanner(Resource):
    """
        Scan files in SCAN_DIRECTORY using Yara Rule 'rule'.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('rule', required=True, type=str)

    def post(self):
        args  = self.parser.parse_args()
        
        # Get Yara Rule from parser
        yara_rule = args['rule']
        yara_rule = b64decode(yara_rule).decode()
        
        # Directory Scanner
        try:
            scanner = YaraDirectoryScanner(yara_rule)
            # Scan Directory and Get Matches
            matches = scanner.scan_directory()
        except InvalidYaraRuleError:
            return abort(400, message='Invalid Rule')
        except:
            return abort(400, message="Couldn't Perform Scan")

        response = {
            'matches': matches
        }
        return response

class ReadFile(Resource):
    """
        Read file 'file' from SCAN_DIRECTORY.
    """
    
    decorators = [
        limiter.limit('2 per 10 seconds')
    ]

    parser = reqparse.RequestParser()
    parser.add_argument('file', required=True, type=str)

    def post(self):
        args = self.parser.parse_args()

        # get filename from parser
        filename = args['file']
        filename = b64decode(filename).decode()

        # Try to read the file
        try:
            with open(os.path.join(SCAN_DIRECTORY, filename)) as f:
                filedata = f.read()
        except:
            return abort(400, message="Failed to read file")

        encoded_data = b64encode(filedata.encode()).decode()

        response =  {
                'data': encoded_data
            }        

        return response

class ListDirectory(Resource):
    """
        List files in SCAN_DIRECTORY
    """
    def get(self):
        file_list = glob.glob(os.path.join(SCAN_DIRECTORY, '*'))
        # keep basename only
        file_list = [os.path.basename(file) for file in file_list]
        
        response = {
            'directory': file_list   
        }

        return response

"""
    Routes
"""
api.add_resource(ReadFile, '/api/readfile')
api.add_resource(YaraScanner, '/api/scan')
api.add_resource(ListDirectory, '/api/listdir')

if __name__ == "__main__":
    app.run(debug=True)