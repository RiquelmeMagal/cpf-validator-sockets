# cpf_validator.py

def is_valid_cpf(cpf: str) -> bool:
    """
    Verifica se um CPF é válido.
    
    Regras de validação (padrão no Brasil):
      1. CPF deve ter 11 dígitos após remover caracteres não numéricos.
      2. Não pode ser uma sequência de dígitos repetidos (ex: 11111111111).
      3. Cálculo dos dígitos verificadores conforme algoritmo oficial:
         - Primeiro dígito verificador:
           * Multiplicar os 9 primeiros dígitos respectivamente por 10, 9, ..., 2
           * Somar resultados
           * Digito1 = (resultado * 10) % 11
           * Se der 10, o dígito é 0
         - Segundo dígito verificador:
           * Multiplicar os 10 primeiros dígitos (incluindo o primeiro dígito verificador) 
             respectivamente por 11, 10, ..., 2
           * Somar resultados
           * Digito2 = (resultado * 10) % 11
           * Se der 10, o dígito é 0
    """
    # Removendo caracteres não numéricos
    cpf_numerico = ''.join([char for char in cpf if char.isdigit()])

    # Verifica se tem 11 dígitos
    if len(cpf_numerico) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf_numerico == cpf_numerico[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i, peso in enumerate(range(10, 1, -1)):
        soma += int(cpf_numerico[i]) * peso
    primeiro_digito = (soma * 10) % 11
    primeiro_digito = 0 if primeiro_digito == 10 else primeiro_digito

    # Verifica se o primeiro dígito confere
    if primeiro_digito != int(cpf_numerico[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i, peso in enumerate(range(11, 1, -1)):
        soma += int(cpf_numerico[i]) * peso
    segundo_digito = (soma * 10) % 11
    segundo_digito = 0 if segundo_digito == 10 else segundo_digito

    # Verifica se o segundo dígito confere
    if segundo_digito != int(cpf_numerico[10]):
        return False

    return True
