def getInput(prompt, type="None"):
	if(type == "None"):
		return input(prompt)
	elif(type == "int"):
		try:
			return int(input(prompt))
		except ValueError:
			return 0
	elif(type == "str"):
		try:
			return str(input(prompt))
		except ValueError:
			return ""		
			
print(getInput("Give me a number:", type="int"))