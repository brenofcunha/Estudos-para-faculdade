# Quantidade de ordens possíveis para processamento
# Imagine que um sistema precisa executar 4 tarefas em sequência, mas quer calcular quantas ordens diferentes existem.

import math

tarefas = ["validar", "salvar", "notificar", "registrar_log"]
quantidade_ordens = math.factorial(len(tarefas))

print(quantidade_ordens)
# 24


# Pode aparecer em:

# orquestração de processos
# análise de complexidade
# testes de sequência