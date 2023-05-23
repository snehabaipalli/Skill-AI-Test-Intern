from flask import Flask, request, jsonify ## importing required libraries
import pandas as pd

df=pd.read_csv('data.csv') #loading the dataset

male_df=df[df['Gender']=='male'] # retrieving the male population
grouped_df= male_df.groupby('City')['Population'].sum() # grouping order by city
sorted_df=grouped_df.sort_values(ascending=False) # sorting the population in descending order
top=sorted_df.head(5) # getting the top 5 cities with highest male population
print(top)

app=Flask(__name__) # initilizing flask application

@app.route('/population/<city>', methods=['GET']) # routing to fetch the population data by passing city as parameter
def get_population(city):
    male_population=df[(df['City']==city) & (df['Gender']=='Male')]['Population'].sum() #fetching the male population of specific city
    return jsonify({'City': city, 'male_population':int(male_population)}) # sending to api to show the results

if __name__=='__main__':
    app.run(debug=True)



