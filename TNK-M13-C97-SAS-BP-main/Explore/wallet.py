from web3 import Web3

ganacheUrl = "http://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider(ganacheUrl))

# Create Account class
class Account():
    # Declare __init__ method
    def __init__(self):
        # Create an account and store it in self.account
        self.account = web3.eth.account.create()
        # Store address in self.address
        self.address = self.account.address

class Wallet():
    def checkConnection(self):
        if web3.is_connected():
           return True
        else:
            return False
    