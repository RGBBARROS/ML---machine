# Modelo de Machine Learning para Avaliação de Crédito

Este é um modelo de Machine Learning desenvolvido para avaliar automaticamente o score de crédito de clientes, classificando-os em "Ruim", "OK" ou "Bom".

## Sobre

Este código implementa um modelo de Machine Learning que utiliza dados de clientes para prever o seu score de crédito. Ele foi desenvolvido utilizando Python e bibliotecas populares de Machine Learning, como Pandas, Scikit-learn e outras.

## Como Utilizar

Para utilizar este código, siga os passos abaixo:

1. **Importação da Base de Dados**: Certifique-se de possuir a base de dados dos clientes. O código foi desenvolvido considerando um arquivo CSV como fonte de dados. Caso a base de dados esteja em outro formato ou localização, modifique o código de acordo.

2. **Preparação dos Dados**: Antes de alimentar os dados ao modelo de Machine Learning, é necessário prepará-los. Isso inclui a transformação de colunas categóricas em numéricas, utilizando a técnica de Label Encoding.

3. **Divisão dos Dados em Treino e Teste**: Divida a base de dados em conjuntos de treino e teste. Isso é essencial para avaliar a performance do modelo.

4. **Criação e Treinamento do Modelo**: Utilize algoritmos de Machine Learning para criar e treinar o modelo. Neste código, foram utilizados dois modelos: KNN (K-Nearest Neighbors) e Random Forest.

5. **Avaliação do Modelo**: Após treinar o modelo, é importante avaliá-lo para verificar sua precisão. Neste código, a métrica de acurácia foi utilizada para avaliar o desempenho dos modelos.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- Pandas
- Scikit-learn

## Execução

Execute o código Python em um ambiente que possua as bibliotecas necessárias instaladas. Certifique-se de ter a base de dados disponível no caminho correto.

## Resultados

Com base nos testes realizados, os modelos apresentaram os seguintes resultados:

- O modelo baseado em árvore de decisão teve uma acurácia de aproximadamente 83%.
- O modelo KNN teve uma acurácia de aproximadamente 74%.

## Contribuição

Sinta-se à vontade para contribuir com melhorias neste projeto. Caso encontre problemas ou tenha sugestões, abra uma issue neste repositório.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE.md para mais detalhes.


______________________________________________________________________________________________________________

PARA MELHORAR A COMPREENSÃO DE TODOS, EU TAMBEM DOCUMENTEI EM INGLES, SEGUE:

# Credit Scoring Machine Learning Model

This is a Machine Learning model developed to automatically assess the credit score of clients, classifying them as "Poor", "OK", or "Good".

## About

This code implements a Machine Learning model that uses client data to predict their credit score. It was developed using Python and popular Machine Learning libraries such as Pandas, Scikit-learn, and others.

## How to Use

To use this code, follow the steps below:

1. **Importing the Dataset**: Make sure you have the client dataset. The code was developed considering a CSV file as the data source. If the dataset is in another format or location, modify the code accordingly.

2. **Data Preparation**: Before feeding the data into the Machine Learning model, it is necessary to prepare it. This includes transforming categorical columns into numerical ones, using the Label Encoding technique.

3. **Splitting Data into Training and Testing Sets**: Split the dataset into training and testing sets. This is essential to evaluate the model's performance.

4. **Model Creation and Training**: Use Machine Learning algorithms to create and train the model. In this code, two models were used: KNN (K-Nearest Neighbors) and Random Forest.

5. **Model Evaluation**: After training the model, it is important to evaluate it to check its accuracy. In this code, the accuracy metric was used to assess the performance of the models.

## Requirements

Make sure you have the following libraries installed:

- Pandas
- Scikit-learn

## Execution

Run the Python code in an environment that has the required libraries installed. Make sure to have the dataset available in the correct path.

## Results

Based on the tests performed, the models showed the following results:

- The decision tree-based model had an accuracy of approximately 83%.
- The KNN model had an accuracy of approximately 74%.

## Contribution

Feel free to contribute improvements to this project. If you encounter issues or have suggestions, open an issue in this repository.

## License

This project is licensed under the MIT License. See the LICENSE.md file for more details.

