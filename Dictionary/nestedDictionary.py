# Nested Dictionary
students = {
    "name" : "Ram",
    "score" : {
        "chem" : 90,
        "phy" : 100,
        "math" : 99,
    }
}

print(students["score"]["chem"])