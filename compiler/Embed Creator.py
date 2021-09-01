# -*- coding: utf-8 -*-
import requests
import fade
import time
import os
from pycenter import center
import colorama
from colorama import Fore, Back, Style
import json
from urllib import request
from urllib.error import HTTPError

# Mettre votre description (qui est le message principale ici) 

txt_desc = """
Mettre votre text ICI

"""


embed_text = """
███████╗███╗   ███╗██████╗ ███████╗██████╗      ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
█████╗  ██╔████╔██║██████╔╝█████╗  ██║  ██║    ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══╝  ██║  ██║    ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗
███████╗██║ ╚═╝ ██║██████╔╝███████╗██████╔╝    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   
                
                                    Disocrd : https://discord.gg/PZaC29DqgA                  
                                    Github : https://github.com/Glaxifiak                                                                
"""

os.system('cls')
embed_text = fade.pinkred(embed_text)
print(center(embed_text))

webhooks = input("[?] Webhooks > ") # demande du webhooks

requests = requests.get(webhooks).status_code #test pour savoir si le lien est good

if requests == 200: 
    os.system('cls')
    print(center(embed_text))
    print(f"{Fore.GREEN}[!] Webhooks valide !")
else: 
     while requests != 200:

        import requests
        from pycenter import center
        import colorama
        from colorama import Fore, Back, Style
        


        
        os.system('cls')
        print(f"{Fore.RED}[!] Webhooks invalide\n")
        webhooks = input("[?] Webhooks > ")
        requests = requests.get(webhooks).status_code

        if requests == 200:

            os.system('cls')    
            print(center(embed_text))    
            break

import requests
from colorama import Fore, Back, Style
import json
from urllib import request
from urllib.error import HTTPError


avatar = input(f"{Fore.WHITE}[!] Entrer le liens pour la photos de profils >") # avatar


requests = requests.get(avatar).status_code #test pour savoir si le lien est good

if requests == 200:
    os.system('cls')            
else :
    while requests != 200:

        import requests
        from pycenter import center
        import colorama
        from colorama import Fore, Back, Style

        os.system('cls')
        print(f"{Fore.RED}[!] Lien invalide !\n")
        avatar = input(f"{Fore.WHITE}[?] Lien > ")
        requests = requests.get(avatar).status_code

        if requests == 200:

            os.system('cls')
            break

print(center(embed_text))
name_webhook = input(f"{Fore.WHITE}[?] Entrer le nom de votre bot webhooks > ")
os.system('cls')
print(center(embed_text))
contained = input(f"{Fore.WHITE}[?] voulez vous mettre du contenue au dessus de l'embed (y/n) > ")

if contained == 'n':
    contained1 = ''


if contained == 'y':
    os.system('cls')
    print(center(embed_text))
    contained1 = input(f"{Fore.WHITE}[!] Contenue > ")


title = input(f"{Fore.WHITE}[?] Voulez mettre un titre (y/n) > ")


if title == 'y':
    os.system('cls')
    print(center(embed_text))
    title1 = input(f"{Fore.WHITE}[!] titre > ")
if title == 'n':
    title1 = ''

# -*- coding: utf-8 -*-

desc = input(f"{Fore.WHITE}[?] Voulez vous mettre une description (corp de l'EMBED) (y/n) > ")


if desc == 'y':
    os.system('cls')
    print(center(embed_text))
    if txt_desc != '':
        print(f"{Fore.GREEN}[!] Text bien trouvé !")
    desc1 = txt_desc
    




if desc == 'n':
    desc1 = ''

author = input(f"{Fore.WHITE}[?] Voulez vous mettre un nom d'auteur (y/n) > ")


if author == 'y':
    os.system('cls')
    print(center(embed_text))
    author1 = input(f"{Fore.WHITE}[!] autheur > ")

if author =='n':
    author1 = ''


url = input(f"{Fore.WHITE}[?] Voulez vous mettre un URL (y/n) > ")


if url == 'y':
    os.system('cls')
    print(center(embed_text))
    url1 = input(f"{Fore.WHITE}[!] URL > ")


if url == 'n':
    url1 = ''

import requests

if url == 'y':
    requests = requests.get(url1).status_code #look si le lien et good

    if requests == 200:
        os.system('cls')            
    else :
        while requests != 200:

            import requests
            from pycenter import center
            import colorama
            from colorama import Fore, Back, Style

            os.system('cls')
            print(f"{Fore.RED}[!] Lien invalide !\n")
            url1 = input(f"{Fore.WHITE}[?] Lien > ")
            requests = requests.get(url1).status_code

            if requests == 200:

                os.system('cls')
                break


payload = {

    'content': contained1,
    'username': name_webhook,
    'avatar_url': avatar,
    'embeds': [
        {      
            'title': title1,  
            'description': desc1, 
            'url': url1, 
            'author': {'name' :author1}, 
        },
    ]
}




headers = {
    'Content-Type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}



req = request.Request(url=webhooks,
                      data=json.dumps(payload).encode('utf-8'),
                      headers=headers,
                      method='POST')

try: 
    response = request.urlopen(req) 
    print(f"{Fore.GREEN}Embed bien envoyé !")
    time.sleep(2)
except HTTPError as e:
    print('ERROR') 
    print(e.reason)
    print(e.hdrs)
    print(e.file.read())