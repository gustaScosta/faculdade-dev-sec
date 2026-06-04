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

# ERRADO — armadilha de mutabilidade
# def adicionar_item(item, lista=[]):
#     lista.append(item)
#     return lista

# print(adicionar_item("a"))  # ['a']
# print(adicionar_item("b"))  # ['a', 'b'] ← esperava ['b']!
# print(adicionar_item("c"))  # ['a', 'b', 'c'] ← bug!

# # Por quê? O argumento padrão [] é criado UMA VEZ quando a função é definida.
# # A mesma lista é reutilizada em cada chamada.

# # CORRETO
# def adicionar_item(item, lista=None):
#     if lista is None:
#         lista = []
#     lista.append(item)
#     return lista

# def saudar(nome):
#     return f"Olá, {nome}!"

# def executar(funcao, valor):
#     return funcao(valor)  # recebe uma função como argumento

# resultado = executar(saudar, "Engenheiro")
# print(resultado)  # "Olá, Engenheiro!"

# # Isso é a base dos decorators, callbacks, e muito do que
# # frameworks web como FastAPI e Flask usam internamente.