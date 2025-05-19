import streamlit as st
# from presentations.introductions import get_slides
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

st.title("Úvod do vizualizace")

text, samples = st.tabs(["Text", "Ukázky grafů"])

with text:
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

with samples:
    st.title("Porovnání vizualizačních knihoven")

    # Vytvoření vzorových dat
    np.random.seed(42)
    data = {
        'měsíc': ['Led', 'Úno', 'Bře', 'Dub', 'Kvě', 'Čvn', 'Čvc', 'Srp', 'Zář', 'Říj', 'Lis', 'Pro'],
        'prodeje': [120, 135, 142, 158, 165, 172, 168, 175, 182, 188, 195, 210],
        'náklady': [100, 110, 115, 125, 130, 140, 135, 142, 150, 155, 160, 170],
        'návštěvnost': [1000, 1200, 1100, 1400, 1600, 1800, 1750, 1900, 2000, 2100, 2200, 2300]
    }
    df = pd.DataFrame(data)

    # 1. Matplotlib
    st.header("1. Matplotlib")

    # Čárový graf
    st.subheader("Čárový graf")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['měsíc'], df['prodeje'], marker='o', label='Prodeje')
    ax.plot(df['měsíc'], df['náklady'], marker='s', label='Náklady')
    ax.set_title('Vývoj prodejů a nákladů')
    ax.set_xlabel('Měsíc')
    ax.set_ylabel('Hodnota (tis. Kč)')
    ax.grid(True)
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)
    plt.close()

    # Sloupcový graf
    st.subheader("Sloupcový graf")
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(df['měsíc']))
    width = 0.35
    ax.bar(x - width / 2, df['prodeje'], width, label='Prodeje')
    ax.bar(x + width / 2, df['náklady'], width, label='Náklady')
    ax.set_xticks(x)
    ax.set_xticklabels(df['měsíc'], rotation=45)
    ax.set_title('Porovnání prodejů a nákladů')
    ax.set_xlabel('Měsíc')
    ax.set_ylabel('Hodnota (tis. Kč)')
    ax.legend()
    ax.grid(True, axis='y')
    st.pyplot(fig)
    plt.close()

    # Bodový graf
    st.subheader("Bodový graf")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['návštěvnost'], df['prodeje'], label='Prodeje', alpha=0.6)
    ax.set_title('Vztah mezi návštěvností a prodeji')
    ax.set_xlabel('Návštěvnost')
    ax.set_ylabel('Prodeje (tis. Kč)')
    ax.grid(True)
    st.pyplot(fig)
    plt.close()

    # 2. Seaborn
    st.header("2. Seaborn")

    # Čárový graf
    st.subheader("Čárový graf")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='měsíc', y='prodeje', marker='o', label='Prodeje')
    sns.lineplot(data=df, x='měsíc', y='náklady', marker='s', label='Náklady')
    plt.title('Vývoj prodejů a nákladů')
    plt.xlabel('Měsíc')
    plt.ylabel('Hodnota (tis. Kč)')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)
    plt.close()

    # Sloupcový graf
    st.subheader("Sloupcový graf")
    plt.figure(figsize=(10, 6))
    df_melted = df.melt(id_vars=['měsíc'], value_vars=['prodeje', 'náklady'])
    sns.barplot(data=df_melted, x='měsíc', y='value', hue='variable')
    plt.title('Porovnání prodejů a nákladů')
    plt.xlabel('Měsíc')
    plt.ylabel('Hodnota (tis. Kč)')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    st.pyplot(plt)
    plt.close()

    # Bodový graf
    st.subheader("Bodový graf")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='návštěvnost', y='prodeje', s=100)
    sns.regplot(data=df, x='návštěvnost', y='prodeje', scatter=False, color='red')
    plt.title('Vztah mezi návštěvností a prodeji')
    plt.grid(True)
    st.pyplot(plt)
    plt.close()

    # 3. Plotly
    st.header("3. Plotly")

    # Čárový graf
    st.subheader("Čárový graf")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['měsíc'], y=df['prodeje'], name='Prodeje',
                             mode='lines+markers'))
    fig.add_trace(go.Scatter(x=df['měsíc'], y=df['náklady'], name='Náklady',
                             mode='lines+markers'))
    fig.update_layout(
        title='Vývoj prodejů a nákladů',
        xaxis_title='Měsíc',
        yaxis_title='Hodnota (tis. Kč)',
        hovermode='x unified'
    )
    st.plotly_chart(fig)

    # Sloupcový graf
    st.subheader("Sloupcový graf")
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Prodeje', x=df['měsíc'], y=df['prodeje']))
    fig.add_trace(go.Bar(name='Náklady', x=df['měsíc'], y=df['náklady']))
    fig.update_layout(
        title='Porovnání prodejů a nákladů',
        xaxis_title='Měsíc',
        yaxis_title='Hodnota (tis. Kč)',
        barmode='group'
    )
    st.plotly_chart(fig)

    # Bodový graf
    st.subheader("Bodový graf")
    fig = px.scatter(df, x='návštěvnost', y='prodeje',
                     title='Vztah mezi návštěvností a prodeji')
    fig.update_layout(
        xaxis_title='Návštěvnost',
        yaxis_title='Prodeje (tis. Kč)'
    )
    st.plotly_chart(fig)

    st.success("""
    ✨ **Shrnutí rozdílů mezi knihovnami:**

    1. **Matplotlib:**
       - Nejnižší úroveň kontroly
       - Vyžaduje více kódu pro úpravy
       - Statické grafy

    2. **Seaborn:**
       - Atraktivnější výchozí vzhled
       - Jednodušší syntaxe
       - Integrované statistické funkce

    3. **Plotly:**
       - Interaktivní grafy
       - Moderní vzhled
       - Nejvíce uživatelsky přívětivé
       - Nejlepší pro webové aplikace
    """)