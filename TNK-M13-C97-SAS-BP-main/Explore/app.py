from flask import Flask, render_template, request, redirect
import os
from time import time
from wallet import Wallet
from wallet import Account

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

myWallet =  Wallet()
# Define account variable and set it ot None
account = None

@app.route("/", methods= ["GET", "POST"])
def home():
    # Access account as global
    global myWallet, account

    isConnected = myWallet.checkConnection()
    # Create balance variable and set it to "No Balance"
    balance = "No Balance"

    # Check if account exits 
    if(account):
        # Set the balance to 0
        balance = 0
   
    # Pass account and balance in respective attributes
    return render_template('index.html', isConnected=isConnected,  account= account, balance = balance)
   
# Create a rout "/createAccount"
@app.route("/createAccount", methods= ["GET", "POST"])
# Define createAccount() function
def createAccount(): 
    # Access myWallet and account a global
    global myWallet, account
    # Create a new object using Account class and store it in global account variable
    account = Account()
    # redirect to home i.e. "/" path
    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True, port=4000)
