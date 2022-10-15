import socket
import time
import random
import numpy
 

msgFromClient       = "requestjoin:mydisplayname"
name = "mydisplayname"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 11000)

bufferSize          = 1024

#bunch of timers and intervals for executing some sample commands
moveInterval = 10
timeSinceMove = time.time()

fireInterval = 5
timeSinceFire = time.time()

stopInterval = 30
timeSinceStop = time.time()

directionMoveInterval = 15
timeSinceDirectionMove = time.time()

directionFaceInterval = 9
timeSinceDirectionFace = time.time()

directions = ["n","s","e","w","nw","sw","ne","se"]


# Create a UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 



def SendMessage(requestmovemessage):
    bytesToSend = str.encode(requestmovemessage)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

observationMatrix = [[],[],[]]
# [[x][y][item code]]
while True:

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)[0].decode('ascii')
    
    ##uncomment to see message format from server
    #print(msgFromServer)
    #Item codes:
    # floors = 0
    # walls = 1
    # items = {food:2,ammo:3, keys:[(r,4),(g,5),(b,6),(y,7)], treasure:8}
    # exit = 9
    if "nearbyitem" in msgFromServer:
        item = msgFromServer.split(":")[1]
        itemSplit = item.split(",")
        posX = itemSplit[1]
        posY = itemSplit[2]
        itemName = itemSplit[0]
        observationMatrix[0].append(posX)
        observationMatrix[1].append(posY)
        match itemName:
            case "food":
                observationMatrix[2].append(2)
                break
            case "ammo":
                observationMatrix[2].append(3)
                break
            case "redkey":
                observationMatrix[2].append(4)
                break
            case "greenkey":
                observationMatrix[2].append(5)
                break
            case "bluekey":
                observationMatrix[2].append(6)
                break
            case "yellowkey":
                observationMatrix[2].append(7)
                break
            case "treasure":
                observationMatrix[2].append(8)
                break

    if "nearbyfloors" in msgFromServer:
        floors = msgFromServer.split(":")[1]
        floorSplit = pos.split(",")
        for loc in floorSplit:
            if floorSplit.index(loc) // 2 == 0:
                observationMatrix[0].append(loc)
            else: 
                observationMatrix[1].append(loc)
                observationMatrix[2].append(0)
        
    if "nearbywalls" in msgFromServer:
        wall = msgFromServer.split(":")[1]
        wallSplit = pos.split(",")
        for loc in wallSplit:
            if wallSplit.index(loc) // 2 == 0:
                observationMatrix[0].append(loc)
            else: 
                observationMatrix[1].append(loc)
                observationMatrix[2].append(1)
        
    if "playerupdate" in msgFromServer:
        pos = msgFromServer.split(":")[1]
        posSplit = pos.split(",")
        posx = float(posSplit[0])
        posy = float(posSplit[1])

    if "exit" in msgFromServer:
        exitLoc = msgFromServer.split(":")[1]
        exitCoords = exitLoc.split(",")
        pos_x = exitCoords[0]
        pos_y = exitCoords[1]
        observationMatrix[0].append(pos_x)
        observationMatrix[1].append(pos_y)
        observationMatrix[2].append(9)


    now = time.time()

    #every few seconds, request to move to a random point nearby. No pathfinding, server will 
    #attempt to move in straight line.
    if (now - timeSinceMove) > moveInterval:
        randomX = random.randrange(-50,50)
        randomY = random.randrange(-50,50)
        posx += randomX
        posy += randomY

        timeSinceMove = time.time()
        requestmovemessage = "moveto:" + str(posx)  + "," + str(posy)
        SendMessage(requestmovemessage)
        print(requestmovemessage)

    #let's fire
    if (now - timeSinceFire) > fireInterval:
        timeSinceFire = time.time()
        fireMessage = "fire:"
        SendMessage(fireMessage)
        print(fireMessage)
       
        

    if(now - timeSinceStop) > stopInterval:
        stopMessage = "stop:"
        SendMessage(stopMessage)
        timeSinceStop = time.time()
        print(stopMessage)


    if(now - timeSinceDirectionMove) > directionMoveInterval:

        randomDirection = random.choice(directions)
        directionMoveMessage = "movedirection:" + randomDirection
        SendMessage(directionMoveMessage)
        timeSinceDirectionMove = time.time()
        print(directionMoveMessage)

    if(now - timeSinceDirectionFace) > directionFaceInterval:

        randomDirection = random.choice(directions)
        directionFaceMessage = "facedirection:" + randomDirection
        SendMessage(directionFaceMessage)
        timeSinceDirectionFace = time.time()
        print(directionFaceMessage)



