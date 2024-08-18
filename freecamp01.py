import pandas as pd

data = pd.read_csv("E:/python/adult_data.csv")
print(data.head())


# How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

race_count = data['race'].value_counts()
print(race_count)

# What is the average age of men?

avg_age = round(data[data['sex'] == 'Male' ]['age'].mean()) 
print("The average age of men is: " , avg_age)

# What is the percentage of people who have a Bachelor's degree?

percentage = round((data[data['education'] == 'Bachelors'].shape[0] / data.shape[0]) * 100 , 1)
print("The percentage is of people who have a Bachelor's degree is: ", percentage)

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

data['income'] = data['income'].str.strip().str.lower()
adv_edu = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

adv_edu_sal = adv_edu[adv_edu['income'] == '>50k']

percentage_adv = round((adv_edu_sal.shape[0] / adv_edu.shape[0]) * 100, 1)
print("The percentage of people with advance education is: ",percentage_adv)

# What percentage of people without advanced education make more than 50K?

Advance_Edu = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
# print(Advance_Edu)
Advance_Edu_Sal = Advance_Edu[Advance_Edu['income'] == '>50k']
percentage_Advance = round((Advance_Edu_Sal.shape[0] / Advance_Edu.shape[0]) * 100 , 1)
print("The percentage of people with advance education is: ",  percentage_Advance)

# What is the minimum number of hours a person works per week?

min_hours = data['hours-per-week'].min()
print(min_hours) 

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

peoples_min_hours = data[data['hours-per-week'] == min_hours]
# print(peoples_min_hours)

sal_peoples_min = peoples_min_hours[peoples_min_hours['income'] == '>50k']
percentage_min = round((sal_peoples_min.shape[0] / peoples_min_hours.shape[0]) * 100 , 1)
print("Percentage of the people who work the minimum number of hours per week have a salary of more than 50K is: ", percentage_min)

# What country has the highest percentage of people that earn >50K and what is that percentage?


data['native-country'] = data['native-country'].str.strip()
data['income'] = data['income'].str.strip()

country_inc = data.groupby('native-country').apply( 
            lambda x: (x['income'] == '>50k').sum() / len(x) * 100).reset_index(name='percentage')
print(country_inc)


# Identify the most popular occupation for those who earn >50K in India.
data['native-country'] = data['native-country'].str.strip()
data['income'] = data['income'].str.strip()


# Cleaning
data['income'] = data['income'].replace( {
    '<=50k.' : '<=50k',
    '>50k.' : '>50k'
})


popular = data[(data['native-country'] == 'India') & (data['income'] == '>50k')]

if popular.empty:
    print("No data Found")
    most_pop_occu = None

else:
    most_pop_occu = popular['occupation'].value_counts().idxmax()
    print(f"Most popular occupation for those earning >50K in India: {most_pop_occu}")




