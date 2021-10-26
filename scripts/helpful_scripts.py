from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

#if network is in development use accounts [0] syntax else pull from our config
def get_account():
    #if network were working on is dev or ganache return account 0
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or 
        network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deploying mocks ...")
    #check if we already have a mock deployed, we dont need 2
    if len(MockV3Aggregator) <= 0:
    #to launch remember to add params constructor takes
    #the toWei function will add 18 zeros to our 2000
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from":get_account()})
    #to get MockV3Aggregator addr
    print("Mocks Deployed!")