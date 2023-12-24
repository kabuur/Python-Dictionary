elements =  {
    "hydrogen": {"number": 1,"weight": 1.00794, "symbol": 'H'},
    "helium": {"number": 2,"weight": 4.002602,"symbol": "He"},
    "oxygen": {"number": 8, "weight": 15.999, "symbol": "O"}}


print(elements["helium"]["number"])



student_records = {
    'John': {'age': 20,'major': 'Computer Science','grades': [85, 90, 92]},
    'Emma': {'age': 19,'major': 'Mathematics','grades': [95, 88, 91]}
}

student_records["ahmed"] = {
    "age": 23 , "major": 'computer science', "grades": [90,91,89]
}

print (student_records)

student_records["ahmed"]["grades"].append(99)

print(student_records)