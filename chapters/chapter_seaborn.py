import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy

st.title("Přehled Seaborn grafů")

# Načtení ukázkových dat
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
flights = sns.load_dataset("flights")
titanic = sns.load_dataset("titanic")

st.header("1. Relační grafy")
st.write("""
Grafy pro zobrazení vztahů mezi proměnnými:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("scatterplot")
    plt.figure()
    sns.scatterplot(data=tips, x="total_bill", y="tip")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.scatterplot(data=tips, x="total_bill", y="tip")
    """)

with col2:
    st.subheader("lineplot")
    plt.figure()
    sns.lineplot(data=flights, x="year", y="passengers")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.lineplot(data=flights, x="year", y="passengers")
    """)

st.header("2. Distribuční grafy")
st.write("""
Grafy pro zobrazení distribuce dat:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("histplot")
    plt.figure()
    sns.histplot(data=tips, x="total_bill")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.histplot(data=tips, x="total_bill")
    """)

with col2:
    st.subheader("kdeplot")
    plt.figure()
    sns.kdeplot(data=tips, x="total_bill", hue="sex")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.kdeplot(data=tips, x="total_bill", hue="sex")
    """)

st.header("3. Kategorické grafy")
st.write("""
Grafy pro kategorická data:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("boxplot")
    plt.figure()
    sns.boxplot(data=tips, x="day", y="total_bill")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.boxplot(data=tips, x="day", y="total_bill")
    """)

with col2:
    st.subheader("violinplot")
    plt.figure()
    sns.violinplot(data=tips, x="day", y="total_bill")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.violinplot(data=tips, x="day", y="total_bill")
    """)

st.header("4. Regresní grafy")
st.write("""
Grafy pro regresní analýzu:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("regplot")
    plt.figure()
    sns.regplot(data=tips, x="total_bill", y="tip")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.regplot(data=tips, x="total_bill", y="tip")
    """)

with col2:
    st.subheader("lmplot")
    plt.figure()
    sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex")
    """)

st.header("5. Maticové grafy")
st.write("""
Grafy pro zobrazení více dimenzí:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("heatmap")
    plt.figure()
    sns.heatmap(tips.corr(numeric_only=True), annot=True)
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.heatmap(tips.corr(), annot=True)
    """)

with col2:
    st.subheader("clustermap")
    plt.figure()
    sns.clustermap(iris.drop('species', axis=1))
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.clustermap(iris.drop('species', axis=1))
    """)

st.header("6. Speciální grafy")
st.write("""
Další užitečné grafy:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("swarmplot")
    plt.figure()
    sns.swarmplot(data=tips, x="day", y="total_bill")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.swarmplot(data=tips, x="day", y="total_bill")
    """)

with col2:
    st.subheader("stripplot")
    plt.figure()
    sns.stripplot(data=tips, x="day", y="total_bill")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.stripplot(data=tips, x="day", y="total_bill")
    """)

st.header("7. Komplexní grafy")
st.write("""
Komplexní vizualizace:
""")

st.subheader("pairplot")
pairgrid = sns.pairplot(iris, hue="species")
st.pyplot(pairgrid.fig)
plt.close()

st.code("""
sns.pairplot(iris, hue="species")
""")

st.header("8. Barevné palety")
st.write("""
Seaborn nabízí různé barevné palety:
- **sequential**: 'Blues', 'Greens', 'Oranges', 'Reds'
- **diverging**: 'RdBu', 'RdGy', 'PRGn', 'BrBG'
- **categorical**: 'Set1', 'Set2', 'Set3', 'Paired'
- **cubehelix**: vlastní palety vytvořené pomocí cubehelix systému
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Kategorická paleta")
    plt.figure()
    sns.set_palette("Set2")
    sns.barplot(data=tips, x="day", y="total_bill")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.set_palette("Set2")
    sns.barplot(data=tips, x="day", y="total_bill")
    """)

with col2:
    st.subheader("Sekvenční paleta")
    plt.figure()
    sns.set_palette("Blues")
    sns.barplot(data=tips, x="day", y="total_bill")
    st.pyplot(plt)
    plt.close()

    st.code("""
    sns.set_palette("Blues")
    sns.barplot(data=tips, x="day", y="total_bill")
    """)

st.success("""
✨ **Tipy pro výběr grafu:**
1. **Relační grafy** - pro zobrazení vztahů mezi proměnnými
2. **Distribuční grafy** - pro zobrazení rozložení dat
3. **Kategorické grafy** - pro porovnání kategorií
4. **Regresní grafy** - pro analýzu závislostí
5. **Maticové grafy** - pro zobrazení více dimenzí najednou
6. **Speciální grafy** - pro specifické případy vizualizace
""")