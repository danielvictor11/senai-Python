class Pessoa(object):
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
  
  
    def getNome(self):
        return self.nome
    

class Fisica(Pessoa):
    def __init__(self, nome, cpf):  
        super().__init__(nome,)
        self.cpf = cpf

    def getCPF(self):
        return self.cpf

class Juridica(pessoa):
    def __init__(self,nome,cnpj):
         super().__init__(nome)
         self.cnpj = cnpj

    def getCNPJ(self):
        return self.cnpj

andre = Fisica('Andre dos santos' , '222.222.222.222')
print (andre.nome)
google = Juridica('Google inc', '0001/658.658.245')

print(google.nome)
print(google.cnpj)