from functools import reduce 
def calcular_expressao(operacoes): 
# operacoes é uma lista de tuplas: [(operador, valor), ...] 
# Ex: [("+", 5), ("*", 2), ("-", 3)] 
 def aplicar_operacao(acumulador, operacao_item): 
  operador, valor = operacao_item 
  if operador == "+": 
   return acumulador + valor 
  elif operador == "-": 
   return acumulador - valor 
  elif operador == "*": 
   return acumulador * valor 
  elif operador == "/": 
    if valor == 0: 
       raise ValueError("Divisão por zero!") 
    return acumulador / valor 
  else: 
      raise ValueError(f"Operador desconhecido: {operador}") 