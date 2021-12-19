from CarsDataCleaner import CarsDataCleaner
from CarsDataCleanerHelper import CarsDataCleanerHelper
from WriteColumnWithAppearancesToFile import WriteColumnWithAppearancesToFile

if __name__ == '__main__':
    prefix = 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\'
    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv')
    # helper.clean()

    # write_makers = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_sorted_makers.csv', 8)
    # write_colors = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_makers.csv', 8)
    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv')
    # helper.clean()

    cleaner = CarsDataCleaner(prefix + 'cars_last_record.csv', prefix + 'cars_last_record_test_class_4.csv', prefix + 'edited_sorted_makers.csv')
    cleaner.clean()

    #write_makers = WriteColumnWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cylinder_capacities.csv', 12)
