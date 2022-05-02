# Natural Language Pre-Processing

The goal here is to introduce students to the main tasks of pre-processing natural-language documents for analysis: eliminating capitalization, punctuation, stopwords, etc.

## Prerequisites

Make sure you're reasonably comfortable with RegEx.

## Learning Goals

- Describe the basic concepts of NLP
- Use pre-processing methods for NLP
    - Tokenization
    - Stopwords removal

## Lesson Materials

- [Jupyter Notebook: Natural Language Pre-Processing](natural_language_pre-processing.ipynb)

## Lesson Plan

### Introduction (10 Mins)

Overview of NLP. Uses and applications of NLP. Many should be familiar to students already!

### Tokenization (10 Mins)

General interest in words, but sometimes higher-order n-grams are worth searching for. Consider, in a corpus to be sorted according to target audience, the value of 'high school' as opposed to finding 'high' and 'school' individually.

### Capitalization (5 Mins)

This is straightforward.

### Punctuation (5 Mins)

Note the use here of str.maketrans() etc.

### Stopwords (10 Mins)

### Numerals and RegEx (15 Mins)

RegEx is obviously a big can of worms. For our purposes we're going to work with a pattern that can found words that may or may not have an apostrophe.

### Conclusion (5 Mins)

Next up is lemmatizing and then vectorization!
