from setuptools import setup
import os


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as wr:
	readme=wr.read()

setup(
    name='wuddz_dapp',
    version='1.0.0',
    description='Multi-Purpose ERC20 Dapp, Create Accounts, Check Balances, Make Transactions, Deploy Verify & Interact With Smart \
Contracts, Swap ERC20 Tokens, Interact With Exchange Using Api Authentication, Convert Crypto To Crypto Value & Get Token Prices In USD',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Wuddz_Devs',
    author_email='wuddz_devs@protonmail.com',
    url='https://github.com/wuddz-devs/wuddz_dapp',
    packages=['wuddz_dapp'],
    py_modules = ['wuddz_dapp.dapp', 'wuddz_dapp.dapp_trade', 'wuddz_dapp.dapp_config'],
    install_requires=[
        'ccxt',
        'pycoingecko',
        'requests',
        'setuptools',
        'web3'
    ],
    entry_points={'console_scripts': [
        'wudz-dapp=wuddz_dapp.dapp:cli_main',
        ]},
	classifiers=[
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
    ],
)
