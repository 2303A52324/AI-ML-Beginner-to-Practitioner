# Unsupervised Learning – Customer Segmentation Using K-Means Clustering

## Objective

The objective of this assignment was to segment customers into meaningful groups using unsupervised learning techniques. The Mall Customer dataset was analyzed using K-Means Clustering and Principal Component Analysis (PCA) to identify customer groups based on age, annual income, and spending score. These insights can help businesses design targeted marketing strategies and improve customer engagement.

## Methodology

The dataset was first explored to understand its structure and verify data quality. The Gender column was encoded into numerical values, and the features Age, Annual Income, and Spending Score were selected for clustering. Since these features have different scales, StandardScaler was applied to normalize the data.

The Elbow Method was used to determine the optimal number of clusters by analyzing the Within-Cluster Sum of Squares (WCSS). Based on the elbow point, five clusters were selected for K-Means clustering.

Principal Component Analysis (PCA) was then applied to reduce the three-dimensional feature space into two principal components, enabling effective visualization of the customer segments.

## Cluster Characteristics

The generated customer clusters exhibited distinct behavioral patterns:

* **Cluster 0:** Young customers with high income and high spending scores. These represent premium customers who contribute significantly to business revenue.
* **Cluster 1:** Customers with moderate income and moderate spending habits. They form the average customer segment.
* **Cluster 2:** Older customers with lower spending scores despite having moderate or high income. These customers are more conservative in their purchases.
* **Cluster 3:** Young customers with relatively low income but high spending scores. Promotional offers and discounts are likely to attract this segment.
* **Cluster 4:** Customers with low income and low spending scores. They represent budget-conscious shoppers and require cost-effective marketing strategies.

## Business Marketing Strategy

Customer segmentation enables businesses to design personalized marketing campaigns rather than using a one-size-fits-all approach. Premium customers can receive exclusive memberships, loyalty rewards, and early access to new products. High-spending young customers may respond well to social media promotions and influencer campaigns. Budget-conscious customers can be targeted with discounts, coupons, and seasonal offers, while moderate spenders can be encouraged through personalized recommendations and cross-selling strategies. Such segmentation improves customer satisfaction, marketing efficiency, and overall business profitability.

## Conclusion

K-Means clustering successfully identified meaningful customer segments based on demographic and spending behavior. PCA provided an effective two-dimensional visualization of the clusters, making the segmentation easier to interpret. This analysis demonstrates how unsupervised learning techniques can help organizations understand customer behavior and support data-driven marketing decisions.
