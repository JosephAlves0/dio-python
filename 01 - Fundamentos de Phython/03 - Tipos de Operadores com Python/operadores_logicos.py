saldo = 1000;
saque = 250;
limite = 200;
conta_especial = True;

print ( (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) )

conta_normal_saldo_suficiente = (saldo >= saque and saque <= limite);

conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque);

exp_3 = conta_normal_saldo_suficiente or conta_especial_com_saldo_suficiente;

print(exp_3);