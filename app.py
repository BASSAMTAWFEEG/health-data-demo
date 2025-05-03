import streamlit as st
import pandas as pd

st.title("تحليل بيانات المرضى")

# قراءة البيانات
data = pd.read_csv("patients.csv")

# عرض البيانات
st.subheader("الجدول الكامل للمرضى")
st.dataframe(data)

# عدد المرضى
st.subheader("عدد المرضى:")
st.write(len(data))

# توزيع الأمراض
st.subheader("توزيع الأمراض:")
st.write(data['Disease'].value_counts())

# متوسط السكر
st.subheader("متوسط نسبة السكر:")
st.write(data['Blood_Sugar'].mean())

# أكبر عمر
st.subheader("أكبر عمر بين المرضى:")
st.write(data['Age'].max())
