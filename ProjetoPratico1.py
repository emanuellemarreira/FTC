# programa em python que simula transações pix, as validando ou não,
# utilizando expressoes regulares
import re

listaClientes = []
entradaClientes = []
validacoes = []

def validar_cpf(cpf):
    cpf_numerico = ''.join(filter(str.isdigit, cpf))
    if len(cpf_numerico) != 11:
        return False
    total = 0
    for i in range(9):
        total += int(cpf_numerico[i]) * (10 - i)
    resto = total % 11
    if resto >= 2:
        digito1 = 11 - resto
    else:
        digito1 = 0
    total = 0
    for i in range(10):
        total += int(cpf_numerico[i]) * (11 - i)
    resto = total % 11
    if resto >= 2:
        digito2 = 11 - resto
    else:
        digito2 = 0
    if int(cpf_numerico[9]) == digito1 and int(cpf_numerico[10]) == digito2:
        return True
    else:
        return False


def validar_cnpj(cnpj):
    cnpj_numerico = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj_numerico) != 14:
        return False
    total = 0
    multiplicador = 5
    for i in range(12):
        total += int(cnpj_numerico[i]) * multiplicador
        if multiplicador == 2:
            multiplicador = 9
        else:
            multiplicador -= 1
    resto = total % 11
    if resto >= 2:
        digito1 = 11 - resto
    else:
        digito1 = 0
    total = 0
    multiplicador = 6
    for i in range(13):
        total += int(cnpj_numerico[i]) * multiplicador
        if multiplicador == 2:
            multiplicador = 9
        else:
            multiplicador -= 1
    resto = total % 11
    if resto >= 2:
        digito2 = 11 - resto
    else:
        digito2 = 0
    if int(cnpj_numerico[12]) == digito1 and int(cnpj_numerico[13]) == digito2:
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
    verifica_origem = False
    verifica_destino = False
    for chaves in listaClientes:
        if (origem in chaves) and (destino not in chaves):
            verifica_origem = True
        if (destino in chaves) and (origem not in chaves):
            verifica_destino = True
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
            print(validacoes)
            if False in validacoes:
                print("False", end = "")
            else:
                print("True", end = "")
            break

