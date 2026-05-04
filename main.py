from colorama import Fore, Style, init

# Inicializa o colorama (importante para Windows)
init(autoreset=True)

print("=== SISTEMA DE MONITORAMENTO DE ÁGUA ===\n")

# Lista de níveis (conforme solicitado)
niveis = [1, 2, 3, 4, 5]

def exibir_status(nivel):
    """
    Define a cor e a mensagem com base no nível e imprime no terminal.
    O uso de autoreset=True no init() dispensa o Style.RESET_ALL manual.
    """
    if nivel == 1:
        print(f"{Fore.RED}Nível 1: Muito baixo (CRÍTICO)")
    elif nivel == 2:
        print(f"{Fore.YELLOW}Nível 2: Baixo")
    elif nivel == 3:
        print(f"{Fore.GREEN}Nível 3: Médio")
    elif nivel == 4:
        print(f"{Fore.CYAN}Nível 4: Alto")
    elif nivel == 5:
        print(f"{Fore.BLUE}Nível 5: Muito alto (ALERTA)")

# Simulação percorrendo a lista
for n in niveis:
    exibir_status(n)

# Garantia extra de restauração do padrão
print(Style.RESET_ALL + "\nMonitoramento finalizado.")
