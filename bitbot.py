import websocket
import json
import bitstamp.client
import credentials

def user():
    return bitstamp.client.Trading(username = credentials.USER, key = credentials.KEY, secret = credentials.SECRET)

def comprar(quantidade):
    trading_client = user()
    trading_client.buy_market_order(quantidade)

def vender():
    trading_client = user()
    trading_client.sell_market_order(quantidade)

def abrir_conexao(ws):
    print("Conexão aberta...")

    json_subscribe = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}    
"""
    ws.send(json_subscribe)

def fechar_conexao(ws):
    print("Conexão fechada...")

def enviar_mensagem(ws, message):
    mensagem = json.loads(message)

    dados = mensagem["data"]
    if 'price' in dados:
        preco = dados["price"]
        print(f"Preço: {preco}")
    else:
        evento = mensagem["event"]
        print(f"Evento: {evento}")


def erro(ws, erro):
    print("Erro...")
    print(erro)

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open=abrir_conexao,
                                on_close=fechar_conexao,
                                on_message=enviar_mensagem,
                                on_error=erro
                                )

    ws.run_forever()