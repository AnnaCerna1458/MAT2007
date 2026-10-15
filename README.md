# Analysis of Health Variables in Smokers vs Never-Smokers
## Project overview
This project aims to analyse data from the Korean National Health Insurance Service by comparing current-smokers to never-smokers. 

The analysis explores whether these two groups differ in average triglyceride levels and height. It also looks at differences between men and women to see how sex composition might influence the results.  

## Data set
The data set contains 991 346 health screening records. 
It originates from the Korean National Health Insurance Service and it was downloaded from Kaggle: https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset.

For this project, these variables were used: 
1. "SMK_stat_type_cd": smoking status
- 1 = never-smoked
- 2 = used to smoke, but quit
- 3 = currently smokes
2. "triglyceride": triglyceride blood concentration (mg/dL)
3. "height": height in cm
4. "sex": male/female 

Only never-smokers and current-smokers are included in this analysis. Former smokers are excluded. 

## Methodology
The data set is first divided into two groups: never-smokers and current-smokers. Height and triglyceride levels are analysed separately for both groups. Each group is divided into 50 subsamples and for each subsample, their mean is calculated. The overall mean is then calculated from the subsample means. Then, statistical uncertainty is calculated as the standard deviation of its 50 subsample means. 

To compare current and never smokers, difference between the corresponding subsample means is calculated, which produces 50 differences. Then, the mean of these differences is calculated and it represents the overall difference between these two groups. The statistical uncertainty of this overall difference is calculated as the standard deviation of the 50 differences. To determine how many standard deviations (sigma) the mean difference is from zero, it is divided by its statistical uncertainty. Differences above 3 sigma are considered statistically significant. 

The same analysis was performed separately for male and female participants. The results are visualised using Matplotlib. 

## Requirements
The analysis was performed using Python 3 and requires these libraries: 
- pandas
- numpy
- matplotlib

They can be installed using: pip install pandas numpy matplotlib

## How to run the code? 
1. Download the dataset using the provided Kaggle link (see Dataset section) 
2. Place the file (smoking_driking_dataset_Ver01.csv) into the same folder as the Python script.
3. Run python Analysis_Smoking_project.py


## Output
The script generates three figures (png): 
1. Mean height by smoking status: compares the average height of current-smokers and never-smokers, overall and separately for men and women. 
2. Mean triglyceride levels: compares the average triglyceride levels of current-smokers and never-smokers, overall and separately for men and women.
3. Sex composition by smoking status: percentage of male and female participants in current and never smokers. 
