# update() method in py
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
students['Ram'].update({'city':'Chandigarh'})
students['Roxy'].update({'city':'Delhi'})
print('Ram :\n',students['Ram'])
print('Roxy :\n',students['Roxy'])