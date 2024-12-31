import pandas as pd

# Carregar a base de dados
file_path = 'Telco-Customer-Churn.xlsx'  # Certifique-se de ajustar o caminho e nome do arquivo
output_file = 'Telco-Customer-Churn-Processed.xlsx'

# Ler o arquivo Excel
df = pd.read_excel(file_path)

# Colunas relacionadas ao InternetService
internet_related_columns = [
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
    'TechSupport', 'StreamingTV', 'StreamingMovies'
]

# Preencher valores em branco nas colunas relacionadas com 'No Internet Service' onde InternetService é 'No'
for column in internet_related_columns:
    df.loc[df['InternetService'] == 'No', column] = df.loc[df['InternetService'] == 'No', column].fillna('No Internet Service')

# Salvar o arquivo atualizado
df.to_excel(output_file, index=False)

print(f"Arquivo processado e salvo como: {output_file}")
