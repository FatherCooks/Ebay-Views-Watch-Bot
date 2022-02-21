
global signup_URL
global signIn_URL

signup_URL = "https://signup.ebay.com/ajax/submit"
signIn_URL = "https://www.ebay.com/signin/s"
signIn_session = "https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F"


class Headers():
    pass 

    getSession = {
    'authority': 'signup.ebay.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.ebay.com/',
    'accept-language': 'en-US,en;q=0.9',
}
    
    accountCreate = {
    'authority': 'signup.ebay.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json',
    'x-ebay-requested-with': 'XMLHttpRequest',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://signup.ebay.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://signup.ebay.com/pa/crte?ru=https%3A%2F%2Fwww.ebay.com%2F',
    'accept-language': 'en-US,en;q=0.9',
    }
    
    signIn = {
    'authority': 'www.ebay.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    #'sec-ch-ua-full-version': '"97.0.4692.71"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-model': '""',
    'upgrade-insecure-requests': '1',
    'origin': 'https://signin.ebay.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://signin.ebay.com/',
    'accept-language': 'en-US,en;q=0.9',
    }
    
    signIn_sess = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
}
    
    addViews = {
    'authority': 'www.ebay.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-full-version': '"97.0.4692.99"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-model': '""',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9'
    }
    
    login = {
    'authority': 'www.ebay.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://signin.ebay.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://signin.ebay.com/',
    'accept-language': 'en-US,en;q=0.9',
    #'cookie': 'ak_bmsc=10EEAD646C1F04335A28D0E279863552~000000000000000000000000000000~YAAQT3QyF7qJTAF/AQAA0mMxFA4zadJPBDqWdyjYrNZgJhhI71sAbnkRdVB/w/cTAZZwSqVtxRZLclsMMTSqheGffjj2pLEeW/f+Tyk6D/zdk7VZwX1uCOokC+yOJDBBhV2AuBbk55Ll0plD7jYuqE6Tsnh9Sbf3JvaAkENi91qcmhmcFVxMe2F9MXPKtUVKRCzVww5sR18OzVhD4BRi8RSJWzMbmN9oFgOhgF12dg+WOVR2NknkLO4NIsPsaduoAj16dzggENwPTAOfdIKqxp0/BUXQRY/piwa4wqK+iqmbm76ZjMgzAVHOSICRt6ewgYYodEVzxQ8GF2H0tYgrPXqahOO/gVqlomGxgSqFxrfUxWChDv6kFfHasWzjO2Bd8ZZvcPHjFAx1UQ==; __uzma=02945e77-e198-4554-b0fa-6f9a454d55d5; __uzmb=1645311256; __uzme=9039; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=00954ae7-04f6-4ee3-8f16-7963b3c94b82; __uzmbj2=1645311256; __gads=ID=d62c03c1c726c917-22f4adba26d000e5:T=1645311256:S=ALNI_Mah742xOv3Tkv9Jm4ofB2sBw0M_vQ; cid=kksv39hshzdRf6bG%231630848009; __uzmcj2=298211334183; __uzmdj2=1645311275; s=CgAD4ACBiEsarMTQzMTYzNTUxN2YwYWFlY2M4MmMwM2M5ZmZmMjM4YmW++0VP; ebay=%5Ejs%3D1%5Esbf%3D%23000000%5E; bm_sv=5E4730C6D8C118220F9EE9EE8289DA2B~LNznjFF22+Iad0vc4UDQSoOOL4xBX3OMTUoDFg70/Bp8yJstCr5CyW1ejMGHjBT0TGJrz8LhDBlc9tAZe/MiLjAL9ymFQcTqgbYd9s9oGRZEQ9iZfvPphenx+06OJmXvsNtbh24hCC4NcaJHnBYKHA==; npii=btguid/1431635517f0aaecc82c03c9fff238be65d3dc56^cguid/1431657c17f0a7b0b307c2f1ffdab78665d3dc56^; dp1=bu1p/QEBfX0BAX19AQA**65d3dc56^pbf/%23e000e0000000000000000063f2a8d6^tzo/1a46211833b^bl/US65d3dc56^; nonsession=BAQAAAX42/BiUAAaAADMABWPyqNYzMzYzNwDKACBl09xWMTQzMTYzNTUxN2YwYWFlY2M4MmMwM2M5ZmZmMjM4YmUAywACYhF8XjE5AocI4vSG3uFnk5NUR4REep8nMlM*; __uzmc=829781680527; __uzmd=1645311318; __uzmf=7f6000b59a442b-efa1-47a4-8907-73ebd6e8a7c7164531125642961910-b69141d05e7c83e816',
}



    



