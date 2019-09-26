# Pattern-Recognition

                                                      CSCE 550 Project1
Due: September 26, 2019<br>
1- Objective<br>
In this assignment, we build a classifier using Naïve Bayesian technique that we investigated in
the class.<br>
2- Dependencies<br>
Python > 2.7<br>
Pandas toolkit (If it is needed)<br>
Numpy toolkit (If it is needed)<br>
Note: Using Python’s Scikit-learn tool is not allowed for this assignment<br>
3- Dataset<br>
This dataset is originally from the National Institute of Diabetes and Digestive and Kidney
Diseases. The objective of the dataset is to diagnostically predict whether a patient has diabetes,
based on certain diagnostic measurements included in the dataset. Several constraints were
placed on the selection of these instances from a larger database. In particular, all patients here
are females at least 21 years old of Pima Indian heritage.<br>
Note: You do not need to download the data. Two subsets of data for training and test is created
and posted for downloading. The original data set also is included for your further testing and
experimenting.<br>
The list of the fields in order of columns in the data file is:<br>
PregnanciesNumber of times pregnant<br>
GlucosePlasma glucose concentration a 2 hours in an oral glucose tolerance test<br>
BloodPressureDiastolic blood pressure (mm Hg)<br>
SkinThicknessTriceps skin fold thickness (mm)<br>
Insulin2-Hour serum insulin (mu U/ml)<br>
BMIBody mass index (weight in kg/(height in m)^2)<br>
DiabetesPedigreeFunctionDiabetes pedigree function<br>
Age (years)<br>
OutcomeClass variable (0 No Diabetes or 1 Diabetes) 268 of 768 are 1, the others are 0.<br>
For more information see<br>
https://www.kaggle.com/uciml/pima-indians-diabetes-database <br>
Publication related to this data<br>
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2245318/pdf/procascamc00018-0276.pdf <br>
It will be beneficial if you review this publication. <br>
4- Classifier program guideline <br>
The guideline to develop your classifier is as follows. You may use your own way to break the
problem in any format/function you like.<br>
a. A function that uses Pandas API to load files (training and test) as a Panda’s data frame <br>
b. A function that calculates 𝜇 and σ for each column<br>
c. A function for calculating normal distribution likelihood<br>
d. A classifier function<br>
e. An accuracy function to count/estimate accuracy ( and hence error)<br>
5- What we need to generate?<br>
Sets of training and test data are posted online and you should use the given data for your training
and test. Your classifier needs to generate the following results:<br>
a- An evaluation of accuracy by counting classified and misclassified points<br>
b- An evaluation of accuracy by using confusion matrix as follows:<br>
A confusion matrix is a table that is often used to describe the performance of a classification
model (or "classifier") on a set of test data for which the true values are known.<br>
 After you construct the confusion matrix, calculate the values below:<br>
 Classification Error: Overall, how often is the classifier correct?<br>
 Accuracy = (TP + TN) / (TP + FP + TN +FN)<br>
 Classifier Error: Overall, how often is the classifier correct?<br>
 Error = (FP + FN) / (TP + FP + TN +FN)<br>
 Classifier Sensitivity: When the actual value is positive, how often is the prediction correct?<br>
 Sensitivity = TP / (FN + TP)<br>
 Classifier Specificity: When actual value is negative, how often is the prediction correct?<br>
 Specificity = TN / (TN/FP)<br>
 What is your interpretation of these values?<br>
