documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "9207"}
]

import datetime
import os
def parametrized_logger(path):
    def logger (old_function):
        def new_function(*args, **kwargs):
            nonlocal path
            func_time=datetime.datetime.now()
            data=old_function(*args, **kwargs)
            file_name = f'{old_function.__name__}'
            file_path = os.path.join(path, str(file_name))
            with open (file_path,'w') as logger_file:
                logger_file.write(str(file_name)+'\n')
                logger_file.write(str(func_time)+'\n')
                logger_file.write(str(args)+'\n')
                logger_file.write(str(kwargs)+'\n')
                logger_file.write(str(data)+'\n')
        return new_function
    return logger

@parametrized_logger('C:/Users/samsung/PycharmProjects/Decorators/logs')
def person_finder(docs):
    num_of_doc=input("Please, input number of document")
    numbers=[doc['number']for doc in docs]
    if num_of_doc in numbers:
        for doc in docs:
            if num_of_doc == doc['number']:
                try:
                    print("Name of person of document", num_of_doc,"is:", doc['name'])
                except KeyError:
                    print("field 'name' is empty")
    else:
        print('Document of number {}'.format(num_of_doc), 'does not exist, please create it')

def main():
    while True:
        user_input = input("Please, input command")
        if user_input == "p":
            person_finder(documents)

        elif user_input == "q":
            print("end of program")
            break
main()