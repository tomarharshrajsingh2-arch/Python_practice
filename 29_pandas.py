import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'amit','sneha','shivam'],    
    'Age': [25, 30, 35, 28, 32],
    'City': ['Chicago', 'Los Angeles', 'Chicago', 'Boston', 'Chicago'],
    "marks": [85, 90, 95, 88, 92]
}
df = pd.DataFrame(data)


print(df)
# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())

# #select columns

# print("df['Name']: \n" ,df['Name'])

# print(df[['Name','marks']])


# print(df[df['marks']>= 92])



# city_avg = df.groupby('City')['marks'].mean()
# print(city_avg)

print("Reading the CSV")
df2 = pd.read_csv('students.csv')
print("cleaning the csv")
df2['Name'] = df2['Name'].str.strip()
print("Writing the CSV")
df2.to_csv('clean_output.csv', index=False)

