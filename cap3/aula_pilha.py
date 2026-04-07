class Pilha: 
    def __init__(self): 
       self._itens = [] 
    def push(self, item): 
       self._itens.append(item) 
    def pop(self): 
        if not self.is_empty(): 
            return self._itens.pop() 
        else: 
            raise IndexError("Pilha vazia!") 
    def peek(self): 
        if not self.is_empty(): 
            return self._itens[-1] 
        else: 
            raise IndexError("Pilha vazia!") 
    def is_empty(self): 
        return len(self._itens) == 0 
    def size(self): 
        return len(self._itens) 
# Exemplo de uso 
p = Pilha() 
p.push(10) 
p.push(20) 
p.push(30) 
print(f"Pilha: {p._itens}") # Saída: Pilha: [10, 20, 30] 
print(f"Topo da pilha: {p.peek()}") # Saída: Topo da pilha: 30 
print(f"Pop: {p.pop()}") # Saída: Pop: 30 
print(f"Pilha: {p._itens}") # Saída: Pilha: [10, 20]