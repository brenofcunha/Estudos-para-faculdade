#Permissões de usuário em uma API
#Um usuário pode receber permissões do próprio perfil e também do grupo ao qual pertence.

permissoes_usuario = {"ler", "editar"}
permissoes_grupo = {"ler", "deletar", "criar"} 
permissoes_admin = permissoes_usuario | permissoes_grupo 
print(permissoes_admin)
 # {'ler', 'editar', 'deletar', 'criar'}

# Exemplos de utilização:
# sistemas de autenticação
# controle de acesso por papéis
# APIs com RBAC
