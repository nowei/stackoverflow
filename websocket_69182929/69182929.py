import numpy as np
# import talib
import websocket, json, pprint

socket = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"


closelist = []

def on_open(ws):
    print('open')
            
def on_close(ws):
    print('close')
    
def on_message(ws, message):
    global closelist
    json_message = json.loads(message)
 #   pprint.pprint(json_message)
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']
    high = candle['h']
    low = candle['l']
    
    if is_candle_closed:

        closelist.append(format(float(close)))
        
        closelist.append(format(float(high)))
        
        closelist.append(format(float(low)))
        np_closelist = np.array(closelist)
         
        b = np.array([int(i) for i in np_closelist])
        print(b)
        print(type(b))
        print(type(b[1]))

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()