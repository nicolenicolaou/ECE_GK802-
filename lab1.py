#1η εργαστηριακή ασκηση 
import time
import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = 'http://python.org/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    
    html = response.text
    more(html)
    
    #erotima a
    hdrs = response.headers
    for key,value in hdrs.items():
        if key=="Server": 
            print("{:30s} {}".format(key,value))

    #erotimata b,c 
    for key,value in enumerate(response.cookies): 
        print("{} {}".format(key,int(value.expires - time.time())/86400))
