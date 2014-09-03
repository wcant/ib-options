import time
from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.ext.TickType import TickType
from ib.opt import ibConnection, message

class DataGetter():
    def __init__(self):
        self.con = ibConnection()
        self.con.register(self.tickPriceHandler, 'TickPrice')
        self.con.registerAll(self.watcher)
        self.con.connect()
        self.tickID = 1

    def watcher(self, msg):
        print msg

    def disconnect(self):
        self.con.disconnect()

    data = {}
    def tickPriceHandler(self, msg):
        if msg.field == 4:
            self.data[msg.tickerId] = msg.price

    def getSpotTick(self, contract):
        self.con.reqMktData(self.tickID, contract, '', True)
        self.tickID += 1


def makeContract(symbol, derivative, exchange, expiration = None,
		 strike = None, call_put = None, currency = "USD"):
    contract = Contract()
    contract.m_symbol = symbol
    contract.m_secType = derivative
    contract.m_exchange = exchange
    contract.m_currency = currency
    if derivative == "OPT":
        contract.m_expiry = expiration
        contract.m_strike = strike
        contract.m_right = call_put
    if derivative == "FUT":
        contract.m_expiry = expiration

    return contract


# here the data retrieval starts
dg = DataGetter()

strikes = [i/2.0 for i in range(20, 100)]
for strike in strikes:
    vixOpt = makeContract("VIX", "OPT", "CBOE", '20140819', strike, "C")
    dg.getSpotTick(vixOpt)

time.sleep(5)

for i, strike in enumerate(strikes):
    if i in dg.data.keys():
        print strike, dg.data[i]

dg.disconnect()
