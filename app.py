from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Importando a base de dados fictícia (utilizada no exemplo)
tabela = pd.read_csv("C:/Users/Roger Barros/Desktop/Polybalas/MLMachine/ML---machine/base de dados/clientes.csv")

# Transformando as colunas necessárias em números utilizando LabelEncoder
codificador = LabelEncoder()
tabela["profissao"] = codificador.fit_transform(tabela["profissao"])
tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])
tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])

# Dividindo a base de dados em treino e teste
y = tabela["score_credito"]
x = tabela.drop(columns=["id_cliente", "score_credito"])
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

# Criando e treinando os modelos de IA
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# Rota principal que renderiza a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para receber os dados do formulário via GET e POST e retornar o resultado da análise
@app.route('/analise', methods=['GET', 'POST'])  # Permitindo solicitações GET e POST
def analisar_credito():
    if request.method == 'GET' or request.method == 'POST':  # Verificando se a solicitação é GET ou POST
        idade = int(request.form['idade']) if request.method == 'POST' else int(request.args.get('idade'))
        profissao = request.form['profissao'] if request.method == 'POST' else request.args.get('profissao')
        salario = int(request.form['salario']) if request.method == 'POST' else int(request.args.get('salario'))

        # Realizando a previsão do modelo de Random Forest
        previsao_arvoredecisao = modelo_arvoredecisao.predict([[idade, profissao, salario]])
        resultado = ''

        if previsao_arvoredecisao[0] == 0:
            resultado = 'Ruim'
        elif previsao_arvoredecisao[0] == 1:
            resultado = 'OK'
        else:
            resultado = 'Bom'

        return jsonify({'resultado': resultado})
    else:
        return jsonify({'error': 'Method Not Allowed'}), 405  # Retornando erro para métodos não permitidos

if __name__ == '__main__':
    app.run(debug=True)
