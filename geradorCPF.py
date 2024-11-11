import re
#declaração de variaveis
entrada = ''
CPFEnviado = ''
antiSequencia = None
CPFGeradoAlgoritmo = ''
contagemRegressiva = 0
soma = 0
resto = 0
primeiroDigito = 0
segundoDigito = 0

#entrada
entrada = input("Digite o CPF a validar: ") 
#remover os caracteres que não são numeros da entrada com expressões regulares
CPFEnviado = re.sub(r'[^0-9]', '', entrada) 
#verificar cpf com numeros full repetidos (essa bomba dá erro)
antiSequencia = entrada == entrada[0] * len(entrada) 
if antiSequencia:
    print("Você digitou uma sequência de digitos iguais, digite o cpf")
else:
#coleta os nove primeiros digitados, é o que nois precisa
    CPFGeradoAlgoritmo = CPFEnviado[0:9]
    #soma e multiplica os nove primeiros digitos com uma contagem regressiva de 10 a 1
    contagemRegressiva = 10
    for digito in CPFGeradoAlgoritmo:
        #transforma digito em int pra fazer os calculos
        digito = int(digito)
        soma += digito * contagemRegressiva
        contagemRegressiva -= 1
    #multiplica a soma por 10
    soma = soma * 10
    #verifica o resto da divisão desse resultado por 11
    resto = soma % 11
    #condicional primeiro digito
    if resto > 9:
        primeiroDigito = 0
    else:
        primeiroDigito = resto
    #agora que acabou os calculos, transformar o primeiro digito em string
    primeiroDigito = str(primeiroDigito)
    #somar o primeiro digito encontrado com os 9 primeiros
    CPFGeradoAlgoritmo = CPFGeradoAlgoritmo + primeiroDigito
    #redefinir resto e soma
    soma = 0
    resto = 0
    #soma e multiplica os nove primeiros digitos com uma contagem regressiva de 11 a 1
    contagemRegressiva = 11
    for digito in CPFGeradoAlgoritmo:
        #transforma o digito em int pra fazer os calculos
        digito = int(digito)
        soma += digito * contagemRegressiva
        contagemRegressiva -= 1
    #multiplica a soma por 10
    soma = soma * 10
    #verifica o resto da divisão desse resultado por 11
    resto = soma % 11
    #condicional primeiro digito
    if resto > 9:
        segundoDigito = 0
    else:
        segundoDigito = resto
    #agora que acabou os calculos, retransformar CPFGeradoAlgoritmo em string e o segundo digito tbm
    CPFGeradoAlgoritmo = str(CPFGeradoAlgoritmo)
    segundoDigito = str(segundoDigito)
    #somar o segundo digito com os 11 primeiros digitos
    CPFGeradoAlgoritmo = CPFGeradoAlgoritmo + segundoDigito
    #verificação de validação
    if CPFGeradoAlgoritmo == CPFEnviado:
        print("O CPF é válido")
    else:
        print("O CPF é inválido")
        



        











    


    



    












