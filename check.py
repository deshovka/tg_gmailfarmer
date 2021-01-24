def editing(test):

    print(test)
    data_get = test.splitlines()
    # print(data_get)

    email_get = data_get[2:3]
    # print(email_get)

    name_get = data_get[3:4]
    # print(name_get)

    surname_get = data_get[4:5]
    # print(surname_get)

    pass_get = data_get[6:7]
    # print(pass_get)

    # data editing
    email_get = ''.join(email_get)
    email_get = email_get[7:-10]
    print(email_get)

    name_get = ''.join(name_get)
    name_get = name_get[5:]
    print(name_get)

    surname_get = ''.join(surname_get)
    surname_get = surname_get[9:]
    print(surname_get)

    pass_get = ''.join(pass_get)
    pass_get = pass_get[8:]
    print(pass_get)
    return email_get, name_get, surname_get, pass_get