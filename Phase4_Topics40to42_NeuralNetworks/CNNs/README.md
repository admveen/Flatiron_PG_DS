# Convolutional Neural Networks (CNNs)

This material is in the appendix on Canvas, but we judged it important enough to include in the lecture material. The main goal here is to introduce the distinctive layers found in CNNs and run through a demo with `keras` on the MNIST data.

## Learning Goals

- Describe the types of layers that are distinctive for convolutional nets
- Utilize `tensorflow` to build CNNs
- Evaluate CNN models

## Lecture Materials

[Jupyter Notebook: Intro to CNNs](intro_to_cnns.ipynb)

## Lesson Plan 

### Introduction (5 Mins)

Great utility of CNNs for image processing, effected by new and different types of NN layers

### Biological Inspiration (10 Mins)

Useful to note the parallels between (animal) optical neurons and CNN structures. Trying to "zoom out" and pick up on the larger objects.

### Nature of Convolutions (15 Mins)

The mathematical definition is not so very important, but there are good examples (links in ntbk) of filters and what convolution looks like in the case of image processing.

### Perform the Convolution! (5 Mins)

Good check to see if students understand the transformation and good verification simultaneously that the filter does indeed do the service of finding horizontal edges.

### Nature of Pooling (5 Mins)

Not much time is needed here, but it's useful to describe a couple strategies here, especially max pooling.

### Tensorflow's Demo of MNIST Performance (15 Mins)

Useful to walk through the code here.

### Conclusion (5 Mins)

Checking the model's predictions to see how it does on a particular image. (Thanks, Alex!)

## Tips

### Greg Damico, 04/16/21

I like to spend a good bit of time on several of the links in the notebook. One describes convolutions abstractly, and there's a nice animation there of a convolution of two "pulses". Another describes CNNs in detail. A third shows the effects of applying various kinds of filter to images.
