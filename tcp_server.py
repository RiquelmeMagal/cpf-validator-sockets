# tcp_server.py

import socket
from cpf_validator import is_valid_cpf
from rich import print
from rich.console import Console

console = Console()

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5000         # Porta que o servidor irá escutar

def start_tcp_server():
    """
    Inicia o servidor TCP, escuta na porta definida (PORT)
    e aguarda conexões de clientes para validar CPF.
    """
    # Criação do socket TCP (SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Permite reutilizar endereço/porta sem problemas de TIME_WAIT
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Associa o socket a um endereço IP e porta
        server_socket.bind((HOST, PORT))
        
        # Coloca o socket em modo de escuta
        server_socket.listen(1)

        console.print(f"[bold green]Servidor TCP aguardando conexões em {HOST}:{PORT}...[/bold green]")

        while True:
            # Aguarda conexão de um cliente
            conn, addr = server_socket.accept()
            console.print(f"[bold cyan]Conexão estabelecida com {addr}[/bold cyan]")

            # Trata a conexão em bloco 'with' para garantir fechamento
            with conn:
                # Recebe os dados (CPF) em bytes e decodifica para string
                data = conn.recv(1024).decode('utf-8')

                if not data:
                    console.print("[bold yellow]Nenhum dado recebido. Encerrando conexão...[/bold yellow]")
                    break

                # Valida o CPF
                if is_valid_cpf(data):
                    resposta = "CPF VÁLIDO"
                else:
                    resposta = "CPF INVÁLIDO"

                # Envia a resposta ao cliente
                conn.sendall(resposta.encode('utf-8'))
                console.print(f"[bold magenta]Enviado para {addr}: {resposta}[/bold magenta]")


if __name__ == "__main__":
    start_tcp_server()
