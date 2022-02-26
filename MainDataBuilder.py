import pandas as pd


class MainDataBuilder:
    top_20_makes = ['vauxhall', 'triumph', 'peugeot', 'volvo', 'mazda', 'bmw', 'daewoo', 'jaguar land rover', 'renault',
                    'fiat', 'iveco', 'mercedes benz', 'proton', 'ford', 'volkswagen', 'nissan', 'hyundai', 'ldv',
                    'citroen', 'honda']
    top_colors = ['SILVER', 'BLUE', 'BLACK', 'RED', 'WHITE', 'GREY', 'GREEN']

    def build_main_data_frame(self, file):
        """keep main data
        only relevant columns
        only class 4
        only top 20 makes
        only top colors
        """
        df = pd.read_csv(file)
        main_makes = df[(df['clean_make'].isin(self.top_20_makes)) & (df['test_class_id'] == 4)]
        main_makes_colors = main_makes[main_makes['colour'].isin(self.top_colors)]
        return main_makes_colors

    def write_df_to_file(self, df, file_name):
        """ write the given df to the file"""
        df.to_csv(file_name, encoding='utf-8')
