text = "all zip files are zipped"
first_index = text.find('zip')
second_index = text.find('zip',first_index+1)
print(second_index)
