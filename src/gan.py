import random

class GAN:
    """
    :param n_iterations:
    :type n_iterations:
    :param steps:
    :type steps:
    :param m:
    :type m:
    """
    def __init__(generator, discriminator, epochs=120, batch_size=40, k=1, learning_rate=0.0002, optimizer='ADAM'):
        self.generator = generator
        self.discriminator = discriminator
        self.epochs = epochs
        self.batch_size = batch_size
        self.k = k
        self.learning_rate = learning_rate
        self.optimizer = optimizer
    
    def fit(self, imgreal_path):
        """
        :param data: local onde as imagens verdadeiras estão.
        :type data: string
        """
        for i in range(self.epochs):
            for j in range(self.k)
                real_imgs = [cv2.imread(str(file)) for file in random.sample(imgreal_path, 40)]
                X_real_train = real_imgs
                y_real_train = np.ones(shape=(40,))
                
                # dúvida: qual a real dimensão das imagens fakes
                random_noise = [np.random.normal(loc=0, scale=1, size=(100,100)) for _ in range(40)]
                X_fake_train = random_noise
                y_fake_train = np.zeros(shape=(40,))
                
                X = X_real_train + X_fake_train
                y = np.hstack((y_real_train,y_fake_train))
                
                #Update the discriminator by ascending its stochastic gradient
                self.discriminator.train(X,y)
            
            #Update the generator by descending its stochastic gradient
            random_noise = [np.random.normal(loc=0, scale=1, size=(100,100)) for _ in range(40)]
            self.generator.train(random_noise)
        
class Generator:
    def __init__():
        pass
    
    def __train__():
        pass
    
class Discriminator:
    def __init__():
        pass
    
    def __train__():
        pass