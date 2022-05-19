from os import path, remove
import requests
from data.config import PROXY_RESOURCES
from sys import stdout
from colorama import init, Fore, Style, Back
import urllib.request
import socket
import urllib.error

init()


def steal_proxy_from_api(site, file):
    try:
        data = requests.get(site)
        text_for_parse = data.text
        res = text_for_parse.split()
        with open(f'../{file}.txt', 'a') as proxy_file:
            proxy_file.writelines('\n'.join(res))
        return True
    except Exception as Error:
        return Error


class ProxyTools:
    def __init__(self):
        self.init_files()
        socket.setdefaulttimeout(10)

    @staticmethod
    def init_files():
        if not path.exists('../http.txt'):
            http_file = open('../http.txt', 'w')
            http_file.close()
        if not path.exists('../socks.txt'):
            socks_file = open('../socks.txt', 'w')
            socks_file.close()
        if not path.exists('../proxy.txt'):
            proxy_file = open('../proxy.txt', 'w')
            proxy_file.close()

    @staticmethod
    def count_proxies(px_type=None):
        if px_type is None:
            with open('../proxy.txt', 'r') as http_file:
                http_list = http_file.read().split('\n')
                res = []
                for elem in http_list:
                    if elem.strip() != '':
                        res.append(elem)
                return len(res)
        elif px_type is not None:
            if px_type == 'http' or px_type == 'socks':
                with open(f'../{px_type}.txt', 'r') as http_file:
                    http_list = http_file.read().split('\n')
                    res = []
                    for elem in http_list:
                        if elem.strip() != '':
                            res.append(elem)
                    return len(res)
        else:
            return False

    @staticmethod
    def steal_proxies(px_type=None):
        if px_type is None:
            socks_api = []
            http_api = []
            api_list = []
            for api in PROXY_RESOURCES:
                res = api.split(':')[1]
                if 'socks' in res:
                    socks_api.append(api)
                elif 'http' in res:
                    http_api.append(api)
                api_list.append(api)
            for elem in api_list:
                add = steal_proxy_from_api(elem, 'proxy')
                if add:
                    print(Fore.GREEN + 'SUCCESSFUL ' + Fore.WHITE + elem)
                else:
                    print(Fore.RED + 'FAILURE ' + Fore.WHITE + elem)
            for elem in socks_api:
                add = steal_proxy_from_api(elem, 'socks')
                if add:
                    print(Fore.GREEN + 'SUCCESSFUL ' + Fore.WHITE + elem)
                else:
                    print(Fore.RED + 'FAILURE ' + Fore.WHITE + elem)
            for elem in http_api:
                add = steal_proxy_from_api(elem, 'http')
                if add:
                    print(Fore.GREEN + 'SUCCESSFUL ' + Fore.WHITE + elem)
                else:
                    print(Fore.RED + 'FAILURE ' + Fore.WHITE + elem)
            return True
        if px_type is not None:
            if px_type == 'socks':
                socks_api = []
                for api in PROXY_RESOURCES:
                    res = api.split(':')[1]
                    if 'socks' in res:
                        socks_api.append(api)
                for elem in socks_api:
                    add = steal_proxy_from_api(elem, 'socks')
                    if add:
                        print(Fore.GREEN + 'SUCCESSFUL ' + Fore.WHITE + elem)
                    else:
                        print(Fore.RED + 'FAILURE ' + Fore.WHITE + elem)
            elif px_type == 'http' or px_type == 'https':
                http_api = []
                for api in PROXY_RESOURCES:
                    res = api.split(':')[1]
                    if 'http' in res:
                        http_api.append(api)
                for elem in http_api:
                    add = steal_proxy_from_api(elem, 'http')
                    if add:
                        print(Fore.GREEN + 'SUCCESSFUL ' + Fore.WHITE + elem)
                    else:
                        print(Fore.RED + 'FAILURE ' + Fore.WHITE + elem)
            else:
                return False

    def delete_proxies(self, px_type=None):
        if px_type is None:
            remove('../http.txt')
            remove('../socks.txt')
            remove('../proxy.txt')
            self.init_files()
        elif px_type == 'http' or px_type == 'https':
            remove('../http.txt')
            self.init_files()
        elif px_type == 'socks':
            remove('../socks.txt')
            self.init_files()

    # I Love StackOverflow
    @staticmethod
    def is_bad_proxy(pip):
        try:
            proxy_handler = urllib.request.ProxyHandler({'http': pip})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            req = urllib.request.Request('http://www.example.com')  # change the URL to test here
            sock = urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            #print('Error code: ', e.code)
            return e.code
        except Exception as detail:
            #print("ERROR:", detail)
            return True
        return False

    def check_proxy(self, proxy):
        proxy = str(proxy)
        if self.is_bad_proxy(proxy):
            return False
        else:
            return True
