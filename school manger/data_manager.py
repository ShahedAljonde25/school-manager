import json

from models import
def read_studant_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return [Student(s['name'], s['age'], s['id'], s['level']) for s in data]
    except FileNotFoundError as e:
        print("Can't read student data:", e)
        return []

def write_studant_data(students):
    data = [{'name': s.name, 'age': s.age, 'id': s.id, 'level': s.level} for s in students]
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def read_t_data():
    try:
        with open("t_data.json", "r") as file:
            tdata = json.load(file)
            return [Employee(e["id"], e["name"], e["postion"], e["salary"]) for e in tdata]
    except FileNotFoundError as e:
        print("Can't read employee data:", e)
        return []

def write_t_data(employees): 
    data_t = [{'id': e.id, 'name': e.name, 'postion': e.pos, 'salary': e.salary} for e in employees]
    with open('t_data.json', 'w') as file:
        json.dump(data_t, file, indent=4)
