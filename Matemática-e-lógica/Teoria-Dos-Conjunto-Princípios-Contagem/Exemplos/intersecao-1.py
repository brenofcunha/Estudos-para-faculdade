#Permissões realmente autorizadas
#O usuário pede uma ação. O sistema compara o que ele quer fazer com o que ele realmente pode fazer.

acoes_solicitadas = {"ler", "editar", "exportar"} 
acoes_permitidas = {"ler", "editar", "deletar"} 
acoes_autorizadas = acoes_solicitadas & acoes_permitidas
print(acoes_autorizadas)
 # {'ler', 'editar'}

# Isso pode ser usado em:

# middleware de autorização
# validação de escopos JWT
# APIs protegidas