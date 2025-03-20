import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualization(df):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 6))

    survived_counts = df['survived'].value_counts()

    colors = ['orange' if x == 1 else 'blue' for x in survived_counts.index]
    survived_counts.plot(kind='bar', color=colors)

    plt.title("Survival Status (Orange: Survived, Blue: Not Survived)", fontsize=16)
    plt.xlabel('Survival Status', fontsize=14)
    plt.ylabel('Count', fontsize=14)

    plt.savefig('vis.png')

if __name__ == "__main__":
    df = pd.read_csv('res_dpre.csv')
    create_visualization(df)
    print("Visualization saved as vis.png!")