import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#number of trials
n =  20

#Probability that question is right
p = 0.5

experiment=np.zeros(1)
acctual=np.zeros(1)
data_binom = binom.rvs(n,p,size=simlen)  #Simulating the event 
defects,stimulation = np.unique(data_binom , return_counts= True)
stimulation = np.cumsum(stimulation)/simlen
experiment[0]=stimulation[11]
acctual[0]=binom.cdf(11,n,p)
exp = str(round((1-experiment[0]),4))
act = str(round((1-acctual[0]),4))
print("For answer  stimulation value is "+ exp +" and acctual value is "+ act )
