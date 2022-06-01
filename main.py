from sys import stdout
import os
from data.config import *
from colorama import init, Fore, Style, Back
import random
from data.ProxyToolsLib import ProxyTools

init()


def inputf():
    print(Fore.GREEN + f'''
  ╔═══[root@ProxyTools]
  ╚══> ''', end=' ')
    return input().strip().lower()


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_screen():
    clr()

    proxy_tool = ProxyTools()

    stdout.write(Fore.GREEN + f'''
               ╦══╩═════════════MAIN════════════════╩══╦
          {TITLE_TEXT}
                 — {random.choice(welcome_message)}

               ╩══╦══════════════o══════════════════╦══╩
        ╔═════════╩═════════════════════════════════╩═════════╗
                               DELUXE 
          ➡ proxies              |         counts proxies
          ➡ steal                |         steal proxies
          ➡ delete               |         delete proxies
          ➡ check                |         check proxies
          ➡ credits              |         information
          ➡ cwh                  |         check website history  
          ➡ rel/reload           |         reload this win

                   By @JuicexNet for KILLNET_Jacky

        ╠═════════╦══════════════$══════════════════╦═════════╣
               ╦══╩═════════════════════════════════╩══╦

      ''')
    while True:
        cmnd = inputf().lower()
        if cmnd.split()[0] == 'proxies':
            if len(cmnd.split()) == 1:
                res = proxy_tool.count_proxies()
                stdout.write(Fore.GREEN + f"Number of proxies found: " + Fore.MAGENTA + str(res) + Fore.GREEN + "")
            elif cmnd.split()[1] == 'http' or cmnd.split()[1] == 'https':
                res = proxy_tool.count_proxies('http')
                stdout.write(
                    Fore.GREEN + f"Number of HTTP/HTTPS proxies found: " + Fore.MAGENTA + str(res) + Fore.GREEN + "")
            elif cmnd.split()[1] == 'socks' or cmnd.split()[1] == 'socks5' or cmnd.split()[1] == 'socks4':
                res = proxy_tool.count_proxies('socks')
                stdout.write(
                    Fore.GREEN + f"Number of SOCKS5/SOCKS4 proxies found: " + Fore.MAGENTA + str(res) + Fore.GREEN + "")
            else:
                stdout.write(Fore.RED + 'Wrong argument' + Fore.GREEN + "")
        elif cmnd.split()[0] == 'steal':
            if len(cmnd.split()) == 1:
                res = proxy_tool.steal_proxies()
                stdout.write(Fore.MAGENTA + "Steal function is done!" + Fore.GREEN + "")
            elif cmnd.split()[1] == 'http' or cmnd.split()[1] == 'https':
                res = proxy_tool.steal_proxies('http')
                stdout.write(Fore.MAGENTA + "Steal function is done!" + Fore.GREEN + "")
            elif cmnd.split()[1] == 'socks' or cmnd.split()[1] == 'socks5':
                res = proxy_tool.steal_proxies('socks')
                stdout.write(Fore.MAGENTA + "Steal function is done!" + Fore.GREEN + "")
            else:
                stdout.write(Fore.RED + 'Wrong argument' + Fore.GREEN + "")
        elif cmnd.split()[0] == 'delete' or cmnd.split()[0] == 'del' or cmnd.split()[0] == 'remove':
            if len(cmnd.split()) == 1:
                proxy_tool.delete_proxies()
                stdout.write(Fore.MAGENTA + "ALL PROXIES HAS BEEN DELETED!" + Fore.GREEN + "")
            elif cmnd.split()[1] == 'http' or cmnd.split()[1] == 'https':
                proxy_tool.delete_proxies('http')
                stdout.write(Fore.MAGENTA + "HTTP/HTTPS PROXIES HAS BEEN DELETED!" + Fore.GREEN + "")
            elif cmnd.split()[1] == 'socks' or cmnd.split()[1] == 'socks5':
                proxy_tool.delete_proxies('http')
                stdout.write(Fore.MAGENTA + "SOCKS5/SOCKS4 PROXIES HAS BEEN DELETED!" + Fore.GREEN + "")
        elif cmnd.split()[0] == 'check' or cmnd.split()[0] == 'checker':
            ip = input('IP: ')
            # check ip or not
            if ip.count(':') == 1 and ip.count('.') == 3:
                stdout.write(Fore.LIGHTGREEN_EX + "Checking..." + Fore.GREEN + "\n")
                res = proxy_tool.check_proxy(str(ip))
                if res:
                    stdout.write(Fore.MAGENTA + "This proxy is working!" + Fore.GREEN + "")
                else:
                    stdout.write(Fore.RED + "This proxy isn't working!" + Fore.GREEN + "")
            else:
                stdout.write(Fore.RED + 'Wrong argument' + Fore.GREEN + "")
        elif cmnd.split()[0] == 'cwh':
            domain = input('URL: ')
            # check url or not
            if '//' in domain:
                res = proxy_tool.check_site_history(domain)
                if res:
                    for elem in res:
                        stdout.write(f'''
                        
        IP: {elem['ip']}
        LOCATION: {elem['location']}
        OWNER: {elem['owner']}
        LASTSEEN: {elem['lastseen']} 
                        
                        ''')
                    stdout.write(
                        Fore.MAGENTA + f'RECORDS FOUNDED: {len(res)} // viewdns.info/api' + Fore.GREEN)
                else:
                    stdout.write(Fore.RED + 'NO RECORDS FOUNDED :(' + Fore.GREEN + "")
            else:
                stdout.write(Fore.RED + 'Wrong argument' + Fore.GREEN + "")
        elif cmnd.split()[0] == 'credits' or cmnd.split()[0] == 'info':
            while True:
                clr()
                stdout.write(Fore.GREEN + f'''
               ╦══╩═════════════INFO════════════════╩══╦
          {TITLE_TEXT}
                 — {random.choice(welcome_message)}
    
               ╩══╦══════════════o══════════════════╦══╩
        ╔═════════╩═════════════════════════════════╩═════════╗
                             CREDITS :) 
          ➡ coder & idea         |         @JuicexNet
          ➡ team                 |         @Killnet_Jacky
          ➡ support              |         @AuraNetz
          
                type "back" to return to the main menu
    
                   By @JuicexNet for KILLNET_Jacky
    
        ╠═════════╦══════════════$══════════════════╦═════════╣
               ╦══╩═════════════════════════════════╩══╦

                      ''')
                cmnd = inputf().lower()
                if cmnd != 'back':
                    stdout.write(Fore.RED + 'Wrong command. Type "back" to return to the main menu' + Fore.GREEN + "")
                else:
                    clr()
                    welcome_screen()
        elif cmnd == 'rel' or cmnd == 'reload':
            clr()
            welcome_screen()
        else:
            stdout.write(Fore.RED + 'Unknown command' + Fore.GREEN + "")
            welcome_screen()


if __name__ == '__main__':
    welcome_screen()
