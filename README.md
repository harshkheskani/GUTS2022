# GTUS2022

Glasgow university tech society Hackthon 2022 
Morgan Stanleys project.

# The Challenge

### Build an AI Bot to compete in MS Gauntlet, a retro-styled game inspired by the 1980s classic 

* Build your bot in any language that supports UDP socket communication.
* Control your bot via an API, and receive information about the world from the server. 
* Survive, find treasure and get to the exit!
 
[[https://github.com/NickMcCrea/MSGUTS2022/blob/ac752cbfe681474d859cbe9cd1a2655b5e046141/WikiImages/StartScreen.PNG]]

# What You Need to Do

* Grab the server / sample bot from the repo. Running the server may need you to install dotnet core 6 for your platform (e.g. Linux / Mac) - [.NET 6.0](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) > .NET Runtime 6.0.10
  * Once installed on MacOS/Linux: dotnet <path/to/MSGauntlet.dll>
* **READ THESE INSTRUCTIONS**
* Write a bot in a language that supports UDP (i.e. almost any). 
* Use the network API to spawn a character on the server. 
* Use the information the server provides about the environment to navigate your way around.
* Survive, battle your enemies, collect treasure.
* Find your respective key, then head to the exit! 


# The Dungeon

The dungeon is randomly generated, and contains a number of items:
1. Food. Increases health if picked up.
2. Ammo. 
3. Colour coded keys, one per player.
4. Treasure.
5. An exit!

[[https://github.com/NickMcCrea/MSGUTS2022/blob/ac752cbfe681474d859cbe9cd1a2655b5e046141/WikiImages/dungeon.PNG]]


# Understanding the World

* Dungeons are composed of floor tiles and wall tiles. 
* The server informs clients of nearby dungeon tiles, in a radius around the player.
* The server informs clients of nearby items (keys, food, ammo, players, exit). 
* Dungeon tiles are 8x8 in size. 
* The X,Y coordinates are the center of the tile. 

[[https://github.com/NickMcCrea/MSGUTS2022/blob/355ae4380cb4017b44cd84893f19f750e95f4e7b/WikiImages/warrior.PNG]]

# API

* Messages are simple string format - "messagetype:argument1,argument2,argument3..."
* Messages are sent via UDP. This is a connection-less protocol, that does not guarantee delivery or order. 
* Connections to port 11000.
  * Note: This will be localhost(127.0.0.1) on your local machine - however address and port should be parameters as these will be different during the challenge phase when connecting to our server.

**Please be aware at initial boot the server is in LOBBY mode and will not accept any API messages until you hit the SPACE BAR on the client window**

## Client to Server Messages - commands the client can send to the server



* requestjoin:name  (name should be a short string display name unique to your bot). 
* moveto:posX,posY (this will attempt to move in a straight line, no pathfinding)
* fire:
* facedirection:direction (where direction can be n,s,e,w,ne,nw,se,sw)
* movedirection:direction (where direction can be n,s,e,w,ne,nw,se,sw)
* stop:


## Server to Client Messages - information the server sends to clients

* playerjoined:character_class,display_name,posX,posY
* playerupdate:posX,posY,health,ammo,hasKey
* nearbywalls:posX,posY,posX,posY,posX,posY.....  (posX,posY pairs will repeat for every nearby wall segment)
* nearbyfloors:posX,posY,posX,posY,posX,posY....  (posX,posY pairs will repeat for every nearby floor segment)
* nearbyitem:itemType,posX,posY
* nearbyplayer:character_class,name,posX,posY
* exit:posX,posY

# Character Classes

* Warrior - Red
* Elf - Green
* Wizard - Yellow
* Valkyrie - Blue

The above is IMPORTANT - as the keys are coloured to your class. You cannot pick up another classes key.

# Config / Control Options

* There is a config file allowing you to change some options - **GauntletConfig.txt**
* Dungeon size can be "s", "m", or "l" - useful to make it small during testing.
* If you enable manual player one / two, the game will spawn a manual player to help with testing. Control with WSAD or IJKL, and left / right ctrl to fire. 
* Dungeoneditmode - if enabled, no items will spawn. You can hand place everything using numpad 0-7 (exit and items), and F1-F4 (character spawn points)
* Use C, V, B or N to set the camera to follow the warrior, valkyrie, elf or wizard respectively. 
* Use X to set the camera back to manual mode. 

# Judging Criteria

* We will hold a competition at the end of the hackathon to determine our greatest dungeon crawlers, with heats / final depending on the number of contestants.
* The game is scored - your final score will be a combination of treasure collected, time to find the exit, and number of kills. 
* We reserve the right to reward particularly insane / amusing strategies.


# Tips

* The key challenge here is navigation. Your bot will have only limited information about the world around it.
* You could build up a more complete picture of the dungeon by wandering and storing / remembering what you see. 
* Visualise what your bot is doing! It really helps...

[[https://github.com/NickMcCrea/MSGUTS2022/blob/c6f2fc33f0da0ca451d3295bf34389f3de6302e4/WikiImages/botNavigation.PNG]]
