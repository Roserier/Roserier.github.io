import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

@app.route('/api',methods=['GET'])
def main():
    return jsonify({'hasil' : 'HAHA','status':'1'})


if __name__ == '__main__':
    app.run(debug=False")
