import numpy as np

def prefix_sum_2d(a): 
    a = np.array(a)
    R, C = a.shape 
    psa = np.zeros(a.shape)
  
    psa[0][0] = a[0][0] 
  
    # Filling first row  
    # and first column 
    for i in range(1, C) : 
        psa[0][i] = (psa[0][i - 1] + 
                       a[0][i]) 
    for i in range(0, R) : 
        psa[i][0] = (psa[i - 1][0] + 
                       a[i][0]) 
  
    # updating the values in  
    # the cells as per the  
    # general formula 
    for i in range(1, R) : 
        for j in range(1, C) : 
  
            # values in the cells of  
            # new array are updated 
            psa[i][j] = (psa[i - 1][j] + 
                         psa[i][j - 1] - 
                         psa[i - 1][j - 1] + 
                           a[i][j]) 
  
    return psa