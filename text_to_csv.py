import pandas as pd

#read text file and create dataframealg
df = pd.read_csv("C:/Users/Admin/Downloads/Iiwari/Data.txt", delimiter=":',",header=None)

df = df[0].str.extract(r"'ts':\s*'(?P<ts>.*?)',\s*'node':\s*'(?P<node>.*?)',\s*'x':\s*(?P<x>\d+),\s*'y':\s*(?P<y>\d+),\s*'z':\s*(?P<z>\d+),\s*'q':\s*(?P<q>\d+),\s*'alg':\s*(?P<alg>\d+)")

#add heading columns
df.columns = ['ts', 'node', 'x', 'y', 'z', 'q', 'alg']

#store dataframe into csv file
df.to_csv('Data.csv',index=None)