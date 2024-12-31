import pickle
import pandas as pd

# Carregar o modelo salvo
model_path = 'random_forest_model.model'  # Altere para o caminho correto do modelo salvo
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Dados de entrada (exemplo)
# Certifique-se de que os dados estão no mesmo formato das colunas usadas no treino
data = pd.DataFrame([{
    'Genero': 0,               # 0 para Feminino, 1 para Masculino
    'Idoso': 0,                # 0 para Não, 1 para Sim
    'Parceiro': 1,             # 0 para Não, 1 para Sim
    'Dependentes': 0,          # 0 para Não, 1 para Sim
    'Meses_Cliente': 1,       # Número de meses
    'Servico_Telefone': 0,     # 0 para Não, 1 para Sim
    'Multiplas_Linhas': 0,     # 0 para Não, 1 para Sim
    'Servico_Internet': 1,     # 0 para Não, 1 para DSL, 2 para Fibra Ótica
    'Seguranca_Online': 0,     # 0 para Não, 1 para Sim, 3 para Sem Servico_Internet
    'Backup_Online': 1,        # 0 para Não, 1 para Sim, 3 para Sem Servico_Internet
    'Protecao_Dispositivo': 0, # 0 para Não, 1 para Sim, 3 para Sem Servico_Internet
    'Suporte_Tecnico': 0,      # 0 para Não, 1 para Sim, 3 para Sem Servico_Internet
    'Streaming_TV': 0,         # 0 para Não, 1 para Sim, 3 para Sem Servico_Internet
    'Streaming_Filmes': 0,     # 0 para Não, 1 para Sim, 3 para Sem Servico_Internet
    'Contrato': 1,             # 1 para Mensal, 2 para Um Ano, 3 para Dois Anos
    'Fatura_Papel': 1,         # 0 para Não, 1 para Sim
    'Pagamento': 1,            # 1 para Cheque Eletronico, 2 para Cheque Enviado, 3 para Transferencia, 4 para Cartao de Credito
    'Cobranca_Mensal': 29.85,   # Valor numérico
    'Cobranca_Total': 29.85   # Valor numérico
}])

# Fazer previsões
prediction = model.predict(data)
print("Previsão:", prediction)
