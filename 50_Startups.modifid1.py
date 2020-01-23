# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:10:39 2019

@author: admin
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# loading the data
startup=pd.read_csv("file:///E:/excelr/course/assignment ans/multilinear regression/50_Startups.modifid.csv")
print(startup)
type(startup)
# to get top 6 rows
##cars.head(10) # to get top n rows use cars.head(10)

# Correlation matrix 
startup.corr()
type(startup)
# we see there exists High collinearity between input variables especially between
# [Hp & SP] , [VOL,WT] so there exists collinearity problem
 
# Scatter plot between the variables along with histograms
import seaborn as sns
sns.pairplot(startup.iloc[:,:])


# columns names
startup.columns

# pd.tools.plotting.scatter_matrix(cars); -> also used for plotting all in one graph
                             
# preparing model considering all the variables 
import statsmodels.formula.api as smf # for regression model
         
# Preparing model                  
ml1 = smf.ols('Profit~Spend+Administration+Market+State',data=startup).fit() # regression model

# Getting coefficients of variables               
ml1.params

# Summa# p-values for WT,VOL are more than 0.05 and also we know that [WT,VOL] has high correlation value 

# preparing model based only administaraytion
ml_v=smf.ols('Profit~Administration',data = startup).fit()  
ml_v.summary() # 0.162
# p-value <0.05 .. It is significant 

# Preparing model based only on market
ml_w=smf.ols('Profit~Market',data = startup).fit()  
ml_w.summary() # 0.0000

# Preparing model based only on state & administaration
ml_wv=smf.ols('Profit~State+Administration',data = startup).fit()  
ml_wv.summary() # 0.297,0.167



# Both coefficients p-value became insignificant... 
# So there may be a chance of considering only one among state & administartion

# Checking whether data has any influential values 
# influence index plots

import statsmodels.api as sm
sm.graphics.influence_plot(ml1)
# index 76 AND 78 is showing high influence so we can exclude that entire row

# Studentized Residuals = Residual/standard deviation of residuals


startup_new = startup.drop(startup.index[[46,49,48]],axis=0) # ,inplace=False)

#startup.drop(["price"],axis=1)

# X => A B C D 
# X.drop(["A","B"],axis=1) # Dropping columns 
# X.drop(X.index[[5,9,19]],axis=0)

#X.drop(["X1","X2"],aixs=1)
#X.drop(X.index[[0,2,3]],axis=0)


# Preparing model                  
ml_new = smf.ols('Profit~Spend+Market',data = startup_new).fit()    

# Getting coefficients of variables        
ml_new.params

# Summary
ml_new.summary() # 0.96

# Confidence values 99%
print(ml_new.conf_int(0.01)) # 99% confidence level


# Predicted values of profit 
mpg_pred = ml_new.predict(startup_new)
mpg_pred

startup_new.head()
# calculating VIF's values of independent variables
rsq_hp = smf.ols('Spend~Administration+Market+State',data=startup_new).fit().rsquared
  
vif_hp = 1/(1-rsq_hp) # 2.71

rsq_ap = smf.ols('Administration~Spend+Market+State',data=startup_new).fit().rsquared
  
vif_ap = 1/(1-rsq_ap) # 1.23

rsq_mp = smf.ols('Market~Administration+Spend+State',data=startup_new).fit().rsquared
  
vif_mp = 1/(1-rsq_mp) # 2.70

rsq_sp = smf.ols('State~Administration+Market+Spend',data=startup_new).fit().rsquared
  
vif_sp = 1/(1-rsq_sp) # 1.03

           # Storing vif values in a data frame
d1 = {'Variables':['Spend','Administration','Market','State'],'VIF':[vif_hp,vif_ap,vif_mp,vif_sp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame
# As weight is having higher VIF value, we are not going to include this prediction model

# Added varible plot 
sm.graphics.plot_partregress_grid(ml_new)

# added varible plot for weight is not showing any significance 

# final model
final_ml= smf.ols('Profit~Spend+Market',data = startup_new).fit()
final_ml.params
final_ml.summary() # 0.96
# As we can see that r-squared value has increased from 0.810 to 0.812.

mpg_pred = final_ml.predict(startup_new)

import statsmodels.api as sm
# added variable plot for the final model
sm.graphics.plot_partregress_grid(final_ml)

