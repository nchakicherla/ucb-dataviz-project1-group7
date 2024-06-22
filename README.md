# ucb-dataviz-project1-group7
Mental Health Data Analysis
Mental health is defined based on factors and symptoms negatively affecting an individual’s mental well being.

Objectives:
Compare mental health correlation between different groups/ attributes (e.g., self-employed vs. employed individuals, different countries, gender, etc) to identify disparities or similarities and their potential causes and provide insights that could inform public health policies, interventions, or initiatives aimed at improving mental health outcomes at local, national, or global levels.

Data: Survey Results (https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset/data)

Data Cleaning and Preprocessing:
- Remove blanks and remove time stamp
- Converted categorical values into integers for better statistical analysis
- Added 2 features:
  Mental Health Candidacy = Family history + treatment + mental health history + growing stress + changes_habits

  Mental Health Severity = coping_struggles + mood_swings + work_interest + social_weakness

![image](https://github.com/nchakicherla/ucb-dataviz-project1-group7/assets/168052679/439796db-67ee-4baf-91b7-a578e6215946)

Exploratory Data Analysis (EDA): 
Q1 Does Gender play a significant role in mental health? 

  A p-value of 1.0 from Chi-Squared test strongly supports the null hypothesis, indicating that there is no evidence of a relationship between gender and mental health history based on sample study. These results suggest that any observed differences in mental health history between genders are due to random chance or other factors. (refer to gender_mental_health.ipynb)

Q2 Does one’s chosen occupation play a significant role in mental health?

  Chi-Squared test indicates no significant association between Occupation and Mental Health. These results suggest that any observed differences in mental health history between occupations are due to random chance or other factors. (refer to occupation_mental_health.ipynb)

Q3 Does mental health factors have an impact on one’s interest in their work?  

  A large volume of respondents showcased a mid range raying for a propensity to mental health issues while also being negatively impacted by mental health issues and the volume of people's interest in work was evenly spread across the low/mid and high impact ratings (refer to Question 3 folder) 

Q4 Are self-employed less susceptible to mental health? 

  Based on the significant t-statistic and very low p-value, there is strong evidence to support the alternative hypothesis that self-employed individuals are less susceptible to mental health compared to non self-employed individuals based on identified factors (Family history + treatment + mental health history + growing stress + changes_habits) (refer to final_self_employed.ipynb)

Q5 Is mental health severity lower in the US?

Neither test revealed a lower average mental health score in the US than in countries outside the US. 
        Mann-Whitney U-test - No significant indication that median severity of mental health is lower in the United States.
        Two-sample t-test - No significant indication that mean mental health severity is lower in the United States. (refer to country_severity.ipynb)

Q6 - weighted population analysis of cluster samples that are classified by highest similarilty.  TOP 50/Bottom 50
Modeling Approach: 
  Description of the machine learning models used, the rationale behind their selection, and any parameter tuning performed should be documented. This section helps in understanding the analytical techniques applied.
Q6 - columns were dropped which had the least normal distributions first
Results: 
  Detailed presentation of the model performance metrics, such as accuracy, precision, recall, F1 score, etc., should be provided. Visualizations like confusion matrices or ROC curves can also be included to support the results.
Conclusions:
  A summary of the key findings, implications of the results, limitations of the analysis, and recommendations for future work should be outlined. This section helps in drawing meaningful insights from the analysis.
Q6 - Shows that by creating a ranking system that is weighted by mental traits of the following columns (family_history	treatment	growing_stress	mental_health_history	mood_swings	coping_struggles	work_interest	social_weakness) the top most 50 percent of results show a strong correlation between treatment and family history while the bottom 50 percent show a very weak correlation.  This shows that the more random or unique set of answers of a subjects results are more likely to have no correlation between treatment and family history. But the top 50 percent of subjects that had answered similarly to their pairs showed they were also more likely to have answered in high correlation the same way for family history and treatment (refer to question_6 folder)

