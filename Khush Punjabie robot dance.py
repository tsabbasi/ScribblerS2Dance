# Khush Punjabies ("Happy" & "Mundian To Bach Ke" mix)
 # Deshaun Crawford, Tuba Abbasi, Jomah Kpengba, Brandon Gaymond,and Francisco Cruz
from Myro import *
from robots import *
from SdlDotNet.Audio import *
import random

# Variables
m = Music('/Users/Deshaun/Desktop/Kush Panjabi Song.aiff')
brandon = makeRobot("Scribbler",brandonBot) # Felix
tuba = makeRobot("Scribbler",tubaBot) # Ju Ju Ba
deshaun = makeRobot("Scribbler",deshaunBot) # Betty
jomah = makeRobot("Scribbler",jomahBot) # Oscar
francisco = makeRobot("Scribbler",franciscoBot) # Cisco

# Intro Functions

def intro(): # Introduction speech
    #Female first
    setVoice('hy-west+f1')
    
    deshaun.moveBy(100,0)
    speak('Hello, my name is Betty.')
    deshaun.moveBy(-100,0)
    tuba.moveBy(100,0)
    speak('Hello, my name is JujuBa.')
    tuba.moveBy(-100,0)
    #Male next
    setVoice('default')
    
    francisco.moveBy(100,0)
    speak('Hi, my name is Cisco.')
    francisco.moveBy(-100,0)
    jomah.moveBy(100,0)
    speak('Hello, my name is Oscar.')
    jomah.moveBy(-100,0)
    brandon.moveBy(100,0)
    speak('Hello, my name is Felix.')
    brandon.moveBy(-100,0)
    
# Functions
def normalizeIR(value):
    ''' This function normalizes a given IR value. 1 = 0 and 0 = 1.
'''
    if value > 1:
        value = 1
    elif value < 0:
        value = 0
    return(1-value)

def scatter(robot):
    ''' This function will make the robots scatter to asssigned positions
        across the floor.
'''
    robot.setPosition(0,0)
    robot.setAngle(0)
    if robot != deshaun or robot != jomah:
        robot.moveBy(300,100)
    else:
        robot.moveBy(300,-100)

def shake(robot):
    ''' This function will make the robots turn left then to original position then
    the robots will repeat the same thing to the right side.
'''
    robot.setAngle(0)
    robot.turnBy(45)
    robot.turnTo(0)
    robot.turnBy(-45)
    robot.turnTo(0)

def shakeTwice(robot):
    ''' This function does the does the shake function twice.
'''
    robot.setAngle(0)
    robot.turnBy(45)
    robot.turnTo(0)
    robot.turnBy(-45)
    robot.turnTo(0)
    robot.setAngle(0)
    robot.turnBy(45)
    robot.turnTo(0)
    robot.turnBy(-45)
    robot.turnTo(0)

def saveABot(robot):
    ''' This function calls upon betty to go to a
    appointed position to trigger JujuBa's IR Sensor
    and make her stop.
    '''
    robot.setAngle(0)
    robot.setPosition(0,0)
    robot.turnTo(180)
    robot.setPosition(0,0)
    robot.moveBy(-300,-250)

def tantrum(robot):
    ''' This function makes a robot go back and forth untill IR sensor
is triggered.
'''
    while True:
        if normalizeIR(robot.getIR('right')) == 0:
            robot.backward(-1,.01)
            robot.backward(1,.01)
        elif normalizeIR(robot.getIR('right')) == 1:
            stop()
            break
    stop()

def turnAround(robot):
    ''' This function makes a robot turn to the left 180 degrees.
'''
    robot.setAngle(0)
    robot.turnTo(180)

def returnTo(robot):
    ''' This function sends a robot to its orginal coordinates.
'''
    robot.moveTo(0,0)
    robot.turnTo(0)

def becomingHappy(robot):
    ''' This function turns a depressed robot 180 degress then it
will spin from happiness.
'''
    robot.setAngle(0)
    robot.turnTo(180)
    wait(1.5)
    for i in timer(5):
        doTogether([brandon.turnBy,180],[tuba.turnBy,180])

