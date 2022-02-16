import main
from CarsDataCleaner import CarsDataCleaner
from CarsDataCleanerHelper import CarsDataCleanerHelper
from CarsMakesCleaner import CarsMakesCleaner
from CarsModelsCleaner import CarsModelsCleaner
from DataAnalyzer import DataAnalyzer
from WriteColumnWithAppearancesToFile import WriteColumnWithAppearancesToFile
from BuildMakeModelMap import BuildMakeModelMap

prefix = 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\'

if __name__ == '__main__':
    main.clean()

    #############   mini    ##############
    # CarsMakesCleaner(prefix + 'mini\\cars_last_record_mini.csv', prefix + 'mini\\mini_makes_with_appearances.csv', prefix + 'mini\\mini_clean_makes.csv', False)
    # CarsModelsCleaner(prefix + 'mini\\mini_clean_makes.csv', prefix + 'mini\\mini_clean_models.csv', prefix + 'mini\\mini_main_make_models.csv', False)

    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv')
    # helper.clean()

    # write_makers = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_sorted_makers.csv', 8)
    # write_colors = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_makers.csv', 8)
    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv')
    # helper.clean()

    # build clean make and clean model ()
    #     cleaner = CarsDataCleaner(prefix + 'cars_last_record.csv', prefix + 'cars_last_record_clean_make_model_1.csv', prefix + 'makers1.csv')
    #     cleaner.clean()

    # print('analyzing original data:')
    # analyzer = DataAnalyzer(prefix + 'mini\\mini_clean_makes.csv')
    # #CarsMakesCleaner(prefix + 'cars_last_record.csv', prefix + 'test\\makes_with_appearances_only_clean.csv', prefix + 'test\\cars_clean_makes_only_clean.csv', False)
    # CarsModelsCleaner(prefix + 'test\\cars_clean_makes_only_clean.csv', prefix + 'test\\cars_clean_models_only_clean.csv', prefix + 'test\\cars_main_make_models_only_clean.csv', False)
    # print('analyzing clean data:')
    # analyzer = DataAnalyzer(prefix + 'test\\cars_clean_models_only_clean.csv')

    # cleaner = CarsDataCleaner(prefix + 'cars_last_record_test_class_5.csv', prefix + 'cars_last_record_clean_make_model_1.csv',
    #                           prefix + 'makers1.csv')
    # cleaner.clean()
    # print('done cleaning')
    # make_model_map_builder = BuildMakeModelMap('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\mini.csv', 9, 10)
    # make_model_map_builder.build_main_models(10)
    # make_model_map_builder.write_to_file('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\make_model_pairs.csv')

def clean():
    #print('analyzing original data:')
    # analyzer = DataAnalyzer()
    # analyzer.plot_tree_map(prefix + 'mini\\cars_last_record_mini.csv')
    #analyzer = DataAnalyzer(prefix + 'new_test\\cars_clean_models.csv')
    # CarsMakesCleaner(prefix + 'cars_last_record.csv', prefix + 'new_test\\makes_with_appearances.csv',
    #                  prefix + 'new_test\\cars_clean_makes.csv', True)
    # print('makes clean')
    # CarsModelsCleaner(prefix + 'new_test\\cars_clean_makes.csv',
    #                   prefix + 'new_test\\cars_clean_models.csv',
    #                   prefix + 'new_test\\cars_main_make_models.csv', True)
    # analyzer = DataAnalyzer(prefix + 'new_test\\cars_clean_models.csv')
    analyzer = DataAnalyzer()
    analyzer.plot_bars(prefix + 'new_test\\cars_clean_models.csv')
    #print('analyzing clean data:')
    #analyzer = DataAnalyzer(prefix + 'new_test\\cars_clean_models_only_clean.csv')
