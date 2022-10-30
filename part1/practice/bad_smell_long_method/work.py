
csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_list():
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})


def sort_list(data):
