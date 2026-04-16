
# Validar se o usuário possui todas as permissões exigidas
permissoes_necessarias = {"ler", "editar"}
permissoes_usuario = {"ler", "editar", "exportar"}

if permissoes_necessarias.issubset(permissoes_usuario):
    print("Usuário autorizado")
else:
    print("Usuário sem permissão suficiente")


# Muito útil em:

# controle de acesso
# recursos administrativos
# operações sensíveis