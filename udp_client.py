# udp_client.py

import socket
from rich import print
from rich.console import Console

console = Console()

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5001         # Porta do servidor

def run_udp_client():
    """
    Envia CPF para o servidor UDP em um loop até o usuário digitar 'exit'.
    Aguarda a resposta de validação de CPF e exibe.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            cpf_input = console.input("[bold cyan]Digite o CPF (ou 'exit' para sair): [/bold cyan] ")

            if cpf_input.lower() == 'exit':
                console.print("[bold yellow]Saindo do cliente...[/bold yellow]")
                break

            # Envia dados ao servidor UDP
            client_socket.sendto(cpf_input.encode('utf-8'), (HOST, PORT))

            # Aguarda a resposta do servidor
            data, _ = client_socket.recvfrom(1024)
            resposta = data.decode('utf-8')
            console.print(f"[bold magenta]Resposta do servidor:[/bold magenta] {resposta}")


if __name__ == "__main__":
    run_udp_client()
