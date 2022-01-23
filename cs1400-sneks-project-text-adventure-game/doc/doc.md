# Project 5) Text Adventure Game

See complete instructions in Canvas.

## Requirements

- Your game should be original, to some degree. Do not reproduce an existing
  game, although original persepctives or unique takes on existing games are ok.
- You should include sample win and lose paths (one of each) in the `paths.py`
  file. These paths are the commands a user might enter if they were going to
  win or lose the game, respectively.
- You must have a `get_options()` function that, when given a world dictionary,
  determines the player's current status (e.g., location) and returns a list of
  available commands for the user to select from.
- You must have an `update()` function that, when given a world dictionary and a
  command, updates the world based on the command and returns a string that
  describes the results of executing the given command.
- You must not call the `print()` or `input()` functions inside of any function
  definition other than the `choose()` and `main()` functions.
- The user should be able to move around the map.
- The map should be large enough to make the game interesting.
- The user should be able to quit the game from any location in the map (i.e.,
  the "quit" command should always be available).
- You should have extra logic other than moving around the map (e.g., picking up
  and using items).
- Do not use external libraries.
