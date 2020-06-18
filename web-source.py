#coded by shuhaibXro0
#we are not responsible for any risk on your device

from banner import banner
import math
import random

try:
    import requests
except ImportError:
    print('[!] Error: some dependencies are not installed')
    print('Type \'pip install -r requirements.txt\' to install all required packages')
    exit()

def detail():
    print('''
#coded by shuhaibXro0
#we are not responsible for any risk on your device''')

def func(x):
    print('Requesting ',x,'...')
    print('Collecting data...')
    x = requests.get(x)
    print(x.text)
    print('Done.')

banner()
x = str(input('Enter website url:'))

if(x==""):
    print('[!] Error: URL not specified')
    exit()
    
y = input('do you want to continue? (y/n):')

if y == 'y':
    func(x)
elif y == 'n':
    detail()
