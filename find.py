import os

print("Python sucht hier:")
print(os.getcwd())

print("Dateien hier:")
print(os.listdir())

print("Findet Python test.csv?")
print(os.path.exists("test.csv"))