import numpy as np
import scipy.stats 

def testStatistic( data1, data2 ) :
  # This function should calcualte and return the test statistic T that is 
  # described in the panel on the right.  Notice that you will need to compute 
  # estimates of the two sample variances and the combined variance 
  # in order to complete this function.
  

def pvalue( data1, data2 ) : 
  # You need to write code to determine the pvalue here.  This code will need to
  # include a call to test statistic
  
  
data1 = np.array([-0.80, -0.35, -1.41, 0.75, 1.91, 1.52, -0.10, 0.68])
data2 = np.array([-0.55, -0.91, -0.13, 0.00, 0.83,  0.06, 0.31, -0.62])
print("Null hypothesis: the expectations for the two sampled distributions are the same")
print("Alternative hypothesis: the expectations for for the two sampled distributions are different")
print("The p-value for this hypothsis test is", pvalue( data1, data2 ) )
