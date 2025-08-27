# Pandas Guide

**Muallif:** Behruz Maxmudov  
[LinkedIn](https://www.linkedin.com/in/behruz-maxmudov-143666338/) | [Medium](https://medium.com/@behruzmaxmudov263)

---

## 📑 Mundarija
- [Introduction](#introduction)
- [Installation](#installation)
- [Quick Start](#quick-start)
  - [Series](#series)
  - [DataFrame](#dataframe)
- [Useful Methods](#useful-methods)
- [Indexing & Filtering](#indexing--filtering)
- [Grouping & Sorting](#grouping--sorting)
- [Input / Output](#input--output)
- [Visualization Example](#visualization-example)
- [Conclusion](#conclusion)

---

## 🚀 Introduction

Pandas — bu Python kutubxonasi bo‘lib, **ma’lumotlarni tahlil qilish va qayta ishlash** uchun ishlatiladi.  
U **jadval (DataFrame)** va **ustun (Series)** kabi kuchli strukturalarni taqdim etadi.

---

## 🛠 Installation

```bash
pip install pandas
```

---

## ⚡ Quick Start

### Series
```python
import pandas as pd

s = pd.Series([10, 20, 30], name="Numbers")
print(s)
```

### DataFrame
```python
data = {
    "Name": ["Ali", "Vali", "Hasan"],
    "Age": [25, 30, 28],
    "City": ["Tashkent", "Samarkand", "Bukhara"]
}

df = pd.DataFrame(data)
print(df)
```

---

## 🔑 Useful Methods

```python
df.head()       # Birinchi 5 qator
df.tail()       # Oxirgi 5 qator
df.info()       # Umumiy ma’lumot
df.describe()   # Statistik ko‘rsatkichlar
```

---

## 🔎 Indexing & Filtering

**Indekslash:**
```python
df["Name"]              # Bitta ustun
df[["Name", "Age"]]     # Ikki ustun
df.iloc[0]              # Birinchi qator
df.loc[0, "Name"]       # Aniq qiymat
```

**Filtrlash:**
```python
df[df["Age"] > 25]
df[df["City"] == "Tashkent"]
```

---

## 📊 Grouping & Sorting

**Guruhlash:**
```python
df.groupby("City")["Age"].mean()
```

**Sortlash:**
```python
df.sort_values("Age", ascending=False)
```

---

## 📂 Input / Output

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

---

## 📈 Visualization Example

```python
import matplotlib.pyplot as plt

df["Age"].plot(kind="hist", bins=5, color="skyblue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
```

---

## 🎯 Conclusion

Pandas — **ma’lumotlar bilan ishlashni yengillashtiradigan kuchli vosita**.  
U orqali:
- Ma’lumotlarni **o‘qish / yozish**
- **Tozalash / qayta ishlash**
- **Tahlil qilish / vizualizatsiya qilish**

juda oson va tez amalga oshiriladi.  

**Muallif:** Behruz Maxmudov  
[LinkedIn](https://www.linkedin.com/in/behruz-maxmudov-143666338/) | [Medium](https://medium.com/@behruzmaxmudov263)
