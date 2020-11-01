import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) : 
        N1, N2 = len(data1), len(data2)
        mu1, mu2 = sum(data1) / N1,  sum(data2) / N2
        sigma21 = N1*( sum(data1*data1) / N1 - mu1*mu1 )
        sigma22 = N2*( sum(data2*data2) / N2 - mu2*mu2 )
        sigf = (sigma21 + sigma22) / (N1+N2-2)
        stat = ( mu1 - mu2 ) / np.sqrt( sigf / N1  + sigf / N2 )
        self.assertTrue( np.abs( stat - testStatistic( data1, data2 ) )<1e-7, "Your function to compute the test statistic is not correct" )
        
    def test_pvalue(self) : 
        T = testStatistic( data1, data2 )
        if T<0 : pv = 2*scipy.stats.t.cdf( T, len(data1) + len(data2) - 2 )
        else : pv = 2*scipy.stats.t.cdf( -T, len(data1) + len(data2) - 2 )
        self.assertTrue( np.abs( pv - pvalue( data1, data2) )<1e-7, "Your function to compute the p-value is not correct" )
