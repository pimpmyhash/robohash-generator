#!/usr/bin/env python

# RoboHash Generator
# Version: 1.0
# Release: 2021-04-28
# Website: pimpmyhash.org
# Licence: GPLv3
# Credits: RoboHash, Vanityreum

import sys
import os.path
import time
import subprocess
import hashlib
import random
from datetime import datetime
from time import localtime, strftime

coin_module = "ethereum"
coin_title = "Ethereum/Idena"

print "\n****** RoboHash Generator ******\nVersion:  1.0\nRelease:  2021-04-28\nWebsite:  pimpmyhash.org\nLicence:  GPLv3\nCredits:  RoboHash, Vanityreum\n********************************\n\nCoin Module: " + coin_title

if len(sys.argv) > 1:
	hashcode = sys.argv[1]
	auto_mode = True
else:
	hashcode = ""
hashcode_input = False
while hashcode_input == False:
	if hashcode == "":
		auto_mode = False
		hashcode = raw_input("\nEnter Hashcode (6 digits): ")
	elif hashcode[1:6] == "00000":
		print "\nIllegal Operation"
		hashcode = ""
	elif len(hashcode) == 6 and hashcode.isdigit():
		hashcode_input = True
	else:
		print "\nInvalid Hashcode"
		hashcode = ""
if auto_mode == False:
	raw_input("\nPress enter to generate keys for RoboHash Model x" + hashcode[1:6] + " ")
else:
	print "\ngenerating keys for RoboHash Model x" + hashcode[1:6] + " .."
