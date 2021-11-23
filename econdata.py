import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from datetime import datetime
import seaborn as sns
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

import plotly.graph_objects as go

#sns.set_style("dark")
test_df = pd.read_csv('C:\\Users\\NHWM\\PycharmProjects\\steamlit\\test_df_all.csv')
name_list = test_df['Name'].unique().tolist()
df = test_df[test_df['Name'] == name_list[4]]
#df.sort_value

df['date'] = df['date'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').strftime('%Y/%m'))
df.set_index("date", inplace = True)

#plt.figure(figsize=(15,30))
#plt.rc('xtick' , labelsize = 8)
#plt.rc('ytick' , labelsize = 5)
#df[['actual']].plot(kind = "barh")
#
#fig = px.bar(df[['actual']], y='actual', x=df[['actual']].index, title=name_list[4],orientation='v', labels={'actual':'actual (%)', 'date':'date'})
#fig.show()
st.set_page_config(layout='wide')
fig = go.Figure()
fig.add_trace(go.Bar(x=df[['actual']].index,y=df['actual'].to_list(),name='actual'))
fig.add_trace(go.Bar(x=df[['actual']].index,y=df['forecast'].to_list(),name='forecast'))
fig.update_layout(barmode='group',title=name_list[4], yaxis=dict(title = 'y/y %'))
#fig.show()
st.plotly_chart(fig,use_container_width=True)
