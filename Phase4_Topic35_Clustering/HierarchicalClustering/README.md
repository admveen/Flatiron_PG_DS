# Hierarchical Clustering

Overall goal here is to introduce students to hierarchical clustering, its two forms, and how to run the algorithms in `sklearn` and `scipy`.

## Learning Goals

- Describe the algorithms of agglomerative and divisive hierarchical clustering
- Compare and contrast hierarchical clustering with $k$-means clustering
- Implement hierarchical clustering with `scipy` and `sklearn`
- Build and interpret dendrograms

## Lecture Materials

[Jupyter Notebook: Hierarchical Clustering](hierarchical_clustering.ipynb)

## Lesson Plan

### Introduction (5 Mins)

Draw some data points on a whiteboard (a half-dozen or so) and describe the agglomerative clustering algorithm. Students will tend to have the right intuition here about how to cluster.

### Agglomerative Algorithm (15 Mins)

- Nature of dendrograms
- Linkage / Problem of how to measure inter-cluster distances

### Cophenetic Correlation (15 Mins)

- Make sure to point out that this is really just Pearson correlation on the sequences of distances!

### Sample dendrogram in `scipy` (10 Mins)

A picture is worth a thousand words here, but it's also worth saying something about the return of the `scipy.cluster.hierarchy.linkage()` function.

### Clustering on iris dataset for evaluation purposes (10 Mins)

### Conclusion (5 Mins)

Point to various criteria about how to choose a number of clusters. Plus advantages and disadvantages of this sort of clustering. Can point to penguins notebook for a survey of other clustering algorithms.

## Tips

### Greg Damico, 03/12/21

Time Permitting, I like to run through [the supplementary notebook on Minkowski Unit Circles](Supplements/unit_minkowski_circles.ipynb) at the end, as a way of illustrating the differences among possible distance metrics. [The other supplementary notebook on clustering with the penguins dataset](Supplements/the_varieties_of_clustering_and_penguins.ipynb) is really just an illustration of the different modeling techniques available through `sklearn`. Usually time is short and so I just let students look at that one on their own time.

### Greg Damico, 03/17/21

- I like to start the lecture by just drawing points on a whiteboard and eliciting an intuition for agglomerative clustering from the students. Start with each point its own cluster. Then: "What if I wanted (n-1) clusters?" etc.
- I also like to run through Kardi Teknomo's demonstration of building a dendrogram. Link is in the notebook.
