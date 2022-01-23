from cisc108 import assert_equal
def render_introduction():
    '''
    Create the message to be displayed at the start of your game.

    Returns:
        str: The introductory text of your game to be displayed.
    '''
    return("==Game== \n"+
               "=By Donavan Franco="+
               """"
                      />_________________________________
   [########[]_________________________________/
                      \>               """+
                "\nYou wake up not knowing where you are but you know you need something......but what it is you know not \n"+
                "You look around and see a dark corridor")
    ###
def create_player():
    return {
        'location': 'a flowerbed',
        'inventory': [],
        'status': ["Sleepy"]
        }

def create_map():
    return {
        'a flowerbed': {
            'neighbors': ['dark corridor'],
            'about': "A pretty bed of flowers, shining with many different colors",
            'stuff': [],
        },
        'dark corridor': {
            'neighbors': ['a flowerbed','dark hole','dark room'],
            'about': "It is dark here. You have a sixth sense for something",
            'stuff': ["Potato"]
        },
        'dark hole': {
            'neighbors': ['dark corridor'],
            'about': "It is dark here. Just....nothingness",
            'stuff': ["Red rock"]
        },
        'dark room': {
            'neighbors': ['dark corridor','lumpy shrine','attic'],
            'about': "A room with only a single table",
            'stuff': ["Potato"]
        },
        'lumpy shrine': {
            'neighbors': ['dark room', 'potato field'],
            'about': "There seems to be a shrine holding a potato",
            'stuff': ["Potato"]
        },
        'attic': {
            'neighbors': ['dark room','blue room'],
            'about': "nothing here but a potato and a gold bar",
            'stuff': ["Potato", "Shiny orb"]
        },
        'blue room': {
            'neighbors': ['attic', 'lumpy shrine'],
            'about': "A room that is painted blue and decorative clouds fill the air, the bed has a glimmering red potato and gold bar on it, how odd....maybe we should leave the items alone",
            'stuff': ["Evil Potato", "Gold Bar"]
        },
        'potato field': {
            'neighbors': ['lumpy shrine'],
            'about': "A blissfull room, where there is no worries, you feel sleepy and make a bed with your potatos, goodnight",
            'stuff': ["Starlight Potato"]
        }
  }

def create_world():
    '''
    Creates a new version of the world in its initial state.

    Returns:
        World: The initial state of the world
    '''
    return {
        'map': create_map(),
        'player': create_player(),
        'status' : "playing"
        }

def render_location(world):
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    stuff=here['stuff']
    return ("You are in "+location+"\n"+
          about+"\n" )
"""   visible_stuff=", ".join(stuff)
    if len(visible_stuff)<1:
        visible_stuff="Nothing in sight"
"""

def render_visible_stuff(world):
    player=world['player']
    location = world['player']['location']
    here = world['map'][location]
    stuff = here['stuff']
    inventory = world['player']['inventory']
    visible_stuff = []
    for thing in stuff:
        if thing=="Starlight Potato":
            if "Determined" in player['status']:
                visible_stuff.append(thing)
        else:
            visible_stuff.append(thing)
        

    return "You see: " + ', '.join(visible_stuff)

def render_player(world):
    player=world['player']
    inventory = player['inventory']
    status=player['status']
    holdboi="You have: " + ", ".join(inventory)
    statusboi="Your current status is: " +", ".join(status)
    return statusboi+"\n" +holdboi

def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.

    Args:
        world (World): The current world to describe.

    Returns:
        str: A textual description of the world.
    '''
    return (render_location(world) +
        render_player(world))

######################################################


def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.

    Args:
        world (World): The current world to get options for.

    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    things=render_visible_stuff(world)
    location=world['player']['location']
    here = world['map'][location]
    commands = ["quit","look around"]
    for items in here["stuff"]:
        if items in things:
            commands.append("take " + items)
        else:
            pass
    for place in here["neighbors"]:
        commands.append("Go to " + place)
    return commands



def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.

    Args:
        world (World): The current world to modify.

    Returns:
        str: A message describing the change that occurred in the world.
    '''
    player=world['player']
    location=world['player']['location']
    here = world['map'][location]
    if "Starlight Potato" in player["inventory"]:
        world['status']='win'
    elif "Red rock" in player["inventory"]:
        world['status']='lose'
    elif "Shiny orb" in player["inventory"] and "Determined" not in player['status']:
        player['status'].remove("Sleepy")
        player['status'].append("Determined")
    elif command == "quit":
        world['status'] = 'quit'
        return "You quit the game"
    elif "take" in command:
        for items in here["stuff"]:
            if command == ("take " + items):
                player["inventory"].append(items)
                here["stuff"].remove(items)
                return ("You took: {}".format(items))
            else:
                pass
    elif "Go to" in command:
        for place in here["neighbors"]:
            if command==("Go to " + place):
                world["player"]["location"]=str(place)
                return("You moved to {}".format(place))
            else:
                pass
    elif command=="look around":
       return(render_visible_stuff(world))
    ###################################
    if world['status']!='lose':
        return "Unknown command: "+command
    else:
        pass


def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.

    Args:
        world (World): The final world state to use in describing the ending.

    Returns:
        str: The ending text of your game to be displayed.
    '''
    if world['status']=='win':
        return("You won! Potatos for everyone!")
    elif world['status']=='lose':
        return("You lose!")
    else:
        return("What happened")
def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.

    Note:
        Use your answer to Programming Problem #42.3

    Args:
        options (list[str]): The potential commands to select from.

    Returns:
        str: The command that was selected by the user.
    '''
    print(options)
    choice=input("Choose an option: ")
    return choice
    
"""    
world= create_world()
world["player"]["location"]="blue room"
print(get_options(world))
print(update(world,"Go to attic"))
"""
############# Main Function ##############
# Do not modify anything below this line #
##########################################

def main():
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))

if __name__ == '__main__':
    main()