pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}


def get_pet(ID):
    if ID in pets:
        return pets[ID]
    else:
        return False


def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"


def print_pet(ID):
    pet = get_pet(ID)

    if pet == False:
        print("Питомца с таким ID нет в базе данных.")
    else:
        for pet_name in pet:
            pet_type = pet[pet_name]["Вид питомца"]
            pet_age = pet[pet_name]["Возраст питомца"]
            owner_name = pet[pet_name]["Имя владельца"]

            print(
                f'Это {pet_type} по кличке "{pet_name}". '
                f'Возраст питомца: {pet_age} {get_suffix(pet_age)}. '
                f'Имя владельца: {owner_name}'
            )


def pets_list():
    for ID in pets:
        print_pet(ID)


def create():
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")

    age = input("Введите возраст питомца: ")

    while not age.isdigit() or int(age) < 1:
        print("Ошибка: возраст должен быть натуральным числом.")
        age = input("Введите возраст питомца: ")

    age = int(age)

    owner_name = input("Введите имя владельца: ")

    new_id = max(pets.keys()) + 1

    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner_name
        }
    }

    print("Новая запись добавлена.")
    print("ID нового питомца:", new_id)
    print_pet(new_id)


def read():
    ID = input("Введите ID питомца: ").strip()

    if ID.isdigit():
        ID = int(ID)
        print_pet(ID)
    else:
        print("Ошибка: ID должен быть целым числом.")


def update():
    ID = input("Введите ID питомца: ").strip()

    if ID.isdigit():
        ID = int(ID)

        if get_pet(ID) == False:
            print("Питомца с таким ID нет в базе данных.")
        else:
            name = input("Введите новую кличку питомца: ")
            pet_type = input("Введите новый вид питомца: ")

            age = input("Введите новый возраст питомца: ")

            while not age.isdigit() or int(age) < 1:
                print("Ошибка: возраст должен быть натуральным числом.")
                age = input("Введите новый возраст питомца: ")

            age = int(age)

            owner_name = input("Введите новое имя владельца: ")

            pets[ID] = {
                name: {
                    "Вид питомца": pet_type,
                    "Возраст питомца": age,
                    "Имя владельца": owner_name
                }
            }

            print("Запись обновлена.")
            print_pet(ID)
    else:
        print("Ошибка: ID должен быть целым числом.")


def delete():
    ID = input("Введите ID питомца: ").strip()

    if ID.isdigit():
        ID = int(ID)

        if get_pet(ID) == False:
            print("Питомца с таким ID нет в базе данных.")
        else:
            del pets[ID]
            print("Запись удалена.")
    else:
        print("Ошибка: ID должен быть целым числом.")


command = ""

while command != "stop":
    print()
    print("Доступные команды: create, read, update, delete")
    print("Для завершения программы введите stop")

    command = input("Введите команду: ").lower().strip()

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "stop":
        print("Программа завершена.")
    else:
        print("Неизвестная команда.")