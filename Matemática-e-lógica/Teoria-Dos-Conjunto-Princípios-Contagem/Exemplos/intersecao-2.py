#Clientes presentes em duas bases de dados

clientes_loja = {"ana@example.com", "bruno@example.com", "carla@example.com"} 
clientes_newsletter = {"carla@example.com", "daniel@example.com", "ana@example.com"} 
clientes_em_ambas = clientes_loja.intersection(clientes_newsletter) 
print(clientes_em_ambas) 
# {'ana@example.com', 'carla@example.com'}

# Útil para:

# marketing
# CRM
# cruzamento de dados entre sistemas