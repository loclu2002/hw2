import requests

URL = "http://127.0.0.1:5002/"
username = "guest"
password = "password"
your_name = "Lam Bao Loc Lu"  
postmsg = {"inputtext": f"daily message posted by Lam Bao Loc Lu"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'  
}

with requests.Session() as s:
    
    r = s.get(URL, headers=headers)
    print(r)

    userInfo = {"username": username, "password": password}
    r = s.post(URL + "login_action", data=userInfo, headers=headers, allow_redirects=True)
    print(r)

    r = s.post(URL + "homepage_action", data=postmsg, headers=headers, allow_redirects=True)
    print(r)

    r = s.get(URL, headers=headers)
    homepage_content = r.text

    if postmsg["inputtext"] in homepage_content:
        print("Message successfully posted!")
    else:
        print("Message not found on the homepage.")
