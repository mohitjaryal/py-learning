# Program to demonstrate the Dictionary in py
info = {
    "name" : "Ram",
    "age"  : 20,
    "location" : "Chandigarh",
    "Degree" : "Engineering"
}
print("Before changing\n",info)
# Changing the value 
info["age"] = 21
info["name"] = "Sham"
info["location"] = "Dehli"
info["Degree"] = "B.com"
print("After changing\n",info)