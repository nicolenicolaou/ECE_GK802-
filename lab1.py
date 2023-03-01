#1η εργαστηριακή ασκηση 
# εισαγωγή απαραίτητων βιβλιοθηκών
import requests  
from datetime import datetime as dt

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input("give a url: ")    # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    
    html = response.text
    more(html)
    
    #ερώτημα a
    hdrs = response.headers
    for key,value in hdrs.items():
        if key=="Server": 
            print("{:30s} {}".format(key,value))
        else:
            print("unable to find server.\n")

    #ερώτημα b          
    cookies=response.cookies
    a=[]
    for key,value in enumerate(response.cookies):
        a.append(key) 

    if len(a)==0:
        print("This website does not use cookies")        
    
    else: 
        print("This website uses {} cookies \n".format(len(a)))
        #ερώτημα c
        for i in cookies:
            print("Cookie name:{}".format(i.name))
    
            if(i.expires==None):
                print("This cookie doesn't expire.\n")
    
            else:
                print("This cookie expires at: {}\n".format(dt.fromtimestamp(i.expires)))
    
