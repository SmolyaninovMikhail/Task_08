# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def add_person():
    last_name = input('Введите фамилию: ')
    name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    data = open('F:\\Git\\Python\\Tasks\\Task_08\\phonebook.txt', 'a', encoding='utf-8')
    data.writelines([last_name, ' ', name, ' ', surname, ' ', phone, '\n'])
    data.close()

def print_data():
    with open('F:\\Git\\Python\\Tasks\\Task_08\\phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def search():
    search_name = input('Введите данные: ')
    with open('F:\\Git\\Python\\Tasks\\Task_08\\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)

def load_data():
    with open('F:\\Git\\Python\\Tasks\\Task_08\\phonebook.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read().splitlines()
        path = input('Введите адрес файла: ')
    with open(path, 'r', encoding='utf-8') as data_2:
        for line in data_2:
            if line[:-1] not in text_data:
                data.write(line)

def update_contact():
    with open('F:\\Git\\Python\\Tasks\\Task_08\\phonebook.txt', 'r+', encoding='utf-8') as data:
        search_name = input('Введите имя или фамилию контакта: ').lower()
        found = False
        updated_contacts = []
        for line in data:
            contact = line.strip().lower().split(' ')
            if search_name == contact[0] or search_name == contact[1]:
                last_name = input('Введите новую фамилию: ')
                name = input('Введите новое имя: ')
                surname = input('Введите новое отчество: ')
                phone = input('Введите новый номер телефона: ')
                updated_contacts.append(' '.join([last_name, name, surname, phone]))
                found = True
            else:
                updated_contacts.append(line.strip())
        if not found:
            print('Контакт не найден!')
            return
        data.seek(0)
        data.truncate()
        data.write('\n'.join(updated_contacts))
        data.close()
        print(f'Контакт "{search_name}" успешно изменен!')

def delete_contact():
    with open('F:\\Git\\Python\\Tasks\\Task_08\\phonebook.txt', 'r+', encoding='utf-8') as data:
        search_name = input('Введите имя или фамилию контакта, который Вы хотите удалить: ').lower()
        found = False
        updated_contacts = []
        for line in data:
            contact = line.strip().lower().split(' ')
            if search_name == contact[0] or search_name == contact[1]:
                found = True
            else:
                updated_contacts.append(line.strip())
        if not found:
            print('Контакт не найден!')
            return
        data.seek(0)
        data.truncate()
        data.write('\n'.join(updated_contacts))
        data.close()
        print(f'Контакт "{search_name}" успешно удален!')

def ui():
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - изменение контакта
6 - удаление контакта''')
    user_input = input('Введите нужный вариант: ')
    if user_input == '1':
        add_person()
    elif user_input == '2':
        search()
    elif user_input == '3':
        load_data()
    elif user_input == '4':
        print_data()
    elif user_input == '5':
        update_contact()
    elif user_input == '6':
        delete_contact()

def main():
    ui()

if __name__ == "__main__":
    main()