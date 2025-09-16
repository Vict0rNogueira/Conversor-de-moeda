import requests

class ConversorMoeda:
    def converter(self, valor, moeda_origem, moeda_destino):
        moeda_origem = moeda_origem.upper()
        moeda_destino = moeda_destino.upper()
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
        
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            dados = resposta.json()
            chave = f"{moeda_origem}{moeda_destino}"
            cotacao = float(dados[chave]["bid"])
            return valor * cotacao
        except Exception as e:
            print("Erro ao obter cotação:", e)
            return None
