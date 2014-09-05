#! /usr/bin/env python2.7

#IB
import dataAq as daq 
import datetime as dt

#STDLIB
from time import sleep,strftime

dl = daq.Downloader()

symbols = []
with open('symbols.list', 'r') as f:
	for line in f:
		symbols.append(line.rstrip())

def getSecType(symbol):
	if symbol.isalpha():
		return 'OPT'
	else:
		return 'FUT' 

def getDetails(symbol, derivative):
	contract = daq.Contract()
	contract.m_symbol = symbol
	dl.getContractDetails(1,symbol)

#Build Dictionaries for each underlying
#Contracts for each strike will be built 
meta = {}
for s in symbols:
	meta[s] = {}
	derivative = getSecType(s)
	meta[s]['secType'] = derivative	
	
#opt = makeContract("AAPL", "OPT", "SMART", "20140829", 100, "C", multiplier=100)
#dl.getSpotTick(opt)

#strikes = [i/5.0 for i in range(150, 250)]
#for strike in strikes:
#	vixOpt = makeContract("SPY", "OPT", "CBOE", '20141017',
#			strike, "C")
#	dl.getSpotTick(vixOpt)
#sleep(5)

#for i, strike in enumerate(strikes):
#	if i in dl.data.keys():
#		print(strike, dl.data[i])
#dl.disconnect()
