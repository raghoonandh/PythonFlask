from flask import Flask, request
from flask import render_template
import json
import pandas as pd
app = Flask(__name__)

 
@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['usernametest'];
    password = request.form['passwordtest'];
    return json.dumps({'status':'OK','user':user,'pass':password});

@app.route('/getdata')
def getdata():
    df = pd.read_csv('test.csv')
    searchword = request.args.get('search', '')
    print '#####', searchword
    return df.to_json(orient="records")

 
@app.route('/signUp')
def signUp():
    return render_template('signup.html')
 
if __name__ == "__main__":
    app.run()


