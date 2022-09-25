# import libraries
# import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

print("This program evaluates heart disease data from a sample of patients treated at the Cleveland Clinic Foundation. The data was downloaded from the UCI Machine Learning Repository and cleaned for analysis by Codecademy curriculum authors. I performed the statistical calculations needed to describe some facets of the data.")

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd= yes_hd.chol
print(np.mean(chol_hd))
print("In this dataset, the mean cholestrol level for patients who were diagnosed with heart disease is 251.47 mg/dl. This is higher than 240 mg/dl, which is considered high.")
print('\n')

tstat, pval= ttest_1samp(chol_hd, 240)
pval= pval/2
print(pval)
print("It is highly unlikely that patients in the sample who have heart disease have an average cholesterol level of 240 mg/dl., as the p-value for this hypothesis test was 0.0035. Using a significance threshold of 0.05, we can conclude that sample patients with heart disease have an average cholesterol level significantly greater than 240 mg/dl.")
print('\n')

tstat, pval= ttest_1samp(no_hd.chol, 240)
pval= pval/2
print(pval)
print("Patients in the sample without heart disease do not have average cholesterol levels significantly higher than 240 mg/dl, as the p-value for this hypothesis test was 0.26, well above the 0.05 significance threshold.")
print('\n')

num_patients= len(heart)
print(num_patients)
print("The number of patients in the dataset is 303.")
print('\n')

num_highfbs_patients= np.sum(heart.fbs == 1)
print(num_highfbs_patients)
print("The number of patients with fasting blood sugar higher than 120 mg/dl is 45 out of 303.")
print('\n')

print(0.08 * num_patients)
print("In 1988 when the data was collected, about 8% of the US population had diabetes. Fasting blood sugar levels greater than 120 mg/dl can be indicative of diabetes or pre-diabetes. Assuming this sample (n=303) is representative of the population, we would expect about 24 people in the sample to have diabetes. This is about half the actual number of patients with fasting blood sugar higher than 120 mg/dl, which is 45 patients out of 303.")
print('\n')

p_val= binom_test(45, num_patients, 0.08, alternative='greater')
print(p_val)
print("After running a binomial test on our sample, we can conclude that our sample was drawn from a population where much more than 8% of the patients have fasting blood sugar levels of over 120 mg/dl, as the p-value for this binomial test is 0.000047.")
