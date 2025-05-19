import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title("Základní příklady Seaborn grafů")

# Inicializace stavových proměnných
if 'show_hints' not in st.session_state:
    st.session_state.show_hints = [False] * 3
if 'show_solutions' not in st.session_state:
    st.session_state.show_solutions = [False] * 3

def toggle_hint(index):
    st.session_state.show_hints[index] = not st.session_state.show_hints[index]

def toggle_solution(index):
    st.session_state.show_solutions[index] = not st.session_state.show_solutions[index]

# Příklad 1
st.header("1. Čárový graf vývoje cen")
st.subheader("Zadání")
st.write("""
Vytvořte čárový graf zobrazující vývoj cen tří produktů v průběhu roku. 
Přidejte legendu a mřížku pro lepší čitelnost.
""")

st.code("""
# Vzorová data
import pandas as pd
import numpy as np

# Generování dat
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
data = {
    'datum': dates,
    'produkt_A': np.random.normal(100, 10, len(dates)),
    'produkt_B': np.random.normal(150, 15, len(dates)),
    'produkt_C': np.random.normal(80, 8, len(dates))
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
    - Použijte `sns.lineplot()`
    - Pro více řad použijte parametr `data` a více sloupců
    - Nastavte styly pomocí `sns.set_style()`
    - Přidejte popisky os a titulek
    """)

if st.session_state.show_solutions[0]:
    st.subheader("Řešení")
    st.code("""
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # Nastavení stylu
    sns.set_style("whitegrid")
    
    # Vytvoření grafu
    plt.figure(figsize=(12, 6))
    
    # Vykreslení čar pro každý produkt
    sns.lineplot(data=df, x='datum', y='produkt_A', label='Produkt A')
    sns.lineplot(data=df, x='datum', y='produkt_B', label='Produkt B')
    sns.lineplot(data=df, x='datum', y='produkt_C', label='Produkt C')
    
    # Nastavení grafu
    plt.title('Vývoj cen produktů v roce 2023')
    plt.xlabel('Datum')
    plt.ylabel('Cena (Kč)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    """, language="python")

# Příklad 2
st.header("2. Krabicový graf distribuce dat")
st.subheader("Zadání")
st.write("""
Vytvořte krabicový graf zobrazující distribuci hodnot pro různé kategorie. 
Přidejte barevné rozlišení a popisky.
""")

st.code("""
# Načtení ukázkových dat
tips = sns.load_dataset("tips")
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
    - Použijte `sns.boxplot()`
    - Nastavte parametr `hue` pro další rozlišení
    - Přidejte popisky os
    - Upravte orientaci popisků pro lepší čitelnost
    """)

if st.session_state.show_solutions[1]:
    st.subheader("Řešení")
    st.code("""
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # Nastavení stylu
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    
    # Vytvoření krabicového grafu
    sns.boxplot(data=tips, x="day", y="total_bill", hue="time",
                palette="Set3")
    
    # Nastavení grafu
    plt.title('Rozdělení účtů podle dne a času')
    plt.xlabel('Den v týdnu')
    plt.ylabel('Celková částka účtu ($)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    """, language="python")

# Příklad 3
st.header("3. Bodový graf se statistikou")
st.subheader("Zadání")
st.write("""
Vytvořte bodový graf s regresní přímkou zobrazující vztah mezi dvěma proměnnými.
Přidejte barevné rozlišení podle kategorie a statistickou legendu.
""")

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
    - Použijte `sns.scatterplot()` pro body
    - Přidejte regresní přímku pomocí `sns.regplot()`
    - Využijte parametr `hue` pro kategorizaci
    - Přidejte statistické informace do titulku
    """)

if st.session_state.show_solutions[2]:
    st.subheader("Řešení")
    st.code("""
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy import stats
    
    # Nastavení stylu
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Vytvoření bodového grafu
    sns.scatterplot(data=tips, x="total_bill", y="tip", 
                    hue="sex", alpha=0.6)
    
    # Přidání regresní přímky
    sns.regplot(data=tips, x="total_bill", y="tip", 
                scatter=False, color="red", line_kws={"linestyle": "--"})
    
    # Výpočet korelace
    correlation = tips['total_bill'].corr(tips['tip'])
    
    # Nastavení grafu
    plt.title(f'Vztah mezi účtem a spropitným (korelace: {correlation:.2f})')
    plt.xlabel('Celková částka účtu ($)')
    plt.ylabel('Spropitné ($)')
    plt.tight_layout()
    plt.show()
    """, language="python")
