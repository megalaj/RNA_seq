# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:20:11 2018
@author: megaraja
"""
import pandas as pd
#to read data as data frame
data = pd.read_table("C:/Workshop-Python/Day3/VL_vs_Ctrl_DE.txt")
# to read data ()
print(type(data))
# print(f.read())
print(data.head(5))
#print first 5 rows of the dataframe
print(data.shape)
#print total number of rows and column of the dataframe
p_f=data.loc[data ["padj"]<= 0.05]
# filter the data with padj value <= 0.05 in a new variable p_f
print(p_f.shape)
#print the number of rows and column 
data.loc[data ["padj"]<= 0.05]
#print the details of filtered data p_f
L2F=p_f.loc[(-2 <= p_f["log2FoldChange"]) & (p_f["log2FoldChange"] <=2)]
#filter data by setting the range for log2foldchange between -2 and +2
print(L2F.shape)

rawdf1=data[["log2FoldChange", "padj", "external_gene_name"]]
#Select the column with the strings for scatter plot
rawdf1
#to check for the column selected
rawdf1.plot.scatter("log2FoldChange", "padj")
#scatter plot was made with raw data against log2FoldChange on x axis and padj on y axis 

filtereddf1=L2F[["log2FoldChange", "padj", "external_gene_name"]]
filtereddf1.plot.scatter("log2FoldChange", "padj")
#scatter plot was made with filtered data L2F against log2FoldChange on x axis and padj on y axis

df=filtereddf1["external_gene_name"].astype(str)
#for print the gen names in filtereddf1 variable
for x in df:
    print (x)
