import argparse
import requests, json
import sys
from sys import argv
import os
import time

# dx arguments andparser

parser = argparse.ArgumentParser()

parser.add_argument ("-dx", help= " target IP/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

os.system("clear")

# dx color
r = '\033[31m'
y = '\033[93m'
l = '\033[92m'
c = '\033[0m'
b = '\033[01m'
Cc = '\033[96m'

# dx Symbol
X = '\033[1;32m[\033[1;00mム\033[1;32m]\033[1;00m'
D = '\033[1;32m[\033[1;00m〄\033[1;32m]\033[1;00m'
E = '\033[1;32m[\033[1;00m×\033[1;32m]\033[1;00m'
A = '\033[1;32m[\033[1;00m+\033[1;32m]\033[1;00m'
CD = '  \033[1;32m[\033[1;00m</>\033[1;32m]\033[1;00m'
lm = '\033[96m▱▱▱▱▱▱▱▱▱▱▱▱\033[0m〄\033[96m▱▱▱▱▱▱▱▱▱▱▱▱\033[0m'

# dx sprint
def sprint(sentence, second=0.05):
    for word in sentence + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(second)

# dx banner
print ("\n")
print (f"{Cc}")
print (f"{Cc}        ██████╗ ██╗  ██╗     ██╗██████╗")
print (f"{Cc}        ██╔══██╗╚██╗██╔╝     ██║██╔══██╗")
print (f"{Cc}        ██║  ██║ ╚███╔╝█████╗██║██████╔╝")
print (f"{Cc}        ██║  ██║ ██╔██╗╚════╝██║██╔═══╝")
print (f"{Cc}        ██████╔╝██╔╝ ██╗     ██║██║")
print (f"{Cc}        ╚═════╝ ╚═╝  ╚═╝     ╚═╝╚═╝{c}")
print (f"{y}           +-+-+-+-+-+-+-+-+-+")
print (f"{Cc}           |Student|-|hacker|-|team|")
print (f"{y}           +-+-+-+-+-+-+-+-+-+{c}")
print ("\n")


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        print (f"  {D}{Cc}||Victim||{CD} ", data['query'])
        print(f"  {lm}")
        print (f"  {D}{y}||ISP||{CD} ", data['isp'])
        print(f"  {lm}")
        print (f"  {D}{Cc}||Time Zone||{CD} ", data['timezone'])
        print(f"  {lm}")
        print (f"  {D}{y}||City||{CD} ", data['city'])
        print(f"  {lm}")
        print (f"  {D}{Cc}||Region||{CD} ", data['region'])
        print(f"  {lm}")
        print (f"  {D}{y}||Longitude||{CD} ", data['lon'])
        print(f"  {lm}")
        print (f"  {D}{Cc}||Latitude||{CD} ", data['lat'])
        print(f"  {lm}")
        print (f"  {D}{y}||Country||{CD} ", data['country'])
        print(f"  {lm}")
        print (f"  {D}{Cc}||Zip code||{CD} ", data['zip'])
        print(f"  {lm}")
        print (f"  {D}{y}||Region Name||{CD} ", data['regionName'])
        print (" "+Cc)

except KeyboardInterrupt:
        sprint(CD+" \033[96mThanks for using. \033[93mExiting Tools, \033[92mBye (^_^)\033[0m")
        sys.exit()
except requests.exceptions.ConnectionError as e:
        sprint(CD+" \033[96mPlease Check Your Internet Connection¡ \033[31m(T_T)\033[0m")
sys.exit(1)
I'd