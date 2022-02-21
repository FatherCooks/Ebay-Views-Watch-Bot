import random
import re
import requests


def get_proxies():

    # Load proxy from file
    with open(f'D:\Scripts\Python\A Ma Maniere\Config\proxies.txt', "r") as file:
        proxies = file.readlines()
    if len(proxies) > 0:
        line = proxies[random.randint(0, len(proxies) - 1)].strip().split(":")
        if len(line) == 2:  # if proxy length is ==2, its an IP Auth proxy
            formatted_proxy = ":".join(line)
            proxy = {
                'http': f'http://{formatted_proxy}',
                'https': f'https://{formatted_proxy}',
            }

        else:  # if proxy length is anything else, its an USER:PASS
            formatted_proxy = f'{line[2]}:{line[3]}@{line[0]}:{line[1]}'
            proxy = {
                'http': f'http://{formatted_proxy}',
                'https': f'https://{formatted_proxy}'
            }
    else:
        proxy = {}
    
    #print(proxy)
    #a = requests.get("https://www.ipchicken.com/", proxies=proxy)
    #print(a.text)
    return proxy

    print(proxies)
    return proxies
    
if __name__ == '__main__':

    
    get_proxies()