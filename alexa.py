#!/usr/bin/python

import os,time,requests,webbrowser,random,sys,threading
from colorama import *

r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA
res = Style.RESET_ALL

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

               _                _____             _    ____                  _
         /\   | |              |  __ \           | |  |  _ \iraniancoders.ir| |
        /  \  | | _____  ____ _| |__) |__ _ _ __ | | _| |_) | ___   ___  ___| |_ ___ _ __
       / /\ \ | |/ _ \ \/ / _` |  _  // _` | '_ \| |/ /  _ < / _ \ / _ \/ __| __/ _ \ '__|
      / ____ \| |  __/>  < (_| | | \ \ (_| | | | |   <| |_) | (_) | (_) \__ \ ||  __/ |
     /_/    \_\_|\___/_/\_\__,_|_|  \_\__,_|_| |_|_|\_\____/ \___/ \___/|___/\__\___|_|
                                  Alexa Rank Booster v1.0
                                  Cod3d by IWHH <3



    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" %(random.choice(colors), line, clear))
        time.sleep(0.05)




def xx(PROXY, url):
    try:
        sess = requests.session()
        sess.proxies = {'http': PROXY}
        sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                        'Cache-Control': 'max-age=0'}
        aa = sess.get('http://' + url, timeout=5, proxies={'http': PROXY})
        if aa.status_code == 200:
            print y + '[' + r + '+' + y + '] ' + g + PROXY + w + ' --> Ok\n'
        else:
            print y + '[' + r + '-' + y + '] ' + g + PROXY + w + ' --> No\n'
    except:
        print y + '[' + r + '-' + y + '] ' + g + PROXY + w + ' --> No\n'


def main():
    try:
        url = sys.argv[1]
        fileproxy = sys.argv[2]
        webbrowser.open("https://t.me/IRCoders")

    except:
        print_logo()
        print m + '\t--------------------------------------------------------'
        print '\t' + y + '[' + r + '!' + y + '] ' + g + 'python ' + w + 'alexa.py ' + g + 'url Proxy_List.txt'
        print '\t' + y + '[' + r + '!' + y + '] ' + m + 'Example -> ' + g + 'python ' + w + 'alexa.py ' + g + 'https://iraniancoders.ir list.txt'
        sys.exit()

    if url.startswith("http://"):
        url = url.replace("http://", "")
    elif url.startswith("https://"):
        url = url.replace("https://", "")
    else:
        pass
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, url))
        t.start()
        thread.append(t)
        time.sleep(0.05)
    for j in thread:
        j.join()

print res
if __name__ == '__main__': main()
