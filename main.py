import csv

import LineByLineReader

# n issan ->nissan M C -> MC

def write_to_file(file_name, dict_to_print):
    sorted_dict = dict(sorted(dict_to_print.items(), key=lambda item: item[1]))
    with open(file_name, 'w', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in sorted_dict.items():
            writer.writerow([key, value])

if __name__ == '__main__':
    reader = LineByLineReader.LineByLineReader('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record.csv')
    gen = reader.read_lines()
    number_of_rows = 1      # 49019679
    makers = {}
    while True:
        try:
            row = next(gen)
            make = row.split(',')[8]
            if make in makers.keys():
                makers[make] = makers[make] + 1
            else:
                makers[make] = 1
            number_of_rows += 1
        except UnicodeDecodeError:
            print('error - bad line')
        except StopIteration:
            break
    print(number_of_rows)
    # makers = {'mazda':2, 'honda':15, 'fiat':1}
    write_to_file('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\original_sorted_makers.csv', makers)

