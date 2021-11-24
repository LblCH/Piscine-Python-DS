def dict_sorter():
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
    dct = {}
    for country in list_of_tuples:
        dct[country[0]] = country[1]
    dictionary = {}
    for country in list_of_tuples:
        if int(country[1]) not in dictionary:
            dictionary[int(country[1])] = [country[0]]
        else:
            dictionary[int(country[1])].append(country[0])
    for i in sorted(dictionary, reverse=True):
        for cntry in sorted(dictionary[i]):
            print(cntry)


if __name__ == '__main__':
    dict_sorter()
