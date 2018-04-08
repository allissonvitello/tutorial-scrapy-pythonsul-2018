from urllib import request, parse

rec_busca = request.Request(
        "https://www.portaldorugby.com.br/tag/fluminense-a")

dados_brutos = request.urlopen(rec_busca)
dados_parseados = dados_brutos.read()

print(dados_parseados)