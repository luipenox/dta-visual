import streamlit as st

st.title("Vizualizace dat pomocí Pandas")

st.header("Co je Pandas pro vizualizace?")
st.write("""
Pandas je výkonná knihovna pro analýzu dat, která obsahuje také integrované možnosti vizualizace. 
Tyto vizualizační funkce jsou postaveny na knihovně Matplotlib a poskytují jednoduchý způsob, 
jak rychle vizualizovat data přímo z DataFrame nebo Series objektů.
""")

st.header("Hlavní výhody Pandas vizualizací")
st.write("""
🎨 **Klíčové přednosti:**
- Přímá integrace s DataFrame objekty
- Jednoduchá syntax
- Automatické zpracování indexů
- Široká škála základních typů grafů
- Snadná customizace
""")

st.header("Základní typy grafů v Pandas")
st.write("""
📊 **Nejpoužívanější metody:**
- **plot()** - základní čárové grafy
- **plot.bar()** - sloupcové grafy
- **plot.hist()** - histogramy
- **plot.box()** - krabicové grafy
- **plot.scatter()** - bodové grafy
- **plot.pie()** - koláčové grafy
""")

st.header("Praktické použití")
st.code("""
# Základní čárový graf
import pandas as pd

df = pd.DataFrame({'rok': [2020, 2021, 2022, 2023],
                  'prodeje': [100, 120, 140, 180]})
df.plot(x='rok', y='prodeje')
""", language="python")

st.header("Pokročilé techniky")
st.info("""
🔧 **Užitečné parametry:**
1. `figsize` - velikost grafu
2. `color` - barvy prvků
3. `title` - název grafu
4. `legend` - zobrazení legendy
5. `grid` - mřížka v grafu
""")

st.header("Tipy pro práci s Pandas vizualizacemi")
st.info("""
💡 **Osvědčené postupy:**
1. Vždy začněte s čistými daty
2. Používejte vhodné typy grafů pro vaše data
3. Nastavte správné popisky os
4. Využívejte barevné schéma smysluplně
5. Optimalizujte velikost grafů pro lepší čitelnost
""")

st.warning("""
⚠️ **Časté chyby:**
- Nevhodné měřítko os
- Chybějící popisky
- Špatná volba typu grafu
- Přehlcení grafu daty
""")

st.success("""
✨ **Proč používat Pandas vizualizace:**
- Rychlé prototypování grafů
- Jednoduchá syntax
- Přímá integrace s DataFrame
- Snadná customizace
- Dobrá dokumentace
""")

st.header("Ukázkový kód")
st.code("""
# Různé typy grafů v Pandas
import pandas as pd
import numpy as np

# Vytvoření vzorových dat
df = pd.DataFrame({
    'A': np.random.randn(1000) + 0,
    'B': np.random.randn(1000) + 2,
    'C': np.random.randn(1000) + 4
})

# Histogram
df.hist(bins=50)

# Krabicový graf
df.boxplot()

# Sloupcový graf
df.mean().plot(kind='bar')
""", language="python")