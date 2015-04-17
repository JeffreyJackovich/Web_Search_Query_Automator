from google import Search
import pandas as pd
from pandas import DataFrame

#Reads strings from the specified column, "usecols="  
df = pd.read_csv('query_results.csv', usecols=["Fruit"])

#The number after, "stop=" designates total urls to return 
stop = 2

#Indicates the column header to return urls   
urlcols = ["Link1", "Link2"]

#Calls the Search function for each 'row,' and compiles a list from returned urls 
df[urlcols] = df["Fruit"].apply(lambda fruit : pd.Series([url for url in search(fruit, stop=stop, pause=5.0)][:stop]))

#Returns urls to the indicated header rows in "usecols=" 
df.to_csv('query_results.csv', usecols=["Link1", "Link2"])
