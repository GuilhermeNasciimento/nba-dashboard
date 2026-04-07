import streamlit as st
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NBA Dashboard", layout="wide")

st.title("🏀 NBA Analytics Dashboard")

# ==============================
# CARREGAR DADOS
# ==============================
@st.cache_data
def load_data():
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        season_type_all_star='Regular Season'
    )
    return stats.get_data_frames()[0]

df = load_data()

# ==============================
# TRATAMENTO
# ==============================
df['PTS_TOTAL'] = df['PTS'] * df['GP']
df['REB_TOTAL'] = df['REB'] * df['GP']
df['AST_TOTAL'] = df['AST'] * df['GP']
df['MIN_AVG'] = df['MIN'] / df['GP']
df['TS%'] = df['PTS'] / (2 * (df['FGA'] + 0.44 * df['FTA']))

# ==============================
# SIDEBAR
# ==============================
st.sidebar.header("Filtros")

search = st.sidebar.text_input("Buscar jogador")

filtered = df[df['PLAYER_NAME'].str.lower().str.contains(search.lower())] if search else df
players = sorted(filtered['PLAYER_NAME'].unique())

player1 = st.sidebar.selectbox("Jogador 1", players)
player2 = st.sidebar.selectbox("Jogador 2", players)

p1 = df[df['PLAYER_NAME'] == player1].iloc[0]
p2 = df[df['PLAYER_NAME'] == player2].iloc[0]

# ==============================
# MÉTRICAS
# ==============================
st.subheader(f"{player1} vs {player2}")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### {player1}")
    st.metric("PTS", f"{p1['PTS']:.1f}")
    st.metric("REB", f"{p1['REB']:.1f}")
    st.metric("AST", f"{p1['AST']:.1f}")
    st.metric("MIN", f"{p1['MIN_AVG']:.1f}")
    st.metric("TS%", f"{p1['TS%']:.2f}")

with col2:
    st.markdown(f"### {player2}")
    st.metric("PTS", f"{p2['PTS']:.1f}")
    st.metric("REB", f"{p2['REB']:.1f}")
    st.metric("AST", f"{p2['AST']:.1f}")
    st.metric("MIN", f"{p2['MIN_AVG']:.1f}")
    st.metric("TS%", f"{p2['TS%']:.2f}")

# ==============================
# GRÁFICO
# ==============================
radar_df = pd.DataFrame({
    'Categoria': ['PTS', 'REB', 'AST', 'STL', 'BLK'],
    player1: [p1['PTS'], p1['REB'], p1['AST'], p1['STL'], p1['BLK']],
    player2: [p2['PTS'], p2['REB'], p2['AST'], p2['STL'], p2['BLK']]
})

fig = px.line_polar(
    radar_df.melt(id_vars='Categoria'),
    r='value',
    theta='Categoria',
    color='variable',
    line_close=True
)

st.plotly_chart(fig, width='stretch')

# ==============================
# TOP 10
# ==============================
st.subheader("Top 10 Pontuadores")

top10 = df.sort_values(by='PTS', ascending=False).head(10)

fig2 = px.bar(top10, x='PLAYER_NAME', y='PTS')

st.plotly_chart(fig2, width='stretch')
