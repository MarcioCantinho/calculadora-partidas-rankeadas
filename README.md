# calculadora-partidas-rankeadas
Desafio DIO de lógica de programação  — Calculadora de Partidas Rankeadas (Linguagem escolhida: Python)

<div align="center">

# 🎮 Calculadora de Partidas Rankeadas 🏆

### Um desafio de lógica de programação

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DIO](https://img.shields.io/badge/DIO-Digital%20Innovation%20One-FF4C00?style=for-the-badge&logoColor=white)

</div>

---

## 🎯 Sobre o projeto

Todo jogador ranqueado sonha em subir de patente! Este projeto calcula o **saldo de partidas rankeadas** de um jogador (vitórias menos derrotas) e classifica automaticamente seu nível competitivo. 🕹️

Este projeto foi desenvolvido como parte da **Formação Lógica de Programação da DIO (Digital Innovation One/ https://web.dio.me/)**, com o objetivo de praticar os pilares fundamentais da lógica de programação:

- 📦 **Variáveis**
- ➕ **Operadores**
- 🔁 **Laços de repetição**
- 🔀 **Estruturas de decisão**
- 🧩 **Funções**

A linguagem escolhida por mim foi Python 🐍.

---

## 🧮 Objetivo do desafio

Criar uma **função** que recebe como parâmetro a quantidade de **vitórias** e **derrotas** de um jogador, calcule o **saldo** (vitórias − derrotas) e retorne o **nível** correspondente, seguindo a tabela abaixo:

| 🏅 Nível | Saldo necessário |
|:---:|:---:|
| 🔩 Ferro | menor que 10 |
| 🥉 Bronze | 11 – 20 |
| 🥈 Prata | 21 – 50 |
| 🥇 Ouro | 51 – 80 |
| 💠 Diamante | 81 – 90 |
| 🌟 Lendário | 91 – 100 |
| 👑 Imortal | maior ou igual a 101 |

---

## 🖥️ Como funciona

O programa recebe a quantidade de vitórias e derrotas do jogador, calcula o saldo através de uma **função**, e essa mesma função aplica uma estrutura `if / elif / else` para retornar o nível correspondente. O resultado final é exibido assim:

```
O Herói tem de saldo de 50 está no nível de Prata
```

Graças ao laço `while`, é possível calcular o resultado de **quantos jogadores quiser** em uma única execução! 🔁

---

## 🚀 Como executar o projeto

**Pré-requisito:** ter o [Python](https://www.python.org/downloads/) instalado (versão 3.10 ou superior).

```bash
# 1. Clone este repositório
git clone https://github.com/MarcioCantinho/calculadora-partidas-rankeadas.git

# 2. Acesse a pasta do projeto
cd calculadora-partidas-rankeadas

# 3. Execute o programa
python calculadora_rankeada.py
```

---

## 🧩 Tecnologias utilizadas

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![VSCode](https://img.shields.io/badge/-VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)

</div>

---

## 📚 Aprendizados

Este exercício deu continuidade à trilha de **Lógica de Programação** da [DIO (Digital Innovation One)](https://www.dio.me/), introduzindo um novo conceito fundamental: **funções**. Elas permitem organizar e reutilizar lógica, evitando repetição de código.

> "Uma
