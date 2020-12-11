import tkinter as tk
from tkinter import *
import pymongo
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import os

df =pd.read_csv('tmdb_movies_data.csv')

# importing module 
from pymongo import MongoClient 

# creation of MongoClient 
#client=MongoClient() 

# Connect with the portnumber and host 
client = MongoClient("localhost", 27017) 

# Access database 
mydatabase = client.Movie3 

# Access collection of the database 
mycollection=mydatabase["MovieCollection3"]

  

   
#Function to search the movie details by giving the title     
def Search():
    
    root2=tk.Tk()
    root2.geometry('800x800')
    root2.configure(background='yellow green')
    root2.title('Search')
    
    
    
    def search():
        title=Title.get()
        d=mycollection.find({"title":title}).limit(1000)
        

        
        eula.delete(0, 'end')#to clear listbox
        for i in d:
            eula.insert(END,str(i))#to insert text into listbox    
    def search1():
        director=Director.get()
        f=mycollection.find({"director":director}).limit(100)
        eula.delete(0, 'end')#to clear listbox
        for i in f:
            eula.insert(END,str(i))#to insert text into listbox    
    def search2():
        genres=Genres.get()
        f=mycollection.find({"genres":genres}).limit(100)
        eula.delete(0, 'end')#to clear listbox
        for i in f:
            eula.insert(END,str(i))#to insert text into listbox    
            
     

    q=tk.StringVar(root2)
    q.set('')
    f1=tk.Frame(root2,bg='salmon')
    at=tk.Label(f1,text="Title",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='left')
    
    Title=tk.Entry(f1,textvariable=q)
    Title.pack(padx=5,pady=10,side='left')
    
    btu=tk.Button(f1,text="Search",fg='black',font="Helvetica 15 bold",command=search,width=8)
    btu.pack(padx=5,pady=10,side='left')
    f1.pack()
    r=tk.StringVar(root2)
    r.set('')
    f2=tk.Frame(root2,bg='salmon')
    at=tk.Label(f2,text="Director",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='left')
    
    Director=tk.Entry(f2,textvariable=r)
    Director.pack(padx=5,pady=10,side='left')
    btu1=tk.Button(f2,text="Search",fg='black',font="Helvetica 15 bold",command=search1,width=8)
    btu1.pack(padx=5,pady=10,side='left')
    f2.pack()

    s=tk.StringVar(root2)
    s.set('')
    f3=tk.Frame(root2,bg='salmon')
    at=tk.Label(f3,text="Genre",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='left')
    
    Genres=tk.Entry(f3,textvariable=s)
    Genres.pack(padx=5,pady=10,side='left')
    
    btu2=tk.Button(f3,text="Search",fg='black',font="Helvetica 15 bold",command=search2,width=8)
    btu2.pack(padx=5,pady=10,side='left')
    f3.pack()
    xscrollbar = Scrollbar(root2, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    # Vertical (y) Scroll Bar
    yscrollbar = Scrollbar(root2,orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)

    # Text Widget
    eula = Listbox(root2, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,height=90)
    eula.pack(fill=X)
        

    # Configure the scrollbars
    xscrollbar.config(command=eula.xview)
    yscrollbar.config(command=eula.yview)
    
    
    
    
    
    root2.mainloop()
    
def Delete():
    root3=tk.Tk()
    root3.geometry('1000x600')
    root3.configure(background='green yellow')
    root3.title('Delete')
    def delete():
        title=Title.get()
        id=Id.get()
        
        g=mycollection.delete_many({"title":title,"id":id})
    q=tk.StringVar(root3)
    q.set('')
    u=tk.IntVar(root3)
    f1=tk.Frame(root3,bg='salmon')
    at=tk.Label(f1,text="Title",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='left')
    
    Title=tk.Entry(f1,textvariable=q)
    Title.pack(padx=5,pady=10,side='left')
    at1=tk.Label(f1,text="ID",font='Helvetica 18 bold',width=7,height=1)
    at1.pack(padx=5,pady=10,side='left')
    Id=tk.Entry(f1,textvariable=u)
    Id.pack(padx=5,pady=10,side='left')
    btu=tk.Button(f1,text="Delete",fg='black',font="Helvetica 15 bold",command=delete,width=8)
    btu.pack(padx=5,pady=10,side='left')
    f1.pack()
    root3.mainloop()

def ttmg():
    root4=tk.Tk()
    root4.geometry('1100x800')
    root4.configure(background='green yellow')
    root4.title('Search')
    
    
    
    def search():
        genres=Genres.get()
        d=mycollection.find({"genres":genres}).sort([("popularity",pymongo.DESCENDING)]).limit(10)

        eula.delete(0, 'end')#to clear listbox
        for i in d:
            eula.insert(END,str(i))#to insert text into listbox    
            
  
    q=tk.StringVar(root4)
    q.set('')
    f1=tk.Frame(root4,bg='salmon')
    at=tk.Label(f1,text="Category of the movie",font='Helvetica 18 bold',width=25,height=1)
    at.pack(padx=5,pady=10,side='left')
    
    Genres=tk.Entry(f1,textvariable=q)
    Genres.pack(padx=5,pady=10,side='left')
    btu=tk.Button(f1,text="Search",fg='black',font="Helvetica 15 bold",command=search,width=8)
    btu.pack(padx=5,pady=10,side='left')
    f1.pack()
    xscrollbar = Scrollbar(root4, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    # Vertical (y) Scroll Bar
    yscrollbar = Scrollbar(root4,orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)

    # Text Widget
    eula = Listbox(root4, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,height=90)
    eula.pack(fill=X)
        

    # Configure the scrollbars
    xscrollbar.config(command=eula.xview)
    yscrollbar.config(command=eula.yview)
    
    
    
    
    
    root4.mainloop()

def ottm():
    root5=tk.Tk()
    root5.geometry('800x800')
    root5.configure(background='green yellow')
    root5.title('Search')
    xscrollbar = Scrollbar(root5, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    # Vertical (y) Scroll Bar
    yscrollbar = Scrollbar(root5,orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)

    # Text Widget
    eula = Listbox(root5, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,height=90)
    eula.pack(fill=X)
        

    # Configure the scrollbars
    xscrollbar.config(command=eula.xview)
    yscrollbar.config(command=eula.yview)
    d=mycollection.find().sort([("popularity",pymongo.DESCENDING)]).limit(10)
    for i in d:
        eula.insert(END,str(i))#to insert text into listbox




def Update():
    def Upd():
        
        
        revenue=Revenue.get()
        #original_language=Original_language.get()
        popularity=Popularity.get()
        title=Title.get()
        
        dic={"$set":{"revenue" :revenue,"popularity":popularity}}
        x = mycollection.update_many({"title":title},dic)
       
    
    root1=tk.Tk()
    root1.geometry('800x600')
    root1.configure(background='cyan')
    
    
    s=tk.StringVar(root1)
    s.set('')
    f3=tk.Frame(root1,bg='cyan')
    Revenue=tk.Entry(f3,textvariable=s)
    Revenue.pack(padx=5,pady=10,side='right')
    at=tk.Label(f3,text="Enter revenue generated",font='Helvetica 18 bold',width=25,height=1)
    at.pack(padx=5,pady=10,side='right')
    f3.pack()
    
    u=tk.IntVar(root1)
    u.set('')
    f5=tk.Frame(root1,bg='cyan')
    Popularity=tk.Entry(f5,textvariable=u)
    Popularity.pack(padx=5,pady=10,side='right')
    at=tk.Label(f5,text="Enter Popularity",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f5.pack()
    v=tk.StringVar(root1)
    v.set('')
    f6=tk.Frame(root1,bg='cyan')
    Title=tk.Entry(f6,textvariable=v)
    Title.pack(padx=5,pady=10,side='right')
    at=tk.Label(f6,text="Enter Title of movie which has to be updated",font='Helvetica 16 bold',width=36,height=1)
    at.pack(padx=5,pady=10,side='right')
    f6.pack()
    w=tk.IntVar(root1)
    w.set('')
    f32=tk.Frame(root1,bg='cyan')
    but=tk.Button(f32,text="UPDATE",command=Upd,font="Helvetica 18 bold",width=12,height=1)
    but.pack(side='right',padx=5,pady=10)
    f33=tk.Frame(root1,bg='cyan')
    but=tk.Button(f33,text="BACK",command=root1.destroy,font="Helvetica 18 bold",width=12,height=1)
    but.pack(side='right',padx=5,pady=10)
    f32.pack()
    f33.pack()
    root1.mainloop()
    

def Insert():
    def Ins():
        budget=Budget.get()
        genres=Genres.get()
        id=Id.get()
        director=Director.get()
        release_year=Release_year.get()
        popularity=Popularity.get()
        runtime=Runtime.get()
        title=Title.get()
        
        dic={ "budget":budget, "genres" : genres, "id" : id, "director" : director, "release_year" : release_year, "popularity" : popularity, "Runtime" : runtime, "title": title }
        x = mycollection.insert_one(dic)

    root1=tk.Tk()
    root1.geometry('800x600')
    root1.configure(background='cyan')
    q=tk.StringVar(root1)
    q.set('')
    f1=tk.Frame(root1,bg='cyan')
    Budget=tk.Entry(f1,textvariable=q)
    Budget.pack(padx=5,pady=10,side='right')
    at=tk.Label(f1,text="Budget",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f1.pack()
    r=tk.IntVar(root1)
    r.set('')
    f2=tk.Frame(root1,bg='cyan')
    Genres=tk.Entry(f2,textvariable=r)
    Genres.pack(padx=5,pady=10,side='right')
    at=tk.Label(f2,text="Genres",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f2.pack()
    s=tk.StringVar(root1)
    s.set('')
    f3=tk.Frame(root1,bg='cyan')
    Id=tk.Entry(f3,textvariable=s)
    Id.pack(padx=5,pady=10,side='right')
    at=tk.Label(f3,text="Id",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f3.pack()
    t=tk.StringVar(root1)
    t.set('')
    f4=tk.Frame(root1,bg='cyan')
    Director=tk.Entry(f4,textvariable=t)
    Director.pack(padx=5,pady=10,side='right')
    at=tk.Label(f4,text="Director",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f4.pack()
    u=tk.IntVar(root1)
    u.set('')
    f5=tk.Frame(root1,bg='cyan')
    Release_year=tk.Entry(f5,textvariable=u)
    Release_year.pack(padx=5,pady=10,side='right')
    at=tk.Label(f5,text="Release_Year",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f5.pack()
    v=tk.IntVar(root1)
    v.set('')
    f6=tk.Frame(root1,bg='cyan')
    Popularity=tk.Entry(f6,textvariable=v)
    Popularity.pack(padx=5,pady=10,side='right')
    at=tk.Label(f6,text="Popularity",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f6.pack()
    w=tk.IntVar(root1)
    w.set('')
    f7=tk.Frame(root1,bg='cyan')
    Runtime=tk.Entry(f7,textvariable=w)
    Runtime.pack(padx=5,pady=10,side='right')
    at=tk.Label(f7,text="Runtime",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f7.pack()
    x=tk.StringVar(root1)
    x.set('')
    f8=tk.Frame(root1,bg='cyan')
    Title=tk.Entry(f8,textvariable=x)
    Title.pack(padx=5,pady=10,side='right')
    at=tk.Label(f8,text="Title",font='Helvetica 18 bold',width=14,height=1)
    at.pack(padx=5,pady=10,side='right')
    f8.pack()
    f32=tk.Frame(root1,bg='cyan')
    but=tk.Button(f32,text="Insert",command=Ins,font="Helvetica 18 bold",width=10,height=1)
    but.pack(side='right',padx=5,pady=10)
    f33=tk.Frame(root1,bg='cyan')
    but=tk.Button(f33,text="Back",command=root1.destroy,font="Helvetica 18 bold",width=10,height=1)
    but.pack(side='right',padx=5,pady=10)
    f32.pack()
    f33.pack()
    root1.mainloop()
#data cleaning
db=pd.read_csv('tmdb_movies_data.csv')
#removing duplicate rows
#def datacleaning():
    #db.drop_duplicates(inplace = True)
    #print("Afetr Removing Duplicate Values (Rows,Columns) : ",db.shape)
    #removing unwanted columns
    #db.drop(['budget_adj','revenue_adj','overview','imdb_id','homepage','tagline'],axis =1,inplace = True)
def plot():
       
    

    movies_per_year= db['release_year'].value_counts().sort_index()
    plt.plot(movies_per_year,color='crimson')
    plt.title('Movie production trend over the years')
    plt.xlabel('Year')
    plt.ylabel('Number of movies released')
    plt.show()
    
def plot2():
    
    sorted_revenue = db['revenue'].sort_values(ascending=False)[:20]

    high_grossers=pd.DataFrame()
    titles=[]
    revenues=[]
    for i in sorted_revenue.index:
        titles.append(db.loc[i,'original_title'])
        revenues.append(sorted_revenue.loc[i])
    high_grossers['Titles']=titles
    high_grossers['Revenues']=revenues
    high_grossers.set_index('Titles',inplace=True)
    high_grossers.plot(kind ='bar',figsize=(5,5),fontsize=6,color='purple')
    plt.title('Top 20 highest grossing movies (1960 - 2015) ')
    plt.ylabel('Revenue in billions ($)')
    plt.show()
    
def plot3():
    sorted_budget = db['budget'].sort_values(ascending=False)[:20]
    high_budget=pd.DataFrame()
    titles_exp=[]
    budgets=[]
    for i in sorted_budget.index:
        titles_exp.append(db.loc[i,'original_title'])
        budgets.append(sorted_budget.loc[i])
    high_budget['Titles']=titles_exp
    high_budget['Budgets']=budgets
    high_budget.set_index('Titles',inplace=True)
    high_budget.plot(kind ='bar',figsize=(8,8),fontsize=6,color='crimson')
    plt.title('Top 20 most expensive movies (1960 - 2015) ')
    plt.ylabel('Budget in 100\'s of million ($)')
    plt.show()
    
def plot4():
    db['Profit']=db['revenue']-db['budget']
    db.plot(x='vote_average',y='Profit',kind='scatter',figsize=(8,8),color='greenyellow')
    plt.ylabel('Profit in billion ($)')
    plt.xlabel('Rating')
    plt.title('Rating vs Profit')
    plt.show()
def plot5():
    
    def count_genre(x):
        #concatenate all the rows of the genrs.
        data_plot = db[x].str.cat(sep = '|')
        data = pd.Series(data_plot.split('|'))
        #conts each of the genre and return.
        info = data.value_counts(ascending=False)
        return info

    #call the function for counting the movies of each genre.
    total_genre_movies = count_genre('genres')
#plot a 'barh' plot using plot function for 'genre vs number of movies'.
    total_genre_movies.plot(kind= 'barh',figsize =(8,8),fontsize=6,colormap='tab20c')

#setup the title and the labels of the plot.
    plt.title("Genre With Highest Release",fontsize=15)
    plt.xlabel('Number Of Movies',fontsize=13)
    plt.ylabel("Genres",fontsize= 13)
    plt.show()

def plot6():
    
    def count_genre(x):
        #concatenate all the rows of the genrs.
        data_plot = db[x].str.cat(sep = '|')
        data = pd.Series(data_plot.split('|'))
        #conts each of the genre and return.
        info = data.value_counts(ascending=False)
        return info
    i = 0
    genre_count = []
    total_genre_movies = count_genre('genres')
    for genre in total_genre_movies.index:
        genre_count.append([genre, total_genre_movies[i]])
        i = i+1
    
    plt.rc('font', weight='bold')
    f, ax = plt.subplots(figsize=(5, 5))
    genre_count.sort(key = lambda x:x[1], reverse = True)
    labels, sizes = zip(*genre_count)
    labels_selected = [n if v > sum(sizes) * 0.01 else '' for n, v in genre_count]
    ax.pie(sizes, labels=labels_selected,
       autopct = lambda x:'{:2.0f}%'.format(x) if x > 1 else '',
       shadow=False, startangle=0)
    ax.axis('equal')
    plt.tight_layout()
    plt.show()
def plot7():
    def count_genre(x):
        #concatenate all the rows of the genrs.
        data_plot = db[x].str.cat(sep = '|')
        data = pd.Series(data_plot.split('|'))
        #conts each of the genre and return.
        info = data.value_counts(ascending=False)
        return info
    production_companies = count_genre('production_companies')

#plot he barh plot.
    production_companies.iloc[:20].plot(kind='barh',figsize=(8,8),fontsize=8,color='coral')
    plt.title("Production Companies Vs Number Of Movies",fontsize=15)
    plt.xlabel('Number Of Movies',fontsize=14)
    sns.set_style("whitegrid")

    plt.show()
    
def plot8():
    def count_genre(x):
        #concatenate all the rows of the genrs.
        data_plot = db[x].str.cat(sep = '|')
        data = pd.Series(data_plot.split('|'))
        #conts each of the genre and return.
        info = data.value_counts(ascending=False)
        return info
    
    count_director_movies = count_genre('director')

#plot a barh graph
    count_director_movies.iloc[:20].plot(kind='bar',figsize=(8,8),fontsize=8)

#setup the title and the labels 
    plt.title("Director Vs Number Of Movies",fontsize=15)
    plt.xticks(rotation=70)
    plt.ylabel("Number Of Movies",fontsize= 13)
    sns.set_style("whitegrid")
    plt.show()
root0=tk.Tk()
root0.title('Movie Data Analysis')
root0.geometry('1500x1500')
root0.configure(background='salmon')
bt=tk.Label(root0,text="Movie Data Analysis",font="Times 24 bold italic",width='700',fg='gray8',bg='green yellow')
bt.pack()
btu=tk.Button(root0,text="INSERT",fg='black',font="Times 24 bold",command=Insert,width=12)
btu.pack(padx=5,pady=10)

btu1=tk.Button(root0,text="DELETE",fg='black',font="Times 24 bold",command=Delete,width=12)
btu1.pack(padx=5,pady=10)

btu1=tk.Button(root0,text="UPDATE",fg='black',font="Times 24 bold",command=Update,width=12)
btu1.pack(padx=5,pady=10)
btu2=tk.Button(root0,text="SEARCH",fg='black',font="Times 24 bold",command=Search,width=12)
btu2.pack(padx=5,pady=10)
btu3=tk.Button(root0,text="Top 10 movies based on genres",fg='black',font="Helvetica 24 bold",command=ttmg,width=40)
btu3.pack(padx=5,pady=10)
btu3=tk.Button(root0,text="Overall Top 10 movies",fg='black',font="Helvetica 24 bold",command=ottm,width=40)
btu3.pack(padx=5,pady=10)

btu5=tk.Button(root0,text="Year-wise Movie Graph",fg='black',font="Helvetica 10 bold",command=plot,width=18)
btu5.pack(padx=5,pady=10,side=tk.LEFT)

btu6=tk.Button(root0,text="Highest Grossing Movies Graph",fg='black',font="Helvetica 10 bold",command=plot2,width=28)
btu6.pack(padx=5, pady=10,side=tk.LEFT)

btu7=tk.Button(root0,text="Top 20 expensive movies Graph",fg='black',font="Helvetica 10 bold",command=plot3,width=28)
btu7.pack(padx=5, pady=10,side=tk.LEFT)

btu8=tk.Button(root0,text="Rating vs profit",fg='black',font="Helvetica 10 bold",command=plot4,width=24)
btu8.pack(padx=5, pady=10,side=tk.LEFT)

btu9=tk.Button(root0,text="Genre with highest release",fg='black',font="Helvetica 8 bold",command=plot5,width=24)
btu9.pack(padx=5, pady=10,side=tk.LEFT)

btu10=tk.Button(root0,text="Pie graph",fg='black',font="Helvetica 8 bold",command=plot6,width=10)
btu10.pack(padx=5, pady=10,side=tk.LEFT)

btu11=tk.Button(root0,text="Production companies vs No of movies",fg='black',font="Helvetica 8 bold",command=plot7,width=30)
btu11.pack(padx=5, pady=10,side=tk.LEFT)
btu11=tk.Button(root0,text="DirectorVSMovies",fg='black',font="Helvetica 8 bold",command=plot8,width=30)
btu11.pack(padx=5, pady=10,side=tk.LEFT)

root0.mainloop()
