# ============================================
# Calculadora de Partidas Rankeadas
# Desafio DIO - Lógica de Programação (Linguagem escolhida: Python)
# ============================================

# Função: recebe vitórias e derrotas, calcula o saldo e define o nível
def classificar_nivel(vitorias, derrotas):
    # Operador de subtração: calcula o saldo de rankeadas
    saldo = vitorias - derrotas

    # Estrutura de decisão: define o nível de acordo com o saldo
    if saldo < 10:
        nivel = "Ferro"
    elif saldo <= 20:
        nivel = "Bronze"
    elif saldo <= 50:
        nivel = "Prata"
    elif saldo <= 80:
        nivel = "Ouro"
    elif saldo <= 90:
        nivel = "Diamante"
    elif saldo <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    # A função retorna dois valores: o saldo e o nível calculados
    return saldo, nivel


# Laço de repetição: permite calcular o resultado de vários jogadores seguidos
continuar = "s"

while continuar == "s":
    # Variáveis: armazenam a quantidade de vitórias e derrotas do jogador
    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))

    # Chamada da função: passamos vitórias e derrotas como parâmetros
    saldo, nivel = classificar_nivel(vitorias, derrotas)

    # Saída: exibe a mensagem final
    print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}")

    # Pergunta se o usuário quer testar outro jogador
    continuar = input("Deseja calcular outro jogador? (s/n): ").lower()

print("Programa encerrado. Até a próxima!")
