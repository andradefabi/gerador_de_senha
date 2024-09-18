import random
import string #a biblioteca contem números e letras 

def gerar_senha(tamanho, incluir_letras, incluir_numeros, incluir_simbolos):
    caracteres = ""

    if incluir_letras:
        caracteres += string.ascii_letters  # maiúsculas e minúsculas
    if incluir_numeros:
        caracteres += string.digits  # de 0 a 9
    if incluir_simbolos:
        caracteres += string.punctuation  # Símbolos especiais

    if not caracteres:  # Verifica se caracteres está vazio
        return "Nenhum tipo de caractere selecionado!"

    # Gerar a senha com base nos caracteres permitidos
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def obter_preferencias():
    tamanho = int(input("Digite o tamanho da senha: "))
    incluir_letras = input("Incluir letras? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

    return tamanho, incluir_letras, incluir_numeros, incluir_simbolos

def main():
    tamanho, incluir_letras, incluir_numeros, incluir_simbolos = obter_preferencias()

    if not incluir_letras and not incluir_numeros and not incluir_simbolos:
        print("Você deve incluir pelo menos um tipo de caractere!")
    else:
        senha = gerar_senha(tamanho, incluir_letras, incluir_numeros, incluir_simbolos)
        print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()
