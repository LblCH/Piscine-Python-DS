def letter_starter(name):
    email = f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. '\
           f'That’s a precondition for the professionals that our company hires.'
    return email


if __name__ == '__main__':
    with open('employees.tsv') as input_file:
        for string in input_file.readlines():
            name = string.split('\t')[0]
            if '@' in string.split('\t')[2]:
                print(letter_starter(name))
