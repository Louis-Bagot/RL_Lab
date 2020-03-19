# Lab Session 5: Deep Learning

This is an important lab session which aims to develop intuition for DRL. 
Please go through jupyter notebooks in order Lab_session5_1 then Lab_session5_2 before reading further instructions.

Open your Virtualenvironment and install requirements.txt by running
`pip install -r requirements.txt --user`

After going through the Notebooks and getting a hang of the way PyTorch works, we will ask you to play around with the hyperparameters to fine-tune and techniques you can use to greatly improve your network's performance, and get a better intuition for the how and why it works.

Most of the following can be visualized beforehand on a toy problem using the [https://playground.tensorflow.org/#activation=sigmoid&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=2&seed=0.35230&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false](Tensorflow Playground). On this playground, you can change the inputs, depth and width of the network, learning rate, task and noise, activation function, regularizer, batch size. We very strongly recommend you give it some time to play around, as it is excellent to build an intuition and understand the impact of all the choices the NN designer makes.

First, focus on the Multi-Layered Perceptron (MLP).
Multiple hyperparameters or design choices are essential to the network's performance.

### Network architecture
Three main choices can be made about an MLP's architecture:
* *depth*: number of hidden layers
* *width*: number of neurons in each layer
* *non-linearity*: activation functions

First, playing around with the depth of the network - the depth is defined by the number of functions you add in the init method of the NEt class.
Note that for 0 hidden layers, we have a regular linear model. What is its performance on the MNIST problem?
Using only one hidden layer, but with sufficient width, ensures that the network is a Universal Approximator (can approximate any function). However, this is only true for the data it uses: try to observe that, for a very wide layer, the network overfits to the testing data (...leading to a suspicious wine quality accuracy). The width can be controlled by changing how many inputs and outputs each intermediate function (i.e. hidden layer) takes in and gives out.
Try now to compare your overfitting network with a deeper, but less wide network. Hopefully, you get stronger results at test time: a deeper network can help generalize better. You can test the limits of this by using a much deeper network: you will overfit again! A lot of weights often means great expressiveness, which sometimes hurts generelization.
To observe overfitting in TF Playground, try using the maximal network depth and width!

The activation functions can have a very important impact on the network. It is common practice to choose the same for all layers, except the output layer, which controls the nature of the overall function (net). First, visualize, using TF Playground, the difference in hypothesis (function shape) when changing function. The sigmoid function is historically important, but has near 0 gradient for high absolute values, which makes the gradient vanish. Try to compare performance in MNIST between sigmoid and more recent activation functions like ReLU or tanh.

**Note** Try Mnist example with MLP after training CNNs and compare their performance with CNNs.

### Learning Rate and Optimizer
The learning rate of the gradient descent is a very common and crucial hyperparameter is a lot of ML applications, including Deep Learning.
Try tweaking it - you should observe that high values lead to unstable learning, but low values lead to slow learning.

Using simply the SGD update w -= alpha*grad_w(J) is often very naive, and prone to stochasticity. Lately, a lot of methods have appeared to try and add momentum, vary the learning rate depending on the specific parameter, etc. In PyTorch, the optimizer is selected using
`optimizer = torch.optim.SGD(net.parameters(), lr=0.01)`
Try replacing SGD by Adam, the most used optimizer nowadays (see [https://pytorch.org/docs/stable/optim.html](this documentation)). How does this impact learning?

## Loss and Regularization
The most common loss to optimize is simply the Means Squared Error, (h(x) - y)² - trying to minimize the distance between your prediction and the ground truth. However, other measures can be used. After documenting yourself, try comparing MSE with the Cross Entropy Loss in PyTorch on the MNIST problem.

A very common cause for overfitting is that the network weights explode - if you try to fit 10 2D points with a 10 degree polynomial, you will often find very high weight values that lead to severe overfitting, rather than truly trying to find the trend.
In order to prevent weight explosion, *L2 Regularization* add a soft constraint to the loss under the form of a lambda*||w||\_2 term (L1 Reg uses norm 1). This way, the optimizer tries to solve the task using weights as small as possible. Conveniently in PyTorch, as you can see in the doc, the Regularization ("weight decay") is an optional argument to the optimizer!

## Batch size
The reason the optimizer is called Stochastic Gradient Descent, as opposed to usual Gradient Descent, is because we only use subsets (batches) of the training data instead of the whole thing at once, acting like a sample in a stochastic computation. This was found to lead to great gains in wall-clock performance, since we don't have to loop over the whole dataset, which might be millions of entries big. In particular, this has lead to huge gains in efficiency thanks to GPUs, massively excelling in parallelized computing but with limited RAM that cannot hold the whole dataset at once.
The size of the batch becomes a hyperparameter - try to play with it! Can you see the differences in wall-clock performance?

## Dropout
The neurons of a neural network are extremely heavily dependent on the values of the previous neurons - each of the inputs can have a drastic impact on the output. This is often a major culprit for overfitting, where the neurons cannot generalize properly because the new testing distribution looks very different from the training distribution.
In order to prevent these heavy dependencies, one of the core techniques of Deep Learning was invented: Dropout. This simply means that in training, each neuron has some probability to be turned off altogether! This means that the downstream neurons need to be flexible enough to adapt to all kinds of changes in input; no rely too heavily on a single input, but rather find valuable information in all of it.
Dropout can conveniently be seen as an [https://pytorch.org/docs/stable/nn.html#dropout-layers](additional layer), that you can add after any layer (except the output), with a constant giving the probability to turn the neuron off.
Can you see an increase in generalization with Dropout?

