import pandas as pd

# Carregar o arquivo Excel
input_file = 'Telco-Customer-Churn-Processed-Final.xlsx'  # Nome do arquivo de entrada
output_file = 'Telco-Customer-Churn-Processed-Translated-Final.xlsx'  # Nome do arquivo de saída
data = pd.read_excel(input_file)

# Dicionário para traduzir os nomes das colunas
column_translation = {
    'ID': 'ID',
    'customerID': 'ID_Cliente',
    'gender': 'Genero',
    'SeniorCitizen': 'Idoso',
    'Partner': 'Parceiro',
    'Dependents': 'Dependentes',
    'tenure': 'Meses_Cliente',
    'PhoneService': 'Servico_Telefone',
    'MultipleLines': 'Multiplas_Linhas',
    'InternetService': 'Servico_Internet',
    'OnlineSecurity': 'Seguranca_Online',
    'OnlineBackup': 'Backup_Online',
    'DeviceProtection': 'Protecao_Dispositivo',
    'TechSupport': 'Suporte_Tecnico',
    'StreamingTV': 'Streaming_TV',
    'StreamingMovies': 'Streaming_Filmes',
    'Contract': 'Contrato',
    'PaperlessBilling': 'Fatura_Papel',
    'PaymentMethod': 'Pagamento',
    'MonthlyCharges': 'Cobranca_Mensal',
    'TotalCharges': 'Cobranca_Total',
    'Churn': 'Cancelamento'
}

# Traduzir os valores categóricos
value_translation = {
    'Female': 'Feminino',
    'Male': 'Masculino',
    'True': 'Sim',
    'False': 'Nao',
    'No Internet Service': 'Sem Servico_Internet',
    'No Internet service': 'Sem Servico_Internet',
    'No internet Service': 'Sem Servico_Internet',
    'No internet service': 'Sem Servico_Internet',
    'No Internet_Service': 'Sem Servico_Internet',
    'No Internet_service': 'Sem Servico_Internet',
    'No internet_service': 'Sem Servico_Internet',
    'No internet_Service': 'Sem Servico_Internet',
    'No phone service': 'Sem Servico_Telefone',
    'No phone Service': 'Sem Servico_Telefone',
    'No Phone service': 'Sem Servico_Telefone',
    'No Phone Service': 'Sem Servico_Telefone',
    'No phone_service': 'Sem Servico_Telefone',
    'No phone_Service': 'Sem Servico_Telefone',
    'No Phone_service': 'Sem Servico_Telefone',
    'No Phone_Service': 'Sem Servico_Telefone',
    'DSL': 'DSL',
    'Fiber optic': 'Fibra_Otica',
    'Electronic check': 'Cheque Eletronico',
    'Mailed check': 'Cheque Enviado',
    'Bank transfer (automatic)': 'Transferencia',
    'Credit card (automatic)': 'Cartao de Credito',
    'Month-to-month': 'Mensal',
    'One year': 'Um Ano',
    'Two year': 'Dois Anos',
    'Yes': 'Sim',
    'No': 'Nao'
}

# Traduzir os nomes das colunas
data.rename(columns=column_translation, inplace=True)

# Traduzir os valores dentro do DataFrame
for column in data.columns:
    data[column] = data[column].replace(value_translation)

# Salvar o arquivo traduzido
data.to_excel(output_file, index=False)

print(f"Arquivo traduzido salvo como {output_file}")