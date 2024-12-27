"""_summary_
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(
    "C:/Users/gfalmeida2/Desktop/Estudo/venv/data/processed/"+
    "MiningProcess_Flotation_Plant_Database_processed.csv"
)

def boxplot(df : pd.DataFrame) -> None:
    """Box plot figure of all columns'

    Args:
        df (pd.Dataframe): pd.DateFrame

    Returns:
        plt.figure(plt)
    """
    print(type(df))
    cols_plot = df.columns[1:22]
    fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(20,6))
    num_cols = 6
    num_rows = (len(cols_plot) + num_cols - 1) // num_cols
    for i, col in enumerate(cols_plot):
        ax = axes.flatten()[i]
        sns.boxplot(data=df, y=col, ax=ax)
        ax.set_title(f'Boxplot {col}')
        ax.set_ylabel(col)
    for j in range(i + 1, num_rows * num_cols):
        fig.delaxes(axes.flatten()[j])
    plt.tight_layout()
    plt.suptitle('Boxplots of Selected Columns', fontsize=16)
    plt.savefig('box_plot_analysis.png')

boxplot(df)
