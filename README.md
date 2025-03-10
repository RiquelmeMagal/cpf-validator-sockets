# ✅ Validador de CPF - Cliente-Servidor (TCP e UDP)

Este projeto demonstra a validação de CPF em um cenário de **Sistemas Distribuídos**, onde um cliente envia um CPF para o servidor (**via TCP ou UDP**) e recebe a resposta indicando se o CPF é **válido ou inválido**.

## 🏷️ Contexto - Sistemas Distribuídos

No modelo de **cliente-servidor** em **Sistemas Distribuídos**, temos:

- **Servidor**: processo que aguarda requisições (**conexões no TCP ou mensagens no UDP**) em determinada porta.
- **Cliente**: processo que se conecta ao servidor (**TCP**) ou envia mensagens (**UDP**) para solicitar alguma operação — neste caso, a **verificação de um CPF**.

### 🔄 TCP x UDP

- **TCP (Transmission Control Protocol)**: confiável, orientado a conexão, garantindo entrega e ordem dos pacotes.
- **UDP (User Datagram Protocol)**: sem conexão, não garante entrega, mas é mais simples e rápido em cenários que toleram perda ou precisam de **baixa latência**.

---

## 🗂 Estrutura do Projeto

.
├── cpf_validator.py      # Módulo com a lógica de validação de CPF
├── tcp_server.py         # Servidor TCP para validar CPF
├── tcp_client.py         # Cliente TCP para enviar CPF e receber resposta
├── udp_server.py         # Servidor UDP para validar CPF
└── udp_client.py         # Cliente UDP para enviar CPF e receber resposta

---

## 📦 Requisitos

- **Python 3.7+** (ou versão superior)
- Biblioteca padrão do Python (**não precisa instalar nada extra** para usar sockets)
- [Rich](https://pypi.org/project/rich/) (opcional, para formatação de terminal)

---
## 🐍 Criação do Ambiente Virtual

Para isolar dependências, recomenda-se criar um **ambiente virtual** em Python.

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

- `python3 -m venv venv` cria o ambiente virtual na pasta `venv`.
- `source venv/bin/activate` ativa o ambiente.

### Windows

```bash
python -m venv venv
.env\Scripts\activate
```

- `python -m venv venv` cria o ambiente virtual.
- `.env\Scripts\activate` ativa o ambiente no **Windows** (PowerShell ou CMD).

## 📦 Instalação de Dependências

Com o ambiente virtual ativo, instale as dependências:

```bash
pip install -r requirements.txt
```

Caso não tenha o arquivo `requirements.txt`, você pode instalar manualmente:

## 📥 Como Obter o Projeto

Se estiver usando **Git**, clone o repositório:

git clone git@github.com:RiquelmeMagal/cpf-validator-sockets.git
cd cpf-validator-sockets


Caso contrário, basta baixar o projeto como arquivo `.zip`, descompactar e entrar na pasta.

---

## 🚀 Execução

O projeto oferece duas formas de rodar (**TCP ou UDP**). Você pode testar qualquer um deles.

> **Observação**:  
> Agora o cliente TCP faz um loop para permitir o envio de vários CPFs **na mesma execução** (e o servidor aceita cada um). Para sair, basta digitar **exit** no cliente.

### 1️⃣ Versão TCP

**Executar o Servidor TCP:**

```bash
python tcp_server.py
```

O servidor exibirá:

```bash
Servidor TCP aguardando conexões em 127.0.0.1:5000...
```

Isso significa que está pronto para receber conexões TCP na porta **5000**.

**Executar o Cliente TCP:**

```bash
python tcp_client.py
```

Você verá:

```bash
Conectado ao servidor TCP em 127.0.0.1:5000
Digite o CPF (apenas números ou com pontuação, ex: 123.456.789-09):
```

Digite um CPF válido ou inválido e veja a resposta do servidor. Repita quantas vezes quiser. Para encerrar, digite **exit**.

---

### 2️⃣ Versão UDP

**Executar o Servidor UDP:**

```bash
python udp_server.py
```

O servidor exibirá:

```bash
Servidor UDP aguardando mensagens em 127.0.0.1:5001...
```

**Executar o Cliente UDP:**

```bash
python udp_client.py
```

Digite o CPF e pressione **Enter** para enviá-lo ao servidor via **UDP**. O servidor responderá com:

```bash
CPF VÁLIDO ou CPF INVÁLIDO
```

---

## 🔍 O que está acontecendo?

### **Sockets:**
- Em Python, criamos sockets usando:
  - **TCP**: `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  - **UDP**: `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`

### **Servidor (TCP):**
1. Associa-se à porta escolhida (`bind((HOST, PORT))`).
2. Aguarda conexões (`listen()`) e aceita (`accept()`).
3. Recebe CPF, valida e responde ao cliente.

### **Cliente (TCP):**
1. Conecta-se ao servidor (`connect((HOST, PORT))`).
2. Envia o CPF (`sendall()`).
3. Recebe a resposta (`recv()`).

### **Servidor (UDP):**
1. Escuta a porta (`bind((HOST, PORT))`).
2. Recebe CPF do cliente (`recvfrom()`).
3. Valida e responde (`sendto()`).

### **Cliente (UDP):**
1. Envia CPF ao servidor (sendto()).
2. Aguarda resposta (recvfrom()).
3. Também usa um **loop** para permitir múltiplos envios até digitar exit.

### **Validação do CPF:**
- Remove caracteres não numéricos.
- Verifica se tem **11 dígitos**.
- **Evita sequências repetidas**.
- Calcula os **dígitos verificadores**.

---

## ⚙️ Exemplos de Execução

### **Servidor TCP**
```bash
python tcp_server.py
Servidor TCP aguardando conexões em 127.0.0.1:5000...
```

### **Cliente TCP**
```bash
python tcp_client.py
Conectado ao servidor TCP em 127.0.0.1:5000
Digite o CPF (apenas números ou com pontuação, ex: 123.456.789-09): 12345678909
Resposta do servidor: CPF VÁLIDO
```

### **Servidor UDP**
```bash
python udp_server.py
Servidor UDP aguardando mensagens em 127.0.0.1:5001...
```

### **Cliente UDP**
```bash
python udp_client.py
Digite o CPF (ou 'exit' para sair): 11111111111
Resposta do servidor: CPF INVÁLIDO
```

---

## 🏆 Conclusão

Este projeto ilustra o uso de **sockets em Python** para criar aplicações de **Sistemas Distribuídos**, onde um cliente e um servidor trocam mensagens para **validar um CPF**. Foram apresentadas duas versões:
- **TCP**: Mais confiável, pois é **orientado a conexão**.
- **UDP**: Menos confiável, mas **mais rápido e leve**.

Agora os **clientes** (TCP e UDP) fazem **loop** para envio de vários CPFs, podendo encerrar a execução com exit. O servidor (especialmente no TCP) também pode ficar pronto para atender várias requisições consecutivas.

### 📝 Dicas:
- Você pode rodar **várias instâncias** do cliente conectando-se ao mesmo servidor.
- Teste em **máquinas diferentes** (ajuste HOST para o IP real do servidor).
- Sinta-se à vontade para **adicionar logs, melhorar validações ou integrar esse sistema a outras aplicações distribuídas**.

Boa prática e **bons estudos em Sistemas Distribuídos!** 🚀
