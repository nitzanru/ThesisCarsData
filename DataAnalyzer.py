import matplotlib.pyplot as plt
import pandas as pd
import squarify as squarify

class DataAnalyzer:

    def plot_bars(self, file):
        """plot a bar graph of the clean makes"""
        df = pd.read_csv(file)
        df.clean_make.value_counts().plot(kind='bar')
        plt.show()


        # one=df.loc[(df['clean_make'] == 'vauxhall') & (df['clean_model'] == 'cavalier')]
        # two=df.loc[(df['clean_make'] == 'ford') & (df['clean_model'] == 'fiesta')]
        # three=df.loc[(df['clean_make'] == 'renault') & (df['clean_model'] == 'master')]
        # one =one.sort_values('vehicle_id')
        # two =two.sort_values('vehicle_id')
        # three =three.sort_values('vehicle_id')
        # one =three

    def plot_tree_map(self, file):
        """plot a tree map graph of the clean makes"""
        df = pd.read_csv(file)
        series = df.loc[:, "clean_make"].value_counts()
        labels = df.loc[:, "clean_make"].drop_duplicates().values
        dict = {'clean_make': labels, 'sum': series.values}
        data = pd.DataFrame(dict)
        squarify.plot(label=data['clean_make'], sizes =data['sum'], alpha=.8)
        plt.show()

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


