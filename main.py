import json
import pprint


class Contact:
    def __init__(self, name, last_name, phone_number, favorite= False, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite = favorite
        self.additional = kwargs


    def __str__(self):
        additional_lst = list()
        info_str = ''
        for i in self.additional:
            additional_lst.append(f'{i}: {self.additional[i]}')
        for i in additional_lst:
            info_str += f'\n    {i}'
        self.contact_info = f'\n\nИмя: {self.name}\
        \nФамилия: {self.last_name}\
        \nТелефон: {self.phone_number}\
        \nИзбранный контакт: {self.favorite}\
        \nДополнительная информация:{info_str}\n\n'
        return self.contact_info

class PhoneBook:

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.contacts = list()
        self.phone_book = []


    def display_contacts(self):
        return self.phone_book

    def add_contact(self, name, *args, **kwargs):
        contact = Contact(name, args, kwargs)
        self.phone_book.append(str(contact.name). replace('\n', ''))
        return self.phone_book

    def del_contact(self, number):
        self.number = number
        for contact in self.phone_book:
            if self.number in contact:
                self.phone_book.remove(contact)
        return self.phone_book

    def fav_search(self):
        list_favorites = list()
        for contact in self.phone_book:
            if 'Избранный контакт: True' in contact:
                list_favorites.append(contact)
        return list_favorites

    def search(self, name, last_name):
        search_list = list()
        for contact in self.phone_book:
            if name in contact and last_name in contact:
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
    print(john)
    phone_book.add_contact(nick)
    phone_book.add_contact(adam)
    phone_book.add_contact(bias)
    print(phone_book.display_contacts())
    print(phone_book.del_contact('+23455'))
    print(phone_book.fav_search())
    #phone_book.add_contact(jojo)
    #print(phone_book.phone_book)
    # phone_book.add_contact(adam)
    # phone_book.add_contact(bias)
    #phone_book.del_contact('+124')
    print(phone_book.search('Adam', 'Smith'))
    #print(phone_book.fav_search())
    # print(phone_book.display_contacts('phone_book.json'))