def spinTwo(robot1,robot2): # all spin functions are to make the robots spin on happy in order of availabiblity
    for r in timer(5):
        doTogether([robot1.setAngle,0],[robot2.setAngle,0])
        doTogether([robot1.turnBy,180],[robot2.turnBy,180])

def spinFour(robot1,robot2,robot3,robot4):
    for robot in timer(5):
        doTogether([robot1.setAngle,0],[robot2.setAngle,0],[robot3.setAngle,0],[robot4.setAngle,0])
        doTogether([robot1.turnBy,180],[robot2.turnBy,180],[robot3.turnBy,180],[robot4.turnBy,180])

def spinAll(robot1,robot2,robot3,robot4,robot5):
    for robot in timer(5):
        doTogether([robot1.setAngle,0],[robot2.setAngle,0],[robot3.setAngle,0],[robot4.setAngle,0],[robot5.setAngle,0])
        doTogether([robot1.turnBy,180],[robot2.turnBy,180],[robot3.turnBy,180],[robot4.turnBy,180],[robot5.turnBy,180])

# Solo functions

def ciscoSolo(robot):
    robot.setAngle(0)
    robot.setPosition(0,0)
    robot.turnBy(90)
    robot.turnBy(-2*90)
    robot.turnBy(90)

def ciscoSolo2(robot):
    robot.moveBy(100,0)
    robot.moveBy(-100,0)
    robot.setAngle(0)
    robot.turnBy(45)
    robot.turnTo(0)
    robot.turnBy(180)

def oscarSolo(robot):
    robot.moveTo(300, 0)
    robot.turnBy(75)
    robot.turnBy(-75)
    robot.turnBy(-75)
    robot.turnBy(75)
    robot.turnBy(75)
    robot.turnBy(-75)
    robot.turnBy(-75)
    robot.turnBy(75)
    robot.moveTo(260, 0)

def felixSolo(robot):
    wait(1)
    robot.moveBy(500,0)
    robot.turnBy(-45)
    robot.turnBy(90)
    robot.turnBy(-45)
    robot.moveBy(150,0)
    robot.turnBy(180)


def juJuBaSolo(robot):
    robot.setPosition(0,0)
    robot.moveBy(50,0)
    robot.turnBy(45)
    robot.moveBy(90,0)
    robot.turnBy(180)
    robot.turnBy(180)

def bettySolo(robot):
    for time in timer(5):
        robot.motors(random.uniform(-1,1),random.uniform(-1,1))

    robot.stop()



# Solo Spectator functions

# Gets others out of the way for the robots to do their solos

def leftWatch(robot):  # Brandon
    robot.moveBy(-200,0)
    robot.turnBy(90)
    robot.moveBy(0,-200)
    robot.turnBy(90)
    shake(robot)

def getInLine(robot): # Brandon
    ''' The robot Felix will join the other robots.
'''
    robot.moveBy(-750,0)
    robot.turnBy(180)



def jomahWatch(robot):
    '''This function gets Oscar out of the way for Felix's solo.
'''
    robot.moveBy(0,350)
    robot.moveBy(-515,0)
    robot.moveBy(0,300)

def centerWatch(dRobot,tRobot): # Deshaun & Tuba
    ''' CenterWatch function makes the robots perform the shake dance routine
    while other robots perform solos.
'''
    wait(5)
    doTogether([shake,dRobot],[shake,tRobot])
    doTogether([shake,dRobot],[shake,tRobot])
    doTogether([shake,dRobot],[shake,tRobot])


def centerWatch2(dRobot,tRobot,fRobot): # Deshaun, Tuba & Francisco
    doTogether([shake,dRobot],[shake,tRobot],[shake,fRobot])
    doTogether([shake,dRobot],[shake,tRobot],[shake,fRobot])
    doTogether([shake,dRobot],[shake,tRobot],[shake,fRobot])

