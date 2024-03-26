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
accountList = []
# Define noOfAccount variable and set it's value to 0


@app.route("/", methods= ["GET", "POST"])
def home():
    global myWallet, account, accountList

    isConnected = myWallet.checkConnection()
    balance = "No Balance"
    if(account):
        balance = 0
   
    return render_template('index.html', isConnected=isConnected,  account= account, balance = balance, accountList=accountList)
   
@app.route("/createAccount", methods= ["GET", "POST"])
def createAccount(): 
    # Access noOfAccount a global variable
    global myWallet, account, accountList
    # Create new account only if the value of noOfAccount is less than 3.
    if 
    
        # Increment the noOfAccount valible by 1 after creation of new account.
    
    else:        
        print("Already acreated 3 accounts!")
    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True, port=4000)
