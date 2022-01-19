from CarsDataCleaner import CarsDataCleaner
from CarsDataCleanerHelper import CarsDataCleanerHelper
from CarsMakesCleaner import CarsMakesCleaner
from WriteColumnWithAppearancesToFile import WriteColumnWithAppearancesToFile
from BuildMakeModelMap import BuildMakeModelMap

if __name__ == '__main__':
    prefix = 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\'

    # create mini original file
    CarsDataCleaner.write_mini_file(prefix + 'cars_last_record.csv', prefix + 'mini\\cars_last_record_mini.csv')

    # write mini file with cleaned makes
    CarsMakesCleaner(prefix + 'mini\\cars_last_record_mini.csv', prefix + 'mini\\mini_makes_with_appearances.csv', prefix + 'mini\\mini_clean_makes.csv')

