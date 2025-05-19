import streamlit as st
# from presentations.introductions import get_slides

st.title("Úvod do vizualizace")

st.header("Co jsou datové vizualizace?")
st.write("""
Datové vizualizace jsou grafické reprezentace dat a informací. Umožňují nám lépe pochopit vzory, 
trendy a souvislosti v datech prostřednictvím vizuálních prvků jako jsou grafy, diagramy a mapy.
""")

st.header("Základní knihovny pro vizualizace")

st.subheader("1. Matplotlib - Základ vizualizací")
st.write("""
Matplotlib je základní knihovna pro tvorbu vizualizací v Pythonu:
- Poskytuje nízkoúrovňové API pro přesnou kontrolu grafů
- Nabízí objektově orientovaný přístup
- Je základem pro mnoho dalších vizualizačních knihoven
""")

st.subheader("2. Seaborn - Statistické vizualizace")
st.write("""
Seaborn staví na Matplotlib a přidává:
- Atraktivní výchozí styly
- Statistické grafy
- Integraci s pandas DataFrame
""")

st.header("Populární vizualizační knihovny")

st.write("""
V Pythonu máme k dispozici řadu specializovaných knihoven:

📊 **Statické grafy**
- **Matplotlib** - základní vizualizační knihovna
- **Seaborn** - statistické vizualizace
- **Plotly** - interaktivní grafy

📈 **Interaktivní vizualizace**
- **Bokeh** - webové interaktivní grafy
- **Altair** - deklarativní vizualizace
- **Plotly Express** - zjednodušené API pro Plotly

🗺️ **Specializované vizualizace**
- **Folium** - interaktivní mapy
- **NetworkX** - vizualizace sítí a grafů
- **Graphviz** - vizualizace diagramů
""")

st.header("Principy efektivní vizualizace")
st.info("""
🎯 **Základní principy:**
1. Přehlednost a jednoduchost
2. Správný výběr typu grafu
3. Konzistentní barevné schéma
4. Jasné popisky a legendy
5. Odpovídající měřítko os
""")

st.header("Tipy pro začátek")
st.info("""
💡 **Doporučený postup:**
1. Začněte s jednoduchými grafy v Matplotlib
2. Prozkoumejte statistické vizualizace v Seaborn
3. Experimentujte s interaktivními grafy
4. Naučte se práci s různými datovými formáty
5. Zaměřte se na storytelling pomocí dat
""")

st.warning("""
⚠️ **Na co si dát pozor:**
- Přehlcení grafu informacemi
- Zavádějící měřítka
- Nevhodné typy grafů pro daná data
- Špatně čitelné popisky
""")

st.success("""
✨ **Výhody datových vizualizací:**
- Rychlejší pochopení dat
- Objevování skrytých vzorů
- Efektivní komunikace výsledků
- Podpora při rozhodování
- Identifikace odlehlých hodnot
""")

st.header("Praktické ukázky")
st.code("""
# Jednoduchý graf v Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title('Sinusová funkce')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
""", language="python")

st.code("""
# Statistický graf v Seaborn
import seaborn as sns

sns.set_theme()
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title('Rozdělení účtů podle dne')
plt.show()
""", language="python")