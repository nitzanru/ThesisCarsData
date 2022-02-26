from CarsDataCleaner import CarsDataCleaner
from CarsDataCleanerHelper import CarsDataCleanerHelper
from CarsMakesCleaner import CarsMakesCleaner
from MainDataBuilder import MainDataBuilder
from WriteColumnWithAppearancesToFile import WriteColumnWithAppearancesToFile
from BuildMakeModelMap import BuildMakeModelMap

if __name__ == '__main__':
    prefix = 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\'

    # create mini original file
    # CarsDataCleaner.write_mini_file(prefix + 'cars_last_record.csv', prefix + 'mini\\cars_last_record_mini.csv')

    # write mini file with cleaned makes
    # CarsMakesCleaner(prefix + 'mini\\cars_last_record_mini.csv', prefix + 'mini\\mini_makes_with_appearances.csv', prefix + 'mini\\mini_clean_makes.csv')

    # write main mini file - as small as possible
    main_builder = MainDataBuilder()
    main_data = main_builder.build_main_data_frame(prefix + 'mini\\mini_clean_makes.csv')
    main_builder.write_df_to_file(main_data, prefix + 'mini\\mini_main.csv')
    x = 4 + 1


