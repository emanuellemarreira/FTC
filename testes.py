def verificarRepeticoes(entradaClientes):
    contaRepeticoes = 0
    for i in entradaClientes:
        for j in entradaClientes:
            if i == j:
                contaRepeticoes = contaRepeticoes + 1
        if contaRepeticoes == 0:
            return True 
        else:
            return False

lista = [1,2,3,3,4]
print(verificarRepeticoes(lista))