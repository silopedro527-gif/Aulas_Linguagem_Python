"""estudantes = [ 
{"nome": "Ana", "idade": 21, "curso": "Eng. Informática"}, 
{"nome": "Bruno", "idade": 19, "curso": "Gestão"}, 
{"nome": "Carla", "idade": 22, "curso": "Eng. Civil"}, 
{"nome": "Daniel", "idade": 20, "curso": "Eng. Informática"} 
#Tp
#criar uma lista de forma dinaminica em vez de estática.
] 
# Usando compreensão de lista para filtrar e transformar 
nomes_estudantes_maiores_20 = [estudante["nome"].upper()  
for estudante in estudantes  
if estudante["idade"] > 20] 
print(f"Nomes dos estudantes com mais de 20 anos: {nomes_estudantes_maiores_20}") 
# Saída esperada: ['ANA', 'CARLA'] 
# Mudar a forma do exercício 
"""

estudante=[]
n=int(input("digite o valor de n: "))
for i in range (n):
   
     novo_estudante={
         "Nome": input("informe o nome: "),
         "Idade": int(input("informe a idade: ")),
         "curso": input("Informe o curso: "),
    }
     print("\n")

estudante.append(novo_estudante)

for e in estudante:
     if e["Idade"] > 18:
          print(e)
   



 