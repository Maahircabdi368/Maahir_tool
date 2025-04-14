from colorama import Fore,init,Style
import socket

def ip_target():
	while True:
		ip=input(Fore.YELLOW+'gali ip addresska :')
		
		ports=[80,443,22,23,45,110,25,53,3306,3389,143,69,389,2000,5060]
		
		print(Fore.LIGHTCYAN_EX+Style.BRIGHT+f'\nbaaritaanka ports ee {ip}')
		
		for port in ports:
			try:
				sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				sock.settimeout(1)
				result=sock.connect_ex((ip,port))
				if result == 0:
					print(f'port : {port}{Fore.GREEN} its open {Fore.RESET} ')
				else:
					print(f'port : {port} its close')
					
				sock.close()
				
			except Exception as e:
				print(f'Error:{e}')
		
		print(Fore.BLUE+f'\nbaaritanka {ip} waa dhamaaday ')
		
		doorasho_kale=input(Fore.YELLOW+'\nMa doonaysaa inaad IP kale baarto? (yes/no): ').lower()
		if doorasho_kale == 'no':
			print(Fore.LIGHTGREEN_EX+'Thanks for using IP scanner.')
			break
				
				
#ip_track
from colorama import Fore , init , Style
import requests
import re

init(autoreset=True)

def ip_track():
    while True:
        ip = input('Gali IP address-ka: ')
        
        if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', ip):
            print(Fore.RED+'Fadlan gali IP sax ah.\n')
            continue 
        try:
            response1 = requests.get(f'http://ip-api.com/json/{ip}')
            data1 = response1.json()

            if data1['status'] == 'success': 
                print(Fore.CYAN+f'\nNatiijo:')
                print(Fore.GREEN+f'- Wadanka   : {data1["country"]} ')
                print(Fore.GREEN+f'- Magaalada : {data1["city"]} ')
                print(Fore.GREEN+f'- Gobolka   : {data1["region"]} ')
                print(Fore.GREEN+f' -ISP       : {data1["isp"]} ')
                print(Fore.GREEN+f'- TimeZone  : {data1["timezone"]} ')
                print(Fore.GREEN+f'- Zip code : {data1["zip"]} -')
                print(Fore.GREEN+f'- As: {data1["as"]} ')
                print(Fore.GREEN+f'- Longitude : {data1["lon"]} ')
                print(Fore.GREEN+f'- Latitude  : {data1["lat"]} ')
            else:
                print(Fore.RED+'IP lama helin, fadlan hubi.')

            response2 = requests.get(f'http://ipwho.is/{ip}')
            data2 = response2.json()

            if data2['success'] == True: 
                print(Fore.CYAN+f'\nNatiijo ipwho.is:')
                print(Fore.GREEN+f'- Proxy   : {data2.get("proxy", "lama helin")} ')
                print(Fore.GREEN+f'- Reverse DNS : {data2.get("reverse" , "lama helin")} ')
                print(Fore.GREEN+f'- Currency  : {data2.get("currency" , "lama helin")} ')
                print(Fore.GREEN+f'- Country calling   : {data2.get("calling_code", "lama helin")} ')
                print(Fore.GREEN+f'- Hosting : {data2.get("hosting","lama helin")} ')
                print(Fore.GREEN+f'- Continent : {data2.get("continent","lama helin")} ')
            else:
                print(Fore.RED+'IP lama helin, fadlan hubi.')

        except Exception as e:
            print(Fore.RED+f'Error: {e}')
        
        doorasho = input('Ma doonaysaa inaad IP kale baarto? (haa/maya): ').lower()
        if doorasho == 'maya':
            print(Fore.YELLOW+'Thanks for using the IP tracker!')
            break
            
            
            
            
#whois
from colorama import Fore , init , Style
import whois


init(autoreset=True)

def get_whois_info(domain):
	while True:
		try:
			info=whois.whois(domain)
			if info.domain_name is None:
				print(Fore.RED +'macluumadka domain lama helin ')
			else:
		
				print(Fore.CYAN+'\n[+]macluumaadka website[+]:')
				print(Fore.GREEN+f'- Domain    :{info.domain_name}')
				print(Fore.GREEN+f'- Registrar :{info.registrar}')
				if info.creation_date:
					print(Fore.GREEN + f'- creation  : {info.creation_date.strftime("%Y-%m-%d")}')
					
					if info.expiration_date:
						print(Fore.GREEN + f'- expiration : {info.expiration_date.strftime("%Y-%m-%d")}')
				
				
			#	print(Fore.GREEN+f'- creation  :{info.creation_date[0]}')
				#print(Fore.GREEN+f'- expiration :{info.expiration_date[0]}')#0 taariikh kaliya ayuu ku sheegaya
				print(Fore.GREEN+f'- Emails :{info.emails}')
				print(Fore.GREEN+f'- Organisation : {info.org}')
				print(Fore.GREEN+f'- phone  : {info.phone}')
				print(Fore.GREEN+f'- country : { info.country}')
				print(Fore.GREEN+f'- Zip code : {info.zip}')
				print(Fore.GREEN+f'-DNS servers : {info.name_servers}')
			break
		except Exception as e:
			print(Fore.RED+f'[-]Erorr:{e}[-]')
		
			print(Fore.RED+'fadlan hubi domain aad galisay ')
			break
#if __name__ == '__main__':
#	 domain = input('gali domian (tusale:[google.com]):')
	 

	
	
	
	
	
	
	
	
	

import pyfiglet
def menu():
    banner =Style.BRIGHT+pyfiglet.figlet_format("MAAHIR")
    print(banner)
    print(Fore.CYAN+"1. IP Scanner")
    print(Fore.CYAN+"2. IP track")
    print(Fore.CYAN+"3. whois")
    print(Fore.CYAN+"4. Exit")


    

while True:
    menu()
    choice = input(Fore.YELLOW+"\nDooro module: ")

    if choice == "1":
        ip_scanner = Style.BRIGHT + Fore.LIGHTGREEN_EX + pyfiglet.figlet_format('IP SCCANNER')
        print(ip_scanner)
        ip_target()
        print('thanks for using ip_scanner')
        break

    elif choice == "2":
        ip_location = Style.BRIGHT + Fore.LIGHTGREEN_EX + pyfiglet.figlet_format('IP TRACKER')
        print(ip_location)
        ip_track()
        print('thanks for using ip_track')
        break

    elif choice == "3":
        whois_banner = Style.BRIGHT + Fore.LIGHTGREEN_EX + pyfiglet.figlet_format("WHOIS INFO")
        print(whois_banner)
        domain = input(Fore.YELLOW + 'gali domian (tusale:[google.com]):')
        get_whois_info(domain)
        break

    elif choice == "4":
        print(Fore.YELLOW, 'thanks for using ')
        break

    else:
        print(Fore.RED + "Fadlan dooro tiro sax ah!")
        continue
