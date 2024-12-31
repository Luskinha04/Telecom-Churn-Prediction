import xml.etree.ElementTree as ET

# Definição do namespace
namespace = {"pmml": "http://www.dmg.org/PMML-4_2"}

# Carrega o arquivo PMML
pmml_file = "decision_tree_model.pmml"
tree = ET.parse(pmml_file)
root = tree.getroot()

# Localiza o modelo de árvore no PMML
tree_model = root.find(".//pmml:TreeModel", namespace)
if tree_model is None:
    raise ValueError("Modelo de árvore de decisão não encontrado no arquivo PMML.")

# Função de previsão
def predict(tree_node, input_data, level=0):
    # Obtemos o ID e o Score do nó atual
    node_id = tree_node.get('id')
    score = tree_node.get('score')

    # Procura um predicado no nó atual
    predicate = tree_node.find(".//pmml:SimplePredicate", namespace)
    if predicate is not None:
        field = predicate.get('field')
        operator = predicate.get('operator')
        value = predicate.get('value')

        # Avalia a condição com base nos dados de entrada
        if field in input_data:
            input_value = input_data[field]

            # Verifica se o valor é numérico
            try:
                value = float(value)
                input_value = float(input_value)
                condition_met = (
                    (operator == "lessOrEqual" and input_value <= value) or
                    (operator == "greaterThan" and input_value > value) or
                    (operator == "equal" and input_value == value)
                )
            except ValueError:
                # Trata valores categóricos
                condition_met = (operator == "equal" and input_value == value)

            # Se a condição não for atendida, interrompe a previsão
            if not condition_met:
                return None

    # Procura nós filhos e avalia recursivamente
    for child in tree_node.findall("pmml:Node", namespace):
        result = predict(child, input_data, level + 1)
        if result is not None:
            return result

    # Retorna o Score se chegamos a um nó folha
    return score

# Exemplo de entrada
input_example = {
    "Genero": "Feminino",          # Gênero
    "Idoso": 0,                   # Idoso (0 ou 1)
    "Parceiro": 1,                # Parceiro (0 ou 1)
    "Dependentes": 0,             # Dependentes (0 ou 1)
    "Meses_Cliente": 1,           # Meses_Cliente (valor contínuo, em proporção)
    "Servico_Telefone": 1,        # Serviço_Telefone (0 ou 1)
    "Multiplas_Linhas": 0,        # Multiplas_Linhas (0 ou 1)
    "Servico_Internet": 0,        # Serviço_Internet (0 ou 1 ou 2)
    "Seguranca_Online": 1,        # Segurança_Online (0 ou 1)
    "Backup_Online": 0,           # Backup_Online (0 ou 1)
    "Protecao_Dispositivo": 1,    # Proteção_Dispositivo (0 ou 1)
    "Suporte_Tecnico": 0,         # Suporte_Técnico (0 ou 1)
    "Streaming_TV": 0,            # Streaming_TV (0 ou 1)
    "Streaming_Filmes": 0,        # Streaming_Filmes (0 ou 1)
    "Contrato": "Mensal",         # Contrato ("Mensal", "Um Ano", "Dois Anos")
    "Fatura_Papel": 1,            # Fatura_Papel (0 ou 1)
    "Pagamento": "Cheque Eletronico", # Pagamento (opções como "Cheque Eletronico", "Transferencia", etc.)
    "Cobranca_Mensal": 29.85,     # Cobrança_Mensal (valor contínuo)
    "Cobranca_Total": 29.85       # Cobrança_Total (valor contínuo)
}

# Executa a previsão com os dados de exemplo
root_node = tree_model.find("pmml:Node", namespace)
if root_node is not None:
    result = predict(root_node, input_example)
    print("\nPrevisão:", result)
else:
    print("Nenhum nó raiz encontrado no modelo de árvore.")
