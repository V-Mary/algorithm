from hash_table import *

if __name__ == '__main__':
    country_code = [[] for _ in range(3)]
    print(country_code)

    insert(country_code, 0, 'Nepal')
    insert(country_code, 2, 'UK')
    insert(country_code, 1, 'Ukraine')
    print(country_code)

    delete(country_code, 1)
    print(country_code)





