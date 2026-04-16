#Suponha que um sistema receba colunas esperadas e colunas retornadas de uma consulta.

colunas_esperadas = {"id", "nome", "email"}
colunas_retorno_banco = {"id", "nome", "email", "telefone"}

if colunas_esperadas.issubset(colunas_retorno_banco):
    print("Consulta retornou os dados necessários")
else:
    print("Consulta incompleta")

#Outro exemplo, validando resultados:

ids_ativos = {1, 2, 3, 4, 5}
ids_bloqueados = {4, 5, 6}

ids_validos = ids_ativos - ids_bloqueados

print(ids_validos)
# {1, 2, 3}