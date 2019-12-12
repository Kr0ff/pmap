#!/usr/bin/python
import sys
import time
from datetime import datetime
from socket import *
from os import system, name

ascii = """

 _______  _______  _______  _______   
(  ____ )(       )(  ___  )(  ____ )  
| (    )|| () () || (   ) || (    )|  
| (____)|| || || || (___) || (____)|  
|  _____)| |(_)| ||  ___  ||  _____)  
| (      | |   | || (   ) || (        
| )      | )   ( || )   ( || )        
|/       |/     \||/     \||/         
                                      
        Python port scanner !
"""

target = ''
maxp = 65536
minp = 20


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def scan(target, port, response = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((target,port))
        if code == 0:
            response = code
        s.close()
    except Exception as e:
        pass
    return response

def gettargetinfo():
    try:
        target = input("[*] Enter target IP address: ")
    except KeyboardInterrupt:
        print("\n\n[*] Program Terminated !")
        sys.exit(1)

    target_hostname = gethostbyname(target)
    print("\n[*] Target IP: {} & Target hostname: {}".format(target_hostname, target))
    print("[*] Starting scan at {} ....\n".format((time.strftime("%H:%M:%S"))))
    print('-'*60)

    start_time = datetime.now()

    for port in range (minp, maxp):
        try:
            response = scan(target, port)
            if response == 0:
                print("[+] Found Open Port: {}".format(port))
        except Exception as e:
            pass
        except KeyboardInterrupt:
            print("Program Terminated !")
            sys.exit(1)

    stop_time = datetime.now()

    final_time = stop_time - start_time
    print("-"*60)
    print("\n[*] Scan Finished at {} ".format(time.strftime("%H:%M:%S")))
    print("[*] Duration of scan: {} ".format(final_time))


if __name__ == "__main__":
    clear()
    print(ascii)
    gettargetinfo()

