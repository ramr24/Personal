# main.py for flask-calculator

import os

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route("/add", methods=["GET", "POST"])
def add():
    return render_template("add.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
