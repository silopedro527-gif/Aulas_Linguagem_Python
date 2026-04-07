from collections import deque 
class Fila: 
   def __init__(self): 
      self._itens = deque() 
   def enqueue(self, item): 
      self._itens.append(item) 
   def dequeue(self): 
      if not self.is_empty(): 
        return self._itens.popleft() 
      else: 
         raise IndexError("Fila vazia!") 
   def front(self): 
      if not self.is_empty(): 
         return self._itens[0] 
      else: 
          raise IndexError("Fila vazia!") 
   def is_empty(self): 
        return len(self._itens) == 0 
   def size(self): 
        return len(self._itens) 
# Exemplo de uso 
f = Fila() 
f.enqueue("Tarefa A") 
f.enqueue("Tarefa B") 
f.enqueue("Tarefa C") 
print(f"Fila: {list(f._itens)}") # Saída: Fila: ["Tarefa A", "Tarefa B", "Tarefa C"] 
print(f"Frente da fila: {f.front()}") # Saída: Frente da fila:Tarefa A 
print(f"Dequeue: {f.dequeue()}") # Saída: Dequeue: Tarefa A 
print(f"Fila: {list(f._itens)}") # Saída: Fila: ["Tarefa B", "Tarefa C"] 