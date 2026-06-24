Introduction to AI & ML Foundations – Basic Data Exploration Report
Student Exam Scores and Study Habits Dataset
Objective
The objective of this assignment was to perform basic data exploration and preprocessing on the Student Exam Scores and Study Habits dataset. The dataset contains information about students' study habits, attendance, sleep patterns, previous academic performance, and final exam scores. The goal was to clean the dataset, analyze the data, and identify factors that influence academic performance.
Data Cleaning Process
Several preprocessing steps were performed to improve data quality and ensure accurate analysis:
1.	Inspection of Dataset
o	The dataset was loaded using Pandas.
o	Data types, dimensions, summary statistics, and missing values were examined.
2.	Handling Missing Values
o	Missing values in numerical columns were replaced using the median value to minimize the effect of outliers.
o	Missing values in categorical columns were replaced using the mode (most frequent value).
3.	Renaming Columns
o	Column names were standardized by converting them to lowercase and replacing spaces with underscores.
o	This improved consistency and made the dataset easier to work with.
4.	Removing Duplicate Records
o	Duplicate rows were identified and removed to avoid bias in the analysis.
5.	Saving Cleaned Data
o	The cleaned dataset was exported as a new CSV file for further use.
Data Visualization and Analysis
Several visualizations were created to understand the distribution of variables and their relationships with exam performance:
•	Histogram of Final Exam Scores
•	Histogram of Study Hours
•	Histogram of Sleep Hours
•	Scatter Plot: Study Hours vs Final Exam Score
•	Scatter Plot: Attendance vs Final Exam Score
•	Scatter Plot: Previous Scores vs Final Exam Score
•	Correlation Heatmap
These visualizations helped identify trends and relationships between student habits and academic outcomes.
Key Findings
1.	Students who spend more time studying generally achieve higher final exam scores.
2.	Attendance shows a positive relationship with academic performance, indicating that regular class participation contributes to better results.
3.	Previous academic performance is a strong predictor of future exam success.
4.	Students who maintain healthy sleep schedules tend to perform better than those with insufficient sleep.
5.	Study habits and attendance together have a significant impact on overall student achievement.
Actionable Insights for Educators
•	Encourage students to follow consistent study schedules.
•	Monitor attendance and provide support for students with frequent absences.
•	Identify students with low previous scores and offer additional academic assistance.
•	Promote healthy lifestyle habits, including adequate sleep and effective time management.
•	Use data-driven interventions to support at-risk students before examinations.
Conclusion
The data exploration process demonstrated that study habits, attendance, sleep patterns, and previous academic performance are important factors influencing student exam scores. Proper data cleaning and visualization provided valuable insights that can help educators make informed decisions to improve student learning outcomes. This assignment highlights the importance of data preprocessing and exploratory data analysis as foundational steps in Artificial Intelligence and Machine Learning projects.
