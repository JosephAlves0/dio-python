from abc import ABC, abstractmethod

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")
        print("TV ligada")
    
    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada")
    
    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ar Condicionado ligado")
    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Ar Condicionado desligado")
    
    @property
    def marca(self):
        return "Samsung"
    


controle = ControleTV();
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleArCondicionado();
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)
