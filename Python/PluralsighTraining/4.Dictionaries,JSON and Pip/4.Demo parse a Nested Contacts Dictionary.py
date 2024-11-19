contacts = {
    "number": 4,
    "students":
    [
        {"name" : "CallyManSam", "email": "Callyman@sam.com"},
        {"name" : "Afghanistan Dan", "email": "Afghan@dan.org"},
        {"name" : "Little T", "email" : "LittleT@roadrage.co.uk"},
        {"name" : "Sophie Aspen" , "email" : "SophieAspin@Microsoft.corpo"}
    ]
}

print("Student emails:")
for student in contacts["students"]:
    print(student["email"])
