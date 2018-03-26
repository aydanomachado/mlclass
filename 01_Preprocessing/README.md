# Atividade 01 - Pré-processamento

Para tudo que nos é enviado, assumimos que você está seguindo o código de honra a seguir.

## Código de Honra

>"Como membro da comunidade deste curso, não vou participar nem tolerar a desonestidade acadêmica".

## Objetivo da atividade
*Trabalhar o pré-processamento de dados para o algoritmo k-NN*

## Descrição da atividade
Nesta atividade apresentamos duas versões de um mesmo programa em python que lê um banco de dados de mulheres descendentes do povo Pima. Que segundo a [Wikipédia](https://en.wikipedia.org/wiki/Pima_people): "Os Pima são um povo nativo dos Estados Unidos da América que viviam às margens dos rios Gila e Sal, na parte sul do estado de Arizona."

O primeira versão do programa python (`diabetes_csv.py`) trabalha com arquivos de dados em formato csv e a segunda com os arquivos em formato Excel (`diabetes_xlsx.py`), deste modo você pode escolher o formato que preferir para trabalhar com os dados e fazer seu pré-processamento.

A única modificação que precisa ser realizada no programa python é a inserção da chave enviada no local indicado, substituindo o texto entre aspas pela chave da equipe.

```python
DEV_KEY = "COLOCAR_SUA_KEY_AQUI"
```

Feito isso o programa já está completo, porém ainda não funcional, pois existem erros nos dados que precisam ser pré-processados para que cumpram tudo que é demandado pelo algoritmo k-NN para que este funcione bem.

A atividade da equipe consiste em pré-processar os dados, modificando os arquivos no formato escolhido, para que estes se encontrem da melhor maneira para o funcionamento do algoritmo k-NN.

Supondo que o formato escolhido tenha sido o xlsx (ou Excel), o programa `diabetes_xlsx.py` lê o arquivo `diabetes_dataset.xlsx` e o armazena nos vetores `X` e `y`. Em seguida ele constrói o modelo preditivo utilizando o k-NN com um `k = 3` e utiliza esse modelo para classificar os dados encontrados no arquivo `diabetes_app.xlsx`. Tais previsões são enviadas para o servidor que vai contabilizar a acurácia conseguida com as previsões realizadas, para em seguida retornar e armazenar o melhor desempenho conseguido pela equipe.

## Descrição da base de dados

Esse conjunto de dados pode ser baixado no [UCI Machine Learning Repository: Pima Indians Diabetes Data Set](https://archive.ics.uci.edu/ml/datasets/pima+indians+diabetes). Que foi originalmente do National Institute of Diabetes and Digestive and Kidney Diseases, cujo objetivo é prever se o paciente tem diabetes. Os pacientes selecionados são mulheres com pelo menos 21 de herança indiana Prima. As informações da base de dados são descritas a seguir.

#### Atributos do dataset:
1. **Pregnancies**: número de vezes grávida
2. **Glucose**: concentração plasmática de glicose a 2 horas em um teste oral de tolerância à glicose
3. **BloodPressure**: pressão arterial diastólica (mm Hg)
4. **SkinThickness**: espessura da dobra da pele do tríceps (mm)
5. **Insulin**: insulina sérica de 2 horas (mu U/ml)
6. **BMI**: índice de massa corporal (peso em kg / (altura em m) ^ 2)
7. **DiabetesPedigreeFunction**: função de pedigree do diabetes
8. **Age**: idade (anos)
9. **Outcome**: variável de classe (0 ou 1) para diabetes

## Instalando o python e suas dependências

Uma maneira fácil de instalar a versão mais nova do python com todas as dependências necessárias para aprendizagem de máquina e manipulação de dados é baixar a distribuição [Anaconda](https://www.anaconda.com/download/). 

