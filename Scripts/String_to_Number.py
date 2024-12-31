import pandas as pd

# Carregar o arquivo Excel traduzido
input_file = 'Telco-Customer-Churn-Processed-Translated-Final.xlsx'  # Arquivo de entrada
output_file = 'Telco-Customer-Churn-Final-Normalizado.xlsx'  # Arquivo de saída

# Ler o arquivo Excel
data = pd.read_excel(input_file)

# Dicionário para normalizar valores inconsistentes
normalization = {
    'No Internet Service': 'Sem_Servico',
    'No Internet_Service': 'Sem_Servico',
    'No Phone Service': 'Sem_Servico_Telefone',
    'No Phone_Service': 'Sem_Servico_Telefone',
    'Sim': 'Sim',
    'Nao': 'Nao'
}

# Normalizar todas as colunas categóricas
for column in data.columns:
    if data[column].dtype == object:  # Somente colunas categóricas (texto)
        data[column] = data[column].replace(normalization)

# Atualizar transformações para valores numéricos
transformations = {
    #'Genero': {'Masculino': 1, 'Feminino': 0},
    'Idoso': {'Sim': 1, 'Nao': 0},
    'Parceiro': {'Sim': 1, 'Nao': 0},
    'Dependentes': {'Sim': 1, 'Nao': 0},
    'Servico_Telefone': {'Sim': 1, 'Nao': 0},
    'Multiplas_Linhas': {'Sim': 1, 'Nao': 0, 'Sem Servico_Telefone': 0},
    'Servico_Internet': {'DSL': 1, 'Fibra_Otica': 2, 'Nao': 0},
    'Seguranca_Online': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Backup_Online': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Protecao_Dispositivo': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Suporte_Tecnico': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Streaming_TV': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Streaming_Filmes': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    #'Contrato': {'Mensal': 1, 'Um Ano': 2, 'Dois Anos': 3},
    'Fatura_Papel': {'Sim': 1, 'Nao': 0},
    #'Pagamento': {
    #    'Cheque Eletronico': 1,
    #    'Cheque Enviado': 2,
    #    'Transferencia': 3,
    #    'Cartao de Credito': 4
    #},
    #'Cancelamento': {'Sim': 1, 'Nao': 0}
}

# Aplicar transformações numéricas
for column, mapping in transformations.items():
    if column in data.columns:
        data[column] = data[column].map(mapping)

# Salvar o arquivo transformado
data.to_excel(output_file, index=False)
print(f"Arquivo final normalizado salvo como {output_file}")
