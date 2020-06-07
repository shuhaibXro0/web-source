#code by shuhaibXro0
#we are not responsible for any risk on your device

import math
import random

try:
    import requests
except ImportError:
    print('[!] Error: some dependencies are not installed')
    print('Type \'pip install -r requirements.txt\' to install all required packages')
    exit()

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
w='\033[0m'

def banner():
    
    logo="""                                                  
          ##            ##  #####  #####
           ##    ##    ##   #      #    #
            ##  ####  ##    #####  #####
             ####  ####     #      #    #
              ##    ##      #####  #####
           
                                    -ShuhaibXro0 """
    print(random.choice(colors)+logo+w)
    print("\n")


print(banner())
x = str(input('Enter website url:'))
if(x==""):
    print('[!] Error: URL Required')
else:
    x = requests.get(x)
    print(x.text)
