import os, time, subprocess, webbrowser
import functions
import estoque 

os.system('cls')
print("Iniciando servidores...")
backend = subprocess.Popen(['python', 'app.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
frontend = subprocess.Popen(['python', '-m', 'http.server', '5500'], cwd=os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.5)
print("Servidores iniciados")
time.sleep(1.5)

parar = ''

while parar != "p":
    os.system('cls')
    entrada = input("\nAVISO: NÃO FECHE O TERMINAL PELO BOTAO X\n\nOlá! Seja bem vindo ao gerenciador de bombons do Mercury\n\n\nO que você deseja fazer? (Insira o número correspondente e aperte enter):\n[1] - Aprovar pagamento\n[2] - Ver pagamentos pendentes\n[3] - Verificar estoque de bombons\n[4] - Ver todos os pedidos\n[A] - Abrir Totem de pedidos\n[P] - Sair\n[Deletar] - Apagar pedidos\n\n").lower().strip()

    os.system('cls')  
    while entrada != "1" and entrada != "2" and entrada != "3" and entrada != "4" and entrada != "a" and entrada != "p" and entrada != "deletar":
        entrada = input("Insira uma entrada válida: ").lower().strip()

    if (entrada == "1"):
        functions.aprovarPagamento(False) # funcional 
    elif (entrada == "2"):
        functions.verPendentes(True) # funcional
    elif (entrada == "3"):
        estoque.verificarEstoque() # funcional
    elif (entrada == "4"):
        functions.mostrarPedidos(True) # funcional
    elif (entrada == 'a'):
        webbrowser.open("http://localhost:5500/pages/index.html") # funcional
    elif (entrada == 'p'):
        parar = functions.encerrarPrograma(backend, frontend) # funcional
    elif (entrada == 'deletar'):
        functions.deletarPedidos() # funcional
