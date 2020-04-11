import json


class Contact:
    def __init__(self, name, last_name, phone_number, favorite=False, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite = favorite
        self.additional = kwargs

    def __str__(self):
        additional_lst = list()
        info_str = ''
        for i in self.additional:
            additional_lst.append(f'{i}: {self.additional[ i ]}')
        for i in additional_lst:
            info_str += f'\n\t\t{i}'
        contact_info = f'\n\nИмя: {self.name}\
                                \nФамилия: {self.last_name}\
                                \nТелефон: {self.phone_number}\
                                \nИзбранный контакт: {self.favorite}\
                                \nДополнительная информация:{info_str}\n\n'
        return contact_info


class PhoneBook:
    phone_book = list()

    def __init__(self, name, path):
        self.name = name
        self.path = path
    def json_decoder(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            try:
                self.phone_book = json.load(f)
            except json.JSONDecodeError:
                print('Телефонная книга пуста!')
        return self.phone_book

    def display_contacts(self, path):
        with open(path, encoding='utf-8') as f:
            contacts = json.load(f)
            contacts = json.dumps(contacts, ensure_ascii=False, indent=4)
        return contacts

    def add_contact(self, contact):
        appended_contact = {'Имя': contact.name, 'Фамилия': contact.last_name, 'Телефон': contact.phone_number,
                            'Избранный контакт': contact.favorite, 'Дополнительная информация': contact.additional}

        self.phone_book.append(appended_contact)
        return self.phone_book
    def add_contacts_to_file(self):
        contact__list = list()
        with open('phone_book.json', encoding='utf-8') as f:
            try:
                contact_list = json.load(f)
            except Exception:
                contact_list =list()
        for contact in self.phone_book:
            if contact not in contact_list:
                contact_list.append(contact)
        contact_list = json.dumps(contact_list, indent=4, ensure_ascii=False)
        with open('phone_book.json', 'w', encoding='utf-8') as f:
            f.write(contact_list)

    def del_contact(self, number):
        self.number = number
        self.phone_book = self.json_decoder()
        for contact in self.phone_book:
            if self.number in contact['Телефон']:
                del_contact = contact
                self.phone_book.remove(contact)
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.phone_book, indent=4, ensure_ascii=False))
        return f'{del_contact["Имя"]} {del_contact["Фамилия"]} успешно удален из телефонной книги'

    def fav_search(self):
        list_favorites = list()
        self.phone_book = self.json_decoder()
        for contact in self.phone_book:
            if contact['Избранный контакт']:
                list_favorites.append(contact)
        return list_favorites

    def search(self, name, last_name):
        self.phone_book = self.json_decoder()
        search_list = list()
        for contact in self.phone_book:
            if name == contact['Имя'] and last_name == contact['Фамилия']:
                search_list.append(contact)
        return search_list


if __name__ == '__main__':
    john = Contact('John', 'Smith', '+495952', False, telegram='@johny', email='johny@mail.ru', )
    nick = Contact('Nick', 'Smith', '+23455', False, telegram='@nick', email='nick@mail.ru', )
    bias = Contact('Bias', 'Smith', '+124', True, telegram='@bias', email='bias@mail.ru', )
    jojo = Contact('Jojo', 'Smith', '+555352', False, telegram='@jojo', email='jojo@mail.ru', )
    bill = Contact('Bill', 'Anderson', '+457845', False, telegram='@jojo', email='jojo@mail.ru', )
    adam = Contact('Adam', 'Smith', '+71234567', False, telegram='@adam', email='adam@mail.ru', )
    phone_book = PhoneBook('Smith', 'phone_book.json')

    phone_book.add_contact(john)
    phone_book.add_contact(nick)
    phone_book.add_contact(jojo)
    phone_book.add_contact(adam)
    phone_book.add_contact(bias)
    phone_book.add_contacts_to_file()
    print(phone_book.del_contact('+124'))
    print(phone_book.display_contacts('phone_book.json'))
