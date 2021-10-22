import json

from flask import Flask, render_template, url_for, request, redirect, session,jsonify
import web3Func


w = web3Func.Work('https://ropsten.infura.io/v3/537c4c65f5bd41a9bfb65d33948ece9d')
app = Flask(__name__)


@app.route("/how10")
def how10():
    return jsonify(w.getLast10BlockInfo())


@app.route("/how")
def how():
    block = w.getLastBlockInfo("latest")
    print(block)
    return jsonify(block)

if __name__ == "__main__":
    app.run(debug=True)