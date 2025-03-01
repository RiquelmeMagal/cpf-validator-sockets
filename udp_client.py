# udp_client.py

import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5001         # Porta do servidor

def run_udp_client():
    """
    Envia um CPF para o servidor UDP e aguarda a resposta
    de validação de CPF.
    """
    # Criação do socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        cpf_input = input("Digite o CPF (apenas números ou com pontuação, ex: 123.456.789-09): ")
        
        # Envia dados ao servidor (não há 'connect' para UDP)
        client_socket.sendto(cpf_input.encode('utf-8'), (HOST, PORT))

        # Aguarda a resposta do servidor
        data, _ = client_socket.recvfrom(1024)
        resposta = data.decode('utf-8')
        print("Resposta do servidor:", resposta)


if __name__ == "__main__":
    run_udp_client()
