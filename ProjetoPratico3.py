import re

# Programa em python que simula uma Máquina de Turing.
# As entradas são, respectivamente: Máquina de Turing no formato {'inicial': 'x', 'aceita': 'x', 'rejeita': 'x', 'delta': [(instruções do cabeçote)]},
# a quantidade de fitas que serão lidas e as fitas no alfabeto de entrada {0,1}.
# O resultado final será ACEITA ou REJEITA juntamente com a fita final.

def atribuirMT(entrada):
    listaDeDicionarios = []
    MT = {'inicial': '0', 'aceita': '0', 'rejeita': '0', 'delta': listaDeDicionarios}
    entrada2 = entrada.replace(' ', '')  
    indiceInicial = entrada2.find("'inicial':")
    if indiceInicial != -1:
        MT['inicial'] = entrada2[indiceInicial + len("'inicial':")]

    indiceAceita = entrada2.find("'aceita':")
    if indiceAceita != -1:
        MT['aceita'] = entrada2[indiceAceita + len("'aceita':")]

    indiceRejeita = entrada2.find("'rejeita':")
    if indiceRejeita != -1:
        MT['rejeita'] = entrada2[indiceRejeita + len("'rejeita':")]

    indiceDelta = entrada2.find("'delta':")
    if indiceDelta != -1:
        tuplasDaEntrada = entrada2[indiceDelta:len(entrada2)]
        listaDeTuplas = re.findall(r'\((.*?)\)', tuplasDaEntrada)
        for tupla in listaDeTuplas:
            semaspas = tupla.replace('"', '')
            t = tuple(semaspas.split(','))
            instrucao = {}
            instrucao['estadoAtual'], instrucao['novoEstado'], instrucao['escrito'], instrucao['escrever'], instrucao['cabeçote'] = t
            listaDeDicionarios.append(instrucao)
    return MT;


def computar(MT):
    resultadosDaComputacao = []
    qtdFitas = int(input())
    for i in range(qtdFitas):
        palavraFita = input()
        palavraFitaComBrancos = 'b' + palavraFita + 'b'  
        fita = list(palavraFitaComBrancos)
        estado = MT['inicial']
        pos = 1
        cabecote = 'P'
        while pos < len(fita):
            for instrucoes in MT['delta']: 
                if estado == MT['aceita']:
                    novafita = ''.join(fita).strip('b')
                    resultado = (novafita, 'ACEITA')
                    resultadosDaComputacao.append(resultado)
                    pos = len(fita)
                    break
                if estado == MT['rejeita']:
                    novafita = ''.join(fita).strip('b')
                    resultado = (novafita, 'REJEITA')
                    resultadosDaComputacao.append(resultado)
                    pos = len(fita)
                    break
                if estado == instrucoes['estadoAtual'] and fita[pos] == instrucoes['escrito']:
                    estado = instrucoes['novoEstado']
                    fita[pos] = instrucoes['escrever']
                    if instrucoes['cabeçote'] == 'D':
                        pos += 1
                    elif instrucoes['cabeçote'] == 'E':
                        pos -= 1
    return resultadosDaComputacao


def impressao(resultadosDaComputacao):
    for tuplaDeResultados in resultadosDaComputacao:
        for elemento in tuplaDeResultados:
            print(elemento, end=' ')
        print()


if __name__ == '__main__':
    entrada = input()
    MT = atribuirMT(entrada)
    resultadosDaComputacao = computar(MT)
    impressao(resultadosDaComputacao)
