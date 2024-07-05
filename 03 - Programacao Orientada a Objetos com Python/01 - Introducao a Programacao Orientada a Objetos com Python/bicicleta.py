class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Bibi bibi")

    def parar(self):
        print("Parada")

    def correr(self):
        print("Correndo")

    def trocar_marcha(self, numero_marcha):
        print(numero_marcha)
        print("Marcha trocada ...")
    
    # não é comum em python
    #def get_cor(self):
    #    return self.cor

    #def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bike1 = Bicicleta("Vermelha", "Caloi", "2022", 600);
bike1.buzinar()
bike1.parar()
bike1.correr()
print(bike1.cor, bike1.modelo, bike1.ano, bike1.valor);

b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2) # igual a b2.buzinar()
#print(b2.get_cor()) -> não é comum em python

print(b2);
b2.trocar_marcha(5)


