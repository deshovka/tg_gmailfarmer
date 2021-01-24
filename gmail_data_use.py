def data_use(email_get, name_get, surname_get, pass_get, browser):

    #email
    email_field = browser.find_element_by_name('Username')
    email_field.send_keys(email_get)
    print('Email Done!')


    #name
    Name_field = browser.find_element_by_name('firstName')
    Name_field.send_keys(name_get)
    print('Name Done!')


    # surname
    lstName_field = browser.find_element_by_name('lastName')
    lstName_field.send_keys(surname_get)
    print('Last Name Done!')


    # pass
    passwd_field = browser.find_element_by_name('Passwd')
    passwd_field.send_keys(pass_get)

    passwd_field = browser.find_element_by_name('ConfirmPasswd')
    passwd_field.send_keys(pass_get)
    print('Password Done!')
    return