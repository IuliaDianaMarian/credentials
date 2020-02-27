#ask for credentials, ask again for user and pw each if mistaken

print('welcome. type the user')

while True:
    
    name=input()
    if name=='Dorel':
        print('now type password')
        pw=input()
        while pw!='password':
            print('try the password again')
            pw=input()
        else:
            break
    else:
         print('try the user again')

print('login successful')

