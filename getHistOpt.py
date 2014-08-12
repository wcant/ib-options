#! /usr/bin/env python3.4

#IbPy 
import ib
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message

#Pandas
from pandas import DataFrame, Index

#StdLib
import logger
import os
import datetime as dt
from time import sleep
from extra import timeFormat, dateFormat


#the object passed in will be self.tws, the connection object
class _HistDataHandler(object):
	def __init__(self, tws):
		self._log = logger.getLogger('DH')
		tws.register(self.msgHandler, message.HistoricalData)
		self.reset()

	def reset(self):
		self._log.debug('Resetting data')
		self.dataReady = False
		self._timestamp = []
		self.data = {'open':[],'high':[],'low':[],'close':[],
				'volume':[],'count':[],'WAP':[]}

