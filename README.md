# Comparison of means (small samples)

Now that we know how to calculate the total variance lets try and do a comparison of the sample means.  In `main.py`, there are two NumPy arrays with 8 elements called `data1` and `data2`.  These two data sets may or may not be a series of samples from the same underlying distribution.  You must, therefore, write code to perform a hypothesis test with the following null and alternative hypotheses:

* __null hypothesis__: the sample mean for the distributions from which `data1` and `data2` were sampled are the same.
* __alternative hypothesis__:  the sample mean for the distributions from which `data1` and `data2` were sampled are different.

The test __statistic__ you are going to use for this test is going to be the following:

![](https://render.githubusercontent.com/render/math?math=T=\frac{\frac{1}{n_1}\sum_{i=1}^{n_1}X_i-\frac{1}{n_2}\sum_{j=1}^{n_2}Y_j-\theta_0}{\sqrt{\frac{s^2}{n_1}%2B\frac{s^2}{n_2}}})

where the ![](https://render.githubusercontent.com/render/math?math=X_i) and ![](https://render.githubusercontent.com/render/math?math=Y_j) are the data points from `data1` and `data2` respectively.  ![](https://render.githubusercontent.com/render/math?math=n_1) and ![](https://render.githubusercontent.com/render/math?math=n_2) are the number of elements in these two NumPy arrays and where s is given by:

![](https://render.githubusercontent.com/render/math?math=s^2=\frac{(n_1-1)s_1^2%2B(n_2-1)s_2^2}{n_1%2Bn_2-2})

with ![](https://render.githubusercontent.com/render/math?math=s_1) and ![](https://render.githubusercontent.com/render/math?math=s_2) calculated using:

![](https://render.githubusercontent.com/render/math?math=s^2=\frac{n}{n-1}\left[\frac{1}{n}\sum_{i=1}^nX_i^2-\left(\frac{1}{n}\sum_{i=1}^nX_i\right)^2\right])

The number of samples the test statistic is computed from is small in this case so it is more appropriate to use a student t-distribution than a normal distribution as the probability distribution that the statistic is a sample from under the assumption of the null hypothesis. 

__With all that in mind, your task is to complete the code in `main.py` to perform this hypothesis test__ using the method described above.  In practice, this means you have to complete two functions:

1. `testStatistic` - this function takes two  NumPy arrays in input:  `data1` that contains the samples from the first distribution and `data2` contains the samples from the second distribution.  This function should return the test statistic, T, that is defined using the formula above.   You will also need to compute the two sample variances in this function and the combined variance.  
2. `pvalue` - this function takes two  NumPy arrays in input:  `data1` that contains the samples from the first distribution and `data2` contains the samples from the second distribution.   To complete the task you must use the value of the `testStatistic` to calculate the __p-value__.  The p-value should then be returned.





