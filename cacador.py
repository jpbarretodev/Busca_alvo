import os
import random
import json

caminhos_percorridos = []
dicio = {}

class cacador():

    def __init__(self, raiz):
        self.raiz = raiz #recebe o diretório principal em que, toda vez, terá como ponto de partida e de volta
        self.diretorio_atual = self.raiz

    def buscar(self):
        caminhos_possiveis = os.listdir(self.diretorio_atual) #recolhe somente o nome dos diretórios
        return caminhos_possiveis, len(caminhos_possiveis) #retorna os nomes e a quantidade
        

    def voltar(self):
        os.chdir(self.raiz)
        print(os.getcwd())

    def entrar(self):
        possibilidades, quantidade = self.buscar()

        while True:
            escolha = random.choice(possibilidades) #escolhe um diretorio
            caminho_completo = os.path.join(self.raiz, escolha) #recolhe o caminho completo

            if caminho_completo not in caminhos_percorridos:
                caminhos_percorridos.append(caminho_completo)
                os.chdir(caminho_completo)
                self.diretorio_atual = caminho_completo
                resultado = self.buscar()
                #print(resultado)

                if "alvo" in resultado[0]:
                    print("Alvo encontrado no caminho: {}".format(os.getcwd()))
                    break
                else:
                    print("Alvo não encontrado\n")
                    #print(caminhos_percorridos)

#objeto instanciado, NÃO MEXER
objeto = cacador("") #cria um objeto (o diretório onde será realizada a busca)
objeto.entrar()

#armazena no log em json
for i, j in enumerate(caminhos_percorridos):
    dicio["tentativa: {}".format(i+1)] = "caminho percorrido: {}".format(j)
with open("", "w") as arq: #aqui vai o caminho completo para o arquivo json
    json.dump(dicio, arq, indent=4)
