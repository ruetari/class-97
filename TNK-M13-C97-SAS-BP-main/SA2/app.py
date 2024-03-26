from flask import Flask, render_template
import os
# Import Wallet class
from wallet import Wallet

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

# Create a new Wallet object named myWallet
myWallet = Wallet()

@app.route("/", methods= ["GET", "POST"])
def home():
    # Access myWallet as global
    global myWallet

    # Call checkConnection() method from myWallet and store result in isConnected variable
    isConnected=myWallet.checkConnection()

    # Pass isConnected as isConnected Parameter
    return render_template('index.html',  account=None, balance="No Balance", isConnected = isConnected)


if __name__ == '__main__':
    app.run(debug = True, port=4000)
