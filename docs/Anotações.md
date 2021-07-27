__Artigo__: Minaee2018 - Finger-GAN: Generating Realistic Fingerprint Images Using Connectivity Imposed GAN

- Redes GAN para aprender a distribuição das impressões digitais (Deep Convolutive-GAN)
- Rede descriminativa que verifica a diferença entre dados artificiais e originais

- Although the GAN model should learn this line connectivity from the training data, we found out imposing a regularization term which promotes the connectivity of the generated fingerprint images can help the generator learn this more easily.

- both the discriminator and generator networks in our model are based on convolutional neural networks. The discriminator model consist of 4 convolutional layers followed by batch normalization and leaky ReLU as non-linearity, and a fully connected layer at the end. The generator model contains 5 fractionally-strided convolutional layers (aka deconvolution in literature), followed by batch-normalization and non-linearity.


__Opções de mudança__

- Algoritmo do GAN
- Algoritmo da rede descriminativa
- Algoritmo para impor conectividade em imagens

Possíveis problemas:
- tempo de treinamento
- falta de convergência

__Fundamentação teórica__


As redes GAN foram propostas primeiramente em `Goodfellow2014 - Generative adversarial nets` ...

`Redes convolucionais` são utilizadas para ...

"Since GAN’s invention, it has been used for various computer vision and pattern generation tasks, such as image super-resolution, image to image translation, image generation based on text description, prediction of pedestrian walking patterns for autonomous vehicles, and iris generation"

Since invention of GAN, there have been several works trying to improve/modify GAN in different aspects ...

O artigo base de trabalho utilizou `Deep Convolutional GAN` ..

Falar sobre termos de regularização. O artigo utiliza `Total variation` mas cita outro exemplo, `group sparcity` ...

Falar sobre as bases de dados ...


__Databases__

Login Name : lucas.mazim9@gmail.com
Password : rNDrtId

######################################################



# __Artigo__: Metalearning - application to data mining

## Aplicações

__1) Selecting and Recommending Machine Learning Algorithms__

Duas etapas:
- Reduzir o espaço de amostras;
- Encontrar a melhor opção;

Algoritmos:
- Seleção de melhor algoritmo
- Ranqueamento:
    - adjusted ratio of ratios
    - average ranks
    - KNN ranking method
- Recomenção de parâmetros para algoritmos de aprendizado
    - estimation of the generalization error
    - optimization
    - use of heuristics
    - Knn para recomendação de parametros

Avaliação
- Spearman’s rank correlation coefficient 
- Friedman’s test and Dunn’s multiple comparison procedure
- Top-n

__2) Geração de metafeatures__

Até então, três classes de meta-características foram propostas:
- baseadas em estatísticas e informações teóricas de caracterização;
- baseadas em propriedade do hipotese de indução
- baseadas no desempenho de lardmarks (algoritmos de aprendizado)

Mais no capítulo 2 e 3

__3) Planejamento de tarefas__

__4) Criação e algoritmos de ensemble__

__5) Transfer learning__

__6) Composição de sistemas complexos e aplicações__


__Capítulo 3: criação de sistemas de metaaprendizado para recomendação de algoritmos__

- Meta-level learning
    * Target metafeature
      - Best algorithm in a set
      - Subset of algorithms
      - Ranking of algorithms
      - Estimates of performance
    * Algorithm for meta-level learning
      - Classification algorithms (Qualquer algoritmo de aprendizado pode ser utilizado, inclusive, os mesmo que são utilizados na tarefas)
      - Regression Algorithms
      - Ranking algorithms
        - KNN + (Average ranks OR Rate Ratios OR Significant Wins)
        - Ranqueamento de arvores (Todorovisk 2002)
- Meta-dados
    * Meta-características: descriminitativas, complexidade computacional e dimensionalidade
      - baseadas em estatísticas e informações teóricas de caracterização;
      - baseadas em propriedade do hipotese de indução
      - baseadas no desempenho de lardmarks (algoritmos de aprendizado)
    * Especificação do problema
    * Caracterização de dados iterativa
- Meta-exemplos
- Base-level algorithms
    * Escolha dos algoritmos
    * Avaliação
- Qualidade dos meta-dados






# IDEIAS

- Sugerir um aprendizado por reforço que selecione quais algoritmos seguem em um mistura de BAGGING com BOOSTING
- Heuristica para aprender concept drifting
- Meta-learning decision trees
- VFDT
- Shewhart P-Chart


- __Mestrado__: propor um algoritmo classificação multi-targets.






