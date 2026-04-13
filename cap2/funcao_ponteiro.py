def somar_tudo(*numeros): 
    total = 0 
    for num in numeros: 
        total += num 
    return total 
print(somar_tudo(1, 2, 3))
