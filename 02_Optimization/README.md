# Atividade 02 - Otimização de antena para padrão de radiação

Para tudo que nos é enviado, assumimos que você está seguindo o código de honra a seguir.

## Código de Honra

>"Como membro da comunidade deste curso, não vou participar nem tolerar a desonestidade acadêmica".

## Objetivo da atividade
*Trabalhar os algorítmos de busca de melhoria iterativa para problemas de otmização*
	
## Descrição da atividade
Esta atividade consiste na construção de agentes que têm como objetivo encontrar a melhor configuração de	uma antena de modo a conseguir o maior ganho com o padrão de radiação emitido/recebido pela sua disposição.

Para tal são sugeridos a implementação dos algorítmos de Subida da Encosta (Hill Climbing) e suas variações, bem como os algoritmos da Têmpera Simulada (Simulated Annealing) e os Algorítmos Genéticos (Genetic Algorithm).

Existem vários exemplos da aplicação dessa classe de algoritmos na resolução de diversos problemas práticos, como o do projeto automático de antenas para a espaçonave ST5 da NASA (Figura 1).

O formato da antena apresentado na Figura 1 foi encontrado por um programa de desenho evolutivo, de forma a criar o melhor padrão de radiação possível.	O complicado formato apresentado dificilmente seria desenhado por um humano e o resultado dos algorítmos	implementados conseguiu apresentar os melhores resultados, superando o desempenho dos projetistas humanos.

<p align="center">
	<img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/St_5-xband-antenna.jpg" alt="Antena" height="280" width="218"/>
	<br/>
	<em>Figura 1 - Antena criada para a espaçonave ST5 da NASA.</em>
</p>

## Abstração, representação, descrição e teste da antena
A antena que iremos manipular será um modelo simplificado e será representado utilizando como inspiração o sistema esférico de coordenadas, representado na Figura 2.

Um ponto P(r, φ, θ) nesse sistema esférico de coordenadas é composto de um raio r e mais dois ângulos φ e θ que permitem localizar esse ponto, tal como indicado na Figura 2.

<p align="center">
	<img src="https://upload.wikimedia.org/wikipedia/commons/2/26/Esfera_con_coordenadas_esfericas.png" alt="Coordenadas Esféricas"/>
	<br/>
	<em>Figura 2 - Sistema esférico de coordenadas.</em>
</p>

Nossa antena será composta de segmentos de mesmo tamanho, desse modo o valor de r não vai variar para cada parte dela. E assim as variações do design ou projeto serão somente nos pares de ângulos (φ, θ) para cada junção.

A antenha será composta de 3(três) junções e cada ângulo será representado em graus inteiros variando no intervalo [0º, 360º)

Com os 3(três) pares de angulos definidos esses poderão ser submetidos para teste pode meio da url descrita a seguir, substituindo os ___ pelo valor do respectivo ângulo dentro do intervalo [0;360)

(Obs.: Será mostrado como inicializar o servidor na próxima seção)

```
/antenna/simulate?phi1=___&theta1=___&phi2=___&theta2=___&phi3=___&theta3=___
```
Exemplo de requisição:

```
http://localhost:8080/antenna/simulate?phi1=90&theta1=90&phi2=90&theta2=90&phi3=90&theta3=90
```

Caso a requisição esteja formatada corretamente o servidor retornará o ganho conseguido pela antena (primeira linha), bem como os ângulos utilizados (nas demais linhas), tal como no exemplo descrito a seguir.

Exemplo de resposta:
```
-6.146398388793574
phi1 = 90
theta1 = 90
phi2 = 90
theta2 = 90
phi3 = 90
theta3 = 90
```

Tal como já mencionado anteriormente o objetivo é obter o maior ganho, ou seja, o mair valor representado na primeira linha da resposta do teste da antena.	

## Inicializando o ambiente para teste da antena

Para inicializar o ambiente você vai precisar do Java instalado. Em seguida baixe o arquivo `OPServer.jar` (deste repositório), abra o Terminal (no linux ou mac) ou a Linha de Comando (no Windows) e execute o seguinte comando:

```
java -jar OPServer.jar
```

Isso vai inicializar o ambiente de simulação que foi implementado sob a forma de um servidor web em Java para que este receba as requisições, comentadas anteriormente, calcule o ganho conseguido pela antena e retorne o resultado.

