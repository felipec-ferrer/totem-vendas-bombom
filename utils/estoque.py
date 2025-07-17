import os, json

caminhoEstoqueJSON = "./estoque.json"

def verEstoque():
    os.system('cls')
    estoque = {}

    with open(caminhoEstoqueJSON, 'r') as arquivo:
        estoque = json.load(arquivo)
    
    for key in estoque:
        quantidade = estoque[key]
        print(f"{key}: {quantidade}")
    input("\nPressione enter para continuar")


def gerenciarBombom(entrada, modo):
    os.system('cls')
    dadosCompletos = {}

    if os.path.exists(caminhoEstoqueJSON) == True and os.path.getsize(caminhoEstoqueJSON) > 0:
        verEstoque()
        with open(caminhoEstoqueJSON, 'r') as arquivoLer:
            dadosCompletos = json.load(arquivoLer)

    while entrada == 's':
        bombom = input(f"\nInsira o sabor do bombom para {modo} (aperte [S] para sair): ").lower()
        if bombom == 's':
            return
        else:
            pass

        quantidade = input(f"Insira a quantidade desse bombom para {modo}(aperte [S] para sair): ").lower()
        if quantidade == 's':
            return
        else:
            pass

        while quantidade.isnumeric() == False:
            quantidade = input("Insira uma quantidade válida")

        quantidade = int(quantidade)

        if modo == 'adicionar':
            if bombom not in dadosCompletos:
                dadosCompletos[bombom] = quantidade
            else:
                dadosCompletos[bombom] += quantidade
        elif modo == 'subtrair':
            if bombom in dadosCompletos:
                dadosCompletos[bombom] -= quantidade
            else:
                print("Não existe esse bombom no estoque")
        else:
            print(f"Modo inválido: {modo}")
            
        entrada = input(f"Deseja {modo} mais um sabor?\n[S] - sim / [N] - não ").lower().strip()

    with open(caminhoEstoqueJSON, 'w') as arquivoSalvar:
        json.dump(dadosCompletos, arquivoSalvar)


def tirarBombom():
    dadosCompletos = ''

    verEstoque()
    with open(caminhoEstoqueJSON, 'r') as lerArquivo:
        dadosCompletos = json.load(lerArquivo)
    
    bombom = input("\nInsira o nome exato da opção de bombom que você deseja remover (aperte [S] para sair): ").lower()
    if bombom == 's':
        return
    else:
        pass
    
    dadosCompletos.pop(bombom)
    with open(caminhoEstoqueJSON, 'w') as salvarArquivo:
        json.dump(dadosCompletos, salvarArquivo)
    input("Opção de bombom removido\n\nAperte a tecla enter para voltar")

# função principal desse arquivo
def verificarEstoque():
    os.system('cls')
    entrada = ''

    if os.path.exists(caminhoEstoqueJSON) == False or os.path.getsize(caminhoEstoqueJSON) == 0:
        entrada = input("Não foi encontrado nenhum arquivo do estoque ou o arquivo está vazio. Deseja criar um estoque?\n[S] - Sim\n[N] - Não ").lower().strip()

        while entrada != 's' and entrada != 'n':
            entrada = input("Insira um valor válido: ")
        
        with open(caminhoEstoqueJSON, 'w'):
             pass
        gerenciarBombom(entrada, 'adicionar')
    
    while entrada != 9:
        os.system("cls")
        entrada = int(input("Arquivo de estoque encontrado. O que você deseja fazer?\n[1] - Adicionar bombom no estoque\n[2] - Subtrair bombom do estoque\n[3] - Tirar opção de bombom\n[4] - Ver estoque\n[9] - Voltar\n"))
            
        while entrada < 1 and entrada > 4:
            entrada = int(input("Entrada inválida, insira uma opção válida"))
        
        if (entrada == 1):
            gerenciarBombom('s', 'adicionar')
        elif (entrada == 2):
            gerenciarBombom('s', 'subtrair')
        elif (entrada == 3):
            tirarBombom()
        elif (entrada == 4):
            verEstoque()

def contabilizarEstoque(dadosPedido):
    estoque = None
    with open(caminhoEstoqueJSON, 'r') as arquivo:
        estoque = json.load(arquivo)

    dadosPedido = dadosPedido["bombom"]
    
    for chave in dadosPedido.keys():
        if chave in estoque:
            estoque[chave] -= dadosPedido[chave]
    
    with open(caminhoEstoqueJSON, 'w') as arquivo:
        json.dump(estoque, arquivo)
