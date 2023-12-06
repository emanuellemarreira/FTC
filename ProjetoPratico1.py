# programa em python que simula transações pix, as validando ou não,
# utilizando expressoes regulares
import re

listaClientes = []
entradaClientes = []
validacoes = []


def validarCPF(cpf): 
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
        return True
    else:
        return False

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
        return True
    else:
        return False

def validarChaveRapida(chave_rapida):
    if chave_rapida[0] == chave_rapida[1] or chave_rapida[3] == chave_rapida[4] or chave_rapida[6] == chave_rapida[7] or chave_rapida[9] == chave_rapida[10]:
        return False
    else:
        return True

def validarValor(valor):
    if re.match(r'^\d{1,3}(\.\d{3})*,\d{2}$', valor):
        return True
    else:
        return False

def validarDataHora(datahora):
    if re.match("([0-9][0-9])/([0-9][0-9])/[0-9]{4} [0-9]{2}:[0-9]{2}", datahora):
        dia = int(datahora[0]+datahora[1])
        mes = int(datahora[3]+datahora[4])
        ano = int(datahora[6]+datahora[7]+datahora[8]+datahora[9])
        hora = int(datahora[11]+datahora[12])
        minuto = int(datahora[14]+datahora[15])
        if mes > 12 or ano < 0 or hora > 23 or minuto > 59 or \
        ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31) or \
        ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30) or \
        (mes == 2 and dia > 29):
            return False
        else:
            return True
    else:
        return False

def validarCodigoSeguranca(cod):
    if re.match(r'^(?=(?:[^A-Z]*[A-Z]){3})(?=(?:[^\d]*\d){4})(?=(?:[^$@%(*]*[$@%(*]){2})(?=(?:[^a-z]*[a-z]){3})[A-Za-z\d$@%(*]{12}$', cod):
        return True
    else:
        return False

def verificarRepeticoes(entradaClientes):
    for i in entradaClientes:
        contaRepeticoes = 0
        for j in entradaClientes:
            if i == j:
                contaRepeticoes = contaRepeticoes + 1
                if contaRepeticoes > 1: #nao pode ser igual pq tem a repeticao do inicio
                    return False  # repeticoes retorna False
    return True  #sem repeticoes retorna True

def validarId(id):
    if re.match("[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}", id): #cpf
        validacoes.append(validarCPF(id))
    elif re.match("[0-9]{2}[.][0-9]{3}[.][0-9]{3}[/][0-9]{4}[-][0-9]{2}", id): #cnpj
        validacoes.append(validarCNPJ(id))
    else:
        validacoes.append(False)
        

def validarClientes(entradaClientes):
    validacoes.append(len(entradaClientes) <= 5 and len(entradaClientes) >= 1)
    idCliente = entradaClientes[0]
    validarId(idCliente)
    validacoes.append(verificarRepeticoes(entradaClientes))
    validarChaves(entradaClientes[1:])

def validarChaves(entrada):
    for i in entrada:    
        if re.match(r'[\w.-]+@[\w.-]+', i):
            validacoes.append(True) #email
        elif re.match("^\+55[\(][0-9]{2}[\)][0-9]{4}-[0-9]{4}", i):
            validacoes.append(True)#telefone
        elif re.match("[0-9A-Fa-f]{2}\.[0-9A-Fa-f]{2}\.[0-9A-Fa-f]{2}\.[0-9A-Fa-f]{2}", i):
            validacoes.append(validarChaveRapida(i))#chaverapida
        else:
            validacoes.append(False) #nada


def validarDadosTransacao(entradaTransacoes):
    validacoes.append(entradaTransacoes[2] == "R$")
    validacoes.append(validarValor(entradaTransacoes[3]))
    validacoes.append(validarDataHora(entradaTransacoes[4] + " "+ entradaTransacoes[5]))
    validacoes.append(validarCodigoSeguranca(entradaTransacoes[6]))

def validarTransacoes(entradaTransacoes):
    validacoes.append(len(entradaTransacoes) == 7)
    origem = entradaTransacoes[0]
    destino = entradaTransacoes[1]
    validacoes.append(origem != destino)
    verifica_origem = True
    verifica_destino = True
    for chaves in listaClientes: #ter certeza que a chave da origem está listada
        if origem in chaves:
            verifica_origem = True
            break
        else:
            verifica_origem = False
    for chaves in listaClientes: #ter certeza que a chave de destino está listada
        if destino in chaves:
            verifica_destino = True
            break
        else:
            verifica_destino = False
    validacoes.append(verifica_origem)
    validacoes.append(verifica_destino)
    validarDadosTransacao(entradaTransacoes)


if __name__ == "__main__":
        
    while True:
        entradaClientes.extend(input().split(" "))
        if entradaClientes[0] == "==========":
            break
        validarClientes(entradaClientes)
        listaClientes.append(entradaClientes.copy())
        entradaClientes.clear()

    entradaTransacoes = []
    while True:
        try:
            entradaTransacoes.extend(input().split(" "))
            validarTransacoes(entradaTransacoes)
            entradaTransacoes.clear()
        except EOFError:
            if False in validacoes:
                print("False", end = "")
            else:
                print("True", end = "")
            break

