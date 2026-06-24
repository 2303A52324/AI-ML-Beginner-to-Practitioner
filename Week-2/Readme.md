TITANIC DATASET – INSIGHTS REPORT

Objective:
The goal of this analysis was to clean the Titanic dataset, handle missing values, encode categorical variables, normalize numerical features, and visualize important patterns affecting passenger survival.
Data Cleaning Performed:
• Missing Age values were replaced with the median age to avoid bias from extreme values.
• Missing Embarked values were replaced with the most frequent embarkation point.
• Missing Cabin values were replaced with “Unknown” because a large portion of cabin information was unavailable.
• Categorical features such as Sex and Embarked were encoded into numerical values.
• Numerical features including Age, Fare, SibSp, and Parch were normalized using Min-Max Scaling.
Key Findings:
1. Survival Distribution
   The dataset shows that more passengers did not survive than survived, indicating a significant mortality rate during the disaster.
2. Gender Influence
   Female passengers had a noticeably higher survival rate compared to male passengers. This suggests that rescue efforts prioritized women and children.
3. Passenger Class Impact
   Passengers traveling in First Class had the highest survival rates, while Third Class passengers experienced the lowest survival rates. Socioeconomic status appears to have played an important role.
4. Fare Analysis
   Passengers paying higher fares generally had better survival chances, which aligns with the observation that higher-paying passengers often traveled in higher classes.
5. Age Trends
   Younger passengers exhibited slightly better survival outcomes compared to older passengers, though age alone was not the strongest predictor.
Conclusion:
Passenger class, gender, and fare were among the strongest factors influencing survival. Female passengers and those in higher travel classes experienced significantly better survival rates. These findings demonstrate how exploratory data analysis can reveal meaningful patterns and support data-driven decision-making.

