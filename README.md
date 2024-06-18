# ucb-dataviz-project1-group7
Overview of the Analysis:
  The README file should start with an introduction that explains the purpose and scope of the data analysis. It should provide background information on the dataset, the research questions or objectives, and any specific 
  methodologies used.

Data Cleaning and Preprocessing:
  Details about how the data was cleaned, any missing values handled, outliers treated, and any transformations applied should be included. This section ensures transparency in the data preparation steps.

Exploratory Data Analysis (EDA): 
  Summary statistics, visualizations, and key insights gained from exploring the dataset should be included. EDA helps in understanding the data better and identifying patterns or trends.

  Q6 - weighted population analysis of cluster samples that are classified by highest similarilty.  TOP 50/Bottom 50

Modeling Approach: 
  Description of the machine learning models used, the rationale behind their selection, and any parameter tuning performed should be documented. This section helps in understanding the analytical techniques applied.

  Q6 - columns were dropped which had the least normal distributions first

Results: 
  Detailed presentation of the model performance metrics, such as accuracy, precision, recall, F1 score, etc., should be provided. Visualizations like confusion matrices or ROC curves can also be included to support the results.

Conclusions:
  A summary of the key findings, implications of the results, limitations of the analysis, and recommendations for future work should be outlined. This section helps in drawing meaningful insights from the analysis.

Q6 - Shows that by creating a ranking system that is weighted by mental traits of the following columns (family_history	treatment	growing_stress	mental_health_history	mood_swings	coping_struggles	work_interest	social_weakness) the top most 50 percent of results show a strong correlation between treatment and family history while the bottom 50 percent show a very weak correlation.  This shows that the more random or unique set of answers of a subjects results are more likely to have no correlation between treatment and family history. But the top 50 percent of subjects that had answered similarly to their pairs showed they were also more likely to have answered in high correlation the same way for family history and treatment

Repository Folder Overview 
    ->Code: Organize and document your code effectively to demonstrate your analysis and modeling process clearly. (?? APIs if used) 
    ->Data: Managing raw and processed data files is crucial for reproducibility and transparency in data analytics projects.
    ->Documentation: Providing a README.md file with an overview of the project, instructions, and any necessary documentation can help others understand your work.
    ->Results and Visuals: Including visualizations and results can showcase your findings and insights effectively.
    ->Notebooks: If your project involves machine learning models or data analysis in notebooks, it's beneficial to include these for reference.
    ->Config, Tests, and LICENSE: While these may not always be explicitly required, having configuration files, tests, and licensing information can add professionalism and completeness to your project.
