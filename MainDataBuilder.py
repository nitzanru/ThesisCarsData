import pandas as pd


class MainDataBuilder:
    top_makes = ['ford', 'vauxhall', 'volkswagen', 'peugeot', 'renault', 'jaguar land rover', 'bmw', 'citroen',
                 'mercedes benz', 'fiat', 'toyota', 'nissan', 'honda', 'audi', 'volvo', 'mazda', 'hyundai',
                 'skoda', 'mitsubishi', 'kia', 'suzuki', 'seat', 'saab', 'mg', 'daewoo', 'alfa romeo', 'subaru',
                 'porsche', 'jeep', 'chevrolet', 'daihatsu', 'chrysler', 'isuzu']
    top_colors = ['SILVER', 'BLUE', 'BLACK', 'RED', 'WHITE', 'GREY', 'GREEN']

    def build_main_data_frame(self, file):
        """keep main data
        only relevant columns
        only class 4
        only top makes
        only top colors
        """
        # df = pd.read_csv(file)
        # main_makes_df = df[(df['clean_make'].isin(self.top_makes)) & (df['test_class_id'] == 4)]
        # for top_make in self.top_makes:
        #     # for model in main_makes_df[main_makes_df['clean_make']=='bmw']['clean_model'].drop_duplicates():
        #     counts = main_makes_df[main_makes_df['clean_make'] == top_make][
        #         'clean_model'].value_counts()  # each model and repeats
        #     main_makes_df.drop(main_makes_df[main_makes_df['clean_make'] == top_make]['clean_model'].isin(
        #         counts.index[counts < 10000]))  # remove lines with model that appears less than 10000 times
        #
        # # main_makes_colors = main_makes[main_makes['colour'].isin(self.top_colors)]
        # # drop rows with 'undefined' model
        # return self.drop_columns(main_makes_df)

        df = pd.read_csv(file)
        main_df = pd.DataFrame()
        # for top_make in self.top_makes:
        for top_make in self.top_makes:
            top_make_df = df[(df['clean_make'] == top_make) & (df['test_class_id'] == 4)]
            make_count = top_make_df['clean_make'].value_counts()[0]    # how many times the make repeats in data
            model_count_threshold = (make_count * 0.02).__ceil__()      # take models that appear at least 5%

            # n = top_make_df['model'].to_frame()
            # top_make_df = top_make_df[n.replace(n.apply(pd.Series.value_counts)).gt(model_count_threshold).all(1)]

            top_make_df = top_make_df[top_make_df.groupby("clean_model")["clean_model"].transform('size') > model_count_threshold]
            main_df = pd.concat([main_df, top_make_df])

            # n = main_df['model'].to_frame()
            # n = main_df[(main_df['clean make'] == top_make)]['model'].to_frame()
            # main_df = main_df[n.replace(n.apply(pd.Series.value_counts)).gt(100).all(1)]
            # for model in main_makes_df[main_makes_df['clean_make']=='bmw']['clean_model'].drop_duplicates():
            # counts = main_makes_df[main_makes_df['clean make'] == top_make]['model'].value_counts()   # each model and repeats
            # main_makes_df.drop(main_makes_df[main_makes_df['clean make'] == top_make]['model'].isin(counts.index[counts < 100]))          # remove lines with model that appears less than 10000 times

        # main_makes_colors = main_makes[main_makes['colour'].isin(self.top_colors)]
        # drop rows with 'undefined' model
        return self.drop_columns(main_df)

    def build_class_id_data_frame(self, file):
        """keep main data
        only class 4
        """
        df = pd.read_csv(file)
        return df[(df['test_class_id'] == 4)]

    def drop_columns(self, df):
        return df.drop(columns=['test_id', 'test_type', 'test_week_day', 'years_on_road'])

    def write_df_to_file(self, df, file_name):
        """ write the given df to the file"""
        df.to_csv(file_name, encoding='utf-8')
