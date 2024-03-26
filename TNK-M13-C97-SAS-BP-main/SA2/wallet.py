from web3 import Web3

# Create a variable ganacheUrl and set it to "http://127.0.0.1:7545" 
ganacheUrl="HTTP://127.0.0.1:7545"
# Use Web3 to create a new object named web3. Pass Web3.HTTPProvider(ganacheUrl) as parameter
web3 = Web3(Web3.HTTPProvider(ganacheUrl))

# Create Wallet class
class Wallet():
    # Define checkConnection method
    def checkConnection(self):
        # Check if web3.is_connected() is true
        if web3.is_connected():
           # Return True
           return True
        # Else
        else:
           # Return False
           return False
    