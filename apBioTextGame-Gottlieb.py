import random as rand

directions = "Welcome to the Kevin's AP Bio Semester 1 Review! Slay dragons with correct answers and fall prey their devestating wind attacks with wrong answers! Press S for settings or Enter to Start \n"

playerHp = 100
dragonHp = 100

playerDamage = 10 # The damage the player does to the dragon
dragonAttack = 20 #The damage the dragon does to the player for incorrect questions

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
	dragonHp -= playerAttack
	checkHp()

def dragonAttack():
	playerHp -= dragonAttack
	checkHp()

# Start Game	
print(quijoteStanding)	

start = getInput(directions, type='str')
if(start == 'S' or start == 's'):
	playerHp = getInput("Player HP (default 100):", type='int')
	dragonHp = getInput("Dragon HP (default 100):", type='int')
	playerDamage = getInput("Player Damage for each correct answer (default 10):", type='int')
	dragonDamage = getInput("Dragon Damage for each incorrect answer (default 20):", type='int')
else: #start Game!
	print(1+1)