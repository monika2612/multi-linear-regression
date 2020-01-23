# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:27:40 2019

@author: lenovo
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# loading the data
computerdata = pd.read_csv("file:///E:/excelr/course/assignment ans/multilinear regression/Computer_Data(4).csv")

type(computerdata)
print(computerdata)
# to get top 6 rows
computerdata.head(10) # to get top n rows use cars.head(10)

# Correlation matrix 
computerdata.corr()
type(computerdata)
# we see there exists High collinearity between input variables especially between
# [Hp & SP] , [VOL,WT] so there exists collinearity problem
 
# Scatter plot between the variables along with histograms
import seaborn as sns
sns.pairplot(computerdata.iloc[:,:])


# columns names
computerdata.columns

# pd.tools.plotting.scatter_matrix(cars); -> also used for plotting all in one graph
                             
# preparing model considering all the variables 
import statsmodels.formula.api as smf # for regression model
         
# Preparing model                  
ml1 = smf.ols('price~speed+hd+ram+screen+cd+multi+premium+ads+trend',data=computerdata).fit() # regression model

# Getting coefficients of variables               
ml1.params

# Summary
ml1.summary()
# p-values =0 all atribute
# Checking whether data has any influential values 
# influence index plots


import statsmodels.api as sm
sm.graphics.influence_plot(ml1)

?computerdata.drop
computerdata_new = computerdata.drop(computerdata.index[[1440,1700]],axis=0) # ,inplace=False)
computerdata_new


# Preparing model
###ml1 = smf.ols('price~speed+hd+ram+screen+cd+multi+premium+ads+trend',data=computerdata).fit() # regression model
                  
ml_new =ml1 = smf.ols('price~speed+hd+ram+screen+cd+multi+premium+ads+trend',data=computerdata).fit() # regression model
   

# Getting coefficients of variables        
ml_new.params

# Summary
ml_new.summary() # 0.776

# Confidence values 99%
print(ml_new.conf_int(0.05)) # 99% confidence level


# Predicted values of MPG 
mpg_pred = ml_new.predict(computerdata_new)
mpg_pred

#cars_new.head()
# calculating VIF's values of independent variables
rsq_hp = smf.ols('speed~hd+ram+screen+cd+multi+premium+ads+trend',data=computerdata_new).fit().rsquared 
print(rsq_hp) 
vif_hp = 1/(1-rsq_hp) # 1.26
print(vif_hp)
rsq_wt = smf.ols('hd~speed+ram+screen+cd+multi+premium+ads+trend',data=computerdata_new).fit().rsquared  
vif_wt = 1/(1-rsq_wt) # 4.20

rsq_vol = smf.ols('trend~hd+ram+screen+cd+multi+premium+ads+speed',data=computerdata_new).fit().rsquared  
vif_vol = 1/(1-rsq_vol) #  2.024

rsq_sp = smf.ols('ads~hd+ram+screen+cd+multi+premium+trend+speed',data=computerdata_new).fit().rsquared  
vif_sp = 1/(1-rsq_sp) #  1.21

rsq_rp = smf.ols('ram~hd+screen+cd+multi+premium+speed+trend+ads',data=computerdata_new).fit().rsquared  
vif_rp = 1/(1-rsq_rp) #  2.97
rsq_scp = smf.ols('screen~hd+ram+trend+cd+multi+premium+ads+speed',data=computerdata_new).fit().rsquared  
vif_scp = 1/(1-rsq_scp) #  1.81


rsq_cdp = smf.ols('cd~+trend+hd+ram+screen+multi+premium+ads+speed',data=computerdata_new).fit().rsquared  
vif_cdp = 1/(1-rsq_cdp) #  1.85
rsq_mp = smf.ols('multi~hd+ram+screen+cd+trend+premium+ads+speed',data=computerdata_new).fit().rsquared  
vif_mp = 1/(1-rsq_mp) #  1.29


rsq_p = smf.ols('premium~hd+ram+screen+cd+multi+trend+ads+speed',data=computerdata_new).fit().rsquared  
vif_p = 1/(1-rsq_p) #  1.10
          # Storing vif values in a data frame
d1 = {'Variables':['speed','hd','trend','ads','ram','screen','cd','multi','premium'],
      'VIF':[vif_hp,vif_wt,vif_vol,vif_sp,vif_rp,vif_scp,vif_cdp,vif_mp,vif_p]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame

# Added varible plot 
sm.graphics.plot_partregress_grid(ml_new)

# added varible plot for weight is not showing any significance 

# final model
final_ml= smf.ols('price~speed+hd+ram+screen+cd+multi+premium+ads+trend',data = computerdata_new).fit()
final_ml.params
final_ml.summary() # 0.778
# As we can see that r-squared value has increased from 0.810 to 0.812.

mpg_pred = final_ml.predict(computerdata_new)

import statsmodels.api as sm
# added variable plot for the final model
sm.graphics.plot_partregress_grid(final_ml)

