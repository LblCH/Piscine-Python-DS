import sys


def names_extractor(path):
    with open(path, 'r') as input_file:
        with open('employees.tsv', 'w') as output_file:
            output_file.write('Name\tSurname\tE-mail\n')
            for string in input_file.readlines():
                name, surname = string.split('@')[0].split('.')
                output_file.write(f'{name.capitalize()}\t{surname.capitalize()}\t{string.strip()}\n')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        names_extractor(sys.argv[1])