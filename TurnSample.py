# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:52:22 2017

@author: prver
"""

import pandas as pd
import seaborn as sns

#Import Jan 2017 Turnstile Data and Group By Station/Time
fields = ['Station', 'Time', 'Entries',
       'Exits']
df = pd.read_csv('Jan2017.csv', header=0, skipinitialspace=True, usecols=fields)
df2 = df.groupby(['Station'])['Entries', 'Exits'].agg(sum)
x=df2['Entries']
y=df2['Exits']

#Plot Scatter Plot of Entries vs Exits to Have An Idea of Station Data
p=sns.lmplot(x='Entries', y='Exits', data=df2, fit_reg=False,  scatter_kws={"marker": "D", "s": 50})
p.set_xlabels("Entries")
p.set_ylabels("Exits")
p.fig.suptitle('January 2017 Scatter Plot By Entries vs Exits \n Most Stations Have Little Traffic', weight= 'bold', fontsize=11) # can also get the figure from plt.gcf()


#Plot Hierarchal Clustering Heat Map to Group Similar Traffic Together
sns.set_context("paper", rc={"font.size":4,"axes.titlesize":4,"axes.labelsize":11})  

g=sns.clustermap(df2, cmap="bwr", figsize=(3, 75), standard_scale=1, method="average", yticklabels=1, col_cluster=False,
                cbar_kws={"label": "Standardized\nTraffic"})
g.ax_col_dendrogram.set_title(
        "Hierarchical  Clustering Heat Map \n January 2017 Turnstile Data\n To Group Stations By Foot Traffic \nCould Be used for New Development",
        weight= 'bold', fontsize=11)
g.ax_row_dendrogram.set_axis_on()
g.ax_heatmap.set(xlabel='Foot Traffic')
g.ax_heatmap.set(ylabel='Station')
