import requests
import random

req = requests.get('https://pastebin.com/raw/vxGkayKY')
lines = req.text.strip().replace('\r','').split('\n\n')
choice = random.choice(lines)

print(choice)
