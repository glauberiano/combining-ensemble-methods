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