class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_a_partir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


#p = Pessoa("Bento", 10);
#print(p.nome, p.idade)

p2 = Pessoa.criar_a_partir_data_nascimento(2008, 11, 5, "Bento");
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))