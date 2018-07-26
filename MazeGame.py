#! /usr/bin/python3

def showInstructions():
    print('''
    RPG Game
    ===========
    Commands:
        go[direction]
        get[item]
    ''')
    
def showStatus():
    print("-----------------------")
    print('you are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    
inventory = []

rooms = {
        'Hall':{'south':'Kitchen','east':'Dining Room','item' : 'key'},
        'Kitchen':{'north':'Hall','east':'Garden','item':'monster'},
        'Dining Room':{'west' :'Hall','south' : 'Garden','item':'potion'},
        'Garden' : {'north' : 'Dining Room','west' : 'Kitchen'}
    }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()
    move =''
    while move == '':
        move = input('>')
    
    move = move.lower().split()
    
    if move[0]=='go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You cant\'t go that way!")
    if move[0]=='get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
            #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print("A monster has got you ... GAME OVER!")
        break        
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("You escaped the house.... YOU WIN!")
        break
    