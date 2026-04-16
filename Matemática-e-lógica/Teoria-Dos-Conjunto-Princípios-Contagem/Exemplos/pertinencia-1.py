#Verificar se uma rota exige autenticação
rotas_protegidas = {"/admin", "/perfil", "/financeiro"}

rota_atual = "/perfil"

if rota_atual in rotas_protegidas:
    print("Autenticação obrigatória")
else:
    print("Rota pública")


# Muito comum em:

# APIs REST
# frameworks web
# controle de navegação