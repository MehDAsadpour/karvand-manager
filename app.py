import json
import os

path_karvands = os.path.join(
    os.path.dirname(__file__),
    "data",
    "karvands.json"
)

def load_karvand():
    try:
        with open(path_karvands, "r", encoding="utf-8") as file:
            data_karvands = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        os.makedirs(os.path.dirname(path_karvands), exist_ok=True)

        data_karvands = {
            "bootcamp":{
            "title":"karvand python",
            "year": 2026
        },
            "karvands": []
        }
    return data_karvands

def save_karvands(data_karvands):
    with open(path_karvands, "w", encoding="utf-8") as file:
        json.dump(data_karvands, file, indent=4)

def add(data_karvands):
    person = {
        "id": data_karvands['karvands'][-1]['id'] + 1 if data_karvands['karvands'] else 1,
        "full_name": input("Enter Name: "),
        "city": input("Enter City: "),
        "email":input("Enter email: "),
        "education": {
            "degree": input("Enter degree: "),
            "field": input("Enter field: ")
        },
        "skills": []
    }
    count = int(input("How many skills? "))
    for i in range(count):
        name =input("Skill name: ")
        level=input("Skill level: ")
        while True:
            score=int(input("Skill score: "))
            if score >= 0 and score <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        skill = {
            "name": name,
            "level": level,
            "score": score
        }
        person['skills'].append(skill)        
    data_karvands['karvands'].append(person)
    save_karvands(data_karvands)

def show(data_karvands):
    if len(data_karvands["karvands"]) == 0:
        print("Karvands list is empty")
    else:
        for item in data_karvands["karvands"]:
            print(f"{item['id']}. {item['full_name']}\n"
                f"city : {item['city']}\n"
                f"email : {item['email']}\n"
                f"field : {item['education']['field']}\n"
                f"degree : {item['education']['degree']}")
            for skill in item['skills']:
                print(f"Skills: {skill['name']}  Level: {skill['level']}  Score: {skill['score']}")
        print("---------------------------------------------------")

def search_id(data_karvands):
    id=int(input("Enter user's ID: "))
    found=True
    print("RESULTS:")
    for item in data_karvands['karvands']:
        if item['id']==id:
            print(f"\n#{item['id']}\n{item['full_name']}\n"
                f"city : {item['city']}\n"
                f"email : {item['email']}\n"
                f"field : {item['education']['field']}\n"
                f"degree : {item['education']['degree']}")
            for skill in item['skills']:
                print(f"Skills: {skill['name']}  Level: {skill['level']}  Score: {skill['score']}")
            found=False
            break 
    if found:
        print("!!! ID Not founded !!!")   

def search_skill(data_karvands):
    s=input("Enter skill name: ")
    found=True
    print("RESULTS:")
    for item in data_karvands['karvands']:
        for skill in item['skills']:
            if s==skill['name']:
                print(f"\n{item['id']}. {item['full_name']}\n"
                      f"{skill['name']}  Level: {skill['level']}  Score: {skill['score']}")
                print("---------------------------------------------------")
                found=False
                break
    if found:
        print("!!! Skill not founded !!!")

data_karvands=load_karvand()
msg="""
1.Add
2.Show list
3.Search by ID
4.Search by skills
.
.
.
8.Exit
"""
running=True
while running:
    print(msg)
    c=int(input("choose: "))
    if c==8:
        break
    elif c==1:
        add(data_karvands)
    elif c==2:
        show(data_karvands)
    elif c==3:
        search_id(data_karvands)
    elif c==4:
        search_skill(data_karvands)
    else:
        print("Invalid input.Try again")