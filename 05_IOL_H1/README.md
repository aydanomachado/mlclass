# Atividade 05 - Avaliação de classificadores

Para tudo que nos é enviado, assumimos que você está seguindo o código de honra a seguir.

## Código de Honra

>"Como membro da comunidade deste curso, não vou participar nem tolerar a desonestidade acadêmica".

## Objetivo da atividade
*Trabalhar a metodologia e as técnicas para a avaliação de classificadores*

## Descrição da atividade
A atividade da equipe consiste em construir e validar um modelo(s) preditivo(s) com o intuito de garantir o seu poder de generalização, utilizando a metodologia e técnicas vistas em sala de aula.

Nessa atividade vocês poderão utilizar qualquer algoritmo de aprendizagem mesmo os ainda não vistos em sala de aula tais como: SVM, Redes Neurais, RBFs, etc. Um detalhe importante é que o entendimento do algoritmo é necessário pois as equipes melhores ranqueadas terão, como nas outras atividades, compartilhar o que foi aprendido e isso inclui o algoritmo utilizado.

Para o envio da atividade poderão ser utilizados os mesmos modelos de programas para ler e enviar os resultados utilizados na Atividade 01 - Pré-processamento, fazendo as devidas modificações como por exemplo alterar a URL de envio para https://aydanomachado.com/mlclass/05_Validation.php.

**Atenção:** nessa atividade só será permitido **1 envio a cada 12h** pois o objetivo é fazer uma boa validação do modelo antes desse ser enviado.

Ainda nos mesmos moldes da Atividade 01 os arquivos `h1_dataset.xlsx` ou `h1_dataset.csv` devem ser utilizados para a construção e validação do modelo preditivo (classificador) e os arquivos `h1_app.xlsx` ou `h1_app.csv` utilizados para teste do modelo e as previsões enviadas para o servidor onde será registrado o desempenho do modelo construído, correspondente a sua acurácia.

## Descrição da base de dados

Esse conjunto de dados foi estruturado a partir de um estudo sobre o implante de lente intraoculares para a correção da catarata senil utilizando a técnica de facoemulsificação.

A base consiste de informações do paciente, da anatomia do olho do paciente bem como os dados da lente implantada.

O objetivo é prever o sucesso da cirurgia de acordo com que foi planejado, representado pela coluna label.

Para quem quiser uma leitura rápida para introduzir o assunto deixo dois liks da wikipedia, para uma visão mais detalhada e acurada procurar outras fontes:
- Catarata ([Wikipédia, a enciclopédia livre](https://pt.wikipedia.org/wiki/Catarata))
- Cirurgia de catarata ([Wikipédia, a enciclopédia livre](https://pt.wikipedia.org/wiki/Cirurgia_de_catarata))


#### Atributos do dataset:
1. **Registro_x**: registo identificador **não deve ser usado para fazer a predição**
2. **Idade**: idade do paciente no momento da cirurgia
3. **Sexo**: M e F
4. **Modelo_x**: modelo da lente intraocular implantada
5. **SF**: constante representando o "fator cirurgião", tenta representar as variáveis não computadas diretamente para o resultado da cirurgia
6. **Dioptria**: grau da lente implantada
7. **ACD**: profundidade de câmara anterior do olho
8. **AL**: comprimento axial do olho
9. **WTW**: distância branco à brando do olho
10. **K1**: ceratometria do meridiano mais plano da superfície anterior do olho
11. **K2**: ceratometria do meridiano mais curvo da superfície anterior do olho
12. **K**: ceratometria média da superfície anterior do olho (média do K1 e K2) 
13. **label**: 0 e 1, variável a ser predita, representa o resultado cirúrgico
