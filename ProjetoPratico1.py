# Programa em python que simula transações pix, as validando ou não,
# utilizando expressoes regulares
import re

listaClientes = []
entradaClientes = []
validacoes = []


def validarCpf(cpf): 
    tudo_igual = False
    if int(cpf[0]) == int(cpf[1]) == int(cpf[2]) == int(cpf[4]) == int(cpf[5]) == int(cpf[6]) == int(cpf[8]) == int(cpf[9]) == int(cpf[10]):
        tudo_igual = True

    soma1 = int(cpf[0])*1 + int(cpf[1])*2 + int(cpf[2])*3 + int(cpf[4])*4 + int(cpf[5])*5 + int(cpf[6])*6 + int(cpf[8])*7 + int(cpf[9])*8 + int(cpf[10])*9
    soma2 = int(cpf[0])*0 + int(cpf[1])*1 + int(cpf[2])*2 + int(cpf[4])*3 + int(cpf[5])*4 + int(cpf[6])*5 + int(cpf[8])*6 + int(cpf[9])*7 + int(cpf[10])*8 + int(cpf[12])*9

    resto1 = soma1 % 11
    if resto1 == 10:
        resto1 = 0

    resto2 = soma2 % 11
    if resto2 == 10:
        resto2 = 0

    if resto1 == int(cpf[12]) and resto2 == int(cpf[13]) and tudo_igual == False:
        print("true")
    else:
        print("false")

def validarCNPJ(cnpj): 
    soma1 = int(cnpj[0])*6 + int(cnpj[1])*7 + int(cnpj[3])*8 + int(cnpj[4])*9 + int(cnpj[5])*2 + int(cnpj[7])*3 + int(cnpj[8])*4 + int(cnpj[9])*5 + int(cnpj[11])*6 +  int(cnpj[12])*7 + int(cnpj[13])*8 + int(cnpj[14])*9
    soma2 = int(cnpj[0])*5 + int(cnpj[1])*6 + int(cnpj[3])*7 + int(cnpj[4])*8 + int(cnpj[5])*9 + int(cnpj[7])*2 + int(cnpj[8])*3 + int(cnpj[9])*4 + int(cnpj[11])*5 +  int(cnpj[12])*6 + int(cnpj[13])*7 + int(cnpj[14])*8 + int(cnpj[16])*9
    

    resto1 = soma1 % 11
    if resto1 == 10:
        resto1 = 0

    resto2 = soma2 % 11
    if resto2 == 10:
        resto2 = 0

    if resto1 == int(cnpj[16]) and resto2 == int(cnpj[17]):
        print("true")
    else:
        print("false")


def verificarRepeticoes(entradaClientes):
    contaRepeticoes = 0
    for i in entradaClientes:
        for j in entradaClientes:
            if i == j:
                contaRepeticoes = contaRepeticoes + 1
        if contaRepeticoes > 0:
            return False
    return True


def validarClientes(entradaClientes):
    validacoes.append(len(entradaClientes) > 5 or len(entradaClientes) < 1)
    validacoes.append(verificarRepeticoes(entradaClientes))
    validarChaves(entradaClientes)

def validarChaves(entrada):
    for i in entrada:    
        if re.match("[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}", i): #cpf
            validacoes.append(validarCPF(i))
        if re.match("[0-9]{2}[.][0-9]{3}[.][0-9]{3}[/][0-9]{4}[-][0-9]{2}", i): #cnpj
            validacoes.append(validarCNPJ(i))
        if i == email:
            validacoes.append(validarEmail(i))
        if i == telefone:
            validacoes.append(validarTelefone(i))
        if i == hexadecimal:
            validacoes.append(validarHexadecimal(i))

def validarDadosTransacao(entradaTransacoes):
    validarChaves(entradaTransacoes[0]+entradaTransacoes[1])
    validacoes.append(entradaTransacoes[2] != "R$")
    validacoes.append(validarValor(entradaTransacoes[3]))
    validacoes.append(validarData(entradaTransacoes[4]))
    validacoes.append(validarHora(entradaTransacoes[5]))
    validacoes.append(validarCodigoSeguranca(entradaTransacoes[6]))

def validarTransacoes(entradaTransacoes):
    validacoes.append(len(entradaTransacoes) != 7)
    origem = entradaTransacoes[0]
    destino = entradaTransacoes[1]
    validacoes.append(origem == destino)
    for chaves in listaClientes:
        validacoes.append(origem in chaves)
        validacoes.append(destino in chaves)
    validarDadosTransacao(entradaTransacoes)

while True:
    entradaClientes.extend(input().split(" "))
    if entradaClientes[0] == "==========":
        break

    validarClientes(entradaClientes)

    listaClientes.append(entradaClientes.copy())
    entradaClientes.clear()


print("transacao")

listaTransacoes = []
entradaTransacoes = []
while True:
    try:
        entradaTransacoes.extend(input().split(" "))

        validarTransacoes(entradaTransacoes)

        listaTransacoes.append(entradaTransacoes.copy())
        entradaTransacoes.clear()
    except:
        break


