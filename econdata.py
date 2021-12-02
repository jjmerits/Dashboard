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
import pymongo

#sns.set_style("dark")
url = 'https://raw.githubusercontent.com/jjmerits/Dashboard/main/test_df_all.csv'
test_df = pd.read_csv(url)

#test_df = pd.read_csv('C:/Users/NHWM/PycharmProjects/steamlit/test_df_all.csv')
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

# Initialize connection.
conn = pymongo.MongoClient(st.secrets.db_credentials.HOST,st.secrets.db_credentials.PORT, username=st.secrets.db_credentials.DB_USER,password=st.secrets.db_credentials.DB_TOKEN, tls=True, tlsAllowInvalidCertificates=True)

# Pull data from the collection.
# Uses st.cache to only rerun when the query changes or after 10 min.
USD_list = conn.econdata.glob.find({'currency':'USD'}).distinct('event')
cursor = conn.econdata.glob.find({'event':{"$in":USD_list},'currency':'USD'},{'_id':False})
df =pd.DataFrame(cursor)

df['date'] = df['date'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S').strftime('%Y/%m'))
df.set_index("date", inplace = True)


# plot graph
x = "Final Manufacturing PMI"
df_x = df[df['Name'] == x]
fig = go.Figure()
fig.add_trace(go.Bar(x=df_x[['actual']].index,y=df_x['actual'].to_list(),name='actual'))
fig.add_trace(go.Bar(x=df_x[['actual']].index,y=df_x['forecast'].to_list(),name='forecast'))
fig.update_layout(barmode='group',title=x, yaxis=dict(title = 'y/y %'))
#fig.show()
st.plotly_chart(fig,use_container_width=True)

#st.set_page_config(layout='centered')
st.write(df.head(5))

conn.close()