print "\n" + strftime("%H:%M", localtime()) + " - starting search .."
colors = ['blue', 'brown', 'green', 'grey', 'orange', 'pink', 'purple', 'red', 'white', 'yellow']
colorcodes = ['5', '6', '7', '3', '0', '4', '2', '8', '1', '9']
timer = time.time()
counter = 0
counter1 = 0
cpm = 0
prob = 100000.0
probf = 0.5
probf1 = 0.25
while True:
	timer_now = time.time()
	if timer_now - timer > 60:
		cpm = counter - cpm
		if counter1 > prob * probf:
			probf = probf + probf1
			probf1 = probf1 * 0.5
		remaining = int(((prob*probf)-counter1)/cpm)
		if remaining < 0:
			remaining = 0
		print strftime("%H:%M", localtime()) + " - " + str(counter) + " checked | " + str(cpm) + " per minute | ~" + str("%.2f" % (100 * counter1 / prob)) + "% progress | " + str("%.2f" % (probf * 100)) + "% in " + str(remaining) + " minutes"
		timer = timer_now
		cpm = counter
	keypair = subprocess.check_output([sys.executable, "coin_modules/" + coin_module + "/" + coin_module + ".py"])
	keypair = keypair.rsplit(':', 1)
	address = keypair[0].encode('utf-8')
	privatekey = keypair[1].rstrip()
	hash = hashlib.sha512()
	hash.update(address)
	hexdigest = hash.hexdigest()
	hasharray = []
	count = 11
	for i in range(0,count):
		blocksize = int(len(hexdigest) / count)
		currentstart = (1 + i) * blocksize - blocksize
		currentend = (1 + i) * blocksize
		hasharray.append(int(hexdigest[currentstart:currentend],16))
	color = colors[hasharray[0] % len(colors) ]
	code1 = colorcodes[hasharray[0] % len(colors) ]
	if code1 == '0':
		files_in_dir2 = ['9', '3', '7', '8', '4', '1', '5', '2', '0', '6']
		files_in_dir3 = ['5', '4', '1', '0', '9', '6', '7', '3', '2', '8']
		files_in_dir4 = ['9', '5', '3', '7', '2', '6', '0', '8', '1', '4']
		files_in_dir5 = ['0', '8', '4', '1', '6', '5', '7', '3', '2', '9']
		files_in_dir6 = ['2', '5', '0', '6', '4', '9', '1', '7', '3', '8']
	elif code1 == '1':
		files_in_dir2 = ['6', '1', '8', '0', '9', '2', '3', '5', '7', '4']
		files_in_dir3 = ['5', '6', '7', '0', '3', '9', '1', '2', '4', '8']
		files_in_dir4 = ['8', '6', '4', '7', '0', '9', '2', '3', '1', '5']
		files_in_dir5 = ['9', '4', '1', '2', '6', '0', '7', '3', '5', '8']
		files_in_dir6 = ['3', '7', '8', '4', '6', '2', '0', '9', '5', '1']
	elif code1 == '2':
		files_in_dir2 = ['4', '0', '3', '9', '7', '2', '5', '8', '1', '6']
		files_in_dir3 = ['1', '5', '0', '2', '7', '4', '3', '6', '8', '9']
		files_in_dir4 = ['3', '1', '7', '6', '4', '5', '8', '2', '0', '9']
		files_in_dir5 = ['8', '6', '1', '0', '9', '3', '2', '5', '4', '7']
		files_in_dir6 = ['3', '1', '7', '0', '9', '4', '6', '5', '2', '8']
	elif code1 == '3':
		files_in_dir2 = ['7', '5', '0', '6', '4', '3', '8', '9', '1', '2']
		files_in_dir3 = ['3', '4', '5', '0', '7', '2', '6', '1', '9', '8']
		files_in_dir4 = ['7', '9', '0', '1', '4', '6', '8', '3', '5', '2']
		files_in_dir5 = ['4', '2', '8', '0', '5', '3', '9', '1', '7', '6']
		files_in_dir6 = ['9', '5', '8', '4', '2', '0', '7', '1', '6', '3']
	elif code1 == '4':
		files_in_dir2 = ['6', '7', '3', '1', '5', '8', '9', '4', '2', '0']
		files_in_dir3 = ['6', '8', '4', '3', '5', '2', '7', '1', '9', '0']
		files_in_dir4 = ['9', '5', '2', '7', '6', '0', '3', '8', '1', '4']
		files_in_dir5 = ['2', '5', '4', '8', '0', '9', '1', '7', '6', '3']
		files_in_dir6 = ['8', '1', '9', '7', '0', '6', '5', '4', '2', '3']
	elif code1 == '5':
		files_in_dir2 = ['4', '5', '7', '9', '0', '3', '6', '8', '1', '2']
		files_in_dir3 = ['6', '4', '0', '5', '1', '3', '8', '9', '2', '7']
		files_in_dir4 = ['8', '3', '6', '2', '4', '9', '7', '5', '1', '0']
		files_in_dir5 = ['6', '0', '9', '1', '8', '5', '7', '4', '3', '2']
		files_in_dir6 = ['1', '9', '8', '5', '2', '4', '3', '0', '7', '6']
	elif code1 == '6':
		files_in_dir2 = ['8', '1', '7', '6', '9', '0', '4', '5', '2', '3']
		files_in_dir3 = ['9', '8', '0', '6', '7', '1', '4', '3', '5', '2']
		files_in_dir4 = ['9', '7', '0', '4', '3', '8', '1', '5', '2', '6']
		files_in_dir5 = ['5', '8', '0', '1', '9', '7', '4', '3', '6', '2']
		files_in_dir6 = ['8', '6', '5', '7', '9', '4', '1', '2', '0', '6']
	elif code1 == '7':
		files_in_dir2 = ['1', '6', '2', '8', '0', '9', '7', '4', '3', '5']
		files_in_dir3 = ['3', '6', '4', '7', '6', '0', '2', '8', '5', '1']
		files_in_dir4 = ['9', '8', '2', '5', '3', '0', '6', '1', '7', '4']
		files_in_dir5 = ['4', '9', '7', '5', '2', '8', '0', '6', '1', '3']
		files_in_dir6 = ['8', '5', '6', '2', '9', '3', '7', '0', '1', '4']
	elif code1 == '8':
		files_in_dir2 = ['5', '6', '1', '3', '4', '0', '9', '1', '2', '7']
		files_in_dir3 = ['0', '7', '8', '1', '4', '3', '2', '5', '6', '9']
		files_in_dir4 = ['8', '2', '7', '3', '0', '9', '5', '6', '4', '1']
		files_in_dir5 = ['0', '1', '4', '8', '2', '5', '9', '3', '7', '6']
		files_in_dir6 = ['5', '4', '8', '6', '0', '2', '1', '9', '3', '7']
	elif code1 == '9':
		files_in_dir2 = ['0', '8', '5', '9', '2', '4', '3', '7', '1', '6']
		files_in_dir3 = ['8', '0', '1', '2', '3', '7', '5', '9', '4', '6']
		files_in_dir4 = ['6', '3', '2', '4', '8', '5', '9', '1', '0', '7']
		files_in_dir5 = ['2', '5', '7', '8', '3', '9', '4', '1', '6', '0']
		files_in_dir6 = ['8', '4', '0', '2', '7', '5', '3', '1', '9', '6']
	element_in_list2 = hasharray[7] % 10
	code2 = files_in_dir2[element_in_list2]
	element_in_list3 = hasharray[8] % 10
	code3 = files_in_dir3[element_in_list3]
	element_in_list4 = hasharray[5] % 10
	code4 = files_in_dir4[element_in_list4]
	element_in_list5 = hasharray[4] % 10
	code5 = files_in_dir5[element_in_list5]
	element_in_list6 = hasharray[6] % 10
	code6 = files_in_dir6[element_in_list6]
	hashcode_current = code1 + code2 + code3 + code4 + code5 + code6
	if hashcode_current[1:6] == hashcode[1:6]:
		foundkey = "******* Found RoboHash *******\nHashcode: #" + hashcode_current + " (" + color + ")\nCreation: " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\nAddress: " + address + "\nPrivate Key: " + privatekey + "\n"
		print "\n" + foundkey
		counter1 = 0
		probf = 0.5
		probf1 = 0.25
		with open(address + '.txt', 'w') as f:
			f.write(foundkey)
	counter += 1
	counter1 += 1
