# Supervised Learning – Classification Evaluation Summary

## Objective

The objective of this assignment was to predict whether a student would pass or fail based on factors such as study hours, attendance, previous academic performance, and other study habits. Three supervised classification algorithms—Logistic Regression, K-Nearest Neighbors (KNN), and Random Forest—were implemented and compared.

## Methodology

The student dataset was cleaned by handling missing values, removing duplicate records, and encoding categorical variables. A new target variable named **Pass/Fail** was created, where students scoring 50 or above in the final exam were classified as **Pass**, while those scoring below 50 were classified as **Fail**. The dataset was divided into training and testing sets using an 80:20 ratio. Feature scaling was applied before training the models.

The following classification algorithms were implemented:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Random Forest Classifier

Each model was evaluated using Accuracy, Confusion Matrix, and F1-Score.

## Results

The comparison of model performance showed differences in prediction accuracy and complexity.

* **Logistic Regression** provided a simple and interpretable model. It worked well when the relationship between features and the target variable was approximately linear.
* **KNN** classified students based on similarity to nearby data points. It captured nonlinear relationships but required more computation as the dataset size increased.
* **Random Forest** generally produced the highest accuracy and F1-score because it combined multiple decision trees to improve prediction performance and reduce overfitting.

The confusion matrices showed that Random Forest correctly classified more students than the other models, while Logistic Regression produced results that were easier to explain.

## Impact of Model Complexity on Interpretability

Model complexity has a significant impact on interpretability.

* Logistic Regression is highly interpretable because each feature has a clear coefficient showing its influence on the prediction.
* KNN is moderately interpretable since predictions depend on neighboring data points rather than explicit model parameters.
* Random Forest is the most complex model. Although it often provides better predictive performance, its decision-making process is harder to interpret because predictions are generated from many decision trees.

This demonstrates the common trade-off between **accuracy** and **interpretability**. Simpler models are easier to understand and explain, while more complex models often achieve better prediction accuracy.

## Conclusion

Among the three classification algorithms, the model with the highest accuracy and F1-score demonstrated the best performance for predicting student pass/fail outcomes. Logistic Regression offers simplicity and transparency, KNN captures local patterns effectively, and Random Forest provides robust and accurate predictions. The choice of model depends on whether interpretability or predictive performance is the primary objective.
