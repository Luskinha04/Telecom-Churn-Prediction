# Análise Preditiva de Cancelamento de Clientes e Estratégias de Retenção na Indústria de Telecomunicações: Um Estudo de Caso

## Objetivo

O objetivo deste projeto é desenvolver um modelo preditivo que identifique clientes em risco de cancelamento (churn) de forma precisa. Ao identificar esses clientes, é possível implementar estratégias direcionadas para retenção, reduzindo a perda de clientes e aumentando a satisfação e a lucratividade da empresa.

## Fluxo do Projeto

1. **Compreensão do Negócio (Business Understanding)**
2. **Compreensão dos Dados (Data Understanding)**
3. **Preprocessamento dos Dados (Data Preprocessing)**
4. **Modelagem (Modelling)**
5. **Avaliação (Evaluation)**

---

## Compreensão dos Dados

O dataset utilizado contém as seguintes colunas:

- **Gênero**: Indica se o cliente é masculino ou feminino.
- **Idoso**: Indica se o cliente é idoso (Sim/1 ou Não/0).
- **Parceiro**: Indica se o cliente tem um parceiro.
- **Dependentes**: Indica se o cliente possui dependentes.
- **Meses_Cliente**: Duração (em meses) que o cliente está com a empresa.
- **Serviço_Telefone**: Indica se o cliente possui serviço telefônico.
- **Múltiplas_Linhas**: Indica se o cliente possui múltiplas linhas telefônicas.
- **Serviço_Internet**: Tipo de serviço de internet do cliente (DSL, Fibra Ótica ou Não).
- **Segurança_Online**: Indica se o cliente tem serviços de segurança online.
- **Backup_Online**: Indica se o cliente possui backup online.
- **Proteção_Dispositivo**: Indica se o cliente possui proteção de dispositivo.
- **Suporte_Técnico**: Indica se o cliente possui suporte técnico.
- **Streaming_TV**: Indica se o cliente tem serviços de streaming de TV.
- **Streaming_Filmes**: Indica se o cliente tem serviços de streaming de filmes.
- **Contrato**: Tipo de contrato do cliente (Mensal, Um Ano, Dois Anos).
- **Fatura_Papel**: Indica se o cliente utiliza fatura em papel.
- **Pagamento**: Método de pagamento do cliente.
- **Cobrança_Mensal**: Valor mensal cobrado ao cliente.
- **Cobrança_Total**: Valor total cobrado ao cliente.
- **Cancelamento**: Indica se o cliente cancelou o serviço.

---

## Preprocessamento dos Dados

- **Tradução e Padronização**:
  - O dataset foi traduzido do inglês para o português para facilitar o entendimento e a manipulação dos dados.
  - Realizado preenchimento de valores ausentes utilizando o Simple Imputer.

- **Codificação de Dados**:
  - Utilização de Label Encoder e One Hot Encoder para transformar colunas categóricas em valores numéricos.

- **Balanceamento**:
  - SMOTE (Técnica de Sobreamostragem Minoritária Sintética) foi utilizado para balancear as classes na coluna de cancelamento.

---

## Arquivos do Projeto

### **Pasta Datasets**
- Contém as bases de dados utilizadas e processadas para o projeto, incluindo versões normalizadas e traduzidas.

### **Scripts**
- `fill_missing_values.py`: Script para tratar valores ausentes no dataset.
- `fill_multiplelines_values.py`: Trata valores específicos relacionados a múltiplas linhas telefônicas.
- `string_to_number.py`: Realiza a conversão de dados categóricos em valores numéricos.
- `traduzir_base.py`: Tradução do dataset original do inglês para o português.

### **Testes**
- `decision_tree_model.pmml`: Modelo de árvore de decisão treinado para previsão de cancelamento.
- `interface_previsao.py`: Interface gráfica para entrada de dados e previsão de cancelamento.
- `prever_score.py`: Script para realizar previsões utilizando o modelo.
- `previsao_teste.py`: Testa funcionalidades específicas relacionadas ao modelo.
- `telco-customer-churn-final-normalizado.xlsx`: Dataset final normalizado.

---

## Modelagem

Modelos treinados:
- **Árvore de Decisão** (utilizada na interface).
- Outros modelos explorados incluem:
  - Floresta Aleatória (Random Forest)
  - Regressão Logística (Logistic Regression)
  - Gradient Boosting
  - Máquina de Vetor de Suporte (SVM)

---

## Tecnologias Utilizadas

- **Linguagem de programação**: Python
- **Bibliotecas principais**:
  - Pandas
  - Scikit-learn
  - Tkinter (Interface gráfica)
- **Formatos de modelo**: PMML

---

## Autor

Lucas Lemos (Projeto adaptado e traduzido com base em "Predictive Analysis of Customer Churn" de Newton Kimathi)

---

## Habilidades Desenvolvidas

- Análise e exploração de dados
- Tradução e padronização de datasets
- Desenvolvimento de interface gráfica para previsão
- Modelagem e avaliação de modelos de machine learning
- Tratamento de dados categóricos e balanceamento de classes
