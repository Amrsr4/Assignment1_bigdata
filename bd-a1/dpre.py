import pandas as pd

def data_cleaning(df):
    df_cleaned = df.dropna()
    return df_cleaned

def data_transformation(df):
    df.columns = [col.lower() for col in df.columns]
    return df

def data_reduction(df):
    df_reduced = df[['age', 'fare', 'survived']]
    return df_reduced

def data_discretization(df):
    if 'age' in df.columns:
        df['age'] = pd.cut(df['age'], bins=3, labels=["Young", "Middle-aged", "Old"])
    return df

if __name__ == "__main__":
    df = pd.read_csv('titanic.csv')
    df = data_cleaning(df)
    df = data_transformation(df)
    df = data_reduction(df)
    df = data_discretization(df)
    df.to_csv('res_dpre.csv', index=False)
    print("Data preprocessing completed and saved as res_dpre.csv!")