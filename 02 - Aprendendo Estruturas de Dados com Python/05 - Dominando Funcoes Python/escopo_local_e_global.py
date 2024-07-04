salario = 2000;

def salario_bonus(bonus, lista):
    lista_auxiliar =  lista.copy();
    lista_auxiliar.append(2);

    print(f"Lista auxiliar: {lista_auxiliar}");
    global salario;
    salario += bonus;
    return salario;


lista = [1];
salario_bonus(500, lista);
print(f"Salário atualizado: {salario}");
print(lista);