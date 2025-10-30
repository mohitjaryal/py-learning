# Nested dictionary 
students = {
    # Student 1 - Ram
    "Ram" : {
        'name' : 'Ram',
        'age' : 20,
        'subjects' : {
            'phy' : 100,
            'math' : 99
        }
    },

    "Roxy" : {
        'name' : 'Roxy',
        'age' : 21,
        'subjects' : {
            'phy' : 100,
            'math' : 97
        }
    }

}

print('Ram :\n',students['Ram'])
print('Roxy :\n',students['Roxy'])