from CarsDataCleaner import CarsDataCleaner
from CarsDataCleanerHelper import CarsDataCleanerHelper
from CarsMakesCleaner import CarsMakesCleaner
from CarsModelsCleaner import CarsModelsCleaner
from WriteColumnWithAppearancesToFile import WriteColumnWithAppearancesToFile
from BuildMakeModelMap import BuildMakeModelMap

if __name__ == '__main__':
    prefix = 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\'

    #############   mini    ##############
    #CarsMakesCleaner(prefix + 'cars_last_record_mini.csv', prefix + 'test\\mini_makes_with_appearances.csv', prefix + 'test\\mini_clean_makes.csv')
    #CarsModelsCleaner(prefix + 'mini\\mini_clean_makes.csv', prefix + 'mini\\mini_clean_models.csv', prefix + 'mini\\mini_main_make_models.csv')

    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv')
    # helper.clean()

    # write_makers = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_sorted_makers.csv', 8)
    # write_colors = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_makers.csv', 8)
    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv')
    # helper.clean()

# build clean make and clean model ()
#     cleaner = CarsDataCleaner(prefix + 'cars_last_record.csv', prefix + 'cars_last_record_clean_make_model_1.csv', prefix + 'makers1.csv')
#     cleaner.clean()

    #CarsMakesCleaner(prefix + 'cars_last_record.csv', prefix + 'test\\makes_with_appearances.csv', prefix + 'test\\cars_clean_makes.csv')
    CarsModelsCleaner(prefix + 'test\\cars_clean_makes.csv', prefix + 'test\\cars_clean_models.csv', prefix + 'test\\cars_main_make_models.csv')

    # cleaner = CarsDataCleaner(prefix + 'cars_last_record_test_class_5.csv', prefix + 'cars_last_record_clean_make_model_1.csv',
    #                           prefix + 'makers1.csv')
    # cleaner.clean()
    # print('done cleaning')
    # make_model_map_builder = BuildMakeModelMap('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\mini.csv', 9, 10)
    # make_model_map_builder.build_main_models(10)
    #make_model_map_builder.write_to_file('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\make_model_pairs.csv')
