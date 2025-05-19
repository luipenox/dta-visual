import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Anatomie krabicového grafu")

st.write("""
Krabicový graf (box plot) je statistický nástroj, který nám poskytuje přehled o distribuci dat. 
Zobrazuje pět důležitých statistických hodnot: minimum, první kvartil (Q1), medián, 
třetí kvartil (Q3) a maximum.
""")

# Vytvoření ukázkových dat
np.random.seed(42)
data = np.random.normal(100, 15, 200)
df = pd.DataFrame({'hodnoty': data})

# Základní statistiky
q1 = np.percentile(data, 25)
median = np.percentile(data, 50)
q3 = np.percentile(data, 75)
iqr = q3 - q1
whisker_min = max(np.min(data), q1 - 1.5 * iqr)
whisker_max = min(np.max(data), q3 + 1.5 * iqr)
outliers = data[(data < whisker_min) | (data > whisker_max)]

# Vytvoření interaktivního grafu
st.header("Interaktivní prohlížení částí grafu")

# Zobrazení/skrytí různých částí grafu
show_parts = st.multiselect(
    "Vyberte části grafu pro zobrazení:",
    ["Krabice (Box)", "Vousy (Whiskers)", "Odlehlé hodnoty", "Statistiky"],
    default=["Krabice (Box)", "Vousy (Whiskers)", "Odlehlé hodnoty", "Statistiky"]
)

fig, ax = plt.subplots(figsize=(10, 6))

if "Krabice (Box)" in show_parts:
    sns.boxplot(data=df, y='hodnoty', width=0.3)
else:
    plt.axhline(y=median, color='red', linestyle='-', label='Medián')

if "Statistiky" in show_parts:
    plt.axhline(y=q1, color='green', linestyle='--', label='Q1')
    plt.axhline(y=q3, color='blue', linestyle='--', label='Q3')
    plt.axhline(y=median, color='red', linestyle='-', label='Medián')

if "Odlehlé hodnoty" in show_parts:
    plt.scatter(np.zeros_like(outliers), outliers, color='red', alpha=0.5, label='Odlehlé hodnoty')

plt.title("Krabicový graf s vysvětlením")
plt.legend()
st.pyplot(fig)

# Vysvětlení jednotlivých částí
st.header("Vysvětlení částí krabicového grafu")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Krabice (Box)")
    st.write("""
    - **Horní hrana**: Třetí kvartil (Q3, 75. percentil)
    - **Střední čára**: Medián (Q2, 50. percentil)
    - **Dolní hrana**: První kvartil (Q1, 25. percentil)
    - **IQR (Mezikvartilové rozpětí)**: Rozdíl mezi Q3 a Q1
    """)

    st.subheader("〽️ Vousy (Whiskers)")
    st.write("""
    - **Horní vous**: Sahá k nejvyšší hodnotě do 1.5 × IQR nad Q3
    - **Dolní vous**: Sahá k nejnižší hodnotě do 1.5 × IQR pod Q1
    """)

with col2:
    st.subheader("⭕ Odlehlé hodnoty")
    st.write("""
    - Body ležící za vousy
    - Hodnoty vzdálené více než 1.5 × IQR od Q1 nebo Q3
    - Často indikují anomálie nebo chyby v datech
    """)

    st.subheader("📊 Statistické hodnoty")
    st.write(f"""
    Pro naše data:
    - Minimum: {data.min():.2f}
    - Q1: {q1:.2f}
    - Medián: {median:.2f}
    - Q3: {q3:.2f}
    - Maximum: {data.max():.2f}
    """)

# Interaktivní demonstrace
st.header("Interaktivní demonstrace")

# Generátor dat s různými rozděleními
dist_type = st.selectbox(
    "Vyberte typ rozdělení dat:",
    ["Normální", "Rovnoměrné", "Exponenciální", "Bimodální"]
)

sample_size = st.slider("Velikost vzorku:", 50, 1000, 200)

if dist_type == "Normální":
    data = np.random.normal(100, 15, sample_size)
elif dist_type == "Rovnoměrné":
    data = np.random.uniform(50, 150, sample_size)
elif dist_type == "Exponenciální":
    data = np.random.exponential(50, sample_size)
else:  # Bimodální
    data = np.concatenate([
        np.random.normal(70, 10, sample_size//2),
        np.random.normal(130, 10, sample_size//2)
    ])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Krabicový graf
sns.boxplot(data=data, ax=ax1)
ax1.set_title("Krabicový graf")

# Histogram pro srovnání
sns.histplot(data=data, ax=ax2)
ax2.set_title("Histogram stejných dat")

st.pyplot(fig)

st.success("""
✨ **Výhody krabicového grafu:**
1. Rychlý přehled o distribuci dat
2. Snadná identifikace odlehlých hodnot
3. Možnost porovnání více skupin dat
4. Zobrazení klíčových statistických hodnot
5. Úsporná vizualizace velkých datových souborů
""")

st.info("""
💡 **Kdy použít krabicový graf:**
- Pro zobrazení distribuce numerických dat
- Pro identifikaci odlehlých hodnot
- Pro porovnání rozdělení mezi skupinami
- Pro vizualizaci symetrie/asymetrie dat
- Pro detekci změn v datech v čase
""")