#! /usr/bin/env python2.7

#IbPy
import ib
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message

#StdLib
import logger
import os
import datetime as dt
from time import sleep,strftime


def makeContract(symbol, derivative, exchange, expiration = None,
		strike = None, call_put = None, currency = "USD",
		tradingClass = None, multiplier = None):
	contract = Contract()
	contract.m_symbol = symbol
	contract.m_secType = derivative
	contract.m_exchange = exchange
	contract.m_currency = currency
	if derivative == "OPT":
		contract.m_expiry = expiration
		contract.m_strike = strike
		contract.m_right = call_put
		contract.m_multiplier = multiplier
		contract.m_tradingClass = tradingClass
	if derivative == "FUT":
		contract.m_expiry = expiration

	return contract

class Downloader():
	def __init__(self):
		"""__init__ passes the object its first parameters."""
		self.con = ibConnection()
		self.con.register(self.tickPriceHandler, 'TickPrice')
		self.con.registerAll(self.listener)
		self.con.connect()
		self.tickID = 1
		self.recordFile = open('aapl_100.dat', 'a')
		#self.genericTicklist = [233,221,106,104]

	def listener(self, msg):
		print(msg)
		#self.recordFile.write(str(msg)+"\n"+strftime("%Y-%m-%d %H:%M:%S"))

	def getContractDetails(self, contract):
		#Only accepts Symbol,SecType,Exch,Currency
		self.con.reqContractDetails(contract)

	def disconnect(self):
		self.con.disconnect()
		self.recordFile.close()
		self.symbols.close()

	data = {}
	def tickPriceHandler(self, msg):
		#Tick value of 4 refers to Last Price
		if msg.field == 4:
		  #tickerId was previously specified in the call to reqMktData()
			self.data[msg.tickerId] = msg.price

	def getSpotTick(self, contract):
		self.symbols.close()
		self.con.reqMktData(self.tickID, contract,'', False)
		self.tickID += 1
