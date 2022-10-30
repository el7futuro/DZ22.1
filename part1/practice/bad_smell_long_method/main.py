# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)

    # Чтение данных из строки


def _read(csv):
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data

    # Сортировка по возрасту по возрастанию


def _sort(data):
    _new_data  = sorted(data, key=lambda d: d['age'])
    return _new_data

    # Фильтрация


def _filter(_new_data):
    result_data = []
    for person in _new_data:
        if person['age'] < 10:
            continue
        else:
            result_data.append(person)
    return result_data


if __name__ == '__main__':
    print(get_users_list())
