from flask import Flask, render_template, request, redirect
import os
from time import time
from wallet import Wallet
from wallet import Account

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

myWallet =  Wallet()
account = None
# Create a list to store all the accounts.


@app.route("/", methods= ["GET", "POST"])
def home():
    # Access accountList as global
    global myWallet, account

    isConnected = myWallet.checkConnection()
    balance = "No Balance"

    if(account):
        balance = 0
   
    # Pass accountList as attributes
    return render_template('index.html', isConnected=isConnected,  account= account, balance = balance)
   
@app.route("/createAccount", methods= ["GET", "POST"])
def createAccount(): 
    # Access accountList as global
    global myWallet, account, noOfAccount
    account = Account()
    # Append the the created account in the accountList

    
    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True, port=4000)
