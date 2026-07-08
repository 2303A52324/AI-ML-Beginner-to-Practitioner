# Supervised Learning – Regression Analysis Report

## Objective

The objective of this assignment was to implement and compare multiple supervised regression algorithms for predicting house prices. Four regression models—Linear Regression, Polynomial Regression, Ridge Regression, and Lasso Regression—were trained and evaluated using the California Housing dataset. Model performance was assessed using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and the coefficient of determination (R² Score).

## Dataset Description

The California Housing dataset contains information about housing characteristics collected from various districts in California. Features include median income, house age, average number of rooms, average occupancy, latitude, and longitude. The target variable is the median house value.

## Methodology

The dataset was first explored to understand its structure and statistical properties. After checking for missing values, the features and target variable were separated. The data was divided into training and testing sets using an 80:20 ratio. Since several regression algorithms are sensitive to feature scales, StandardScaler was applied to normalize the input features.

Four regression algorithms were implemented:

* Linear Regression
* Polynomial Regression (Degree 2)
* Ridge Regression
* Lasso Regression

Each model was trained using the training dataset and evaluated on the testing dataset.

## Performance Evaluation

The models were compared using the following evaluation metrics:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

The Actual vs Predicted plots showed how closely each model's predictions matched the true house prices. The bar chart comparison of R² scores provided an easy way to compare model performance.

## Results and Discussion

Linear Regression served as a baseline model and provided good predictive performance for a linear relationship. Polynomial Regression captured nonlinear patterns in the data and often achieved higher prediction accuracy but may become prone to overfitting if the polynomial degree is increased.

Ridge Regression improved model stability by applying L2 regularization, reducing the effect of multicollinearity while maintaining strong predictive performance. Lasso Regression applied L1 regularization, shrinking less important feature coefficients toward zero and effectively performing feature selection.

Among the four models, the one with the highest R² score and lowest prediction errors demonstrated the best overall performance. Ridge and Polynomial Regression generally produced more stable and accurate predictions compared to the standard Linear Regression, while Lasso Regression produced a simpler and more interpretable model.

## Conclusion

This experiment demonstrated the effectiveness of different regression algorithms for house price prediction. Regularization techniques such as Ridge and Lasso improve model generalization by preventing overfitting, while Polynomial Regression can capture nonlinear relationships when appropriate. Selecting the best regression model depends on the balance between prediction accuracy, model complexity, and stability. Overall, the comparison highlights the importance of evaluating multiple algorithms before choosing the most suitable model for a predictive analytics task.

