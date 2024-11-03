import pandas as pd
from collections import Counter

# Đọc file CSV với dấu phân cách là dấu chấm phẩy
file_path = 'results.csv'  # Thay đổi thành đường dẫn đến file của bạn
df = pd.read_csv(file_path, delimiter=';')

# Giả định các cột chỉ số nằm từ cột thứ ba trở đi
# Giả định cột đầu tiên là 'Player' và cột thứ hai là 'Squad' (tên đội bóng)
stats_columns = df.columns[2:]  # Điều chỉnh nếu cột chỉ số nằm ở vị trí khác

# Tìm đội có điểm số cao nhất ở mỗi chỉ số
top_teams = {}
for col in stats_columns:
    # Tìm hàng có giá trị lớn nhất trong cột, lấy tên đội từ cột 'Squad'
    top_team = df.loc[df[col].idxmax(), 'Squad']
    top_teams[col] = top_team

# In kết quả
print("Đội có điểm số cao nhất ở mỗi chỉ số:")
for stat, team in top_teams.items():
    print(f"{stat}: {team}")

# Đếm tần suất xuất hiện của mỗi đội trong danh sách các chỉ số dẫn đầu
team_performance = Counter(top_teams.values())

# Tìm đội có phong độ tốt nhất dựa trên số lần đứng đầu các chỉ số
best_team = team_performance.most_common(1)[0]
print("\nĐội có phong độ tốt nhất:")
print(f"{best_team[0]} với {best_team[1]} lần dẫn đầu các chỉ số")

# In chi tiết số lần mỗi đội dẫn đầu các chỉ số
print("\nSố lần dẫn đầu các chỉ số của mỗi đội:")
for team, count in team_performance.items():
    print(f"{team}: {count} lần")
