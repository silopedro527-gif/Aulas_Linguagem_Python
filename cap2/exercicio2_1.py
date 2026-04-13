"""pessoas = [ 
{"nome": "Ana", "idade": 30}, 
{"nome": "Bruno", "idade": 25}, 
{"nome": "Carla", "idade": 30}, 
{"nome": "Daniel", "idade": 25}, 
{"nome": "Eduardo", "idade": 35} 
] 
# Ordenar usando uma função lambda com múltiplos critérios 
pessoas_ordenadas = sorted(pessoas, key=lambda p: (p["idade"], 
p["nome"])) 
print("\n--- Pessoas Ordenadas ---") 
for pessoa in pessoas_ordenadas: 
  print(pessoa) """

pessoas=[]
n=int(input("infome o número de pessoas a constar na lista: "))
for i in range (n):
  novas_pessoas={
    "nome":input(" digite o nome: "),
    "Idade":int(input("informa a idade: ")),

  }

pessoas.append(novas_pessoas)

#Ordenar usando uma função lambda com múltiplos critérios 
pessoas_ordenadas = sorted(pessoas, key=lambda p: (p["Idade"], 
p["nome"])) 
print("\n--- Pessoas Ordenadas ---") 
for pessoa in pessoas_ordenadas: 
  print(pessoas)