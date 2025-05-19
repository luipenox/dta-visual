import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.title("Interaktivní vizualizace s Plotly")

st.header("Co je Plotly?")
st.write("""
Plotly je knihovna pro tvorbu interaktivních vizualizací v Pythonu. Nabízí:
- Interaktivní grafy s možností přiblížení a oddálení
- Možnost exportu do různých formátů
- Bohatou sadu typů grafů
- Moderní vzhled a animace
""")

# Načtení ukázkových dat
df_tips = px.data.tips()
df_iris = px.data.iris()
df_stocks = px.data.stocks()

st.header("1. Základní grafy")
st.write("Nejčastěji používané typy grafů:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Čárový graf")
    fig = px.line(df_stocks, x='date', y=['GOOG', 'AAPL', 'AMZN'],
                  title='Vývoj cen akcií')
    st.plotly_chart(fig)

    st.code("""
    import plotly.express as px
    
    fig = px.line(df_stocks, x='date', y=['GOOG', 'AAPL', 'AMZN'], 
                  title='Vývoj cen akcií')
    fig.show()
    """)

with col2:
    st.subheader("Sloupcový graf")
    fig = px.bar(df_tips.groupby('day')['total_bill'].mean().reset_index(),
                 x='day', y='total_bill',
                 title='Průměrná útrata podle dne')
    st.plotly_chart(fig)

    st.code("""
    fig = px.bar(df_tips.groupby('day')['total_bill'].mean().reset_index(), 
                 x='day', y='total_bill', 
                 title='Průměrná útrata podle dne')
    """)

st.header("2. Statistické grafy")
st.write("Grafy pro analýzu distribuce dat:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Krabicový graf")
    fig = px.box(df_tips, x='day', y='total_bill', color='time',
                 title='Distribuce útrat podle dne a času')
    st.plotly_chart(fig)

    st.code("""
    fig = px.box(df_tips, x='day', y='total_bill', color='time',
                 title='Distribuce útrat podle dne a času')
    """)

with col2:
    st.subheader("Histogram")
    fig = px.histogram(df_tips, x='total_bill', color='sex',
                       title='Distribuce útrat podle pohlaví')
    st.plotly_chart(fig)

    st.code("""
    fig = px.histogram(df_tips, x='total_bill', color='sex',
                      title='Distribuce útrat podle pohlaví')
    """)

st.header("3. Vztahové grafy")
st.write("Grafy pro zobrazení vztahů mezi proměnnými:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Bodový graf")
    fig = px.scatter(df_iris, x='sepal_length', y='sepal_width',
                     color='species', title='Iris dataset')
    st.plotly_chart(fig)

    st.code("""
    fig = px.scatter(df_iris, x='sepal_length', y='sepal_width', 
                    color='species', title='Iris dataset')
    """)

with col2:
    st.subheader("Bublinkový graf")
    fig = px.scatter(df_tips, x='total_bill', y='tip',
                     size='size', color='time',
                     title='Vztah mezi útratou a spropitným')
    st.plotly_chart(fig)

    st.code("""
    fig = px.scatter(df_tips, x='total_bill', y='tip', 
                    size='size', color='time',
                    title='Vztah mezi útratou a spropitným')
    """)

st.header("4. Složené grafy")
st.write("Komplexnější vizualizace:")

# Subploty
st.subheader("Subploty")
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2,
                    subplot_titles=('Útrata podle dne', 'Spropitné podle dne'))

fig.add_trace(
    go.Box(x=df_tips['day'], y=df_tips['total_bill'], name='Útrata'),
    row=1, col=1
)

fig.add_trace(
    go.Box(x=df_tips['day'], y=df_tips['tip'], name='Spropitné'),
    row=1, col=2
)

fig.update_layout(title_text="Srovnání útrat a spropitného", height=500)
st.plotly_chart(fig)

st.code("""
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2,
                    subplot_titles=('Útrata podle dne', 'Spropitné podle dne'))

fig.add_trace(
    go.Box(x=df_tips['day'], y=df_tips['total_bill'], name='Útrata'),
    row=1, col=1
)

fig.add_trace(
    go.Box(x=df_tips['day'], y=df_tips['tip'], name='Spropitné'),
    row=1, col=2
)

fig.update_layout(title_text="Srovnání útrat a spropitného")
""")

