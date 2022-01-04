from CarsDataCleaner import CarsDataCleaner
from CarsDataCleanerHelper import CarsDataCleanerHelper
from WriteColumnWithAppearancesToFile import WriteColumnWithAppearancesToFile
from BuildMakeModelMap import BuildMakeModelMap

if __name__ == '__main__':
    prefix = 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\'
    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv')
    # helper.clean()

    # write_makers = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_sorted_makers.csv', 8)
    # write_colors = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_makers.csv', 8)
    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv')
    # helper.clean()

# build clean make and clean model ()
    cleaner = CarsDataCleaner(prefix + 'cars_last_record.csv', prefix + 'cars_last_record_clean_make_model_1.csv', prefix + 'makers1.csv')
    cleaner.clean()

    # cleaner = CarsDataCleaner(prefix + 'cars_last_record_test_class_5.csv', prefix + 'cars_last_record_clean_make_model_1.csv',
    #                           prefix + 'makers1.csv')
    # cleaner.clean()
    # print('done cleaning')
    # make_model_map_builder = BuildMakeModelMap('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\mini.csv', 9, 10)
    # make_model_map_builder.build_main_models(10)
    #make_model_map_builder.write_to_file('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\make_model_pairs.csv')

    # make it dynamic - in one pass clean make, clean model, build main make, build main model, replace makes, replace models
