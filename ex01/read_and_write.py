def read_and_write():
    with open('ds.csv', 'r') as ds_csv:
        with open('ds.tsv', 'w') as ds_tsv:
            table = ds_csv.read().replace('\",', '\"\t').replace('false,', 'false\t').replace('true,', 'true\t')
            ds_tsv.write(table)


if __name__ == '__main__':
    read_and_write()