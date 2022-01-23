import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

file_data = pd.read_csv('medium_data.csv')

data = file_data['claps'].tolist()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean_value = statistics.mean(dataset)
    return mean_value


def show_fig(mean_list):
    df = mean_list
    sample_mean = statistics.mean(df)

    fig = ff.create_distplot([df], ['claps'], show_hist=False)

    fig.add_trace(go.Scatter(x = [population_mean, population_mean], y = [0, 0.17], mode = 'lines', name = 'mean'))

    fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = 'lines', name = 'first_stdev_start'))
    fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = 'lines', name = 'first_stdev_end'))

    fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = 'lines', name = 'second_stdev_start'))
    fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = 'lines', name = 'second_stdev_end'))

    fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.17], mode = 'lines', name = 'third_stdev_start'))
    fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = 'lines', name = 'third_stdev_end'))

    fig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0, 0.17], mode = 'lines', name = 'sample_mean'))

    fig.show()

    if sample_mean > population_mean:
        print('Intervention successful')

    z_score_value = (sample_mean - population_mean) / (population_stdev)
    print('Z score value: ', str(z_score_value))

def setup():
    mean_list = []
    for i in (range(0, 100)):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

first_stdev_start, first_stdev_end = population_mean - population_stdev, population_mean + population_stdev
second_stdev_start, second_stdev_end = population_mean - (2 * population_stdev), population_mean + (2 * population_stdev)
third_stdev_start, third_stdev_end = population_mean - (3 * population_stdev), population_mean + (3 * population_stdev)

setup()
