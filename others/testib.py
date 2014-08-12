from ib.opt import ibConnection, message

def my_account_handler(msg):





def my_tick_handler(msg):




connection = ibConnection()
connection.register(my_account_handler, 'UpdateAccountValue')
connection.register(my_tick_handler, 'TickSize', 'TickPrice')
connection.connect()
connection.reqAccountUpdates( )
