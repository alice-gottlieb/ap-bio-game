import random as rand

directions = "Welcome to the Kevin Gottlieb's AP Bio Semester 1 Review! \n Slay dragons with correct answers (Make sure they're capital letters!) and fall prey to their devestating wind attacks with wrong answers! Press S for settings or Enter to Start \n"

playerHp = 100
dragonHp = 100

playerDamage = 20 # The damage the player does to the dragon
dragonDamage = 20 #The damage the dragon does to the player for incorrect questions

questionNum = 0 #number of questions already asked

# Bank of all questions
questionBank = ["Which is NOT an element that is common in life?", \
"Which of the following is NOT a property of water?", \
"Which of the following contains a trans bond?", \
"An amphiphatic molecule...", \
"Co-transport is...", \
"Which is a monomer?", \
"Hemeglobin is made of multiple polypeptide subunits. What is the highest level of structure it has?", \
"If a solution has a water potential of 10 Pa and a pressure potential of 3 Pa, what is its solute potential?", \
"Which of the following supports the endosymbiotic theory?"]
# Bank of all multiple choice responses
responseBank = ["A: K \n B: H \n C: C \n D: Mn \n", \
"A: Cohesion \n B: Adhesion \n C: High vapor pressure \n D: High boiling point \n", \
"""A:
 H     H
  \   /
   C=C
  /   \ 
 X     X

B:
 X     H
  \   /
   C=C
  /   \ 
 H     X
"""
, \
"A: Has both positively and negatively charged ends. \n B: Is present in all membrane formation \n C: Has both hydrophobic and hydrophilic portions \n D: Is critical to facilitated diffusion \n", \
"A: A type of facilitated diffusion \n B: Unable to transfer molecules against their concentraion gradients \n C: Uses vesicles for transport \n D: A and B \n E: A and C \n", \
"A: Peptides \n B: Disaccharides \n C: Amines \n D: Nucleotides \n",
"A: Primary \n B: Secondary \n C: Tertiary \n D: Quaternary \n",
"A: 13 kPa \n B: 13 Pa \n C: 7 Pa \n D: 30 Pa \n", \
"A: Chroloplasts absorb green light best and plants appear green \n B: Mitochondria contain their own set of DNA \n C: Mitochondria are the common to all eukaryotes \n D: Chroloplasts are not present in animals \n"]

# Bank of correct answers
correctBank = ["D", \
"D", \
"B", \
"C", \
"A", \
"D", \
"D", \
"C", \
"B"]

totalQuestionNum = len(questionBank)

questionOrder = rand.sample(range(int(totalQuestionNum)), int(totalQuestionNum)) #step through this list to choose the next question

quijoteStanding = """                  /\       ,,                                        ./
          .---.   ||      /||                                       //
       --'-----`--||    .'  \                                      //
         {{{N `(  ||  .'    @                                     //
         {{{` _/  ||.'    |  \                        _________ _//
         {{{.-.   ||  /  /\   \                        "-------(_)
          {( )| .'||    /  `.  \                               | \\
__        {|\ \'  / )  /     \\O|                              |_|\\
  `-.____.-| \ \ /\/  /       `'                               |_| \\
 -     ////|  \ Y /| |                                         [ ]  \\
   |   |||||`-|\^/|| |                                         F-J   `\
       |||||`-| " [] /                                        J.-'L 
     _ \\\\/`-|   []|\                                        ]`-.[
 ) |`---``| _ |__([]| \                                       |.-'|
  /       |/ `|   FJ|\ \                                      [`-.]
 /        `|  |   FJ) \ \                                     F.-'J
/          |  |   FJ|  \ )                                   J -._ L
|          |  F  J  L  ||                                    ]    >[
`.         )-(> '----` ||                                    | .-' |
`.\        | |    |||  ||                                    [<    ]
| \\       |-|    ||| / |                                    F `-. J
 \ )\    *_)/`-.__|| \\ |                                   J     ` L"""
 

quijoteCharging = """                _~}                                 _      _
             _(<\_-~=.                          /\//_    _\\/\
         _=/`  `+--/\|                          `7/\/    \/\\'
_______~~  \ )-`\ 7 _____________________x___X___Z_\______/_T______
          `/ \  / >
          '   `   ' """
		  
quijoteOverwhelmed = """    _         _         _         _           _         _
/\//_     /\//_     /\//_     /\//_    _  /\//_     /\//_    _
`7/\/   _ `7/\/   _ `7/\/   _ `7/\/ /\//_ `7/\/   _ `7/\/ /\//_    _
 Z_\ /\//_ l_\ /\//_ T_\ /\//_ T_\  `7/\/  l_\ /\//_ Z_\  `7/\/ /\//_
     `7/\/     `7/\/     `7/\/       Z_\       `7/\/       T_\  `7/\/
   _  T_\   _   T_\     _ Z_\    *              T_\              l_\
/\//_    /\//_    _  /\//_        \   ~
`7/\/    `7/\/ /\//_ `7/\/     _,, \ {]            ?
 l_\      Z_\  `7/\/  T_\     "-=\;_\ %        \` ( )
                T_\             _ \\;(#)%     /" \_x\_
                              _\| \_%%        `'\   / )`~
                              \  \/\  \         ( ) ' |
                                    ( )~~~      | |   `
                                    | \         ` `
                                   /  / """
		  

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

def checkHp():
	if(playerHp <= 0):
		print("You died! :-(")
		return 1 # Shows the player has died
	elif(dragonHp <= 0):
		print("You won! :-)")
		return 2
	else:
		return 0 #Show that neither dragon nor player is dead			

def playerAttack():
	global dragonHp
	dragonHp -= playerDamage
	print(quijoteCharging)

def dragonAttack():
	global playerHp
	playerHp -= dragonDamage
	print(quijoteOverwhelmed)
	
def showStats():
	print("Your HP: " + str(playerHp))
	print("Dragon's HP: " + str(dragonHp))

def askQuestion(qn):
	if(qn >= totalQuestionNum):
		print("It seems we've run out of questions, you win by default!")
		global dragonHp
		dragonHp = 0
	else:
		currentQuestion = questionOrder[qn]
		print(questionBank[currentQuestion] + "\n")
		currentAnswer = getInput(responseBank[currentQuestion], type='str')
		if(currentAnswer == correctBank[currentQuestion]):
			playerAttack()
			print("Great job!")
		else:
			dragonAttack()
			print("Better luck next time! The correct answer was:" + correctBank[currentQuestion])

def startGame():
	global playerHp
	global dragonHp
	
	# Start Game	
	print(quijoteStanding)	

	start = getInput(directions, type='str')
	if(start == 'S' or start == 's'):
		playerHp = getInput("Player HP (default 100):", type='int')
		dragonHp = getInput("Dragon HP (default 100):", type='int')
		playerDamage = getInput("Player Damage for each correct answer (default 20):", type='int')
		dragonDamage = getInput("Dragon Damage for each incorrect answer (default 20):", type='int')
		
	while(checkHp() == 0):
		showStats()
		global questionNum
		askQuestion(questionNum)
		questionNum += 1
	
	if(getInput("Would you like to play again? Y/N \n", type='str') == "Y"):
		playerHp = 100
		dragonHp = 100
		questionNum = 0
		global questionOrder
		questionOrder = rand.sample(range(int(totalQuestionNum)), int(totalQuestionNum))
		startGame()
	
startGame()