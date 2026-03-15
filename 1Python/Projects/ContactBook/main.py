
while True:
    q = input('Add (a) Search(s) Quit(q)')
    
    if q == 'a':
        with open('contactBook.txt', 'a') as f:
            name = input('Name: ').title()
            phone = input('Phone: ')
            f.writelines((name,':',phone,'\n'))
    
    elif q == 's':
        with open('contactBook.txt','r') as f:
            search = input('Search: ').title()
            for i in f:
                if search in i:
                    print(i)
                    
    elif q == 'q':
        exit()
        
    else:
        print("Enter a valid input")