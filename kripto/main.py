import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
    return jsonify({'hasil' : 'HAHA','status':'1'})
