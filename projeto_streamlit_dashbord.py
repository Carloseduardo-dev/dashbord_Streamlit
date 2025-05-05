import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard ESC Engenharia')
st.subheader('Tabela de Dados')

df = pd.read_csv('esc_engenharia.csv')
df_comeca1 = df.reset_index(drop=True)
df_comeca1.index += 1
st.dataframe(df_comeca1)

st.subheader('Estatísticas Descritivas')

estatisticas = df['Quantidade'].describe()
st.markdown(f'''
- **CONTGEM:** {estatisticas['count']:.0f}
- **MÉDIA:** {estatisticas['mean']:.2f}
- **DESVIO PADRÃO:** {estatisticas['std']:.2f}
- **MÍNIMO:** {estatisticas['min']:.2f}
- **1º QUARTIL (25%):** {estatisticas['25%']:.2f}
- **MEDIANA (50%):** {estatisticas['50%']:.2f}
- **3º QUARTIL (75%):** {estatisticas['75%']:.2f}
- **MÁXIMO:** {estatisticas['max']:.2f}
''')

st.sidebar.header('Filtros')
tipos = st.sidebar.multiselect('Filtrar Projetos:', df['Tipo de Projeto'].unique(), default=df['Tipo de Projeto'].unique())
df_filtrado = df[df['Tipo de Projeto'].isin(tipos)]


st.write('**Dados Filtrados**')
st.dataframe(df_filtrado)

st.subheader('Gráficos')

col1, col2 = st.columns(2)
with col1:
    st.write('**Barras**')
    fig1, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df_filtrado, x='Tipo de Projeto', y='Quantidade', ax=ax, color='purple')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig1)

with col2:
    st.write('**Histograma das Quantidades**')
    fig2, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df_filtrado['Quantidade'], kde=True, bins=10, ax=ax, color='blue')
    plt.tight_layout()
    st.pyplot(fig2)

st.write('**Scatter Plot(Dispersão)**')
fig3, ax = plt.subplots(figsize=(10, 5))
sns.regplot(
    x=df_filtrado.index,     y=df_filtrado['Quantidade'],
    scatter=True,
    color='darkred',
    ax=ax
)
ax.set_xlabel('Índice')
ax.set_ylabel('Quantidade')
plt.tight_layout()
st.pyplot(fig3)

st.markdown('''
###### Fonte:  
Site da empresa  
[http://www.esc.com.br/](http://www.esc.com.br/)
''')
