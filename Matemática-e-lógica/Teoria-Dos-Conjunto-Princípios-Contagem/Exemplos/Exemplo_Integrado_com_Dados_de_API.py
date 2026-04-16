#Neste exemplo, simulamos uma resposta de API com perfis e permissões.

resposta_api = {
    "usuario": "breno",
    "permissoes_usuario": {"ler", "editar"},
    "permissoes_grupo": {"ler", "criar", "deletar"},
    "acoes_solicitadas": {"ler", "exportar", "deletar"}
}

permissoes_totais = resposta_api["permissoes_usuario"] | resposta_api["permissoes_grupo"]
acoes_autorizadas = resposta_api["acoes_solicitadas"] & permissoes_totais

print("Permissões totais:", permissoes_totais)
print("Ações autorizadas:", acoes_autorizadas)

# Saída esperada
# Permissões totais: {'ler', 'editar', 'criar', 'deletar'}
# Ações autorizadas: {'ler', 'deletar'}