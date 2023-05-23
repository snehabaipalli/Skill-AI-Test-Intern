from flask import Flask, request, jsonify
import pandas as pd

df=pd.read_csv('data.csv')

male_df=df[df['Gender']=='male']
grouped_df= male_df.groupby('City')['Population'].sum()
sorted_df=grouped_df.sort_values(ascending=False)
top=sorted_df.head(5)

app=Flask(__name__)

@app.route('/population/<city>', methods=['GET'])
def get_population(city):
    male_population=df[(df['City']==city) & (df['Gender']=='Male')]['Population'].sum()
    return jsonify({'City': city, 'male_population':int(male_population)})

if __name__=='__main__':
    app.run(debug=True)



