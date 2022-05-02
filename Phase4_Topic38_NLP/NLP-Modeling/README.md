# NLP: Modeling

Goal here is to demonstrate how Naive Bayes modeling applies to NLP problems.

## Learning Goals

- Explain the use of Bayesian Reasoning for building NLP models
- Describe Laplace Smoothing
- Use `sklearn` and `nltk` to build NLP models

## Lesson Materials

[Jupyter Notebook: NLP Modeling](nlp_modeling.ipynb)

## Lesson Plan

### Introduction (10 Mins)

Set up small problem of identifying either "music" or "politics" from a string of text.

### Review of Bayes's Theorem (5 Mins)

### Application to Present Task (20 Mins)

- calculation of priors as initial distributions
- calculation of likelihoods (Laplace Smoothing + naive Bayes assumption)
- coding this up

### Back to Satire (5 Mins)

Text pre-processing, including vectorization

### Modeling (15 Mins)

Note that the first vectorizer uses only the top 5 vocab words!

### Conclusion (5 Mins)

Plenty of rabbit holes here:

- what about using other predictors along with text?
- what value of the Lidstone parameter should I use?
- what vectorizer should I use?

But we're moving on!
