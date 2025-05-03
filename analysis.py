import pandas as pd 
data = pd.read_csv('patients.csv')
print("عدد المرضى:", len(data))
print("\nتوزيع الامراض:")
print(data['Disease'].value_counts())
print("\nمتوسط السكر:", data['blood_sugar'].mean())
