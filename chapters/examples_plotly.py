import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.title("Příklady s Plotly")

# Inicializace stavových proměnných
if 'show_hints' not in st.session_state:
    st.session_state.show_hints = [False] * 4
if 'show_solutions' not in st.session_state:
    st.session_state.show_solutions = [False] * 4

def toggle_hint(index):
    st.session_state.show_hints[index] = not st.session_state.show_hints[index]

def toggle_solution(index):
    st.session_state.show_solutions[index] = not st.session_state.show_solutions[index]

# Příklad 1: Liniový graf
st.header("1. Vývoj prodejů v průběhu roku")
st.write("""
Vytvořte interaktivní liniový graf zobrazující měsíční vývoj prodejů tří produktů. 
Graf by měl obsahovat legendu a umožňovat zobrazení/skrytí jednotlivých produktů.
""")

st.code("""
# Data pro graf
data = {
    'měsíc': pd.date_range('2023-01-01', '2023-12-31', freq='M'),
    'Produkt A': [120, 125, 135, 140, 160, 175, 165, 180, 185, 190, 200, 210],
    'Produkt B': [90, 95, 100, 110, 120, 125, 115, 130, 140, 145, 150, 155],
    'Produkt C': [150, 155, 165, 170, 180, 185, 175, 190, 195, 200, 210, 220]
}
df = pd.DataFrame(data)
""")

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
    - Použijte `px.line()`
    - Data musí být ve formátu long (použijte `melt()`)
    - Nastavte parametry pro osy a legendu
    - Přidejte interaktivní prvky pomocí `update_traces()`
    """)

if st.session_state.show_solutions[0]:
    st.code("""
    import plotly.express as px
    
    # Převod dat do dlouhého formátu
    df_long = df.melt(id_vars=['měsíc'], 
                      value_vars=['Produkt A', 'Produkt B', 'Produkt C'],
                      var_name='Produkt', value_name='Prodeje')
    
    # Vytvoření grafu
    fig = px.line(df_long, x='měsíc', y='Prodeje', color='Produkt',
                  title='Vývoj prodejů v roce 2023',
                  labels={'měsíc': 'Datum', 'Prodeje': 'Počet prodaných kusů'})
    
    # Úprava vzhledu
    fig.update_layout(
        hovermode='x unified',
        legend_title='Produkty',
        xaxis_title='Datum',
        yaxis_title='Počet prodaných kusů'
    )
    
    fig.show()
    """)

# Příklad 2: Sloupcový graf
st.header("2. Porovnání prodejů podle kategorií")
st.write("""
Vytvořte interaktivní sloupcový graf zobrazující prodeje podle kategorií s možností 
přepínání mezi absolutními a relativními hodnotami.
""")

st.code("""
# Data pro graf
data = {
    'Kategorie': ['Elektronika', 'Oblečení', 'Potraviny', 'Sport', 'Knihy'],
    'Prodeje': [850, 620, 930, 450, 380],
    'Region': ['Sever', 'Jih', 'Sever', 'Východ', 'Západ']
}
df = pd.DataFrame(data)
""")

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
    - Použijte `px.bar()`
    - Přidejte parametr `color` pro rozlišení regionů
    - Nastavte `barmode` pro typ zobrazení
    - Přidejte přepínač pro procenta pomocí `update_layout()`
    """)

if st.session_state.show_solutions[1]:
    st.code("""
    import plotly.express as px
    
    # Výpočet procentuálních podílů
    df['Prodeje_pct'] = df['Prodeje'] / df['Prodeje'].sum() * 100
    
    # Vytvoření grafu
    fig = px.bar(df, x='Kategorie', y=['Prodeje', 'Prodeje_pct'],
                 color='Region',
                 barmode='group',
                 title='Prodeje podle kategorií a regionů',
                 labels={'value': 'Prodeje', 'variable': 'Metrika'})
    
    # Přidání přepínače pro procenta
    fig.update_layout(
        updatemenus=[dict(
            type='buttons',
            direction='left',
            buttons=[
                dict(args=[{'y': [df['Prodeje']]}],
                     label='Absolutní hodnoty',
                     method='restyle'),
                dict(args=[{'y': [df['Prodeje_pct']]}],
                     label='Procenta',
                     method='restyle')
            ],
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.1,
            xanchor='left',
            y=1.1,
            yanchor='top'
        )]
    )
    
    fig.show()
    """)

