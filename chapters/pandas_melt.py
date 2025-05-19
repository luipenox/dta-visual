import streamlit as st
import pandas as pd

st.title("Vysvětlení pandas.melt()")

st.write("""
Funkce `melt()` slouží k transformaci dat z "širokého" do "dlouhého" formátu. Je užitečná především když:
- Potřebujeme převést sloupce na řádky
- Chceme data připravit pro vizualizaci
- Potřebujeme upravit strukturu dat pro analýzu
""")

# Příklad 1: Základní použití
st.header("1. Základní použití melt()")

st.code("""
# Původní data
data = {
    'jméno': ['Jan', 'Eva', 'Petr'],
    'matematika': [85, 92, 78],
    'čeština': [88, 95, 82],
    'angličtina': [90, 87, 85]
}
df = pd.DataFrame(data)
""")

# Vytvoření DataFrame
data = {
    'jméno': ['Jan', 'Eva', 'Petr'],
    'matematika': [85, 92, 78],
    'čeština': [88, 95, 82],
    'angličtina': [90, 87, 85]
}
df = pd.DataFrame(data)

st.write("**Původní data (široký formát):**")
st.dataframe(df)

# Použití melt
df_melted = df.melt(id_vars=['jméno'],
                    var_name='předmět',
                    value_name='známka')

st.write("**Data po použití melt() (dlouhý formát):**")
st.dataframe(df_melted)

st.code("""
# Transformace pomocí melt
df_melted = df.melt(
    id_vars=['jméno'],      # sloupce, které zůstanou jak jsou
    var_name='předmět',     # nový název pro sloupec s původními názvy sloupců
    value_name='známka'     # nový název pro sloupec s hodnotami
)
""")

# Příklad 2: Více ID sloupců
st.header("2. Melt s více ID sloupci")

st.code("""
# Data s více ID sloupci
data = {
    'student': ['Jan', 'Eva', 'Petr'],
    'třída': ['A', 'B', 'A'],
    'Q1_2023': [85, 92, 78],
    'Q2_2023': [88, 95, 82],
    'Q3_2023': [90, 87, 85]
}
df = pd.DataFrame(data)
""")

# Vytvoření DataFrame
data = {
    'student': ['Jan', 'Eva', 'Petr'],
    'třída': ['A', 'B', 'A'],
    'Q1_2023': [85, 92, 78],
    'Q2_2023': [88, 95, 82],
    'Q3_2023': [90, 87, 85]
}
df = pd.DataFrame(data)

st.write("**Původní data:**")
st.dataframe(df)

# Použití melt s více ID sloupci
df_melted = df.melt(id_vars=['student', 'třída'],
                    var_name='kvartál',
                    value_name='výsledky')

st.write("**Data po transformaci:**")
st.dataframe(df_melted)

st.code("""
# Transformace s více ID sloupci
df_melted = df.melt(
    id_vars=['student', 'třída'],  # zachováme oba identifikační sloupce
    var_name='kvartál',
    value_name='výsledky'
)
""")

# Příklad 3: Selektivní melt
st.header("3. Selektivní melt s value_vars")

st.code("""
# Data s různými typy sloupců
data = {
    'jméno': ['Jan', 'Eva', 'Petr'],
    'věk': [25, 23, 24],
    'test_1': [85, 92, 78],
    'test_2': [88, 95, 82],
    'test_3': [90, 87, 85]
}
df = pd.DataFrame(data)
""")

# Vytvoření DataFrame
data = {
    'jméno': ['Jan', 'Eva', 'Petr'],
    'věk': [25, 23, 24],
    'test_1': [85, 92, 78],
    'test_2': [88, 95, 82],
    'test_3': [90, 87, 85]
}
df = pd.DataFrame(data)

st.write("**Původní data:**")
st.dataframe(df)

# Použití melt pouze pro vybrané sloupce
df_melted = df.melt(id_vars=['jméno', 'věk'],
                    value_vars=['test_1', 'test_2', 'test_3'],
                    var_name='test',
                    value_name='skóre')

st.write("**Data po selektivní transformaci:**")
st.dataframe(df_melted)

st.code("""
# Selektivní transformace
df_melted = df.melt(
    id_vars=['jméno', 'věk'],           # sloupce, které zachováme
    value_vars=['test_1', 'test_2', 'test_3'],  # sloupce pro transformaci
    var_name='test',
    value_name='skóre'
)
""")

st.success("""
✨ **Hlavní parametry melt():**
1. **id_vars**: Seznam sloupců, které zůstanou nezměněné
2. **value_vars**: Seznam sloupců, které chceme transformovat (volitelné)
3. **var_name**: Název nového sloupce pro původní názvy sloupců
4. **value_name**: Název nového sloupce pro hodnoty
""")

st.info("""
💡 **Typické použití melt():**
1. **Vizualizace dat** - mnoho vizualizačních knihoven preferuje data v dlouhém formátu
2. **Časové řady** - převod více časových sloupců na řádky
3. **Analýza opakovaných měření** - převod měření z různých časových bodů
4. **Příprava dat pro statistické testy** - některé testy vyžadují data v dlouhém formátu
""")