def k_means(X, Y, k=2):
    """This function will calculate and plot k-means clusters for two-dimensional data input as X and Y"""
    from matplotlib import pyplot as plt
    import random
    import numpy as np
    import pandas as pd
    
    fig, ax = plt.subplots(1, 5, figsize = (15, 3))
    ax[0].set_title('the data')
    ax[0].scatter(X, Y, c='k')
    all_pts = list(zip(X, Y))
    pts = random.sample(all_pts, k)
    arr_pts = np.array(pts)
    ax[1].set_title('initialize centroids')
    ax[1].scatter(X, Y, c='k')
    ax[1].scatter(arr_pts[:, 0], arr_pts[:, 1], c='r')
    
    clusts = []
    for pt in pts:
        clusts.append([pt])
    
    for pt in all_pts:
        dists = []
        for c_pt in pts:
            dists.append(np.linalg.norm(np.array(pt) - np.array(c_pt)))
        dist_min = dists.index(min(dists))
        clusts[dist_min].append(pt)
    
    clusts = [list(set(clust)) for clust in clusts]
    
    # Calculate centroids
    centers = []
    for clust in clusts:
        arr_clust = np.array(clust)
        centers.append((arr_clust[:, 0].mean(), arr_clust[:, 1].mean()))
    
    arr_centers = np.array(centers)
    ax[2].set_title('first cluster assignments')
    ax[2].scatter(X, Y, c='k')
    ax[2].scatter(arr_centers[:, 0], arr_centers[:, 1], c='r')
    
    df = pd.DataFrame(clusts).T
    for j in range(len(df.T)):
        points = df[j].dropna()
        ax[2].scatter([i[0] for i in points], [i[1] for i in points])
        
    
    
    new_clusts = []
    for cen in centers:
        new_clusts.append([cen])
    for pt in all_pts:
        dists = []
        for c_pt in centers:
            dists.append(np.linalg.norm(np.array(pt) - np.array(c_pt)))
        dist_min = dists.index(min(dists))
        new_clusts[dist_min].append(pt)
    for i in range(len(centers)):
        if centers[i] not in all_pts:
            new_clusts[i].remove(centers[i])
    
    
    # Are the new clusters different? If so, recalculate centroids!
    verdict = 'done'
    for i in range(len(clusts)):
        if set(clusts[i]) != set(new_clusts[i]):
            verdict = 'not done'
            break
        else:
            continue
    
    while verdict == 'not done':
        old_clusts = new_clusts
        centers = []
        for clust in new_clusts:
            arr_clust = np.array(clust)
            centers.append((arr_clust[:, 0].mean(), arr_clust[:, 1].mean()))
    
        new_clusts = []
        for cen in centers:
            new_clusts.append([cen])
        for pt in all_pts:
            dists = []
            for c_pt in centers:
                dists.append(np.linalg.norm(np.array(pt) - np.array(c_pt)))
            dist_min = dists.index(min(dists))
            new_clusts[dist_min].append(pt)
        for i in range(len(centers)):
            if centers[i] not in all_pts:
                new_clusts[i].remove(centers[i])
        verdict = 'done'
        for i in range(len(clusts)):
            if set(old_clusts[i]) != set(new_clusts[i]):
                verdict = 'not done'
                break
            else:
                continue
    
    last_centers = centers
    arr_last_centers = np.array(last_centers)
    
    ax[3].set_title('final centroids')
    ax[3].scatter(X, Y, c='k')
    ax[3].scatter(arr_last_centers[:, 0], arr_last_centers[:, 1], c='r')

    df = pd.DataFrame(new_clusts).T
    
    ax[4].set_title('final clusters')
    ax[4].scatter(arr_last_centers[:, 0], arr_last_centers[:, 1], c='r')
    for j in range(len(df.T)):
        points = df[j].dropna()
        ax[4].scatter([i[0] for i in points], [i[1] for i in points])
    
    return df