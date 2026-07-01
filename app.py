import json
import os

path_karvands = os.path.join(
    os.path.dirname(__file__),
    "data",
    "karvands.json"
)

path_report = os.path.join(
    os.path.dirname(__file__),
    "data",
    "report.json"
)

def load_report():
    try:
        with open(path_report, "r", encoding="utf-8") as file:
            data_report = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        os.makedirs(os.path.dirname(path_report), exist_ok=True)

        data_report = {       
            "total_karvands": 0,
            "total_skills": 0,
            "average_skill_score": 0,
            "cities": [],
            "unique_skills": []
        }
    return data_report

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

def save_report(data_report):
    with open(path_report, "w", encoding="utf-8") as file:
        json.dump(data_report, file, indent=4)

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
    while True:
        try:
            count = int(input("How many skills? "))
            break 
        except ValueError:
            print("Invalid Input.Enter a number(1~8)")    
    for i in range(count):
        name =input("Skill name: ")
        level=input("Skill level: ")
        while True:
            try:
                score = float(input("Skill score: "))

                if 0 <= score <= 100:
                    break
                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")
        
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
        for person in data_karvands["karvands"]:
            print(f"{person['id']}. {person['full_name']}\n"
                f"city : {person['city']}\n"
                f"email : {person['email']}\n"
                f"field : {person['education']['field']}\n"
                f"degree : {person['education']['degree']}")
            for skill in person['skills']:
                print(f"Skills: {skill['name']}  Level: {skill['level']}  Score: {skill['score']}")
        print("---------------------------------------------------")

def search_id(data_karvands):
    while True:
        try:
            id=int(input("Enter user's ID: "))
            break 
        except ValueError:
            print("Invalid Input.Enter a number.")
    found=True
    print("RESULTS:")
    for person in data_karvands['karvands']:
        if person['id']==id:
            print(f"\n#{person['id']}\n{person['full_name']}\n"
                f"city : {person['city']}\n"
                f"email : {person['email']}\n"
                f"field : {person['education']['field']}\n"
                f"degree : {person['education']['degree']}")
            for skill in person['skills']:
                print(f"Skills: {skill['name']}---Level: {skill['level']}---Score: {skill['score']}")
            found=False
            break 
    if found:
        print("!!! ID Not founded !!!")   

def search_skill(data_karvands):
    s=input("Enter skill name: ")
    found=True
    print("RESULTS:")
    for person in data_karvands['karvands']:
        for skill in person['skills']:
            if s==skill['name']:
                print(f"\n{person['id']}. {person['full_name']}\n"
                      f"{skill['name']}---Level: {skill['level']}---Score: {skill['score']}")
                print("---------------------------------------------------")
                found=False
                break
    if found:
        print("!!! Skill not founded !!!")

def edit(data_karvands):
    while True:
        try:
            id=int(input("which ID should be edited? "))
            break 
        except ValueError:
            print("Invalid Input.Enter a number.")
    found=True
    for person in data_karvands['karvands']:
        if person['id']==id:
            attribute=input("Which user attribute to change? ")
            if attribute in person:
                person[attribute]=input(f"Enter new {attribute}: ")
                found=False
                break
            elif attribute in person['education']:
                person['education'][attribute]=input(f"Enter new {attribute}: ")
                found=False
                break
    if found:
        print("---------------------------------------------------")
        print("!!!ID not founded!!!")                    
    save_karvands(data_karvands)

def Delete(data_karvands):
    New_list=[]
    found=True
    while True:
        try:
            id=int(input("Which user should be deleted? "))
            break 
        except ValueError:
            print("Invalid Input.Enter a number.")
    for person in data_karvands['karvands']:
        if person['id']!=id:
            New_list.append(person)
        else:
            found=False
    data_karvands['karvands']=New_list
    if found:
        print("!!!ID not founded!!!")
    save_karvands(data_karvands)

def report(data_karvands):
    cities=[]
    uskills=[]
    sum=0
    total=0
    for person in data_karvands['karvands']:
        cities.append(person['city'])
        for skill in person['skills']:
            uskills.append(skill['name'])
            sum+=skill['score']
            total+=1
        i=-1
    us=[] #unique skills
    uc=[] #cities
    for person in data_karvands['karvands']:
        for skill in person['skills']:
            c=0
            for uniques in uskills:
                if uniques==skill['name']:
                    c+=1
            if c==1:
                us.append(skill['name'])         
    for city in cities:
        if city not in uc:
            uc.append(city)   

    if len(data_karvands["karvands"]) != 0:             
        data_reports = {       
            "total_karvands": len(data_karvands['karvands']),
            "total_skills": total,
            "average_skill_score": (float)(sum/total),
            "cities": uc,
            "unique_skills": us
        }
    else:
        data_reports = {       
        "total_karvands": 0,
        "total_skills": 0,
        "average_skill_score": 0.0,
        "cities": [],
        "unique_skills": []
        }
    save_report(data_reports)


data_karvands=load_karvand()
data_report=load_report()
msg="""
1.Add
2.Show list
3.Search by ID
4.Search by skills
5.Edit by ID
6.Delete by ID
7.Report
8.Exit
"""
running=True
while running:
    print(msg)
    while True:
        try:
            c = int(input("Choose: "))
            break 
        except ValueError:
            print("Invalid Input.Enter a number(1~8)")
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
    elif c==5:
        edit(data_karvands)
    elif c==6:
        Delete(data_karvands)
    elif c==7:
        report(data_karvands)
    else:
        print("Invalid input.Try again")