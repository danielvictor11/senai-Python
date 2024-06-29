class Cachorro(object):
    def __init__(self,nome,anoNasc):
        self.nome = nome
        self.anoNasc = anoNasc
        print( f'Parabens  sou {self.nome}  seu novo cachorro')
        

    def som(self):
        print(f'{self.nome} late')

    def getIdade(self):
        return 2024 - self.anoNasc
    
    def setAnoNasc(self,ano):
        self.anoNasc = ano

    def setPeso(self ,peso):
            self.peso = peso

caramelo = Cachorro('caramelo', 2010)
caramelo.som()
#idadeCaramelo = caramelo.getIdade()
#print('idade :' , idadeCaramelo)
caraDeChinelo = Cachorro('cara de chinelo', 2022)
#caraDeChinelo.som()
print('idade :' , caraDeChinelo.getIdade())
caraDeChinelo.setAnoNasc(2023)
print('idade :' , caraDeChinelo.getIdade)
caraDeChinelo.anoNasc = 2021
print('idade :' ,caraDeChinelo.getIdade)
print('ano nascimento :', caraDeChinelo.anoNasc)
caraDeChinelo.setPeso(500)
print(caraDeChinelo.peso)
caraDeChinelo.cor = 'azul'
print(caraDeChinelo.cor)

class Gato(object):
    def __init__(self,nome, anoNasc):
        self.nome = nome
        self.anoNasc = anoNasc
        print(f'parabens sou {self.nome} seu novo gato')  

    def som(self):
            print(f'{self.nome} mia')  

    def getIdade(self):
     return 2024 - self.anoNasc
            
moon = Gato('Moon' , 2009)
moon.som()
idadeMonn = moon.getIdade()
print('idade :' , idadeMonn)       
lina = Gato('Lina' , 2023)
lina.som()   
idadeLina = lina.getIdade()
print("idade :" , idadeLina)