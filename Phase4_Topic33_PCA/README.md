# Principal Component Analysis (PCA)

Walk through using PCA with an artificial example, talking about the motivation, concepts and math behind the method. Then let students try to do it on their own.

## Learning Goals

- Explain the concepts behind principal component analysis (PCA)
- Explain how PCA addresses the problem of multicollinearity
- Explain the idea of eigendecomposition
- Implement PCA using `sklearn`

## Lesson Materials

- [Jupyter Notebook: Principal Component Analysis](principal_component_analysis.ipynb)

## Lesson Plan

### Introduction (5 Mins)

Welcome to the big leagues/Phase 4, where we tackle a bunch of specific modeling types and issues. Today: What do we do if we have tons of features?

### Scenario: Shipping Costs (35 Mins)

Walk through the scenario step by step, pausing occasionally to check for questions.

### Scenario: Car MPG (15 Mins)

Pair students up to run PCA on the car dataset. Walk them through the preprocessing that's already been done for them, and remind them to do validation with the test set. Potential things students will need to work out that you might need to help with:

* Fitting the PCA object on the train data
* Getting & examining the eigenvalues
* How many components to keep
* Modeling with the new features
* Interpreting the new features

### Conclusion (5 Mins)

Debrief the exercise, surface sticking points to discuss, open Q&A

##  Additional Resources

### Lecture Source Materials

Data generated using [this Google Sheet](https://docs.google.com/spreadsheets/d/1KeYVADLh24cCSmoyENA0zdeZ6KI58GR01TN9Q7u7Il4/edit?usp=sharing)