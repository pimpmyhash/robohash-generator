#!/usr/bin/env python
# coding=utf8
# Ethereum wallet key creation. Modified Vanityreum (https://github.com/antonio-fr/Vanityreum)

from lib.ECDSA_BTC import *
import lib.python_sha3

def hexa(cha):
	hexas=hex(cha)[2:-1]
	while len(hexas)<64:
		hexas="0"+hexas
	return hexas

def hashrand(num):
	rng_data=''
	for idat in xrange(num):
		rng_data = rng_data + os.urandom(32)
	assert len(rng_data) == num*32
	return hashlib.sha256(rng_data).hexdigest()

def randomforkey():
	candint = 0
	r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
	while candint<1 or candint>=r:
		cand=hashrand(1024)
		candint=int(cand,16)
	return candint

def compute_adr(priv_num):
	try:
		pubkey = Public_key( generator_256, mulG(priv_num) )
		pubkeyhex = (hexa(pubkey.point.x())+hexa(pubkey.point.y())).decode("hex")
		return lib.python_sha3.sha3_256(pubkeyhex).hexdigest()[-40:]
	except KeyboardInterrupt:
		return "x"

if __name__ == '__main__':
	import multiprocessing
	p = multiprocessing.Pool(int(multiprocessing.cpu_count()))
	import hashlib
	import re
	import sys
	import time
	import os.path
	from lib.humtime import humanize_time 
	load_gtable('coin_modules/ethereum/lib/G_Table')
	privkeynum = randomforkey()
	address = compute_adr(privkeynum)
	foundprivkeynum = privkeynum
	if 'inter' not in locals():
		assert compute_adr(foundprivkeynum) == address
		pvhex = hexa(foundprivkeynum)
		print "0x%s" % address + ":%s" % pvhex
