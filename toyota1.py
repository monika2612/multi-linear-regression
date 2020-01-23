# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:30:38 2019

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:02:54 2018

@author: madis
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# loading the data
toyota = pd.read_csv("file:///E:/excelr/course/assignment/multi linear regression/ToyotaCorolla.csv")

type(toyota)
print(toyota)
# to ges
toyota.head(10) # to get top n rows use cars.head(10)

# Correlation matrix 
toyota.corr()
type(toyota)
# we see there exists High collinearity between input variables especially between
# [Hp & SP] , [VOL,WT] so there exists collinearity problem
 
# Scatter plot between the variables along with histograms
import seaborn as sns
sns.pairplot(toyota.iloc[:,:])


# columns names
toyota.columns

# pd.tools.plotting.scatter_matrix(cars); -> also used for plotting all in one graph
                             
# preparing model considering all the variables 

import statsmodels.formula.api as smf # for regression model
         
# Preparing model                  
ml1 = smf.ols('Price~Age+KM+HP+cc+Doors+Gears+Tax+Wei',data=toyota).fit() # regression model

# Getting coefficients of variables               
ml1.params

# Summary
ml1.summary()
# p-values for cc,doors are more than 0.05 and also we know that [WT,VOL] has high correlation value 

# preparing model based only on cc
ml_v=smf.ols('Price~cc',data = toyota).fit()  
ml_v.summary() # 0.
# p-value <0.05 .. It is significant 

# Preparing model based only on doors
ml_w=smf.ols('Price~Doors',data = toyota).fit()  
ml_w.summary() # 0.

# Preparing model based only on cc&doors
ml_wv=smf.ols('Price~cc+Doors',data = toyota).fit()  
ml_wv.summary() # 0.

# Both coefficients p-value became significant... 
# So there may be a chance of considering only one among VOL & WT

# Checking whether data has any influential values 
# influence index plots


import statsmodels.api as sm
sm.graphics.influence_plot(ml1)
# index  80 is showing high influence so we can exclude that entire row

# Studentized Residuals = Residual/standard deviation of residuals

?toyota.drop
toyota_new = toyota.drop(toyota.index[[80]],axis=0) # ,inplace=False)
toyota_new
#cars.drop(["MPG"],axis=1)

# X => A B C D 
# X.drop(["A","B"],axis=1) # Dropping columns 
# X.drop(X.index[[5,9,19]],axis=0)

#X.drop(["X1","X2"],aixs=1)
#X.drop(X.index[[0,2,3]],axis=0)


# Preparing model   
ml1 = smf.ols('Price~Age+KM+HP+cc+Doors+Gears+Tax+Wei',data=toyota).fit() # regression model
               
#
# Getting coefficients of variables        
# Confidence values 99%
print(ml1.conf_int(0.05)) # 99% confidence level


# Predicted values of price 
mpg_pred = ml1.predict(toyota)
mpg_pred

#cars_new.head()
# calculating VIF's values of independent variables
rsq_hp = smf.ols('Age~KM+HP+cc+Doors+Gears+Tax+Wei',data=toyota).fit().rsquared 
print(rsq_hp) 
vif_hp = 1/(1-rsq_hp) # 
print(vif_hp)
rsq_wt = smf.ols('KM~HP+cc+Doors+Gears+Tax+Wei+Age',data=toyota).fit().rsquared  
vif_wt = 1/(1-rsq_wt) # 

rsq_vol = smf.ols('HP~Age+KM+cc+Doors+Gears+Tax+Wei',data=toyota).fit().rsquared  
vif_vol = 1/(1-rsq_vol) #  


rsq_sp = smf.ols('cc~Age+KM+HP+Doors+Gears+Tax+Wei',data=toyota).fit().rsquared  
vif_sp = 1/(1-rsq_sp) #  
rsq_dd = smf.ols('Doors~Age+KM+HP+cc+Gears+Tax+Wei',data=toyota).fit().rsquared 
print(rsq_dd) 
vif_dd = 1/(1-rsq_dd) 
rsq_gp = smf.ols('Gears~Age+KM+HP+cc+Doors+Tax+Wei',data=toyota).fit().rsquared 
print(rsq_gp) 
vif_gp = 1/(1-rsq_gp) 
rsq_tp = smf.ols('Tax~Age+KM+HP+cc+Doors+Gears+Wei',data=toyota).fit().rsquared 
print(rsq_tp) 
vif_tp = 1/(1-rsq_tp)
 
rsq_wp = smf.ols('Wei~Age+KM+HP+cc+Doors+Gears+Tax',data=toyota).fit().rsquared 
print(rsq_wp)
vif_wp = 1/(1-rsq_wp)  

           # Storing vif values in a data frame
d1 = {'Variables':['Age','KM','HP','cc','Doors','Gears','Tax','Wei'],
      'VIF':[vif_hp,vif_wt,vif_vol,vif_sp,vif_dd,vif_gp,vif_tp,vif_wp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame

# Added varible plot 
sm.graphics.plot_partregress_grid(ml1)

# added varible plot for weight is not showing any significance 

# final model
final_ml= smf.ols('Price~Age+KM+HP+cc+Doors+Gears+Tax+Wei',data = toyota).fit()
final_ml.params
final_ml.summary() # 0.869
# As we can see that r-squared value has increased from 0.810 to 0.812.

mpg_pred = final_ml.predict(toyota)

import statsmodels.api as sm
# added variable plot for the final model
sm.graphics.plot_partregress_grid(final_ml)

