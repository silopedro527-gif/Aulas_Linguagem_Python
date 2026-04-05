import re
from collections import Counter

def analisar_frequencia_palavra (texto, num_palavras=5):
    texto_limpo =re.sub(r'[^\w\s]','', texto).lower()
    
    palavras=texto_limpo.split()

    frequencia=Counter(palavras)

    texto_exemplo="Python é uma  linguagem de programação muito poderosa." \
    "Python é facil de aprender e usar. Programação com Python é divertida ! "

    resultado=analisar_frequencia_palavra(texto_exemplo,3)
    for palavras, contagem in resultado:
       print(f"- {palavras}: {contagem}")