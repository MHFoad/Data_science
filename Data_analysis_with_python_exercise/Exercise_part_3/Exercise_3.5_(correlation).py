from scipy.stats import pearsonr
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv(".\iris.csv").drop('species', axis=1).values

def lengths():
    data= load()
    sepal_length=data[:,0]
    petal_length=data[:,2]
    correlation,_= pearsonr(sepal_length,petal_length)
    #print(correlation,_)
    return correlation

def correlations():
    data=load()
    correlation_matrix=np.corrcoef(data.T)
    return correlation_matrix

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()