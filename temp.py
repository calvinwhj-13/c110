import csv
import statistics
import random
import pandas as pd 
import plotly.figure_factory as ff 
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print('population mean : ', population_mean)
print('standard deveation of population : ', std_dev)

def random_set_of_mean(counter) :
    dataset = []

    for i in range (0, counter) :
        random_index = random.randint(0, len(data))
        value = data[random_index-1]
        dataset.append(value)
    mean = statistics.mean(dataset) 

    return mean 

#std_dev = statistics.stdev(dataset)
#print('mean of sample : ', mean)
#print('standard deviation of sample : ', std_dev)

def show_fig(meanlist) :
    df = meanlist
    mean = statistics.mean(df)
    print('mean of sampling distribution : ', mean)

    fig = ff.create_distplot([df], ['temp'], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = 'lines', name = 'mean'))
    fig.show() 

def standard_deviation() : 
    meanlist = [] 
    
    for i in range(0, 1000-1) :
        set_of_means = random_set_of_mean(100) 
        meanlist.append(set_of_means)
    std_dev = statistics.stdev(meanlist)
    print('standard deveation of sampling disribution : ', std_dev) 

standard_deviation() 

def setup() : 
    meanlist = [] 
    
    for i in range(0, 1000) :
        set_of_means = random_set_of_mean(100) 
        meanlist.append(set_of_means)
    
    show_fig(meanlist)

setup() 