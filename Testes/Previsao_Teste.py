import xml.etree.ElementTree as ET

# Caminho do arquivo PMML
pmml_file = 'decision_tree_model.pmml'

# Carregar o arquivo PMML
tree = ET.parse(pmml_file)
root = tree.getroot()

# Namespace do PMML
namespace = {"pmml": "http://www.dmg.org/PMML-4_2"}

# Extraindo campos do DataDictionary
print("Campos do modelo:")
for data_field in root.findall(".//pmml:DataField", namespace):
    name = data_field.get('name')
    data_type = data_field.get('dataType')
    optype = data_field.get('optype')
    print(f"- Campo: {name}, Tipo: {data_type}, Operação: {optype}")

# Extraindo regras da árvore de decisão
print("\nRegras da Árvore de Decisão:")
def parse_node(node, level=0):
    node_id = node.get('id')
    score = node.get('score')
    print("  " * level + f"Node ID: {node_id}, Score: {score}")

    # Predicados (condições)
    predicate = node.find(".//pmml:SimplePredicate", namespace)
    if predicate is not None:
        field = predicate.get('field')
        operator = predicate.get('operator')
        value = predicate.get('value')
        print("  " * level + f"-> Condição: {field} {operator} {value}")

    # Percorrer filhos
    for child in node.findall("pmml:Node", namespace):
        parse_node(child, level + 1)

# Encontrar o nó raiz da árvore de decisão
tree_model = root.find(".//pmml:TreeModel", namespace)
if tree_model is not None:
    root_node = tree_model.find("pmml:Node", namespace)
    if root_node is not None:
        parse_node(root_node)
