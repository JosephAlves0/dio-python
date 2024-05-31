def sacar(valor: float):
    saldo = 500;

    if (saldo >= valor):
        print("Valor Sacado!");
        print("Retire seu dinheiro!");
    else:
        print("Saldo insuficiente!");
        print("Saldo: ", saldo);
    
    print("Obrigado pela preferencia!");
    
def depositar(valor: float):
    saldo = 500;
    saldo += valor;
    print("Saldo atual: ", saldo);

sacar(1000);
depositar(1000);