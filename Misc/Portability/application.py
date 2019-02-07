"""
    An App For My Love.
"""

import os
from flask import Flask, request, flash, redirect, url_for, jsonify

"""
    App
"""
app = Flask(__name__)

"""
    Secret Key
"""
app.secret_key = "pm77p~'G{Fh=RrGx!j`R&cPFk-5FH`hk"

"""
    Flag
"""
FLAG = os.getenv("FLAG", "evlz{}ctf")


@app.route('/beauty', methods=["GET"])
def beauty():
    return jsonify({
        'flag': FLAG
    })


if __name__ == '__main__':
    app.run(debug=True)