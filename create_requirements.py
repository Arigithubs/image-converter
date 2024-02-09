# Script to create a requirements.txt file

required_packages = ["Pillow"]

with open("requirements.txt", "w") as file:
    for package in required_packages:
        file.write(package + "\n")

print("requirements.txt file created successfully.")
