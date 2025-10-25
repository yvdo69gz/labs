def describe_person(name, age=30):
    return f"Имя: {name}, Возраст: {age}"

print(describe_person("Сергей"))
print(describe_person("Иван", 25))