# Příklad 3: Koláčový graf
st.header("3. Rozložení rozpočtu")
st.write("""
Vytvořte interaktivní koláčový graf zobrazující rozložení rozpočtu s možností 
zvýraznění vybraných kategorií a zobrazením detailů po najetí myší.
""")

st.code("""
# Data pro graf
data = {
    'Kategorie': ['Marketing', 'Vývoj', 'Administrativa', 'Prodej', 'Podpora'],
    'Rozpočet': [300000, 500000, 200000, 400000, 250000]
}
df = pd.DataFrame(data)
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
    - Použijte `go.Pie()`
    - Nastavte vlastní formát tooltipů
    - Přidejte animaci při najetí myší
    - Upravte zobrazení hodnot pomocí `textinfo`
    """)

if st.session_state.show_solutions[2]:
    st.code("""
    import plotly.graph_objects as go
    
    # Výpočet procent
    df['Procenta'] = df['Rozpočet'] / df['Rozpočet'].sum() * 100
    
    # Vytvoření grafu
    fig = go.Figure(data=[go.Pie(
        labels=df['Kategorie'],
        values=df['Rozpočet'],
        hovertemplate="<b>%{label}</b><br>" +
                      "Rozpočet: %{value:,.0f} Kč<br>" +
                      "Podíl: %{percent:.1f}%<extra></extra>",
        textinfo='label+percent',
        hole=0.3
    )])
    
    # Úprava vzhledu
    fig.update_layout(
        title='Rozložení rozpočtu podle kategorií',
        annotations=[dict(text='Celkem:<br>' + 
                         f"{df['Rozpočet'].sum():,.0f} Kč",
                         x=0.5, y=0.5,
                         font_size=14, showarrow=False)],
        showlegend=True
    )
    
    fig.show()
    """)

# Příklad 4: Bodový graf
st.header("4. Analýza vztahu mezi proměnnými")
st.write("""
Vytvořte interaktivní bodový graf zobrazující vztah mezi dvěma proměnnými s možností 
filtrování dat a zobrazení trendové křivky.
""")

st.code("""
# Generování dat
np.random.seed(42)
n_points = 100
data = {
    'x': np.random.normal(100, 15, n_points),
    'y': np.random.normal(50, 8, n_points),
    'kategorie': np.random.choice(['A', 'B', 'C'], n_points),
    'velikost': np.random.uniform(10, 50, n_points)
}
df = pd.DataFrame(data)
""")

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
    - Použijte `px.scatter()`
    - Přidejte trendovou křivku pomocí `trendline`
    - Implementujte filtrování pomocí `update_traces()`
    - Přidejte animované přechody
    """)

if st.session_state.show_solutions[3]:
    st.code("""
    import plotly.express as px
    
    # Vytvoření grafu
    fig = px.scatter(df, x='x', y='y',
                     color='kategorie',
                     size='velikost',
                     trendline="ols",
                     title='Vztah mezi proměnnými podle kategorií',
                     labels={'x': 'Proměnná X',
                            'y': 'Proměnná Y',
                            'kategorie': 'Kategorie',
                            'velikost': 'Velikost'})
    
    # Přidání ovládacích prvků
    fig.update_layout(
        updatemenus=[dict(
            type='buttons',
            showactive=True,
            buttons=[
                dict(label='Všechny kategorie',
                     method='update',
                     args=[{'visible': [True] * len(df['kategorie'].unique())}]),
                dict(label='Pouze A',
                     method='update',
                     args=[{'visible': [True, False, False]}]),
                dict(label='Pouze B',
                     method='update',
                     args=[{'visible': [False, True, False]}]),
                dict(label='Pouze C',
                     method='update',
                     args=[{'visible': [False, False, True]}])
            ]
        )]
    )
    
    # Přidání animací
    fig.update_traces(
        marker=dict(size=10,
                   line=dict(width=2,
                            color='DarkSlateGrey')),
        selector=dict(mode='markers'))
    
    fig.show()
    """)

st.success("""
✨ **Obecné tipy pro práci s Plotly:**
1. Vždy přidávejte popisné titulky a popisky os
2. Využívejte interaktivní prvky pro lepší uživatelský zážitek
3. Přizpůsobujte vzhled grafů pomocí `update_layout`
4. Implementujte smysluplné tooltips pro detail informací
5. Používejte vhodné barevné schéma pro váš účel
""")