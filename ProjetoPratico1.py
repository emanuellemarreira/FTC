listaClientes = []
entradaClientes = []
validacoes = []

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


def validarClientes(entradaClientes):
    validacoes.append(len(entradaClientes) > 5 or len(entradaClientes) < 1)
    validacoes.append(verificarRepeticoes(entradaClientes))
    validarChaves(entradaClientes)

def verificarRepeticoes(entradaClientes):
    contaRepeticoes = 0
    for i in entradaClientes:
        for j in entradaClientes:
            if i == j:
                contaRepeticoes = contaRepeticoes + 1
        if contaRepeticoes > 0:
            return False
    return True

def validarChaves(entrada):
    for i in entrada:    
        if i == CPF:
            validacoes.append(validarCPF(i))
        if i == CNPJ:
            validacoes.append(validarCNPJ(i))
        if i == email:
            validacoes.append(validarEmail(i))
        if i == telefone:
            validacoes.append(validarTelefone(i))
        if i == hexadecimal:
            validacoes.append(validarHexadecimal(i))

def validarTransacoes(entradaTransacoes):
    validacoes.append(len(entradaTransacoes) != 7)
    origem = entradaTransacoes[0]
    destino = entradaTransacoes[1]
    validacoes.append(origem == destino)
    for chaves in listaClientes:
        validacoes.append(origem in chaves)
        validacoes.append(destino in chaves)
    validarDadosTransacao(entradaTransacoes)

def validarDadosTransacao(entradaTransacoes):
    validarChaves(entradaTransacoes[0]+entradaTransacoes[1])
    validacoes.append(entradaTransacoes[2] != "R$")
    validacoes.append(validarValor(entradaTransacoes[3]))
    validacoes.append(validarData(entradaTransacoes[4]))
    validacoes.append(validarHora(entradaTransacoes[5]))
    validacoes.append(validarCodigoSeguranca(entradaTransacoes[6]))


