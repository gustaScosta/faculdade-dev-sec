# # Identidade de objetos - cada objeto tem um ID único na memória
# x = [1, 2, 3]
# y = x           # y aponta para o mesmo objeto 
# z = [1, 2, 3]   # z é um novo objeto diferente 

# print(id(x))    #endereço de memória do objeto x
# print(id(y))    #endereço de memória do objeto y (mesmo que x)
# print(id(z))    #endereço de memória do objeto z (diferente de x e y)

# print(x is y)   # comparação de identidade (True, pois x e y são o mesmo objeto)
# print(x is z)   # comparação de identidade (False, pois x e z são objetos diferentes)
# print(x == z)   # comparação de valor (True, pois os valores dos objetos são iguais)

# y.append(4)    # Modificando o objeto através de y
# print(x)       # x também é afetado, pois x e y são o mesmo objeto
# print(z)       # z permanece inalterado, pois é um objeto diferente

