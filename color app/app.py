from flask import Flask, url_for, redirect, render_template, request, abort, jsonify
import hashlib
import requests
import fileinput
import sys

app = Flask(__name__)


@app.route("/")
def trades():
    jsonData = []
    with open('UPT.txt') as f:
        for line in f:
            split_line = line.split(",")
            new_json = {"COIN": split_line[0], "DATE":split_line[1], "URL":split_line[2]}
            jsonData.append(new_json)
        f.closed
    return jsonify(jsonData)


@app.route("/updateTrades", methods=['POST', 'GET'])
def updateTrades():
    if request.method == 'POST':
        coin = request.form.get('coin')
        date = request.form.get('date')
        url = request.form.get('url')
        password = request.form.get('password')
        if isPasswordValid (password):
            with open('UPT.txt', "a") as f:
                f.write("\n"+coin + "," + date + "," + url)
                f.close() 
            return jsonify({"message": "Success"})
        else:
            return jsonify({"message": "Authentication Failure"})

def isPasswordValid(password):
    passd = hashlib.sha256(password.encode(encoding='UTF-8',errors='strict') ).hexdigest()
    if passd == "b4788e9005b1150780694cdaea5b4f345858a24397a74dda6f94a6c200fb2e38":
        return True
    else:
        return False
    



@app.route("/delete", methods=['POST', 'GET'])
def delete():
    print (request.method)
    if request.method == 'POST':
        password = request.form.get('password')
        index = request.form.get('line')
        if isPasswordValid (password):
            with open('UPT.txt') as f:
                lines = f.readlines()
                f.close()
            del lines[int(index)]
            with open('UPT.txt', "w+") as f:
                for line in lines:
                    f.write(line)
            f.close()

            return jsonify({"message": "Success"})
        else:
            return jsonify({"message": "Authentication Failure"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)


