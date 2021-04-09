arquivo = './arquivo.txt'
transacoes = './transações.txt'

def cadastroadd():
    cadastro = open(arquivo, 'a', encoding='UTF-8')
    cadastro.writable()
    nome = str(input('Digite nome completo: '))
    nConta = int(input('Digite sua conta Bancaria: '))
    bco = str(input('Escolha seu banco: '))
    saldoopc = str(input('Deseja inserir um saldo ? [s/n]: '))
    if (saldoopc=='s' or saldoopc=='S'):
        saldo = float(input('Quantia a adicionar?: '))
    else:
        saldo = 0
    cadastro.writelines('Nome: {}\nConta: {}\nBanco: {}\nsaldo: {}\n'.format(nome, nConta, bco, saldo))

    saqueop = str(input('Deseja fazer um saque ou deposito? [s/n]: '))
    if (saqueop =='s' or saqueop=='S'):
        saqdep = int(input('1 para saque\n2 para deposito\n: '))
    else:
        print('Tenha um bom dia, volte sempre!')

        return        

    if (saqdep==1):
        saque = float(input('Quantia que  deseja sacar: '))
        novosaldo = saldo - saque
    else:
        dep = float(input('Quantia que deseja depositar: '))
        novosaldo = saldo + dep

    cadastro.write('\n')
    from datetime import datetime
    hora = datetime.now().strftime('%d-%m-%Y')

    comprovante = open('transações.txt', 'a', encoding='UTF-8')
    comprovante.writable()
    if(saqdep == 1):
        comprovante.writelines('Nome: {};Conta: {};Banco: {};Saldo anterior: {};Saque: {};Saldo Atual: {};Horario: {};'.format(nome, nConta, bco, saldo, saque, novosaldo, hora))
    else:
        comprovante.writelines('Nome: {};Conta: {};Banco: {};Saldo anterior: {};Deposito: {};Saldo Atual: {};Horario: {};'.format(nome, nConta, bco, saldo, dep, novosaldo, hora))
    comprovante.write('\n')
    comprovante.close()
    cadastro.close()

def verTransacoes():
    t = open(transacoes, 'r', encoding='UTF-8')
    for dados in t:
        print(dados.replace(';', '\n'), end = '')
    t.close

def menuPrincipal():
    menu = 'CAIXA 24H'
    
    print(menu.center(50),'\n\n')
    print('1 - NOVO CADASTRO\n')
    print('2 - VER EXTRATO\n')
    print('3 - SAIR\n')
    print('\n')
    
    opc = int(input('Escolha uma opcão: '))
    if(opc == 1):
        cadastroadd()
    elif(opc == 2):
        verTransacoes()
    elif(opc == 3):
        print('Até logo!')
    else:
        print('Digite uma opção válida!')

def separa():
    separar = open(transacoes, 'r', encoding='UTF-8')

    soma = 0
    from datetime import datetime
    hora = datetime.now().strftime('%d-%m-%Y')
    for itens in separar:
       dados = itens.split(';')
       h = str(dados[6].replace('Horario: ', ''))
       if('Saque: ' in itens and hora == h):
           d = float(dados[4].replace('Saque: ', ''))
           soma = soma + d

    print('Total de saques efetuados diario: ', soma)
    separar.close()

menuPrincipal()
separa()