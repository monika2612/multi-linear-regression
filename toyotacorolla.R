
data("mttoyotacorolla")
View(mttoyotacorolla)


toyotacorolla <- read.csv(file.choose()) # choose the toyotacorolla.csv data set
View(toyotacorolla)

attach(toyotacorolla)
### Partial Correlation matrix - Pure Correlation  b/n the varibles
#install.packages("corpcor")
library(corpcor)
cor2pcor(cor(toyotacorolla))


# The Linear Model of interest
model.toyotacorolla <- lm(Price~Age_08_04+KM+HP+cc+Doors+Gears+Quarterly_Tax+Weight,data = toyotacorolla)
summary(model.toyotacorolla)
###r-squared:0.78,so above 0.86 model is strong corelated
# Prediction based on only age_08_04 
model.computer_dataA<-lm(Price~Age_08_04)
summary(model.computer_dataA) # age_08_04 became significant
#r-squared:0.76 modrate corelated
# Prediction based on only KM
model.computer_dataKM<-lm(Price~KM)
summary(model.computer_dataKM) # km became significant
# Prediction based on only HP
model.computer_dataHP<-lm(Price~HP)
summary(model.computer_dataHP) # Hp became significant
# Prediction based on only cc 
model.computer_datacc<-lm(Price~cc)
summary(model.computer_datacc) # cc became significant
# Prediction based on only doors
model.computer_dataD<-lm(Price~Doors)
summary(model.computer_dataD) # doors significant
## Prediction based on only Gears
model.computer_dataP<-lm(Price~Gears)
summary(model.computer_dataP) # Gears became significant
# Prediction based on only  Quartely_tax
model.computer_dataQ<-lm(Price~Quarterly_Tax)
summary(model.computer_dataQ) # quartely_tax became significant
# Prediction based on only  Weight
model.computer_dataW<-lm(Price~Weight)
summary(model.computer_dataW) #  weight became significant


####final model
model.toyotacorollaf <- lm(Price~Age_08_04+KM+HP+Gears+Quarterly_Tax+Weight,data = toyotacorolla)
summary(model.toyotacorollaf)


library(psych)
pairs.panels(toyotacorolla)


library(car)
## Variance Inflation factor to check collinearity b/n variables 
vif(model.toyotacorollaf)
## vif>10 then there exists collinearity among all the variables 

## Added Variable plot to check correlation b/n variables and o/p variable
avPlots(model.toyotacorollaf)

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
pairs(toyotacorolla,upper.panel = panel.cor,main="Scatter plot matrix with Correlation coefficients")

# It is Better to delete influential observations rather than deleting entire column which is 
# costliest process
# Deletion Diagnostics for identifying influential observations
influence.measures(model.toyotacorollaf)
library(car)
## plotting Influential measures 
windows()
influenceIndexPlot(model.toyotacorollaf,id.n=3) # index plots for infuence measures
influencePlot(model.toyotacorollaf,id.n=3) # A user friendly representation of the above


model_1<-lm(price~.,data=toyotacorolla[-c(961)])
summary(model_1)
model_2<-lm(price~.,data=toyotacorolla[-c(222)])
summary(model_2)
model_3<-lm(price~.,data=toyotacorolla[-c(602,222)])
summary(model_3)

########fianl model
plot(lm(price~.,data=computer_data[-c(602,222)]))

summary(lm(price~.,data=computer_data[-c(602,222)]))

# Evaluate model LINE assumptions 

#Residual plots,QQplot,std-Residuals Vs Fitted,Cook's Distance 
qqPlot(model.toyotacorollaf,id.n = 4)
# QQ plot of studentized residuals helps in identifying outlier 




hist(residuals(model_3)) # close to normal distribution

