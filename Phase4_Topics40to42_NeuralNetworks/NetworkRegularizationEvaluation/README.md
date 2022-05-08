# Network Regularization and Evaluation

Exploring the options available in `keras` for coding up densely connected NNs.

## Learning Goals

- Use `keras` to code up a neural network model
- Explain dropout and early stopping as distinctive forms of regularization in neural networks
- Use wrappers inside `keras` to make models that can jibe with `sklearn`

## Lesson Materials

- [Jupyter Notebook: Network Regularization and Evaluation](network_regularization_and_evaluation.ipynb)

## Lesson Plan 

### Introduction (5 Mins)

Let's get our hands dirty in `keras`!

### Adjusting Training Parameters (15 Mins)

Experimenting with number of epochs, batch size, optimizer. Exercise here to have students add in validation data.

### Connecting with `sklearn` (10 Mins)

The example uses the KerasClassifier to build a model that we can run cross_val_score() on.

### Regularization (20 Mins)

Some new types here as well as L2 (and L1, though it's rarely used in NNs). Dropout and EarlyStopping are almost always good ideas!

### Multiclass Problem (5 Mins)

Now we convert to the natural "recognize the digit" problem, thus adjusting the model to include ten neurons in the output layer with softmax activation etc.

### Conclusion (5 Mins)

Next up: More complexity with CNNs.
