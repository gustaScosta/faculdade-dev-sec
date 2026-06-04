## Exercício 2 — Escopo LEGB
# variavel = "global"

# def externa():
#     variavel = "enclosing"
    
#     def interna():
#         variavel = 'local'
#         print(variavel)
    
#     interna()
#     print(variavel)

# externa()
# print(variavel)

## Exercício 3 — Funções como objetos

lista = [10 + 10,
         10 - 10,
         10 * 10,
         ]

def aplicar_todas():
    print(lista)
    

aplicar_todas()