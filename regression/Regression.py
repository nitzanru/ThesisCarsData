import math
import os
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np
import seaborn as sn
from matplotlib import pyplot as plt


def correlations(data):
    # sn.histplot(x='milege_day', data=data)
    # plt.savefig('histogram.png', dpi=300, bbox_inches='tight')

    # columns of the dataset to check correlation
    values = ['log_mileage', 'cylinder_capacity', 'n_days_on_road', 'n_months_on_road', 'n_years_on_road']

    data['log_mileage'] = np.log2(data['test_mileage'])

    # Correlation Matrix formation
    corr_matrix = data.loc[:, values].corr()

    # Using heatmap to visualize the correlation matrix - build and save
    plt.figure(figsize=(16, 6))
    heatmap = sn.heatmap(corr_matrix, annot=True)
    heatmap.set_title('Log Mileage Correlation Heatmap', fontdict={'fontsize': 18}, pad=12)
    plt.savefig('log mileage heatmap.png', dpi=300, bbox_inches='tight')


def fit(data):
    data['log_mileage'] = np.log2(data['test_mileage'])

    # # convert to dummy values
    # data['colour'] = data['colour'].astype('category').cat.codes
    # data['clean_make'] = data['clean_make'].astype('category').cat.codes
    # data['clean_model'] = data['clean_model'].astype('category').cat.codes
    # data['fuel_type'] = data['fuel_type'].astype('category').cat.codes
    # data['postcode_area'] = data['postcode_area'].astype('category').cat.codes

    # split to predictors and dv
    predictors_cols = ['log_mileage']
    # predictors_cols = ['test_mileage', 'cylinder_capacity', 'colour', 'clean_make', 'clean_model', 'fuel_type', 'postcode_area']
    X = data[predictors_cols]  # iv
    # y = data.n_months_on_road  # dv
    # y = data.n_days_on_road  # dv
    y = data.n_years_on_road  # dv

    # sn.scatterplot(x="test_mileage",
    #                y="y_on_road",
    #                data=data)
    # plt.savefig('plot.png', dpi=300, bbox_inches='tight')

    model = LinearRegression().fit(X, y)
    r_sq = model.score(X, y)
    print(f"r^2: {r_sq}")
    print(f"intercept: {model.intercept_}")
    print(f"slope: {model.coef_}")


def add_time_on_road(data):
    # add days, months and years on road
    data['n_months_on_road'] = (
            (pd.to_datetime(data['test_date']) - pd.to_datetime(data['first_use_date'])) / np.timedelta64(1, 'M'))
    data['n_months_on_road'] = data['n_months_on_road'].astype(int)

    data['n_years_on_road'] = (
            (pd.to_datetime(data['test_date']) - pd.to_datetime(data['first_use_date'])) / np.timedelta64(1, 'Y'))
    data['n_years_on_road'] = data['n_years_on_road'].astype(int)

    data['n_days_on_road'] = pd.to_datetime(data['test_date']).sub(pd.to_datetime(data['first_use_date']),
                                                                   axis=0).dt.days
    return data


def add_dummy_values(data):
    string_predictors = ['colour', 'clean_make', 'clean_model', 'fuel_type', 'postcode_area']
    return data


if __name__ == '__main__':
    # Loading the dataset
    data = pd.read_csv("C:/Users/nrukhamin/Desktop/BGU/thesis/cars_last_record/new_test/main_cars_clean.csv")
    # data = pd.read_csv("C:/Users/nrukhamin/Desktop/BGU/thesis/cars_last_record/mini/main_cars_clean_models.csv")
    # remove rows with empty values
    data = data.dropna(axis=0, how='any')

    data = add_time_on_road(data)
    # data = add_dummy_values(data)
    correlations(data)
    # fit(data)
