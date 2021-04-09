import ssl
import json

import websocket

def buy():
  pass

def sell():
  pass

def on_open(ws):
  print("Abriu a conexão")

  json_subscribe = """
  {
    "event": "bts:subscribe",
    "data": {
      "channel": "live_trades_btcusd"
    }
  }
  """
  ws.send(json_subscribe)

def on_close(ws):
  print("Fechou a conexão")

def on_error(ws, error):
  print("Deu erro")
  print(error)

def on_message(ws, message):
  message = json.loads(message)
  price = message['data']['price']
  
  if buy > 59000:
    vender()
  elif price < 58100:
    comprar()
  else:
    print("Aguardar")

if __name__=="__main__":
  ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                              on_open=on_open,
                              on_close=on_close,
                              on_message=on_message,
                              on_error=on_error)
  ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})