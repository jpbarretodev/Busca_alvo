import os
import random
import json

caminhos_percorridos = []
dicio = {}

class cacador():

    def __init__(self, raiz):
        self.raiz = raiz
        self.diretorio_atual = self.raiz

    def buscar(self):
        caminhos_possiveis = os.listdir(self.diretorio_atual) #recolho somente o nome das pastas
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
objeto = cacador("/home/hunter/Documentos/codigos/Floresta")
objeto.entrar()

#armazena no log em json
for i, j in enumerate(caminhos_percorridos):
    dicio["tentativa: {}".format(i+1)] = "caminho percorrido: {}".format(j)
with open("/home/hunter/Documentos/codigos/log.json", "w") as arq:
    json.dump(dicio, arq, indent=4)