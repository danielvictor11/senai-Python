#Nome: Daniel Victor Santos Basilio

class Pet(object):
    def __init__(self,nome,anoNasc):
        self.nome = nome  # criando um atributo nome
        self.anoNasc = anoNasc
        print( f'Parabens sou {self.nome} seu novo Pet')
   
    def getIdade(self):
        idade = 2024 - self.anoNasc
        return idade
   
    def setAnoNasc(self,anoNasc):
        self.anoNasc = anoNasc
        return None
   
    def setPeso(self,peso):
        self.peso = peso
      #----------------classe cachorro--------------------------------------------------------
class Cachorro(Pet):
    def __init__(self, nome, anoNasc):
        super().__init__(nome, anoNasc)
   
    def som(self):
        print(f'{self.nome} late')


    #--------------classe gato----------------------------------------------------------------
class Gato(Pet):
    def __init__(self, nome, anoNasc):
        super().__init__(nome, anoNasc)
    def som(self):
         print(f'{self.nome} mia')
       #------------------------------classe Peixe---------------------------------------------------------------
class Peixe(Pet):
    def __init__(self, nome, anoNasc):
        super().__init__(nome, anoNasc)
    def som(self):
        print(f'{self.nome} Glub Glub')
    
print('==================','Instanciando gato , cachorro e peixe','==================')


caramelo = Cachorro('caramelo',2015)
frajola = Gato('Frajola',2017)
print('idade caramelo',caramelo.getIdade())
print('idade frajola:',frajola.getIdade())
caramelo.som()
frajola.som()     
garri = Peixe('garri',2001)
print('idade garri: ',garri.getIdade())
garri.som