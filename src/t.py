class Funcionario:
    def __init__(self,nome,data,sexo):
        self.nome = nome
        self.data = data
        self.sexo = sexo


f1 = Funcionario("JH","07/11/2008","M")
f2 = Funcionario("HJ","24/11/1964","M")
f3 = Funcionario("MA","13/06/1968","F")


lista_1= [f1,f2,f3]

for contagem,item in enumerate(lista_1):
    print(contagem,item.nome)

# for i in range(len(lista_1)):
#     if lista_1[i].nome == "JH":
#         print('Certo',lista_1[i].nome)
#     else:
#         print('Errado')