import pandas as pd
import datetime


def analyze(list):

    data_set = pd.DataFrame(list)

    data_count = data_set.groupby(
        data_set['date']).size().reset_index(name='count')

    return data_count.values.tolist()


def outliers(df, ft):
    Q1 = df[ft].quantile(0.25)
    Q3 = df[ft].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    ls = df.index[(df[ft] < lower_bound) | (df[ft] > upper_bound)]

    return ls


def remove(df, ls):
    ls = sorted(set(ls))
    df = df.drop(ls)
    return df


def analyze_sales(sales):
    data_set = pd.DataFrame(sales)

    index_list = []
    for feature in ['Amount']:
        index_list.extend(outliers(data_set, feature))

    data_set_cleaned = remove(data_set, index_list)

    data_set_cleaned['Date'] = data_set_cleaned['Date'].astype(
        'datetime64[ns]')
    data_sample = data_set_cleaned.resample('D', on='Date')['Amount'].sum()
    data_index = data_sample.index
    date_i = []
    date = []
    for x in data_index:
        date_i.append(str(x.date()))
    for (x, y) in zip(date_i, data_sample):
        if y != 0.0:
            date.append({'Date': x, 'Amount': y})

    new_sales = pd.DataFrame(data=date, columns=['Date', 'Amount'])
    return new_sales.values.tolist()
