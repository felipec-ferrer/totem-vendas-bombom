import json, os, time

pastaPedidos = "./pedidos"

def salvarPedido(dadosPedido):
    id = len(os.listdir(pastaPedidos)) + 1
    nomeArquivo = f'pedido#{id:03}.json'
    
    dadosPedido["id"] = str(id)
    dadosPedido["statusPagamento"] = "pendente"

    caminhoArquivo = os.path.join(pastaPedidos, nomeArquivo)
    print(caminhoArquivo)

    with open(caminhoArquivo, 'w') as salvar:
        json.dump(dadosPedido, salvar)


def encerrarPrograma(backend, frontend):
    print("Encerrando servidores...")
    backend.terminate()
    time.sleep(1.5)
    frontend.terminate()
    print("Finalizado com sucesso. Até outro dia!")
    time.sleep(1.5)
    return 'p'

def listarPedidos():
    pedidos = []
    for i in os.listdir(pastaPedidos):
        pedidos.append(i)
    return pedidos

def printarPedido(pedido):
    sabores = pedido['bombom']
    print(f"\nPedido#{int(pedido['id']):03d}\n   Nome: {pedido['nomeCliente']}\n   Pedido:")
    for sabor in sabores:
        if sabores[sabor] == 0:
            pass
        else:
            print(f"     - {sabor}: {sabores[sabor]}")
    print(f"   Total: R${pedido['valorTotal']}.00\n\n--------------------------------------")

def mostrarPedidos(voltar):
    pedidos = listarPedidos()
    for i in pedidos:
        with open(f"{pastaPedidos}/{i}", 'r') as arquivo:
            pedido = json.load(arquivo)
        printarPedido(pedido)
    
    if voltar == True:
        input("Aperte a tecla [Enter] para voltar")
    else:
        input("Aperte a tecla [Enter] para continuar")

def verPendentes(somenteLer):
    entrada = 'a'
    pedidos = listarPedidos()
    controle = False

    while entrada == 'a':
        os.system('cls')
        for i in pedidos:
            with open(f"{pastaPedidos}/{i}") as arquivo:
                pedido = json.load(arquivo)
            if pedido['statusPagamento'] == 'pendente':
                printarPedido(pedido)
                controle = True
            else:
                pass
        
        if controle == False:
            input("Nenhum pedido pendente encontrado. Aperte [Enter] para voltar")
            return

        if somenteLer == False:
            entrada = input("\nDeseja atualizar os pedidos, aprovar um pagamento ou voltar? [A] - Atualizar / [C] - Aprovar pagamento / [P] - Voltar \n").lower().strip()
            while entrada != 'a' and entrada != 'p' and entrada != 'c':
                entrada = input("Entrada inválida. Insira uma entrada válida: ")
        else:
            input("Aperte a tecla [Enter] para voltar")
            entrada = 'p'
        
        if entrada == 'p':
            return 'n'
        elif entrada == 'c':
            return 's'
        else:
            pass
            

def aprovarPagamento(somenteAprovar):
    condicao = 's'

    if somenteAprovar == False:
        condicao = verPendentes(False)
        if condicao == 'n':
            return
        else:
            pass
    else:
        pass

    while condicao == 's':
        pedidos = listarPedidos()
        cont = 0
        
        codigo = input("\nQual o número do pedido? Desconsidere os '0's\nPedido: ").lower().strip()
        for i in pedidos:
            with open(f"{pastaPedidos}/{i}", 'r') as arquivo:
                pedido = json.load(arquivo)
            if codigo == pedido['id'] and pedido['statusPagamento'] == 'pendente':
                printarPedido(pedido)
                entrada = input("\nDeseja confirmar o pagamento? [s] - Sim / [n] - Não ").lower().strip()
                while entrada != 's' and entrada != 'n':
                    entrada = input("Entrada inválida. Insira uma entrada válida: ")

                if entrada == 's':
                    pedido['statusPagamento'] = 'aprovado'
                    with open(f"{pastaPedidos}/{i}", 'w') as arquivo:
                        json.dump(pedido, arquivo)
                cont += 1
            else:
                pass
            
        if cont == 0:
            condicao = input("Nenhum pedido encontrado com essa busca\nVocê deseja buscar por outro código? [s] - Sim / [n] - Não ").lower().strip()
        else:
            condicao = input("Você deseja aprovar outro pagamento? [s] - Sim / [n] - Não ").lower().strip()
        while condicao != 's' and condicao != 'n':
            condicao = input("Entrada inválida. Insira uma entrada válida: ").lower().strip()

    
def deletarPedidos():
    os.system('cls')
    entrada = input("Você tem certeza que deseja apagar todos os pedidos? Essa ação não pode ser desfeita\n[S] - Sim, desejo apagar / [N] - Não, não desejo apagar\n")

    while entrada != 's' and entrada != 'n':
        entrada = input("Entrada inválida. Insira uma entrada válida: ")
    
    if entrada == 's':
        entrada = input("\nVocê realmente tem certeza? Essa ação NÃO tem volta\n[S] - Sim, desejo apagar / [N] - Não, não desejo apagar ")
        if entrada == 's':
            print("\nApagando os pedidos.", end='')
            time.sleep(1)
            print(".", end='')
            time.sleep(1)
            print(".")
            
            pedidos = listarPedidos()
            for i in pedidos:
                os.remove(f"{pastaPedidos}/{i}")
            os.system('cls')
            print("Pedidos excluídos. Voltando ao menu principal...")
            time.sleep(2)

