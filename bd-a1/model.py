import pandas as pd
from sklearn.cluster import KMeans

def apply_kmeans(df, k=3):
    df_for_kmeans = df[['age', 'fare']]
    
    if df_for_kmeans['age'].dtype == 'object':
        df_for_kmeans.loc[:, 'age'] = df_for_kmeans['age'].map({'Young': 0, 'Middle-aged': 1, 'Old': 2})
    
    df_for_kmeans = df_for_kmeans.dropna()
    
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_for_kmeans)
    
    df['cluster'] = kmeans.labels_
    
    cluster_counts = pd.Series(kmeans.labels_).value_counts()
    
    with open('k.txt', 'w') as f:
        f.write(f"Cluster distribution (k=3):\n{cluster_counts}")
    
    df.to_csv('res_kmeans.csv', index=False)
    
    print("K-means clustering completed, results saved to k.txt and res_kmeans.csv!")

if __name__ == "__main__":
    df = pd.read_csv('res_dpre.csv')
    apply_kmeans(df, k=3)