# lendo o bando de dados
from ast import iter_child_nodes

def ler_banco():
    """Essa função lê um banco de dados"""
    with open("estoque.csv", "r") as file:
        dados_do_banco = file.read()
        dados_do_banco.split("\n") # pegando os dados do banco em formato de texto
        dados_do_estoque = dados_do_banco.split("\n")  # quebrando em linas
        menu = dados_do_estoque[0].split(",")
        quantidades_no_estoque = dados_do_estoque[1].split(",")
        return menu, quantidades_no_estoque
 

itens_menu  =  ler_banco()[0]
estoque_menu  =  ler_banco()[1]      

print("Faça seu pedido: ")
for posicao, item in enumerate(itens_menu):
    print(f"[{posicao + 1}] - {item}")

pedido = int(input(">>> ")) # input sempre retorna texto

tamanho_menu = len(itens_menu) # len sempre retorna numeros inteiros

if pedido > tamanho_menu or pedido < 1:
    print("Opção inválida")

pedido = pedido - 1 # tirando a mascara do input + 1 (ou pedido -=1)
estoque_menu[pedido] = str(int(estoque_menu[pedido]) - 1) # salve o resultado em uma variavel

with open("estoque.csv", "w") as file:
    file.write(",".join(itens_menu))
    file.write("\n")
    file.write(",".join(estoque_menu))
    