st.header("5. Interaktivní prvky")
st.write("Ukázka interaktivních možností Plotly:")

# Dropdown menu
st.subheader("Graf s výběrem proměnné")
selected_var = st.selectbox(
    'Vyberte proměnnou pro zobrazení:',
    ['total_bill', 'tip', 'size']
)

fig = px.box(df_tips, x='day', y=selected_var, color='time',
             title=f'Distribuce {selected_var} podle dne')
st.plotly_chart(fig)

st.code("""
selected_var = 'total_bill'  # nebo jiná proměnná
fig = px.box(df_tips, x='day', y=selected_var, color='time',
             title=f'Distribuce {selected_var} podle dne')
""")

st.success("""
✨ **Výhody Plotly:**
1. **Interaktivita** - zoom, pan, tooltips
2. **Moderní vzhled** - atraktivní výchozí styly
3. **Flexibilita** - mnoho možností přizpůsobení
4. **Export** - možnost uložení do různých formátů
5. **Integrace** - snadné použití v Jupyter notebooks a webových aplikacích
""")

st.info("""
💡 **Tipy pro práci s Plotly:**
1. Používejte `px` pro jednoduché grafy
2. Využívejte `go` pro větší kontrolu
3. Experimentujte s interaktivními prvky
4. Přizpůsobujte vzhled pomocí `update_layout`
5. Kombinujte různé typy grafů pomocí subplotů
""")

st.title("Komplexní ukázka fig.update_layout v Plotly")

# Generování ukázkových dat
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
data = {
    'datum': dates,
    'hodnota_A': np.random.normal(100, 15, len(dates)),
    'hodnota_B': np.random.normal(150, 20, len(dates)),
    'kategorie': np.random.choice(['X', 'Y', 'Z'], len(dates))
}
df = pd.DataFrame(data)

fig = go.Figure()

# Přidání dat
fig.add_trace(go.Scatter(x=df['datum'], y=df['hodnota_A'], name='Řada A'))
fig.add_trace(go.Scatter(x=df['datum'], y=df['hodnota_B'], name='Řada B'))

# Komplexní update_layout
fig.update_layout(
    # Základní nastavení
    title={
        'text': 'Komplexní graf s různými nastaveními',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, color='darkblue', family='Arial')
    },

    # Rozměry grafu
    width=800,
    height=500,

    # Pozadí
    plot_bgcolor='rgba(240, 240, 240, 0.95)',
    paper_bgcolor='white',

    # Okraje
    margin=dict(l=80, r=80, t=100, b=80),

    # Nastavení os
    xaxis=dict(
        title='Časová osa',
        showgrid=True,
        gridwidth=1,
        gridcolor='white',
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    ),

    yaxis=dict(
        title='Hodnoty',
        showgrid=True,
        gridwidth=1,
        gridcolor='white',
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    ),

    # Legenda
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        bgcolor='rgba(0, 0, 0, 0.8)',
        bordercolor='black',
        borderwidth=1
    ),

    # Anotace
    annotations=[
        dict(
            x='2023-07-01',
            y=150,
            xref='x',
            yref='y',
            text='Důležitý bod',
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-40
        )
    ],

    # Vodící čáry
    shapes=[
        # Horizontální čára
        dict(
            type='line',
            x0='2023-01-01',
            x1='2023-12-31',
            y0=100,
            y1=100,
            line=dict(
                color='red',
                width=2,
                dash='dash'
            )
        )
    ]
)

st.plotly_chart(fig)

st.code("""
fig.update_layout(
    # Základní nastavení
    title={
        'text': 'Komplexní graf s různými nastaveními',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=24, color='darkblue', family='Arial')
    },

    # Rozměry grafu
    width=800,
    height=500,

    # Pozadí
    plot_bgcolor='rgba(240, 240, 240, 0.95)',
    paper_bgcolor='white',

    # Okraje
    margin=dict(l=80, r=80, t=100, b=80),

    # Nastavení os
    xaxis=dict(
        title='Časová osa',
        showgrid=True,
        gridwidth=1,
        gridcolor='white',
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    ),

    # Legenda
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        bgcolor='rgba(0, 0, 0, 0.8)',
        bordercolor='black',
        borderwidth=1
    )
)
""")
