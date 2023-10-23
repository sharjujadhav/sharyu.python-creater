56.Implement a simple address book using a dictionary.

adressDict = {'phony' : {'name' : 'Phony Phony', 'phone' : 'PhonyNum', 'adress' : 'Pony adress'}}
 
def addPerson():
    nickname = input('Type a nickname for the person\n - ')
    name = input('Type their full name\n - ')
    adress = input('Type their adress\n - ')
    phone = input('Type their phone number\n - ')
    add = False
    for i in adressDict:
        if i.lower() == name.lower():
            print('Name already there')
        elif adressDict[i]['name'].lower() == name.lower():
            print('Name already there')
        else:
            add = True
    if add:
        adressDict.update({nickname : {'name' : name, 'phone' : phone, 'adress' : adress}})
 
def indexPerson():
    name = input('Type the person\'s name or nickname\n - ')
    for i in adressDict:
        if i.lower() == name.lower() or adressDict[i]['name'].lower() == name.lower():
            print('\nName: %s\nPhone Number: %s\nAdress: %s\n' %(adressDict[i]['name'], adressDict[i]['phone'], adressDict[i]['adress']))
        else:
            print('Name not found')
