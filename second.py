import os

first_name = os.environ.get("FIRST_NAME")
last_name = os.environ.get("LAST_NAME")

if not first_name and not last_name:
    print("Both FIRST_NAME and LAST_NAME environmental values are missing, set both of them and try again")
    exit(1)
if not first_name:
    print("FIRST_NAME environment value is missing, set it and try again")
    exit(1)
if not last_name:
    print("LAST_NAME environment value is missing, set it and try again")
    exit(1)

home_dir = os.path.expanduser("~")
tmp_dir = os.path.join(home_dir, "tmp")
os.makedirs(tmp_dir, exist_ok=True)

num_sub_dirs = 5
for i in range(num_sub_dirs):
    sub_dir = os.path.join(tmp_dir, f"training_project_{i+1}")
    os.makedirs(sub_dir, exist_ok=True)
    for file_type in ['a', 'b']:
        file_name = f"module_{i+1}_{file_type}.txt"
        file_path = os.path.join(sub_dir, file_name)
        content = f'Hello {first_name} {last_name} Welcome to file {i+1}.{file_type}'
        with open(file_path, 'w') as f:
            f.write(content)
print("The directories and txt files are successfully created")

