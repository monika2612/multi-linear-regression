
data("mtstartups")
View(mtstartups)

startups <- read.csv(file.choose())
View(startups)
attach(startups)
####3here,we have a exchange a data in current excelrshit,we put A STATE:newyork=1,california=2,florida=0
summary(startups)
pairs(startups)
plot(startups)
cor(startups)
library(corpcor)
cor2pcor(cor(startups))
model.startups <- lm(Profit~R.D.Spend+Administration+Marketing.Spend+State,data=startups)
summary(model.startups)


model.startupsR<-lm(Profit~R.D.Spend)
summary(model.startupsR) # r.d.spend became significant

# Prediction based on only administrtiont
model.startupsA<-lm(Profit~Administration)
summary(model.startupsA) # administrtion became significant

# Prediction based on state
model.startupsS<-lm(Profit~State)
summary(model.startupsS) # statebecame Insignificant


model.startupsM <- lm(Profit~Marketing.Spend)
summary(model.startupsM)

model.startupsf <- lm(Profit~R.D.Spend)
summary(model.startupsf)

#####################################3

library(psych)
pairs.panels(startups)


library(car)
## Variance Inflation factor to check collinearity b/n variables 
vif(model.startups)
## vif>10 then there exists collinearity among all the variables 

## Added Variable plot to check correlation b/n variables and o/p variable
avPlots(model.startups)

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
pairs(startups,upper.panel = panel.cor,main="Scatter plot matrix with Correlation coefficients")

# It is Better to delete influential observations rather than deleting entire column which is 
# costliest process
# Deletion Diagnostics for identifying influential observations
influence.measures(model.startupsf)
library(car)
## plotting Influential measures 
windows()
influenceIndexPlot(model.startupsf,id.n=3) # index plots for infuence measures
influencePlot(model.startupsf,id.n=3) # A user friendly representation of the above

# Regression after deleting the 50th observation, which is influential observation
model_1<-lm(Profit~R.D.Spend,data=startups[-50,])
summary(model_1)

# Regression after deleting the 50th & 37st Observations
model_2<-lm(Profit~R.D.Spend,data=startups[-c(50,37),])
summary(model_2)
# Regression after deleting the 50th & 37st Observations
model_3<-lm(Profit~R.D.Spend,data=startups[-c(50,37,15,49,3),])
summary(model_3)



## Final model
plot(lm(Profit~R.D.Spend,data=startups[-c(50),]))
     
summary(lm(Profit~R.D.Spend,data=startups[-50,]))
  




plot(lm(Profit~R.D.Spend,data=startups[-c(50,15)]))

summary(lm(Profit~R.D.Spend,data=startups[-c(50,15)]))


# Its not a feasible solution if we remove all the 
# influential values 
# We need to consider other assumptions to likes
# Heteroscadasticity | Normal Distribution of Residuals
#final model



## Final model

# Evaluate model LINE assumptions 
#Residual plots,QQplot,std-Residuals Vs Fitted,Cook's Distance 
qqPlot(model.startupsf,id.n = 4)
# QQ plot of studentized residuals helps in identifying outlier 

hist(residuals(model_3)) # close to normal distribution
