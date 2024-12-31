import pandas as pd

# Carregar o arquivo ajustado
df = pd.read_excel('Telco-Customer-Churn-Processed.xlsx')

# Preencher valores ausentes em MultipleLines
df['MultipleLines'] = df.apply(
    lambda row: 'No phone service' if row['PhoneService'] == 'False' else row['MultipleLines'],
    axis=1
)

# Verificar se ainda há valores ausentes
missing_values = df['MultipleLines'].isnull().sum()
if missing_values > 0:
    print(f"Valores ausentes restantes em 'MultipleLines': {missing_values}")
else:
    print("Todos os valores preenchidos em 'MultipleLines'!")

# Salvar o arquivo ajustado
df.to_excel('Telco-Customer-Churn-Processed-Final.xlsx', index=False)
print("Arquivo atualizado salvo como 'Telco-Customer-Churn-Processed-Final.xlsx'.")
