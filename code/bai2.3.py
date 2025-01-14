import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc file CSV với dấu phân cách phù hợp
file_path = 'results.csv'
df = pd.read_csv(file_path, delimiter=';')

# Lấy danh sách các cột chỉ số, bỏ qua các cột không phải là chỉ số (giả sử cột đầu là tên cầu thủ và đội bóng)
stats_columns = df.columns[4:]  # điều chỉnh theo vị trí các cột chỉ số

# Vẽ histogram phân bố cho toàn giải
for col in stats_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col].dropna(), kde=True)  # vẽ histogram với đường phân bố
    plt.title(f'Phân bố {col} cho toàn giải')
    plt.xlabel(col)
    plt.ylabel('Số lượng cầu thủ')
    plt.show()

# Vẽ histogram phân bố cho từng đội bóng
teams = df['Squad'].unique()  # giả định cột 'Squad' chứa tên đội bóng
for team in teams:
    df_team = df[df['Squad'] == team]
    for col in stats_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df_team[col].dropna(), kde=True)
        plt.title(f'Phân bố {col} cho đội {team}')
        plt.xlabel(col)
        plt.ylabel('Số lượng cầu thủ')
        plt.show()
