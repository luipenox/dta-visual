import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Příklady úprav grafů")

# 1. Příklad - Mřížky
st.header("1. Typy mřížek")

x = np.linspace(0, 10, 100)
y = np.sin(x)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Základní mřížka")
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.grid(True)
    plt.title("Základní mřížka")
    st.pyplot(plt)
    plt.close()

with col2:
    st.subheader("Stylizovaná mřížka")
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title("Stylizovaná mřížka")
    st.pyplot(plt)
    plt.close()

st.code("""
# Základní mřížka
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.grid(True)
plt.title("Základní mřížka")
plt.show()
plt.close()

# Stylizovaná mřížka
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title("Stylizovaná mřížka")
plt.show()
plt.close()
""", language="python")

# 2. Příklad - Nastavení os
st.header("2. Nastavení os")

data = np.random.normal(100, 20, 1000)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Standardní osy")
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30)
    plt.title("Standardní osy")
    st.pyplot(plt)
    plt.close()

with col2:
    st.subheader("Upravené osy")
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30)
    plt.title("Upravené osy")
    plt.xlabel("Hodnota (Kč)", fontsize=10)
    plt.ylabel("Četnost", fontsize=10)
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.close()

st.code("""
# Standardní osa
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30)
plt.title("Standardní osy"))

# Upravená osa
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30)
plt.title("Upravené osy")
plt.xlabel("Hodnota (Kč)", fontsize=10)
plt.ylabel("Četnost", fontsize=10)
plt.xticks(rotation=45)
plt.show()
plt.close()
""", language="python")

# 3. Příklad - Dvojitý graf
st.header("3. Více datových řad")

# Data pro ukázku
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.grid(True, linestyle='--', alpha=0.7)
plt.title("Graf s více datovými řadami")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
st.pyplot(plt)
plt.close()

st.code("""
# Graf s více datovými řadami
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.grid(True, linestyle='--', alpha=0.7)
plt.title("Graf s více datovými řadami")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
plt.close()
""", language="python")

# 5. Příklad - Různé styly
st.header("5. Styly grafů")

data = pd.DataFrame({
    'A': np.random.randn(50),
    'B': np.random.randn(50) + 2
})

styles = ['default', 'bmh', 'ggplot']
cols = st.columns(len(styles))

for style, col in zip(styles, cols):
    with col:
        st.subheader(f"Styl: {style}")
        with plt.style.context(style):
            plt.figure(figsize=(8, 5))
            plt.plot(data['A'], label='A')
            plt.plot(data['B'], label='B')
            plt.legend()
            plt.title(f"Styl: {style}")
            st.pyplot(plt)
            plt.close()

st.code("""
styles = ['default', 'bmh', 'ggplot']

for style in styles:
    with plt.style.context(style):
        plt.figure(figsize=(8, 5))
        plt.plot(data['A'], label='A')
        plt.plot(data['B'], label='B')
        plt.legend()
        plt.title(f"Styl: {style}")
        plt.show()
        plt.close()
""", language="python")

