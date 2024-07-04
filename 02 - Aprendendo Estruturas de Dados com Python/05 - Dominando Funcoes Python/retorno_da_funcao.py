def calcular_total(numeros):
    return sum(numeros);

def retorna_antecessor_e_sucesso(numero):
    antecessor = numero - 1;
    sucessor = numero + 1;
    return antecessor, sucessor;

def func_3():
    print("Olá mundo!");

print(calcular_total([10, 20, 34]));
print(retorna_antecessor_e_sucesso(10));
print(func_3());