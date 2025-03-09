# udp_server.py

import socket
from cpf_validator import is_valid_cpf
from rich import print
from rich.console import Console

console = Console()

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5001         # Porta que o servidor irá escutar no protocolo UDP

def start_udp_server():
    """
    Inicia o servidor UDP, escuta na porta definida (PORT)
    e aguarda mensagens de clientes para validar CPF.
    """
    # Criação do socket UDP (SOCK_DGRAM)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # Permite reutilizar endereço/porta sem problemas de TIME_WAIT
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Associa o socket ao endereço e porta
        server_socket.bind((HOST, PORT))

        console.print(f"[bold green]Servidor UDP aguardando mensagens em {HOST}:{PORT}...[/bold green]")

        while True:
            # Recebe dados (até 1024 bytes) e endereço do cliente
            data, addr = server_socket.recvfrom(1024)
            cpf_recebido = data.decode('utf-8')
            console.print(f"[bold cyan]Recebido de {addr}:[/bold cyan] {cpf_recebido}")

            # Valida o CPF
            if is_valid_cpf(cpf_recebido):
                resposta = "CPF VÁLIDO"
            else:
                resposta = "CPF INVÁLIDO"

            # Envia resposta ao cliente
            server_socket.sendto(resposta.encode('utf-8'), addr)
            console.print(f"[bold magenta]Enviado para {addr}:[/bold magenta] {resposta}")


if __name__ == "__main__":
    start_udp_server()
