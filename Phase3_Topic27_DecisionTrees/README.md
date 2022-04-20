# Decision Trees

## Learning Goals

- Describe the decision tree modeling algorithm
- Use attribute selection methods to build different trees
- Explain the pros and cons of decision trees
- Interpret the feature importances of a fitted model

## Lecture Materials

[Jupyter Notebook: Decision Tree Modeling](decision_tree_modeling.ipynb)

## Lesson Plan

### Introduction (5 Mins)

Popular and highly effective (though often overfitting) classification model. (Note it CAN also be used for regression using variances of groups etc.)

### Branching as Partitioning (10 Mins)

Building a decision tree is effectively a matter of asking a sequence of yes/no questions of your data. Our predictive features and their distributions of values give us the framework for these questions.

### Entropy and Gini (15 Mins)

All we need now is some measure of the quality of each possible split. Both entropy and Gini consider the membership percentages of the various classes. A group that has an even mix of the target labels would be "maximally unhelpful". Or, if you like, it would provide the least possible information about the likely target value of one of its data points. Note that the choice of the binary logarithm is customary since that corresponds to the idea of binary states (bits).

### Trees in `sklearn` (10 Mins)

API is much the same as for other `sklearn` models. Note the `plot_tree()` function. It's useful to go through the numbers in the pictorial output that represnt the class membership, Gini impurities, etc.

### Terminology (5 Mins)

Root Nodes, Decision Nodes, Leaf Nodes, Parent/Child/Sibling etc. Intutitive but worth mentioning.

### Bias/Variance and Regularization (10 Mins)

It's good here to show the documentation for the `sklearn` tool, highlighting various hyperparameters, especially those used for regularization like `min_samples_leaf` and `max_depth`.

### Conclusion (5 Mins)

Pros and cons of decision trees. Their full utility will be found when used in ensemble models.