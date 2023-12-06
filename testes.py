import re
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

def validarValor(valor):
    if re.match(r'^\d{1,3}(\.\d{3})*,\d{2}$', valor):
        return True
    else:
        return False

def validarCodigoSeguranca(cod):
    if re.match(r'^(?=(?:[^A-Z]*[A-Z]){3})(?=(?:[^\d]*\d){4})(?=(?:[^$@%(*]*[$@%(*]){2})(?=(?:[^a-z]*[a-z]){3})[A-Za-z\d$@%(*]{12}$', cod):
        return True
    else:
        return False

def validarChaveRapida(chave_rapida):
    if chave_rapida[0] == chave_rapida[1] or chave_rapida[3] == chave_rapida[4] or chave_rapida[6] == chave_rapida[7] or chave_rapida[9] == chave_rapida[10]:
        return False
    else:
        return True

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

# Exemplo de uso
cnpj_input = "11.111.111/1111-11"
if validar_cnpj(cnpj_input):
    print("CNPJ válido!")
else:
    print("CNPJ inválido.")

