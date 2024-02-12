import requests
import json
import os
import urllib.request
import time

def verifica_conexao_internet():
    try:
        #verificar se à conexão com o banco de dados
        urllib.request.urlopen('http://www.google.com', timeout=1)
        #aguarde 10 segundos
        time.sleep(10)
        return True
    except Exception as e:
        return False

#variavel verificadora para executar apenas uma vez
verificador = False


#enquanto faça enquanto não conseguir uma conexão com a internet
while not verificador:
    try:
        #pegar as informações de data de são paulo da api
        req = requests.get('http://worldtimeapi.org/api/timezone/America/Sao_Paulo')
        time = json.loads(req.text)['datetime'].split("T")
        data = time[0].split("-")
        string_Formatada = data[2] + "-" + data[1] + "-" + data[0]

        #Setar as informações de horario e de data
        os.system("time %s" % time[1].split(".")[0])
        os.system("date %s" % string_Formatada)
        print("Data do sistema definida com sucesso!")
        verificador = verifica_conexao_internet()
    except Exception as e:
        print("Erro")
        print(e)
        exit()
