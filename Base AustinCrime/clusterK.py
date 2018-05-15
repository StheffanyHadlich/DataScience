from __future__ import division
from linear_algebra import squared_distance, vector_mean, distance
import math, random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class KMeans:
    """performs k-means clustering"""

    def __init__(self, k):
        self.k = k          # number of clusters
        self.means = None   # means of clusters
        
    def classify(self, input):
        """return the index of the cluster closest to the input"""
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))
                   
    def train(self, inputs):
    
        self.means = random.sample(inputs, self.k)
        assignments = None
        print(self.k)
        while True:
            # Find new assignments
            new_assignments = list(map(self.classify, inputs))

            # If no assignments have changed, we're done.
            if assignments == new_assignments:                
                return

            # Otherwise keep the new assignments,
            assignments = new_assignments    

            for i in range(self.k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]
                # avoid divide-by-zero if i_points is empty
                if i_points:                                
                    self.means[i] = vector_mean(i_points)    

					
def squared_clustering_errors(inputs, k):
    """finds the total squared error from k-means clustering the inputs"""
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = map(clusterer.classify, inputs)
    
    return sum(squared_distance(input,means[cluster])
               for input, cluster in zip(inputs, assignments))



if __name__ == "__main__":
    
    data = pd.read_csv('austin_crime.csv',header=0, names = ["clearance_date","clearance_code","clearance_status","description_code","description","district_code","district","latitude","longitude","timestamp","time"])
    data = data.drop(["clearance_date","clearance_code","clearance_status","description_code","description","district","latitude","longitude","timestamp"],axis=1)
    x = data[:-1] #tipo de crime e status de clarificação

    #inputs = np.array(x)
    inputs = np.array(x)
    print (inputs)
    print (len(inputs))
    
    x = [row[0] for row in inputs]
    print (x)
    y = [row[1] for row in inputs]
    print (y)
    plt.scatter(x, y)
    plt.title("Tempo por distrito para encerramento de crimes")
    plt.xlabel("distrito")
    plt.ylabel("tempo")
    plt.show()


    #ks = range(1, len(inputs) + 1)
    ks = range(1, 20)
    errors = [squared_clustering_errors(list(inputs), k) for k in ks]
    plt.plot(ks, errors)
    plt.xticks(ks)
    plt.xlabel("k")
    plt.ylabel("total squared error")
    plt.show()


    random.seed(0)
    clusterer = KMeans(2)

    clusterer.train(inputs)
    print ("2-means:")
    print (clusterer.means)
	
    plt.plot(x, y, 'b*')
    plt.title("distribuicao pontos")
    plt.xlabel("x")
    plt.ylabel("y")
    clusterX = [row[0] for row in clusterer.means]
    clusterY = [row[1] for row in clusterer.means]
    plt.plot(clusterX, clusterY, 'rs')
    plt.show()



    random.seed(0) # so you get the same results as me
    clusterer = KMeans(3)
    clusterer.train(inputs)
    print ("3-means:")
    print (clusterer.means)
    print ()

    plt.plot(x, y, 'b*')
    plt.title("distribuicao pontos")
    plt.xlabel("x")
    plt.ylabel("y")
    clusterX = [row[0] for row in clusterer.means]
    clusterY = [row[1] for row in clusterer.means]
    plt.plot(clusterX, clusterY, 'rs')
    plt.show()
