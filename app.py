from flask import Flask, render_template, url_for
import os


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/certificate")
def certificate():
    certificates = os.listdir('static/certificate')
    return render_template('certificate.html',certificates=certificates)

if __name__ == "__main__":
    app.run(debug=True)
