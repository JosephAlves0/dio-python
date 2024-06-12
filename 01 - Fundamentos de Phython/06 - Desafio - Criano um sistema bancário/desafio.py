menu = """

Escolha uma opção:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

=> """

saldo = 0;
limite = 500;
extrato = "";
numero_saque = 0;
LIMITE_SAQUES = 3;

while (True):

    opcao = int(input(menu));

    if (opcao == 1):
        print("Você escolheu a opção Depositar");
        valor_deposito = float(input("Valor a ser depositado: "));

        if(valor_deposito <= 0):
            print("Valor inválido para depósito");
        else:
            saldo += valor_deposito;
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
            print(f"O valor R$ {valor_deposito:.2f} foi depositado com sucesso!");

    elif (opcao == 2):
        print("Você escolheu a opção Sacar");
        if (numero_saque >= 3):
            print(f"Você atingiu o número máximo diário de saque. Saques permitidos por dia: {numero_saque}");
        else:
            valor_saque = float(input("Valor a ser sacado: "))
            if(valor_saque > limite):
                print(f"Saque não liberado. Valor do saque maior que o limite de R$ {limite:.2f}");
            elif (valor_saque > saldo):
                print("Saldo insuficiente.");
            else:
                saldo -= valor_saque;
                numero_saque += 1;
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                print("Saque realizado com sucesso!");
                
    elif (opcao == 3):
        print("Você escolheu a opção para visualizar o Extrato");
        print(extrato + f"Saldo: R$ {saldo:.2f}")

    elif (opcao == 0):
        print("Sair");
        break;

    else:
        print("Opção inválida. Por favor selecione uma opção válida.")