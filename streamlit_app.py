import altair as alt
import math
import pandas as pd
import streamlit as st

# Carregue o DataFrame a partir do arquivo CSV
df = pd.read_csv("./trabalho_microclimatologia.csv")

# Defina o título da página
st.title("Análise Exploratória dos Dados")

# Exiba um texto explicativo antes da tabela de dados
st.write("Aqui estão os dados do seu arquivo CSV:")

# Exiba a tabela com os dados
st.write(df)

# Adicione mais texto explicativo após a tabela
st.write("Agora, vamos incluir uma coluna 'hora_min' aos dados para facilitar a hora do dia:")

# Calcule as horas e minutos separadamente
df['horas'] = df['Hora'].astype(int)  # Parte inteira como horas
df['minutos'] = ((df['Hora'] - df['horas']) * 60).astype(int)  # Parte decimal como minutos

# Combine as horas e minutos no formato 'hora:minuto'
df['hora_min'] = df['horas'].astype(str).str.zfill(2) + ':' + df['minutos'].astype(str).str.zfill(2)

# Mais transformações nos dados...

# Exiba a tabela de dados transformados
st.write("Aqui estão os novos dados:")

# Reorganize as colunas para ter 'hora_min' entre 'Hora' e 'h'
df = df[['NDA', 'Dia', 'Mes', 'Ano', 'Hora', 'hora_min', 'h', 'Declinacao solar', 'hn', 'N', 'ns', 'ps', 'Zn', '(D/d)2', 'Ih', 'Qg', 'PARi', 'PARi corrigida', 'k', 'Tar', 'IAF', 'IAF.1', 'PARt', 'PARa', 'Assimilacao CO2 (milimol/m2.s)', 'Produçcao Glicose (g Glicose/m2.15min)']]

# Exiba a tabela com os dados transformados
st.write(df)

st.write("Para entender os tipos de dados, vamos usar df.info():")

# Crie um DataFrame com informações sobre o DataFrame principal
info_df = pd.DataFrame({
    'Nome da Coluna': df.columns,
    'Tipos de Dados': df.dtypes,
    'Valores Não Nulos': df.count(),
})

# Título para as informações
st.subheader("Informações sobre o DataFrame:")

# Exiba o DataFrame com as informações
st.write(info_df)

# Exiba estatísticas descritivas dos dados
st.write("Estatísticas Descritivas dos Dados:")
st.write(df.describe())

# Exiba estatísticas descritivas dos dados
st.write("Podemos selecionar apenas as colunas de interesse, antes de chamar o método df.describe() e arredondar os números para 2 casas após a vírgula com o método .round():")
selected_columns = ['Zn', 'k']
selected_stats = df[selected_columns].describe().round(2)
st.write(selected_stats)

# Exiba estatísticas descritivas de uma só variável 'Tar'
st.write("Estatísticas Descritivas de uma só variável 'Tar'")
tar_stats = df['Tar'].describe().round(2)
st.write(tar_stats)

# Título da página
st.title("Gráfico de Dispersão com Eixo Secundário")

# Escolha as colunas para os eixos X, Y (principal) e Y2 (secundário)
x_column = st.selectbox("Selecione a coluna para o eixo X:", df.columns)
y_column_primary = st.selectbox("Selecione a coluna para o eixo Y principal:", df.columns)
y_column_secondary = st.selectbox("Selecione a coluna para o eixo Y secundário:", df.columns)

# Crie o gráfico de dispersão com escala secundária
scatter_chart = alt.Chart(df).mark_circle().encode(
    x=x_column,
    y=alt.Y(y_column_primary, axis=alt.Axis(title='Eixo Principal')),
    color=alt.ColorValue("blue")  # Cor dos pontos no eixo principal
).properties(
    width=600,  # Defina a largura do gráfico
).interactive()

# Adicione uma camada com um segundo eixo Y (escala secundária)
scatter_chart_with_secondary_axis = scatter_chart + alt.Chart(df).mark_circle().encode(
    x=alt.X('index:Q', axis=None),  # Use um eixo sem rótulos
    y=alt.Y(y_column_secondary, axis=alt.Axis(title='Eixo Secundário')),
    color=alt.ColorValue("red")  # Cor dos pontos no eixo secundário
).transform_calculate(index='0')

# Exiba o gráfico com escala secundária
st.altair_chart(scatter_chart_with_secondary_axis, use_container_width=True)
