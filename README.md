# Regression
## 
 This study was conducted to test the relationship between a predictor on a response 
variable. To be able to test whether the predictor was significant or not it was necessary to test 
what percentage of the regression model could be explained by this predictor. Since the 
predictors, the slope, and the intercept were all randomly generated using a  it is likely that there 
will be a weak correlation between the predictor and the response variable.  
 In this study, 100 points of data were randomly generated using software. These 100 
points of data acted as the explanatory or predictor variables, and will be the population that the 
data will represent.  Then, a random alphanumeric sequence was generated and split into several 
substrings. These substrings were used to generate the slope, intercept, standard deviation, and 
seed value for the random number generator.  

![pic1](/stats/pic1.png)

Then, using this slope, intercept, and standard deviation, an array of 100 response variables were 
generated. The predictor will be tested against the response variable to check how much of an 
effect (if any) this predictor has on the response. 

![pic2](/stats/pic2.png)

These are the population predictor points and their corresponding response variables. 

  To accurately test the effects of the predictor on the response variable, two things were 
done. First, a sample was chosen to represent the population. This sample consisted of every 10th 
value from the population.

![pic3](/stats/pic3.png)

The pictures below contain all the information relating to the sample predictors and their 
corresponding response values, as well as their corresponding boxplots. As you can tell from 
looking at the boxplots there exists high variability in the response variables (the boxplot on the 
left) because not only is there a large IQR, but there is also a broad range. This large spread in 
data can probably be attributed to the outliers that are present in the predictors. While the box 
plot for the predictors may be more compact, there exists several outliers which will affect the 
response variables.  
 
![pic4](/stats/pic4.png) ![pic5](/stats/pic5.png)

The second step that was necessary for accurately testing the effectiveness of the 
predictor is by implanting the method of least squares to minimize the sum of squares residuals. 
By doing so it became possible to accurately measure how much of the total variation among of 
observed responses could be explained by the regression model. Since it’s a univariate regression 
model, measuring the total amount of variation accounted for by the model also proves how 
effective the predictor is at measuring the response variable.

![pic6](/stats/pic6.png) ![pic7](/stats/pic7.png) ![pic8](/stats/pic8.png)

  Using these results, a hypothesis test can be performed. If the predictor is effective, then it will 
somehow affect the slope of the regression model. The null hypothesis is that the slope = 0, and 
the alternate hypothesis is that slope is not equal to 0. First, it is important to look at the 
confidence interval for the slope. The confidence interval for the slope is ( -0.581, 7.794) for a 
confidence level of 95%. Since 0 is contained in this confidence interval, then there is evidence 
to accept the null hypothesis. However, to make sure that a false null hypothesis isn’t being 
accepted it is important to also perform a T-test and an F-test. Both values give the same results, 
as they should since the T-test and F-test are equivalent in univariate regression. Both tests say 
that these T/ F values are no significant at a 95% confidence interval, therefore the null 
hypothesis should not be rejected. Finally, by looking at the coefficient of determination, which 
also equals the sample correlation coefficient, it is evident that only 33% of the total variation 
can be explained by the model. These results point to the same conclusion, the predictor is not 
effective.  
 The results of the test were consistent with the hypothesis, the predictor was not effective 
at describing the variance in the model. This ineffectiveness can be attributed to the 
randomization of the data. Perhaps a different seed value could’ve produced a more effective 
predictor. In order to increase the R-square value different and more effective predictors would 
have to be factored in so that the variance explained by the model could increase.
