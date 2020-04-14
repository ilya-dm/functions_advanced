import json
import pprint


class Contact:
    def __init__ (self, name, last_name, phone_number, favorite=False, **kwargs):

        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite = favorite
        self.additional = kwargs


    def __str__ (self):
        additional_lst = list()
        info_str = ''
        for i in self.additional:
            additional_lst.append(f'{i}: {self.additional[ i ]}')
        for i in additional_lst:
            info_str += f'\n    {i}'
        self.contact_info = f'Имя: {self.name}\
        \nФамилия: {self.last_name}\
        \nТелефон: {self.phone_number}\
        \nИзбранный контакт: {self.favorite}\
        \nДополнительная информация:{info_str}'
        return self.contact_info


class PhoneBook:

    def __init__ (self, name):
        self.name = name
        self.contacts = list()
        self.phone_book = [ ]

    def display_contacts (self):
        for contact in self.phone_book:
            print(contact)

    def add_contact (self, name, last_name, phone_number, *favorite, **kwargs):
        self.contact = Contact(name, last_name, phone_number, favorite, **kwargs)
        if not self.contact.favorite:
            self.contact.favorite = False
        else:
            self.contact.favorite = True
        self.phone_book.append(self.contact)
        return self.phone_book

    def del_contact (self, number):
        self.number = number
        for contact in self.phone_book:
            if self.number in contact.phone_number:
                self.phone_book.remove(contact)
        return self.phone_book

    def fav_search (self):
        list_favorites = list()
        for contact in self.phone_book:
            if contact.favorite:
                list_favorites.append(contact)
        for contact in list_favorites:
            print(contact)

    def search (self, name, last_name):
        search_list = list()
        for contact in self.phone_book:
            if name in contact.name and last_name in contact.last_name:
                search_list.append(contact)
        for contact in search_list:
            print(contact)


if __name__ == '__main__':
    john = Contact('John', 'Smith', '+495952', True, telegram='@johny', email='johny@mail.ru', )
    nick = Contact('Nick', 'Smith', '+23455', telegram='@nick', email='nick@mail.ru', )
    bias = Contact('Bias', 'Smith', '+124', telegram='@bias', email='bias@mail.ru', )
    jojo = Contact('Jojo', 'Smith', '+555352', telegram='@jojo', email='jojo@mail.ru', )
    bill = Contact('Bill', 'Anderson', '+457845', telegram='@jojo', email='jojo@mail.ru', )
    adam = Contact('Adam', 'Smith', '+71234567', telegram='@adam', email='adam@mail.ru', )
    phone_book = PhoneBook('Smith')
    phone_book.add_contact('John', 'Smith', '+495952', True, telegram='@johny', email='johny@mail.ru', )
    phone_book.add_contact('Nick', 'Smith', '+23455', telegram='@nick', email='nick@mail.ru', )
    phone_book.add_contact('Bias', 'Smith', '+124', telegram='@bias', email='bias@mail.ru', )
    phone_book.add_contact('Jojo', 'Smith', '+555352', telegram='@jojo', email='jojo@mail.ru', )
    phone_book.add_contact('Bill', 'Anderson', '+457845', telegram='@jojo', email='jojo@mail.ru', )
    phone_book.add_contact('Adam', 'Smith', '+71234567', telegram='@adam', email='adam@mail.ru', )
    # print(phone_book.display_contacts())
    # phone_book.del_contact('+555352')
    print(phone_book.display_contacts())
    # print(phone_book.search('John', 'Smith'))
    #rint(phone_book.fav_search())
