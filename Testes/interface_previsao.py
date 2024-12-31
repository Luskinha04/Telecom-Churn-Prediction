import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Definição do namespace
namespace = {"pmml": "http://www.dmg.org/PMML-4_2"}

# Mapeamento de valores para as opções
options_map = {
    'Genero': {'Masculino': 1, 'Feminino': 0},
    'Idoso': {'Sim': 1, 'Nao': 0},
    'Parceiro': {'Sim': 1, 'Nao': 0},
    'Dependentes': {'Sim': 1, 'Nao': 0},
    'Servico_Telefone': {'Sim': 1, 'Nao': 0},
    'Multiplas_Linhas': {'Sim': 1, 'Nao': 0, 'Sem Servico_Telefone': 3},
    'Servico_Internet': {'DSL': 1, 'Fibra_Otica': 2, 'Nao': 0},
    'Seguranca_Online': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Backup_Online': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Protecao_Dispositivo': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Suporte_Tecnico': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Streaming_TV': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Streaming_Filmes': {'Sim': 1, 'Nao': 0, 'Sem Servico_Internet': 3},
    'Contrato': {'Mensal': 1, 'Um Ano': 2, 'Dois Anos': 3},
    'Fatura_Papel': {'Sim': 1, 'Nao': 0},
    'Pagamento': {
        'Cheque Eletronico': 1,
        'Cheque Enviado': 2,
        'Transferencia': 3,
        'Cartao de Credito': 4
    }
}

# Função para realizar a previsão com base nos inputs da interface
def predict(tree_node, input_data):
    predicate = tree_node.find(".//pmml:SimplePredicate", namespace)
    if predicate is not None:
        field = predicate.get('field')
        operator = predicate.get('operator')
        value = predicate.get('value')
        if operator in ["lessOrEqual", "greaterThan"]:
            value = float(value)
        input_value = input_data[field]
        condition_met = (
            (operator == "lessOrEqual" and input_value <= value) or
            (operator == "greaterThan" and input_value > value) or
            (operator == "equal" and input_value == value)
        )
        if not condition_met:
            return None

    for child in tree_node.findall("pmml:Node", namespace):
        result = predict(child, input_data)
        if result is not None:
            return result
    return tree_node.get('score')

# Função para buscar resultados mais próximos no Excel
def find_closest_match(input_data):
    try:
        # Carrega o arquivo Excel
        df = pd.read_excel(r"C:\Users\lucas\Downloads\3TrabalhoIN\Testes\Telco-Customer-Churn-Final-Normalizado.xlsx")

        # Remove colunas irrelevantes
        df = df.drop(columns=["ID", "ID_Cliente"])

        # Converte os valores de texto no Excel para números usando o mapeamento
        for column, mapping in options_map.items():
            if column in df.columns:
                df[column] = df[column].map(mapping)

        # Substitui valores NaN por 0
        df = df.fillna(0)

        # Prepara os dados para cálculo de similaridade
        input_vector = [input_data[field] for field in df.columns[:-1]]
        df_features = df.iloc[:, :-1].values
        df_labels = df.iloc[:, -1].values

        # Calcula similaridade
        similarities = cosine_similarity([input_vector], df_features)
        closest_index = similarities.argmax()

        # Retorna o resultado mais próximo
        return df_labels[closest_index]
    except Exception as e:
        return f"Erro ao buscar no Excel: {str(e)}"

# Função chamada ao clicar no botão
def get_prediction():
    try:
        # Coleta os valores dos campos
        input_data = {
            field: options_map[field][var.get()] if field in options_map else float(var.get())
            for field, var in variables.items()
        }

        # Carrega o arquivo PMML
        tree = ET.parse('decision_tree_model.pmml')
        root = tree.getroot()
        tree_model = root.find(".//pmml:TreeModel", namespace)
        root_node = tree_model.find("pmml:Node", namespace)

        # Realiza a previsão
        result = predict(root_node, input_data)

        if result is None:
            # Busca no Excel se nenhuma condição foi satisfeita
            result = find_closest_match(input_data)

        # Exibe o resultado
        messagebox.showinfo("Resultado da Previsão", f"Cancelamento: {result}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Criação da janela principal
window = tk.Tk()
window.title("Previsão de Cancelamento")

# Variáveis para armazenar os valores dos campos
variables = {}

fields = [
    "Genero", "Idoso", "Parceiro", "Dependentes", "Servico_Telefone",
    "Multiplas_Linhas", "Servico_Internet", "Seguranca_Online", "Backup_Online",
    "Protecao_Dispositivo", "Suporte_Tecnico", "Streaming_TV", "Streaming_Filmes",
    "Contrato", "Fatura_Papel", "Pagamento", "Meses_Cliente", "Cobranca_Mensal", "Cobranca_Total"
]

for i, field in enumerate(fields):
    tk.Label(window, text=field).grid(row=i, column=0, padx=5, pady=5, sticky="w")
    if field in options_map:
        variables[field] = tk.StringVar()
        tk.OptionMenu(window, variables[field], *options_map[field].keys()).grid(row=i, column=1, padx=5, pady=5)
    else:
        variables[field] = tk.StringVar()
        tk.Entry(window, textvariable=variables[field]).grid(row=i, column=1, padx=5, pady=5)

# Botão para realizar a previsão
btn_predict = tk.Button(window, text="Prever Cancelamento", command=get_prediction)
btn_predict.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Executa a interface
window.mainloop()
