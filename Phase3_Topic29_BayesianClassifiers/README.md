# Naive Bayes

## Learning Goals

- describe how Bayes's Theorem can be used to make predictions of a target
- identify the appropriate variant of Naive Bayes models for a particular business problem

## Lecture Materials

[Jupyter Notebook: Naive Bayes](naive_bayes.ipynb)

## Lesson Plan

### Introduction (5 Mins)

Bayes is back! Natural application of Bayes's Theorem to machine learning: Think of the hypothesis whose posterior we're calculating as the class prediction, and the evidence on which we condition as the values of the predictors.

### Spam Filter as Example (15 Mins)

NLP (Phase 4) is a very common application for NaiveBayes modeling. Note that the likelihoods and priors are simply calculated directly from the distributions of values in the data! Note also that the "naivety" is the assumption of probabilistic independence. For the spam filter this amounts to the (rather implausible) claim that individual words are probabilistically independent of each other when it comes to correct classification as ham or spam.

### Elephant Example (20 Mins)

Note the `sklearn` variations: `MultinomialNB`, `GaussianNB`, `BernoulliNB`. These variations are for different types of _predictors_.

This example uses normal PDFs as approximations of the relevant likelihoods. Note also that the full calculation of Bayes's Theorem is not really necessary in this case since the priors and denominators are identical for every class. So all we really need to compare are the likelihoods.

This example also introduces the idea of a multivariate normal distribution (normal distribution in multiple dimensions).

### Comma Survey Example (15 Mins)

For this example note that we compare our results not with those of `GaussianNB` but with those of `MultinomialNB`. Note also that  the priors are NOT identical in this case.

### Conclusion (5 Mins)

We'll see this type of modeling again when we get to NLP in Phase 4.