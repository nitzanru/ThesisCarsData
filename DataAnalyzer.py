import matplotlib.pyplot as plt
import pandas as pd
import squarify as squarify


class DataAnalyzer:

    def plot_bars(self, df):
        """plot a bar graph of the clean makes"""
        # df["first_use_date.year"].value_counts().plot(kind='bar')
        # plt.show()

        df["test_date.year"].value_counts().plot(kind='bar')
        plt.show()

    def plot_first_use_year_tree_map(self, df):
        """plot a tree map graph of the first use year"""
        series = df.loc[:, "first_use_date.year"].value_counts()
        labels = series.axes[0]
        dict = {'first_use_date.year': labels, 'sum': series.values}
        data = pd.DataFrame(dict)
        squarify.plot(label=data['first_use_date.year'], sizes=data['sum'], alpha=.8)
        plt.show()

    def plot_make_tree_map(self, df):
        """plot a tree map graph of the clean makes"""
        series = df.loc[:, "clean_make"].value_counts()
        labels = series.axes[0]
        dict = {'clean_make': labels, 'sum': series.values}
        data = pd.DataFrame(dict)
        squarify.plot(label=data['clean_make'], sizes=data['sum'], alpha=.8)
        plt.show()

    def describeDataFrame(self, df):
        """write some statistics description of the given df"""
        print("summary:")
        df.info(verbose=True)
        df.head()
        print('group by clean make')
        print(df.groupby('clean_make').count())

    def describe(self, file):
        """write some statistics descirption of the given file"""
        df = pd.read_csv(file)

        # df.make.value_counts().plot(kind='bar')
        plt.show()
        # df.colour.value_counts().plot(kind='bar')
        # plt.show()
        #
        # # a = df.groupby('make').count()
        # # a.plot.bar(x='make', y='val', rot=0)

        print('describe clean make')
        print(df.loc[:, "clean_make"].describe())
        print('describe clean model')
        print(df.loc[:, "clean_model"].describe())
        print('describe colors')
        print(df.loc[:, "colour"].describe())

        print('group by make')
        print(df.groupby('make').count())
        print('group by clean make')
        print(df.groupby('clean_make').count())
        print('group by model')
        print(df.groupby('model').count())
        print('group by clean model')
        print(df.groupby('clean_model').count())
        print('group by colors')
        print(df.groupby('colour').count())
        # print("summary:")
        # df.info(verbose=True)
        # df.head()

        # data = sns.load_dataset(file)
        # data.head()
        # # makes = data.groupby('make').sum()
        # a = data.groupby('make').sum().index.get_level_values(0).tolist()
        # d = data.groupby('make').sum().reset_index().survived.values.tolist()

        # series.plot(kind='bar', color='r', alpha=0.5)
        # counts =
        # makes_names = df.groupby('make')
        # print(makes_names)
        # df.make.value_counts()
        # squarify.plot(sizes=d, label=a, alpha=.8)
        # plt.axis('off')
