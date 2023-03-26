#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:29:14 2023

@author: dixons
"""

import pandas as pd
import numpy as np

# Define a function to calculate the covariance matrix
def covariance_matrix(stocks_df):
    """
    Calculates the covariance matrix of multiple stocks based on their price changes.
    
    Arguments:
    stocks_df -- a pandas DataFrame object representing the stocks data
    
    Returns:
    cov_matrix -- a numpy array representing the covariance matrix
    """
    returns = stocks_df.pct_change().dropna() # Calculate the percentage change of the stock prices and remove any NaN values
    cov_matrix = np.cov(returns.T) # Calculate the covariance matrix of the percentage changes
    
    return cov_matrix

# Example usage
stock_data = {
    'AAPL': [100, 105, 110, 115, 120],
    'GOOG': [500, 510, 520, 530, 540],
    'AMZN': [1000, 1020, 1040, 1060, 1080]
}
stocks_df = pd.DataFrame(stock_data)
cov_matrix = covariance_matrix(stocks_df)

# Print the covariance matrix
print(cov_matrix)



import networkx as nx
import numpy as np

# Define a function to create a graph
def create_graph(covariance_matrix, threshold):
    """
    Creates a graph based on the covariance matrix and a threshold value
    
    Arguments:
    covariance_matrix -- a numpy array representing the covariance matrix between the assets
    threshold -- a float representing the threshold value
    
    Returns:
    G -- a networkx Graph object representing the graph
    """
    n = len(covariance_matrix)
    G = nx.Graph()
    
    # Add nodes to the graph
    for i in range(n):
        G.add_node(i)
        
    # Add edges to the graph based on the covariance matrix
    for i in range(n):
        for j in range(i+1, n):
            if covariance_matrix[i][j] > threshold:
                G.add_edge(i, j, weight=covariance_matrix[i][j])
                
    return G

# Example usage
covariance_matrix = np.array([[1.0, 0.7, 0.3], [0.7, 1.0, 0.4], [0.3, 0.4, 1.0]])
threshold = 0.5
G = create_graph(covariance_matrix, threshold)

# Print the nodes and edges of the graph
print("Nodes:", G.nodes)
print("Edges:", G.edges)
