#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:09:09 2023

@author: dixons
"""

# libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# I build a data set: 10 individuals and 5 variables for each
df1 = pd.read_excel("CORR.xlsx")
#df = pd.DataFrame({ 'A':ind1, 'B':ind1 + np.random.randint(10, size=(10)) , 'C':ind1 + np.random.randint(10, size=(10)) , 'D':ind1 + np.random.randint(5, size=(10)) , 'E':ind1 + np.random.randint(5, size=(10)), 'F':ind5, 'G':ind5 + np.random.randint(5, size=(10)) , 'H':ind5 + np.random.randint(5, size=(10)), 'I':ind5 + np.random.randint(5, size=(10)), 'J':ind5 + np.random.randint(5, size=(10))})

# Calculate the correlation between individuals. We have to transpose first, because the corr function calculate the pairwise correlations between columns.
#corr = df.corr()

# Transform it in a links data frame (3 columns only):
links = df1.stack().reset_index()
links.columns = ['Index', 'Ticker', 'Value'] 

#links.columns
links['Value'] = links['Value'].apply(lambda x: x if not isinstance(x, str) else 1)

df2 = pd.read_excel("filtered_links.xlsx")

# Keep only correlation over a threshold and remove self correlation (cor(A,A)=1)
links_filtered=df2.loc[ (df2['Value'] != 1) ]

#& (df2['Value'] >= 0.9)


#links_filtered.to_excel("Linksfiltered.xlsx")

# Build your graph
G=nx.from_pandas_edgelist(links_filtered, 'Ticker','Index')

G.nodes

pos = nx.spring_layout(G, k=1)
# Plot the network:
nx.draw_networkx(G, pos,with_labels=True, node_color='orange', node_size=400, edge_color='black', linewidths=1, font_size=15)
pos = nx.spring_layout(G, k=2, seed=42)


# =============================================================================
# =============================================================================
# # Covariance Matrix
# =============================================================================
# =============================================================================

df3 = pd.read_excel("COV2.xlsx")

links = df3.stack().reset_index()
links.columns = ['Index', 'Ticker', 'Value'] 

links.to_excel("cov2Links.xlsx")


-----

df4 = pd.read_excel("covLinks.xlsx")
df4

# Keep only correlation over a threshold and remove self correlation (cor(A,A)=1)
links_filtered=df4.loc[ (df4['Value'] != 1) & (df4['Value'] >= 5000)| (df4['Value'] <= -5000)]


#links_filtered.to_excel("Linksfiltered.xlsx")

# Build your graph
G=nx.from_pandas_edgelist(links_filtered, 'Ticker','Index')

G.nodes

# =============================================================================
# pos = nx.random_layout(G, k=2)
# pos = nx.kamada_kawai_layout(G, k=2)
# pos = nx.spring_layout(G, k=2)
# =============================================================================


# Plot the network:
nx.draw_networkx(G,with_labels=True, node_color='orange', node_size=1200, edge_color='black', linewidths=1, font_size=15)
#pos = nx.spring_layout(G, k=2, seed=42)



# =============================================================================
# =============================================================================
# # Summary Statistics
# =============================================================================
# =============================================================================



# Calculate the degree of each node
degree = dict(G.degree())
print("Degree of each node:", degree)

dfDegree = pd.DataFrame(G.degree())

# Convert DataFrame to LaTeX table
latex_table = dfDegree.to_latex(index=False)

print(latex_table)

########

# Calculate the clustering coefficient of each node
clustering_coefficient = nx.clustering(G)
print("\nClustering coefficient of each node:", clustering_coefficient)

# Calculate the average clustering coefficient of the graph
average_clustering = nx.average_clustering(G)
print("\nAverage clustering coefficient:", average_clustering)

# Calculate the betweenness centrality of each node
betweenness_centrality = nx.betweenness_centrality(G)
print("\nBetweenness centrality of each node:", betweenness_centrality)

# Calculate the shortest path between all pairs of nodes
shortest_paths = dict(nx.all_pairs_shortest_path(G))
print("\nShortest paths between all pairs of nodes:")
for source, paths in shortest_paths.items():
    print(f"Node {source}: {paths}")

# Calculate the diameter of the graph
diameter = nx.diameter(G)
print("\nDiameter of the graph:", diameter)

# Calculate the density of the graph
density = nx.density(G)
print("\nDensity of the graph:", density)
density


# =============================================================================
# =============================================================================
# # Do a KMeans Graph
# =============================================================================
# =============================================================================
from sklearn.cluster import KMeans
# Create a DataFrame with the network metrics
data = {
    'degree': [degree[node] for node in G.nodes()],
    'clustering_coefficient': [clustering_coefficient[node] for node in G.nodes()],
    'betweenness_centrality': [betweenness_centrality[node] for node in G.nodes()],
}
df = pd.DataFrame(data, index=G.nodes())

# Apply the k-means algorithm with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42).fit(df)

# Assign the cluster labels to each node
cluster_labels = kmeans.labels_
clusters = {node: cluster_labels[i] for i, node in enumerate(G.nodes())}

# Create a color map based on the cluster labels
color_map = {0: 'pink', 1: 'green', 2: 'blue', 3: 'orange', 4:'yellow', 5:'pink'}
colors = [color_map[clusters[node]] for node in G.nodes()]

# Draw the graph with node colors representing the clusters
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, node_color=colors, with_labels=True, node_size=800, alpha=0.8)


# =============================================================================
# =============================================================================
# # Draw A Graph Where Node size increases wit Degree
# =============================================================================
# =============================================================================

# Define the scaling factor for node size
scaling_factor = 200

# Calculate node sizes based on degree
node_sizes = [degree[node] * scaling_factor for node in G.nodes()]

# Draw the graph with node size proportional to degree
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=True, node_color = colors, node_size=node_sizes, alpha=0.8)
plt.title('Crypto Covariance Network')
plt.show()
