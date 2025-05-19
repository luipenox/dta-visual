import streamlit as st


def home():
    st.title('Vizualizace')


def tools():
    st.title("Užitečné nástroje")
    st.write(
        "[Google Colab](https://colab.research.google.com/) - bezplatné webové prostředí ve stylu Jupyter notebooků, které umožňuje psát a spouštět Python kód přímo v prohlížeči s přístupem k výpočetním zdrojům včetně GPU a TPU, což je ideální zejména pro strojové učení a analýzu dat.")


def contact():
    st.title('Kontaktní informace')
    col1, col2 = st.columns(2)

    with col1:
        st.info('Luděk Reif', icon=":material/signature:")
        st.info('+420 720 116 008', icon=":material/call:")
        st.info('luipenox@gmail.com', icon=":material/mail:")
        st.info('https://www.linkedin.com/in/luipenox/', icon=":material/link:")

    with col2:
        st.image('assets/images/luipenox.jpg', width=272)


introduction = st.Page(
    "chapters/introduction.py",
    title="Úvod do visualizací",
    icon=":material/counter_0:")

boxplot = st.Page(
    "chapters/boxplot.py",
    title="Krabicový graf",
    icon=":material/counter_1:")

pandas_melt = st.Page(
    "chapters/pandas_melt.py",
    title="pd.melt()",
    icon=":material/counter_2:")

pandas = st.Page(
    "chapters/pandas.py",
    title="Pandas",
    icon=":material/counter_3:")

pyplot = st.Page(
    "chapters/pyplot.py",
    title="Pyplot",
    icon=":material/counter_4:")

pandas_examples = st.Page(
    "chapters/pandas_examples.py",
    title="Pandas - cvičení",
    icon=":material/counter_5:")

chapter_seaborn = st.Page(
    "chapters/chapter_seaborn.py",
    title="Seaborn",
    icon=":material/counter_6:")

seaborn_examples = st.Page(
    "chapters/examples_seaborn.py",
    title="Seaborn - cvičení",
    icon=":material/counter_7:")

chapter_plotly = st.Page(
    "chapters/chapter_plotly.py",
    title="Plotly",
    icon=":material/counter_8:")

examples_plotly = st.Page(
    "chapters/examples_plotly.py",
    title="Plotly - příklady",
    icon=":material/counter_9:")

page_dict = {'Kapitoly': [
    introduction,
    boxplot,
    pandas_melt,
    pandas,
    pyplot,
    pandas_examples,
    chapter_seaborn,
    seaborn_examples,
    chapter_plotly,
    examples_plotly

]}

home_page = st.Page(home, title="O kurzu", icon=":material/info:")
tools_page = st.Page(tools, title="Užitečné nástroje", icon=":material/favorite:")
contact_page = st.Page(contact, title="Kontakt", icon=":material/import_contacts:")

account_pages = [home_page, tools_page, contact_page]

pg = st.navigation({"Informace": account_pages} | page_dict)
pg.run()