def centerWatch3(dRobot,fRobot,jRobot): # Francisco, Jomah & Deshaun
    jRobot.turnBy(-90)
    fRobot.moveBy(200,0)
    wait(2)
    doTogether([shake,dRobot],[shake,fRobot],[shake,jRobot])

def centerWatch4(dRobot,fRobot,jRobot,bRobot):
    doTogether([shake,dRobot],[shake,tRobot],[shake,fRobot],[shake,bRobot])

def franciscoWatch(robot):
    ''' The robot cisco will move away because he has already done his solo.
'''
    robot.moveBy(-400,0)
    robot.turnBy(-90)
    robot.moveBy(0,700)
    robot.turnBy(-90)

# Dance sequences

def scatterSequence():
    ''' This function has all parts of the scatter sequence.
'''
    doTogether([scatter,deshaun],[scatter,tuba],[scatter,francisco],[scatter,jomah],[scatter,brandon])
    wait(1)
    doTogether([deshaun.moveTo,0,0],[tuba.moveTo,0,0],[francisco.moveTo,0,0],[jomah.moveTo,0,0],[brandon.moveTo,0,0])
    doTogether([deshaun.turnTo,0],[tuba.turnTo,0],[francisco.turnTo,0],[jomah.turnTo,0],[tuba.turnTo,0],[brandon.turnTo,0])
    wait(1)

def shakeSequence():
    ''' This function consists of all parts of the shake sequence.
'''
    doTogether([shake,deshaun],[shake,tuba],[shake,francisco],[shake,jomah],[shake,brandon])
    wait(.5)
    doTogether([turnAround,deshaun],[turnAround,tuba],[turnAround,francisco],[turnAround,jomah],[turnAround,brandon])
    doTogether([shake,deshaun],[shake,tuba],[shake,francisco],[shake,jomah],[shake,brandon])

def spinSequence():
    ''' This function consists of all parts of the spin sequence.
'''
    doTogether([returnTo,jomah],[becomingHappy,tuba],[ciscoSolo2,francisco],[returnTo,deshaun],[becomingHappy,brandon])
    doTogether([spinTwo,deshaun,jomah],[shake,tuba],[shake,francisco],[shake,brandon])
    wait(.5)
    doTogether([spinFour,deshaun,tuba,jomah,brandon],[shake,francisco])
    spinAll(deshaun,tuba,francisco,jomah,brandon)

def soloSequence():
    ''' This function consists of the second part of the Khush Punjabie song dance
the rest of the robots do their solos.
'''
    doTogether([oscarSolo,jomah],[leftWatch,brandon],[franciscoWatch,francisco],[centerWatch,deshaun,tuba])
    doTogether([felixSolo,brandon],[jomahWatch,jomah],[centerWatch2,deshaun,tuba,francisco])
    doTogether([juJuBaSolo,tuba],[getInLine,brandon],[centerWatch3,deshaun,francisco,jomah])
    bettySolo(deshaun)
    doTogether([bettySolo,deshaun],[bettySolo,francisco],[bettySolo,jomah],[bettySolo,tuba],[bettySolo,brandon])

# Intro Sequence (Robots introduce themselves.)
doTogether([robot1.setPosition, 0, 0],[robot2.setPosition, 0, 0],[robot3.setPosition, 0, 0],[robot4.setPosition, 0, 0],[robot5.setPosition, 0, 0])
doTogether([robot1.setAngle,0],[robot2.setAngle,0],[robot3.setAngle,0],[robot4.setAngle,0],[robot5.setAngle,0])
intro()

    # Dance Begins here
print('Running the Dance routine...')
m.Play()
scatterSequence()
shakeSequence()
        # IR sensor sequence
doTogether([saveABot,deshaun],[tantrum,tuba],[ciscoSolo,francisco],[saveABot,jomah],[tantrum,brandon])
spinSequence()
wait(2) # ("Voice over" new song begins)
doTogether([deshaun.turnTo,0],[tuba.turnTo,0],[francisco.turnTo,0],[jomah.turnTo,0],[tuba.turnTo,0],[brandon.turnTo,0])
soloSequence()
print('Dance complete !')



