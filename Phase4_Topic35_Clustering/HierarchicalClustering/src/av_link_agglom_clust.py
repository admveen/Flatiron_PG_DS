def centrAggClust(X, Y):
    """This function uses centroid distances for agglomerative clustering, plotting all cluster
    assignments for 2 clusters up to n - 1 clusters, where n = len(X) = len(Y). It returns the
    suggested number of clusters (based on the shortest minimum distance used for agglomeration)."""
    
    # Import some necessary tools
    import numpy as np
    from matplotlib import pyplot as plt
    
    # Set the number of plots
    rows = int((len(X)-2) / 4)
    if (len(X) - 2) % 4 != 0:
        rows += 1
    if len(X) > 5:
        cols = 4
    else:
        cols = len(X)
    fig, ax = plt.subplots(rows, cols, figsize=(8,2*rows))
    plt.subplots_adjust(hspace=0.5)
    
    # Define the datapoints
    pts = list(zip(X, Y))
    clusts = [[pt] for pt in pts]
    end = len(clusts)
    
    # Keep track of minimum distances
    mins = []
    
    # We'll show assignments until we're down to 2 clusters
    while end > 2:
        
        # Initialize the minimum distance
        min_dist = 0
        for ptx in clusts[0]:
            for pty in clusts[1]:
                min_dist += np.sqrt((ptx[0] - pty[0])**2 + (ptx[1] - pty[1])**2)
        min_dist /= (len(clusts[0])*len(clusts[1]))
        
        # Record the clusters between which the distance is minimal
        nearest1 = 0
        nearest2 = 1
        
        # Start measuring distances
        # Select the first cluster
        for clust1 in range(end - 1):
            arr_clust1 = np.array(clusts[clust1])
            
            # Select the second cluster
            for clust2 in range(clust1 + 1, end):
                arr_clust2 = np.array(clusts[clust2])
                
                dist = 0
                for pt1 in arr_clust1:
                    for pt2 in arr_clust2:
                        dist += np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
                dist /= (len(arr_clust1)*len(arr_clust2))
                
                # Update if appropriate
                if dist < min_dist:
                    min_dist = dist
                    nearest1 = clust1
                    nearest2 = clust2
        
        # Record all minimal distances
        mins.append(min_dist)
        
        # Consolidate the nearest clusters
        clusts[nearest1].extend(clusts[nearest2])
        
        # Drop the absorbed cluster
        del clusts[nearest2]
        
        # Plot
        for clust in clusts:
            num = len(X) - end
            p_row = int(num / 4)
            p_col = num % 4
            if p_row < rows and p_col < cols and rows > 1:
                ax[p_row, p_col].set_title(f'{end - 1} clusters')
                ax[p_row, p_col].scatter(np.array(clust)[:, 0], np.array(clust)[:, 1])
            else:
                if p_row < rows and p_col < cols:
                    ax[p_col].set_title(f'{end - 1} clusters')
                    ax[p_col].scatter(np.array(clust)[:, 0], np.array(clust)[:, 1])
        
        # Update end
        end=len(clusts)
    
    # Find the suggested number of clusters
    if len(X) <= 2:
        out = 2
    else:
        out = len(X) - mins.index(np.max(mins))
    return out