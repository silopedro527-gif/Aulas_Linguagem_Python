class NoArvore: 
  def __init__(self, valor): 
     self.valor = valor 
     self.esquerda = None 
     self.direita = None 
class ArvoreBuscaBinaria: 
   def __init__(self): 
     self.raiz = None 
   def inserir(self, valor): 
      if self.raiz is None: 
        self.raiz = NoArvore(valor) 
      else: 
        self._inserir_recursivo(self.raiz, valor) 
   def _inserir_recursivo(self, no_atual, valor): 
      if valor < no_atual.valor: 
         if no_atual.esquerda is None: no_atual.esquerda = NoArvore(valor) 
         else: 
             self._inserir_recursivo(no_atual.esquerda, valor) 
      elif valor > no_atual.valor: 
          if no_atual.direita is None: no_atual.direita = NoArvore(valor) 
          else: 
             self._inserir_recursivo(no_atual.direita, valor) 
# Ignora valores duplicados 
   def buscar(self, valor): 
      return self._buscar_recursivo(self.raiz, valor) 
   def _buscar_recursivo(self, no_atual, valor): 
      if no_atual is None or no_atual.valor == valor: 
         return no_atual is not None 
      elif valor < no_atual.valor: 
          return self._buscar_recursivo(no_atual.esquerda, valor) 
      else: 
          return self._buscar_recursivo(no_atual.direita, valor) 
   def em_ordem(self): 
             """Percorre a árvore em ordem (esquerda, raiz, direita) - retorna elementos ordenados.""" 
             elementos = [] 
             self._em_ordem_recursivo(self.raiz, elementos) 
             return elementos
   def _em_ordem_recursivo(self, no_atual, elementos): 
      if no_atual: 
        self._em_ordem_recursivo(no_atual.esquerda, elementos) 
        elementos.append(no_atual.valor) 
        self._em_ordem_recursivo(no_atual.direita, elementos) 
# Exemplo de uso 
ab = ArvoreBuscaBinaria() 
ab.inserir(50) 
ab.inserir(30) 
ab.inserir(70) 
ab.inserir(20) 
ab.inserir(40) 
ab.inserir(60) 
ab.inserir(80) 
print(f"Elementos em ordem: {ab.em_ordem()}") # Saída: Elementos em ordem: [20, 30, 40, 50, 60, 70, 80] 
print(f"Buscar 40: {ab.buscar(40)}") # Saída: Buscar 40: True 
print(f"Buscar 90: {ab.buscar(90)}") # Saída: Buscar 90: False