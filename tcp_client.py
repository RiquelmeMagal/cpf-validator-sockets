# tcp_client.py

import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5000         # Porta do servidor

def run_tcp_client():
    """
    Conecta ao servidor TCP, envia um CPF para validação
    e exibe a resposta recebida.
    """
    # Criação do socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Conecta ao servidor
        client_socket.connect((HOST, PORT))
        print(f"Conectado ao servidor TCP em {HOST}:{PORT}")

        # Solicita CPF do usuário
        cpf_input = input("Digite o CPF (apenas números ou com pontuação, ex: 123.456.789-09): ")

        # Envia dados
        client_socket.sendall(cpf_input.encode('utf-8'))

        # Recebe resposta do servidor
        resposta = client_socket.recv(1024).decode('utf-8')
        print("Resposta do servidor:", resposta)


if __name__ == "__main__":
    run_tcp_client()
