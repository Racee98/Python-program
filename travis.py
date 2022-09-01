known_users=['Alice','Bob','Claire','Dan','Emma','Fred','Georgie','Harry']



while True:
    print('hi my name is travis')
    name=input('what is your name?:').strip().capitalize()

    if name in known_users:
        print('Hello {}!'.format(name))
        remove=input('would you like to be removed from the  system (y/n)?:').lower()
        if remove=='y':
            known_users.remove(name)
        elif remove=='n':
            print('No problem I didnt want youto leave anyway!')
            
            
        
        
            
            
            
    else:
        print('Hmmmm I dont think I have meet you yet {} '.format(name))
        add_me=input('would you like to be added to the system (y/n)?:').strip().lower()
        if add_me=='y':
            known_users.append(name)
        elif add_me=='n':
            print('No worries , see you around!')
            




