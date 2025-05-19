import streamlit as st

st.title("5 Příkladů vizualizace pomocí Pandas")

# Inicializace stavových proměnných v session_state
if 'show_hints' not in st.session_state:
    st.session_state.show_hints = [False] * 5
if 'show_solutions' not in st.session_state:
    st.session_state.show_solutions = [False] * 5

def toggle_hint(index):
    st.session_state.show_hints[index] = not st.session_state.show_hints[index]

def toggle_solution(index):
    st.session_state.show_solutions[index] = not st.session_state.show_solutions[index]

# Příklad 1
st.header("1. Časová řada prodejů")
st.subheader("Zadání")
st.write("""
Vytvořte čárový graf zobrazující vývoj měsíčních prodejů za rok 2023. 
Data obsahují sloupce 'měsíc' a 'prodeje'.
""")

st.code("""
# Vzorová data
import pandas as pd

data = {
    'měsíc': ['Led', 'Úno', 'Bře', 'Dub', 'Kvě', 'Čvn', 
              'Čvc', 'Srp', 'Zář', 'Říj', 'Lis', 'Pro'],
    'prodeje': [120, 135, 142, 158, 165, 172, 
                168, 175, 182, 188, 195, 210]
}
df = pd.DataFrame(data)
""", language="python")

col1, col2 = st.columns(2)
with col1:
    if st.button("Zobrazit/skrýt nápovědu", key="hint1"):
        toggle_hint(0)
with col2:
    if st.button("Zobrazit/skrýt řešení", key="solution1"):
        toggle_solution(0)

if st.session_state.show_hints[0]:
    st.info("""
    💡 **Nápověda:**
    - Použijte metodu `plot()`
    - Nastavte parametry `x` a `y`
    - Přidejte titulek a popisky os
    """)

if st.session_state.show_solutions[0]:
    st.subheader("Řešení")
    st.code("""
    import matplotlib.pyplot as plt
    
    df.plot(x='měsíc', y='prodeje', 
            title='Měsíční prodeje 2023',
            figsize=(10, 6),
            marker='o')
    plt.grid(True)
    plt.xlabel('Měsíc')
    plt.ylabel('Prodeje (tis. Kč)')
    plt.show()
    """, language="python")

# Příklad 2
st.header("2. Porovnání kategorií produktů")
st.subheader("Zadání")
st.write("""
Vytvořte sloupcový graf zobrazující celkové prodeje podle kategorií produktů.
""")

st.code("""
# Vzorová data
data = {
    'kategorie': ['Elektronika', 'Oblečení', 'Potraviny', 
                  'Nábytek', 'Sport'],
    'prodeje': [850, 620, 930, 450, 380]
}
df = pd.DataFrame(data)
""", language="python")

col1, col2 = st.columns(2)
with col1:
    if st.button("Zobrazit/skrýt nápovědu", key="hint2"):
        toggle_hint(1)
with col2:
    if st.button("Zobrazit/skrýt řešení", key="solution2"):
        toggle_solution(1)

if st.session_state.show_hints[1]:
    st.info("""
    💡 **Nápověda:**
    - Použijte metodu `plot.bar()`
    - Přidejte barevné rozlišení
    - Zobrazte hodnoty nad sloupci
    """)

if st.session_state.show_solutions[1]:
    st.subheader("Řešení")
    st.code("""
    import matplotlib.pyplot as plt
    
    ax = df.plot.bar(x='kategorie', y='prodeje',
                     title='Prodeje podle kategorií',
                     figsize=(10, 6),
                     color='skyblue')
    plt.grid(axis='y')
    for i, v in enumerate(df['prodeje']):
        ax.text(i, v, str(v), ha='center', va='bottom')
    plt.show()
    """, language="python")

# Příklad 3
st.header("3. Rozložení cen produktů")
st.subheader("Zadání")
st.write("""
Vytvořte histogram a krabicový graf pro analýzu rozložení cen produktů.
""")

st.code("""
# Vzorová data
import numpy as np
np.random.seed(42)
data = {
    'cena': np.random.normal(1000, 200, 500)
}
df = pd.DataFrame(data)
""", language="python")

col1, col2 = st.columns(2)
with col1:
    if st.button("Zobrazit/skrýt nápovědu", key="hint3"):
        toggle_hint(2)
with col2:
    if st.button("Zobrazit/skrýt řešení", key="solution3"):
        toggle_solution(2)

