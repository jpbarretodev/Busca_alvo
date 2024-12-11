import os
import random
import json

caminhos_percorridos = []
dicio = {}

class cacador():

    def __init__(self, raiz, alvo):
        self.raiz = raiz #recebe o diretório principal em que, toda vez, terá como ponto de partida e de volta
        self.alvo = alvo #recolhe o nome do alvo a ser buscado
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

                if self.alvo in resultado[0]: #adicionar o nome do arquivo que deseja achar
                    print("Alvo encontrado no caminho: {}".format(os.getcwd()))
                    break
                else:
                    print("Alvo não encontrado\n")
                    #print(caminhos_percorridos)

#objeto instanciado
cacador = cacador("", "") #indicar o caminho completo do diretório pai onde será realizada a busca e o nome do alvo (com extensão se for um arquivo específico)
cacador.entrar()

#armazena no log em json
for i, j in enumerate(caminhos_percorridos):
    dicio["tentativa: {}".format(i+1)] = "caminho percorrido: {}".format(j)

with open("", "w") as arq: #indicar o caminho completo onde será salvo o arquivo json de log
    json.dump(dicio, arq, indent=4)

with open("", "a+") as arq: #indicar o caminho completo onde será salvo o arquivo txt de log (opcional)
    for i, j in dicio.items():
        arq.write("{}: {}\n".format(i, j))
