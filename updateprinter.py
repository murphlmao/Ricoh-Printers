from printers import Ricoh
import csv

printer_conn = dict(
    host='10.10.40.160',
    username='admin',
    password=''
)

# Access via context manager so that all connections are closed automatically.
with Ricoh(**printer_conn) as ricoh:
    print(repr(ricoh))
    # <Ricoh(10.10.2.8)> at 51441168

    print(ricoh)
    # There are 94 users in 10.10.40.160

    print(len(ricoh))
    # 94

    # print all users
    for user in ricoh:
        print(user.id, user.name)
        # 1 John Doe
        # 2 Billy Bob
        # 3 ...

    with open('employees.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader) # skip headers
        for row in reader:
            first, last, email = row
            name = f"{first} {last}"
            displayName = f"{first} {last[0]}."
            userid = first.lower()
            ricoh.add_user(userid=userid, name=name, displayName=displayName, email=email)
            
    # add a user
    #ricoh.add_user(userid='james', name='James Dean', displayName='James D', email='jdean@gmail.com')

    # delete user (by id)
    #ricoh.delete_user(138)
    
    """for user in ricoh:
        print(user.id, user.name)
        # 1 John Doe
        # 2 Billy Bob
        # 3 ...
        ricoh.delete_user(user.id)"""