if st.session_state.show_hints[2]:
    st.info("""
    💡 **Nápověda:**
    - Použijte metody `hist()` a `boxplot()`
    - Nastavte vhodný počet binů pro histogram
    - Přidejte statistické údaje
    """)

if st.session_state.show_solutions[2]:
    st.subheader("Řešení")
    st.code("""
    import matplotlib.pyplot as plt
    
    # Histogram
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    df['cena'].hist(bins=30, color='lightgreen')
    plt.title('Histogram cen')
    plt.xlabel('Cena')
    plt.ylabel('Četnost')

    # Krabicový graf
    plt.subplot(1, 2, 2)
    df.boxplot(column='cena')
    plt.title('Krabicový graf cen')
    plt.show()
    """, language="python")

# Příklad 4
st.header("4. Korelace mezi veličinami")
st.subheader("Zadání")
st.write("""
Vytvořte bodový graf znázorňující vztah mezi cenou produktu a počtem prodaných kusů.
""")

st.code("""
# Vzorová data
np.random.seed(42)
data = {
    'cena': np.random.uniform(100, 1000, 50),
    'prodané_kusy': np.random.uniform(10, 100, 50)
}
df = pd.DataFrame(data)
""", language="python")

col1, col2 = st.columns(2)
with col1:
    if st.button("Zobrazit/skrýt nápovědu", key="hint4"):
        toggle_hint(3)
with col2:
    if st.button("Zobrazit/skrýt řešení", key="solution4"):
        toggle_solution(3)

if st.session_state.show_hints[3]:
    st.info("""
    💡 **Nápověda:**
    - Použijte metodu `plot.scatter()`
    - Přidejte trend pomocí regresní přímky
    - Upravte velikost a barvu bodů
    """)

if st.session_state.show_solutions[3]:
    st.subheader("Řešení")
    st.code("""
    import matplotlib.pyplot as plt
    from scipy import stats

    plt.figure(figsize=(10, 6))
    df.plot.scatter(x='cena', y='prodané_kusy',
                    alpha=0.5, color='purple')

    # Přidání regresní přímky
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['cena'], 
                                                                  df['prodané_kusy'])
    line = slope * df['cena'] + intercept
    plt.plot(df['cena'], line, color='red', linestyle='--')

    plt.title(f'Vztah mezi cenou a prodanými kusy (R² = {r_value**2:.3f})')
    plt.xlabel('Cena produktu')
    plt.ylabel('Prodané kusy')
    plt.show()
    """, language="python")

# Příklad 5
st.header("5. Složení portfolia")
st.subheader("Zadání")
st.write("""
Vytvořte koláčový graf zobrazující rozložení investičního portfolia.
""")

st.code("""
# Vzorová data
data = {
    'kategorie': ['Akcie', 'Dluhopisy', 'Nemovitosti', 
                  'Komodity', 'Hotovost'],
    'podíl': [40, 25, 20, 10, 5]
}
df = pd.DataFrame(data)
""", language="python")

col1, col2 = st.columns(2)
with col1:
    if st.button("Zobrazit/skrýt nápovědu", key="hint5"):
        toggle_hint(4)
with col2:
    if st.button("Zobrazit/skrýt řešení", key="solution5"):
        toggle_solution(4)

if st.session_state.show_hints[4]:
    st.info("""
    💡 **Nápověda:**
    - Použijte metodu `plot.pie()`
    - Přidejte procenta do popisků
    - Zvýrazněte největší segment
    """)

if st.session_state.show_solutions[4]:
    st.subheader("Řešení")
    st.code("""
    import matplotlib.pyplot as plt
    
    explode = [0.1 if x == df['podíl'].max() else 0 for x in df['podíl']]

    df.plot.pie(y='podíl', labels=df['kategorie'],
                autopct='%1.1f%%',
                explode=explode,
                title='Složení investičního portfolia',
                figsize=(10, 8))
    plt.ylabel('')  # Odstranění popisku osy y
    plt.show()
    """, language="python")

st.success("""
✨ **Tipy pro všechny grafy:**
- Vždy používejte jasné a výstižné popisky
- Přizpůsobte velikost grafu podle potřeby
- Využívejte vhodné barevné schéma
- Přidávejte mřížku tam, kde je to užitečné
- Nezapomeňte na legendu u složitějších grafů
""")