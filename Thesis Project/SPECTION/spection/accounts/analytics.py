import pandas as pd


def analyze(list):

    data_set = pd.DataFrame(list)

    data_count = data_set.groupby(
        data_set['date']).size().reset_index(name='count')

    return data_count.values.tolist()
