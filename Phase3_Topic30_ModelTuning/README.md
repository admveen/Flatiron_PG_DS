# Tuning Models

## Learning Goals

- explain what hyperparameters are
- describe the purpose of gridsearching
- implement gridsearching for the purposes of model optimization

## Lecture Materials

[Jupyter Notebook: Model Tuning](model_tuning.ipynb)

## Lesson Plan

### Nature of Hyperparameters (5 Mins)

Hyperparameters allow for "variations on a theme" for different model types. This is NOT like the parameters of a parametric model, which are optimized during training and then not adjusted.

### Preparing the Penguins Dataset (10 Mins)

The three-class species column of the dataset will be our target. The prep involves scaling of numerical variables and one-hot-encoding of categorical variables.

### Tweaking a Few Hyperparameters Randomly (5 Mins)

Goal here is just to illustrate different model performance with different hyperparameter settings.

### Systematic Searching with `GridSearchCV` (20 Mins)

Some guidelines here about how to choose ranges for your hyperparameters. (Is the relevant variable discrete or continuous? Is there a maximum or minimum value? Etc.)

### Intro to Pipelines (15 Mins)

Pipelines will re-appear in the sequel to the classification-workflow lecture. We also here illustrate gridsearching a pipeline.

### Exercise (0-5 Mins)

This exercise asks for code and a short paragraph. There will likely not be enough time for this.

### Conclusion (5 Mins)

Level-Ups here on `RandomizedSearchCV` (good for continuously-valued hyperparameters) and on SMOTE. The classification-workflow lecture will make a point of using SMOTE only with **`imblearn`** pipelines.
