# username Generator
Python script to generate possible usernames using first and last name.

# Requires
- Python3

# Usage
```sh
usernameGenerator.py [-h] -i INPUT_FILE [-o OUTPUT_FILE]
```

If you do not specify an output file all usernames will be printed on terminal.
## Exemple:
list.txt
```
John doe
```

```sh
python3 usernameGenerator.py -i list.txt -o list.out
```

list.out
```
john.doe
John.doe
john.Doe
John.Doe
JOHN.doe
john.DOE
JOHN.Doe
John.DOE
JOHN.DOE
doe.john
doe.John
Doe.john
Doe.John
doe.JOHN
Doe.JOHN
DOE.john
DOE.John
DOE.JOHN
john.d
john.D
John.d
John.D
JOHN.D
JOHN.d
doe.j
doe.J
Doe.j
Doe.J
DOE.j
DOE.J
j.doe
J.doe
j.Doe
J.Doe
j.DOE
J.DOE
d.john
d.John
D.john
D.John
d.JOHN
D.JOHN
```
