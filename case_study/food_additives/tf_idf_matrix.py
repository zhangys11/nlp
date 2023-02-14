from scipy.sparse.csr import csr_matrix
import numpy as np
    
def tf_idf_matrix(X, IDF = None):

    # convert X to np array if it is a csr matrix
    # Following matrix operations require that.
    if isinstance(X, csr_matrix):
        X = X.A

    if IDF is None:
        # (X>0).sum(axis = 0) 得到每列>0的元素数目，即|{d∈D:t∈d}|
        IDF = np.log((1+X.shape[0])/(1 + (X>0).sum(axis = 0)))+1
        
    TF_IDF = X * IDF
    
    return TF_IDF, IDF