# tcp_client.py

import socket
from rich import print
from rich.console import Console

console = Console()

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5000         # Porta do servidor

def run_tcp_client():
    """
    Conecta ao servidor TCP, envia um CPF para validação
    e exibe a resposta recebida em um loop até o usuário digitar 'exit'.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        console.print(f"[bold green]Conectado ao servidor TCP em {HOST}:{PORT}[/bold green]")

        while True:
            cpf_input = console.input("[bold cyan]Digite o CPF (ou 'exit' para sair): [/bold cyan] ")

            if cpf_input.lower() == 'exit':
                console.print("[bold yellow]Saindo do cliente...[/bold yellow]")
                break

            # Envia dados
            client_socket.sendall(cpf_input.encode('utf-8'))

            # Recebe resposta do servidor
            resposta = client_socket.recv(1024).decode('utf-8')
            console.print(f"[bold magenta]Resposta do servidor:[/bold magenta] {resposta}")


if __name__ == "__main__":
    run_tcp_client()
