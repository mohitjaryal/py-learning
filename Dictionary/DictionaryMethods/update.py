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
students['Ram'].update({'city':'Chandigarh'}) # Adding new key - 'city'. and value 'Chandigarh' to Ram key
students['Roxy'].update({'city':'Delhi'}) # Adding new key - 'city'. and value 'Delhi' to Roxy key
print('Ram :\n',students['Ram'])
print('Roxy :\n',students['Roxy'])