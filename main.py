with open('file3.csv', 'r') as file:
  content = file.read()

#Get all the characters except the last one. Using this slicing operation.
#This slicing is suitable when the file contains strings.
modified_content = (content[:-1])

with open('file3_modified.csv', 'w') as file:
  file.write(modified_content)