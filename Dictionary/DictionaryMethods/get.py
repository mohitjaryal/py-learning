# get() mehthod in py 
students = {
    # Student 1 - Ram
    "Ram" : {
        'name' : 'Ram',
        'age' : 20,
        'subjects' : {
            'phy' : 100,
            'math' : 99,
             'chem' : 91
        }
    },

    "Roxy" : {
        'name' : 'Roxy',
        'age' : 21,
        'subjects' : {
            'phy' : 100,
            'math' : 97,
            'chem' :90
        }
    }

}

print('Ram :\n',students['Ram'].get('subjects')) # accessing key - 'subjects' in key 'Ram'
print('Ram (age) :\n',students['Ram'].get('age')) # accessing key - 'age' in key 'Ram'
print('Roxy :\n',students['Roxy'].get('subjects')) # accessing key - 'subjects' in key 'Roxy'
print('Roxy(age):\n',students['Ram'].get('age')) # accessing key - 'age' in key 'Roxy'