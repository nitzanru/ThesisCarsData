from CarsDataCleaner import CarsDataCleaner
from WriteMakersWithAppearancesToFile import WriteMakersWithAppearancesToFile

if __name__ == '__main__':
    # helper = CarsDataCleanerHelper('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv')
    # helper.clean()

    write_makers = WriteMakersWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_sorted_makers.csv')
    #write_colors = WriteMakersWithAppearancesToFile('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', 'C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\edited_makers.csv')