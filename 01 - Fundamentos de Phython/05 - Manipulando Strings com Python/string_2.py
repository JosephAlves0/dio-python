nome = "Bento";
idade = 28;
profissao = "Programador";
linguagem = "Python";
saldo = 45.435;

dados= {"nome": "Bento", "idade": 28};

print("Nome: %s Idade: %d" % (nome, idade));
print("Nome: {} Idade: {}" .format(nome, idade));
print("Nome: {0} Idade: {1}" .format(nome, idade));
print("Nome: {0} Idade: {1} Nome: {0}" .format(nome, idade));
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade));
print("Nome: {nome} Idade: {idade}" .format(**dados));

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}");
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}");
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.5f}");