
data("mtcomputer_data")
View(mtcomputer_data)
View(computer_data)


computer_data <- read.csv(file.choose()) # choose the computer_data.csv data set
View(computer_data)

attach(computer_data)
# Exploratory Data Analysis(60% of time)
# 1. Measures of Central Tendency
# 2. Measures of Dispersion
# 3. Third Moment Business decision
# 4. Fourth Moment Business decision
# 5. Probability distributions of variables
# 6. Graphical representations
#  > Histogram,Box plot,Dot plot,Stem & Leaf plot, 
#     Bar plot



# 7. Find the correlation b/n Output (price) & (speed,hd,ram,screen,cd,multi,premium,ads,trend)-Scatter plot
pairs(computer_data)
plot(computer_data)
# 8. Correlation Coefficient matrix - Strength & Direction of Correlation
cor(computer_data)

### Partial Correlation matrix - Pure Correlation  b/n the varibles
#install.packages("corpcor")
library(corpcor)
cor2pcor(cor(computer_data))


# The Linear Model of interest
model.computer_data <- lm(price~speed+hd+ram+screen+cd+multi+premium+ads+trend,data = computer_data)
summary(model.computer_data)
###r-squared:0.78,so above 0.67 model is moderated
# Prediction based on only speed 
model.computer_dataS<-lm(price~speed)
summary(model.computer_dataS) # speed became significant
#r-squared:0.09 poor corelated
# Prediction based on only hd
model.computer_dataH<-lm(price~hd)
summary(model.computer_dataH) # hd became significant
# Prediction based on only ram
model.computer_dataR<-lm(price~ram)
summary(model.computer_dataR) # ram became significant
# Prediction based on only screen 
model.computer_dataSc<-lm(price~screen)
summary(model.computer_dataSc) # screen became significant
# Prediction based on only cd 
model.computer_dataC<-lm(price~cd)
summary(model.computer_dataC) # cd significant
## Prediction based on only multi
model.computer_dataM<-lm(price~multi)
summary(model.computer_dataS) # multi became significant
# Prediction based on only premium 
model.computer_dataP<-lm(price~premium)
summary(model.computer_dataP) # premium became significant
# Prediction based on only ads 
model.computer_dataA<-lm(price~ads)
summary(model.computer_dataA) # ads became significant
# Prediction based on only trend
model.computer_dataT<-lm(price~trend)
summary(model.computer_dataT) # trend became significant
library(psych)
pairs.panels(computer_data)


library(car)
## Variance Inflation factor to check collinearity b/n variables 
vif(model.computer_data)
## vif>10 then there exists collinearity among all the variables 

## Added Variable plot to check correlation b/n variables and o/p variable
avPlots(model.computer_data)

## VIF and AV plot has given us an indication to delete "wt" variable
panel.cor<-function(x,y,digits=2,prefix="",cex.cor)
{
  usr<- par("usr"); on.exit(par(usr))
  par(usr=c(0,1,0,1))
  r=(cor(x,y))
  txt<- format(c(r,0.123456789),digits=digits)[1]
  txt<- paste(prefix,txt,sep="")
  if(missing(cex.cor)) cex<-0.4/strwidth(txt)
  text(0.5,0.5,txt,cex=cex)
}
pairs(computer_data,upper.panel = panel.cor,main="Scatter plot matrix with Correlation coefficients")

# It is Better to delete influential observations rather than deleting entire column which is 
# costliest process
# Deletion Diagnostics for identifying influential observations
influence.measures(model.computer_data)
library(car)
## plotting Influential measures 
windows()
influenceIndexPlot(model.computer_data,id.n=3) # index plots for infuence measures
influencePlot(model.computer_data,id.n=3) # A user friendly representation of the above


model_1<-lm(price~.,data=computer_data[-c(4478,3784)])
summary(model_1)
model_2<-lm(price~.,data=computer_data[-c(1701,1441)])
summary(model_2)
########fianl model
plot(lm(price~.,data=computer_data[-c(1701,1441)]))

summary(lm(price~.,data=computer_data[-c(1701,1441)]))

# Evaluate model LINE assumptions 

#Residual plots,QQplot,std-Residuals Vs Fitted,Cook's Distance 
qqPlot(model.computer_data,id.n = 4)
# QQ plot of studentized residuals helps in identifying outlier 




hist(residuals(model_2)) # close to normal distribution
