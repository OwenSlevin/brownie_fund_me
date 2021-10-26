from brownie import FundMe, MockV3Aggregator, network, config
from brownie.network.account import PublicKeyAccount
from brownie.network.main import show_active
from scripts.helpful_scripts import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3



def deploy_fund_me():
    account = get_account()
    #always need a from account section when making a state change to the blockchain
    #now we need to pass feed addr to fundMe contract
    #if we are on a persistent network like rinkeby, use the associated addr,
    #otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
            ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from":account},
        #we use this to reference yaml file instead of hardcoding value
         publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()