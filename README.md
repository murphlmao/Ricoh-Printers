# Ricoh
Forked project from anthonyfox @ https://github.com/WTFox/printers      
Added more printers, added csv reader.
## About
Whenever my organization hires or fires someone, I have to go into each of our 5 printers and add/remove the user. This is often the step I forget to do, and it's definitely the one I like the least.

So I've written a python wrapper for dealing with these machines from Hell.

## Compatibility
This works on the following models:

xx01 series
* Ricoh Aficio MP C3001
* Ricoh Aficio MP C3501
* Ricoh Aficio MP C4501
* Ricoh Aficio MP C5501

xx02 series
* Ricoh Aficio MP 4002
* Ricoh Aficio MP C6502
* Ricoh Aficio MP 6002
* Ricoh Aficio MP 9002

xx03 series
* Ricoh Aficio MP C3003
* Ricoh Aficio MP C3503
* Ricoh Aficio MP C4503
* Ricoh Aficio MP C5503
* Ricoh Aficio MP C6003

xx04 series
* not tested yet

xx55 series
* Ricoh MP 5055

Also supported
* Ricoh IM C2500
* Ricoh IM C3000
* Ricoh C307
* Ricoh Aficio MP 9001 

## Installation
L
```bash
git clone https://github.com/WTFox/printers.git
cd printers
sudo python setup.py install
```
W
```bash
git clone https://github.com/WTFox/printers.git
python setup.py install
# run updateprinter after filling in your data
```


## Usage
```python
from printers import Ricoh

printer_conn = dict(
    host='10.10.2.13',
    username='admin',
    password=''
)

# Access via context manager so that all connections are closed automatically.
with Ricoh(**printer_conn) as ricoh:
    print(repr(ricoh))
    # <Ricoh(10.10.2.8)> at 51441168

    print(ricoh)
    # There are 94 users in 10.10.2.8

    print(len(ricoh))
    # 94

    for user in ricoh:
        print(user.id, user.name)
        # 1 John Doe
        # 2 Billy Bob
        # 3 ...

    # add a user from csv file containing employees
    # csv structure: First, Last, Email
    with open('employees.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader) # skip headers
        for row in reader:
            first, last, email = row
            name = f"{first} {last}"
            displayName = f"{first} {last[0]}."
            userid = first.lower()
            ricoh.add_user(userid=userid, name=name, displayName=displayName, email=email)
```

## Disclaimer
Even though I've tested this thoroughly, I'm not responsible for any damage it may cause to your fickle, weak-blooded hounds of hell printers.

Contact me [here](mailto:anthonyfox1988@gmail.com) for questions or concerns. Thanks!
