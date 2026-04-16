#Verificar se um status é válido antes de salvar no banco
status_validos = {"ativo", "inativo", "pendente"}

novo_status = "ativo"

if novo_status in status_validos:
    print("Status válido para salvar")
else:
    print("Status inválido")


# Ajuda a:

# validar entrada de formulários
# evitar dados inconsistentes
# reforçar regras de negócio