# K-Means Clustering

Overall goal here is to introduce students to k-means and make them comfortable implementing k-means models in `sklearn`.

## Learning Goals

- Assess what scenarios could use k-means
- Articulate the methodology used by k-means
- Apply KMeans from sklearn.cluster to a relevant dataset
- Select the appropriate number of clusters using the elbow method and Silhouette Scores
- Evaluate the weaknesses and remedies to k-means

## Lecture Materials

[Jupyter Notebook: K-Means Clustering](kmeans_clustering.ipynb)

## Lesson Plan 

### Introduction (5 Mins)

Nature of unsupervised learning. Set up market segmentation scenario.

### Concept Introduction (30 Mins)

- eyeballing an appropriate number of clusters
- watching and interpreting the k-means .gif's
- illustrating with k-means-plotter
- looking at parameters of `sklearn.cluster.KMeans`

### Exercise using 2 and 4 clusters instead of 3 (2 Mins)

### Choosing k (15 Mins)

Describe inertia as "SSE". Inertia only goes down with higher k, but intuitively we want lower k. Plots of inertia and Silhouette Scores vs. k.

### Weaknesses of k-Means (10 Mins)

Illustration of how different variances, densities, shapes, etc. can affect the quality of k-means clustering.

### Conclusion (3 Mins)

Pointing ahead to alternative forms of clustering.

### Level-Up: Exercise

- k-means on wine dataset

## Tips

The k-means notebook runs a little on the long side. Make sure to leave enough time (~20 mins) to talk about the Elbow Method and Silhouette scores.