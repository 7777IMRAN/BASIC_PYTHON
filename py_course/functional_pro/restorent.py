class hotel:
    users={}
    address='hyd'
def login():
    print(hotel.users)

def run():
    choice=input('select:\n1.Register\n2.Login\n')
    match choice:
        case '1':
            u_name=input('enter your name')
            id=int(input('inter ID:'))
            pin=int(input('enter PIN:'))
            if id in hotel.users[u_name] and pin==hotel.users[u_name][pin]:
                print('already registered','pleaze login')
                run()
            else:
                hotel.users[u_name]={'id':id,'pin':pin}
        case '2':
            id=int(input('inter ID:'))
            pin=int(input('enter PIN:'))
            if id in hotel.users[u_name] and pin==hotel.users[u_name][pin]:
                pass
run()
