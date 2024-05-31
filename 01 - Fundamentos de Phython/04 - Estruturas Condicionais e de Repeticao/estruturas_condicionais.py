MAIOR_IDADE = 18;
IDADE_ESPECIAL = 15;

idade = int(input("Informe sua idade: "));

if (idade >= MAIOR_IDADE):
    print("Maior de idade, pode tirar a CNH.");
else:
    print("Ainda não pode tirar a CNH.");


if (idade >= MAIOR_IDADE):
    print("Maior de idade, pode tirar a CNH.");
elif (idade >= 12):
    print("Pode fazer aulas teóricas.");
else:
    print("Ainda não pode tirar a CNH.");