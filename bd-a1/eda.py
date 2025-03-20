import pandas as pd

def explore_data(df):
    insights = []

    missing_values = df.isnull().sum()
    insights.append(f"Missing values per column:\n{missing_values}\n")

    stats = df.describe()
    insights.append(f"Basic statistics:\n{stats}\n")

    numeric_df = df.select_dtypes(include=['number'])
    correlation_matrix = numeric_df.corr()
    insights.append(f"Correlation matrix:\n{correlation_matrix}\n")
    
    return insights

if __name__ == "__main__":
    df = pd.read_csv('res_dpre.csv')
    insights = explore_data(df)

    for i, insight in enumerate(insights, 1):
        with open(f'eda-in-{i}.txt', 'w') as f:
            f.write(insight)
    print("Exploratory Data Analysis completed!")