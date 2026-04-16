#Consolidando tags vindas de banco e API externa

tags_banco = {"python", "backend", "api"} 
tags_api_externa = {"api", "docker", "cloud"} 
tags_consolidadas = tags_banco.union(tags_api_externa) 
print(tags_consolidadas)
 # {'python', 'backend', 'api', 'docker', 'cloud'}

# Esse caso é comum quando:

# você importa dados de múltiplas fontes
# precisa evitar duplicação
# deseja enriquecer informações existentes