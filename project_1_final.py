import numpy as  np 
import pandas as pd
""" reading the data """
path='movie_dataset.csv'
file=pd.read_csv(path)

"""Renaming columns which have space """
file=file.rename(columns={'Revenue (Millions)':'Revenue_(Millions)'})

file=file.rename(columns={'Runtime (Minutes)':'Runtime_(Minutes)'})
""" Removing nAn  """
x = file["Revenue_(Millions)"].mean()

file["Revenue_(Millions)"].fillna(x, inplace = True)

x_1= file["Metascore"].mean()
file["Metascore"].fillna(x_1, inplace = True)

""" 1- What is the highest rated movie in the dataset?  """

#sorting by rate and reseting index.
file_sorted_by_rate=file.sort_values(by='Rating',ascending=False).reset_index()

#Printing the Title on the top it is the highest rating movie.
print(f"1-) The highest rating movie is: {file_sorted_by_rate['Title'][0]}")

"""2- What is the average revenue of all movies in the dataset? """

#We have already defined the mean of revenue by x
print(f'2-) The average revenue of all movies is :{x}')

"""3- What is the average revenue of movies from 2015 to 2017 in the dataset?"""
#Filtring the file 2015 and 2017
file_2015_2017=file[(file['Year']<=2017) & (file['Year']>=2015)]
#Taking the mean of the Revenue_(Millions)
mean_1=file_2015_2017["Revenue_(Millions)"].mean()
print(f"3-) The average revenue of movies from 2015 to 2017: {mean_1}")

""" 4- How many movies were released in the year 2016? """

file_2016=file[file['Year']==2016]
#The number of movies is the number of rows on the file_2016 that the reason why we use len()
num=len(file_2016['Title'])
print(f"4-) {num} movies were released in the year 2016")

""" 5- How many movies were directed by Christopher Nolan? """
#File_CN is the DataFrame where the DIrector is Christopher Nolan
file_CN=file[file['Director']=='Christopher Nolan']
#Like the previous code we use len  because the number of rows is the number of movie
num_2=len(file_CN['Title'])

print(f"5-) {num_2} movies were were directed by Christopher Nolan")

""" 6-How many movies in the dataset have a rating of at least 8.0?"""
#Filtring the file
file_rated_8=file[file['Rating']>=8]

num_3=len(file_rated_8["Title"])

print(f"6-) {num_3} movies have a rating of at least 8.0")
"""7-What is the median rating of movies directed by Christopher Nolan?"""
 #Using median method
num_4=file_CN['Rating'].median()

print(f"7-) {num_4} is the median rating of movies directed by Christopher Nolan")

"""8- Find the year with the highest average rating? """

#grouping the file in Year and applying mean in Rate column then reseting index so
#grouped is the file where there is list of Year in first column and mean of rate in the second column.
grouped=file.groupby("Year")['Rating'].mean().apply(np.array).reset_index()
#We create a dataFrame grouped_max where we store filtered grouped file by the max average rate 
grouped_max=grouped[grouped['Rating']==grouped['Rating'].max()]
 #We print the "Year" with max average ratE( 1 is the index)
print(f"8-) {grouped_max['Year'][1]} is the year with the highest average rating")


"""9- What is the percentage increase in number of movies made between 2006 and 2016?  """
file_2006=file[file['Year']==2006]
file_2016=file[file['Year']==2016]
#finding the percentage:
percentage=((len(file_2016['Title'])-len(file_2006['Title']))*100)/len(file_2006)

print(f"9-) {percentage} is the percentage increase in number of movies made between 2006 and 2016")

"""10- Find the most common actor in all the movies?"""
#First of all we store all actors in the variable Actors k
Actors=file['Actors']
#We create a list where we store the actors in this, list we have a list of string 
#of actors in each movies that are not separated.
Actors=list(Actors)
#We create a new list where using for loop for every elements in the Actors list 
#which are strings, we split them by ',' so now we got a list of list of actors
Actor_list=[i.split(",") for i in Actors]
#Here, we exctract every elements in the Actor_list that is to say in the list 
#And we use another for loop for extracting elements (actor's names) from the lists we got
#rstrip() and is used for cleaning if there is white space.
#The actors_list 2 is a list of of actor's name and we create a dataframe df from this list
#and describe() will show the actror's name which repeats the most "top"
Actor_list_2=[]
for j in Actor_list:
    for k in j:
        l=k.rstrip()
        Actor_list_2.append(l.strip())
df=pd.DataFrame(Actor_list_2)
ye=df.describe()
print(f"10-){ye}")
print(f"the most common actor in all the movies is the top in the description so it is:Mark Wahlberg ")


"""11-) How many unique genres are there in the dataset?"""
#We do the same thing like in question -10
genre=file['Genre']
genre=list(genre)
genre_list=[m.split(",") for m in genre]
genre_list_2=[]
for n in genre_list:
    for o in n:
        p=o.rstrip()
        genre_list_2.append(p.strip())
df_2=pd.DataFrame(genre_list_2)
#There are genres that repeat so we transfrom the genre_list_2 a list where stored 
#all genre. set cannot contain a repeat word so we use it to remove them.
genre_Unique=list(set(genre_list_2))
print(f"11-) There are: {len(genre_Unique)} genres ")