from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

# connect to the Binance Smart Chain network using a Web3 provider
web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org'))

# add the PoA middleware to the Web3 instance
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# define a decimal number
decimal_number = 0
df = open('validones.txt', 'w')
while decimal_number <= 133008264150669715016115996729831652625286932523905794926276832833269408171:
    # convert the decimal number to a hexadecimal string with 64 positions
    hex_string = '0x'
    hex_string += '{:0>64}'.format(hex(decimal_number)[2:])
    try:
        # create an account object from the private key
        account = Account.from_key(hex_string)
        # print the account address
        amount = web3.eth.get_balance(account.address)
        if amount > 0:
            df.write(f"{hex_string} -- balance {str(amount)} wei\n")
            print(f'Found {account.address} -> ({hex_string}) with a balance of ' + str(amount) + ' wei')
        else:
            print(f'{account.address} -> ({hex_string})')
    except Exception as e:
        print(e)
        continue
    decimal_number += 1

