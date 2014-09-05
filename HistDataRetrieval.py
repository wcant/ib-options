from time import sleep
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message

def price_tick_handler(msg):
    print msg


tws = ibConnection()
tws.register(price_tick_handler, message.tickPrice)
tws.connect()

c = Contract
c.m_symbol = "SPY"
c.m_secType = "STK"
c.m_exchange = "SMART"
c.m_currency = "USD"

tws.reqMktData(1, c, "", False)

sleep(10)

print "all done"

tws.disconnect()
