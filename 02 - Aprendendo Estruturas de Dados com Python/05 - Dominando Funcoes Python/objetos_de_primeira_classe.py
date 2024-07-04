def somar(a, b):
    return a + b;


def subtrair(a,b):
    return a - b;


def exibir_resultados(a, b, funcao):
    resultado = funcao(a, b);
    print(f"O resultado da operação é = {resultado}");

exibir_resultados(10, 5, somar);
exibir_resultados(10, 5, subtrair);

op = somar;

print(op (1, 23))