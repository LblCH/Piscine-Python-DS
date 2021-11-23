def to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    dictionary = {}
    for country in list_of_tuples:
        if country[1] not in dictionary:
            dictionary[country[1]] = [country[0]]
        else:
            dictionary[country[1]].append(country[0])
    for key, value in dictionary.items():
        for i in value:
            print("'" + key + "' : '" + i + "'")


if __name__ == '__main__':
    to_dictionary()