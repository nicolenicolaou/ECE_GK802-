#1η εργαστηριακή ασκηση 
# εισαγωγή απαραίτητων βιβλιοθηκών
import requests  
import time as t 

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
    if "Server" in hdrs:
        print("{:30s} {}".format("Server", hdrs["Server"]))
    else:
        print("unable to find server.\n")

    #ερώτημα b  
    cookies = response.cookies
    if len(cookies) == 0:
        print("This website does not use cookies")
    
    else:
        print("This website uses {} cookies \n".format(len(cookies)))
        #ερώτημα c  
        #ερώτημα c  
        for i in cookies:
            print("Cookie name:", i.name)
            if i.expires is None:
                print("This cookie doesn't expire.")
            else:
                expires_str = t.ctime(i.expires)
                print(f"This cookie expires at: {expires_str}")
