# Customer Churn EDA Insights

## Top 5 Business Insights

1. Customers on month-to-month contracts churn at a much higher rate than customers on longer-term contracts. In this dataset, month-to-month churn is about 42.71%, compared with 11.27% for one-year contracts and 2.83% for two-year contracts.

2. Customers who churn tend to have higher monthly charges. The average monthly charge is approximately 74.44 for churned customers versus 61.27 for retained customers, suggesting pricing pressure may be contributing to exits.

3. Early-tenure customers are more vulnerable to churn. The dataset includes many churn cases among customers with short tenure, which indicates onboarding and first-year retention should be a business priority.

4. Missing `TotalCharges` values are tied to edge cases in customer tenure and should be handled carefully during cleaning. Converting `TotalCharges` to numeric and filling blanks consistently prevents analysis errors and preserves records.

5. Contract type, service mix, and payment behavior are likely strong churn indicators. Features such as internet-related add-ons, billing preferences, and payment method should be prioritized in retention dashboards and future churn modeling.

## Interpretation

The strongest retention opportunity is in the early lifecycle of month-to-month customers, especially those paying relatively high monthly charges. A practical business response would be to strengthen onboarding, offer targeted contract upgrade incentives, and monitor high-charge customers for churn risk.
