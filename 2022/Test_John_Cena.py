import math

x1 = 0
y1 = 0

def goto(target_x, target_y, reverse):
    global x1, y1
    brain.screen.print("Starting from ", x1, y1)
    brain.screen.next_row()
    brain.screen.print("Going to ", target_x, target_y)
    brain.screen.next_row()
    brain.screen.print("My heading is", drivetrain.heading(DEGREES))
    brain.screen.next_row()
    #x1 = gps.x_position(MM)
    #y1 = gps.y_position(MM)
    #ni mei you ta jia 
    delta_x = target_x - x1
    delta_y = target_y - y1
    distance = math.sqrt(delta_x**2 + delta_y**2)     # pythagorean theorem
    if ( delta_x == 0 ):
        if ( delta_y < 0):
            direction = 90
        else:
            direction = 270
    else:
        direction = - math.atan(delta_y / delta_x) * 180 / math.pi
    if ( delta_x < 0 ):
        direction = direction + 180
    if ( reverse != 0 ):
        direction = direction + 180
    if ( direction > 360 ):
        direction = direction - 360
    brain.screen.print("Now turning heading to", direction)
    brain.screen.next_row()

    drivetrain.turn_to_heading(direction, DEGREES, wait=True)
    brain.screen.print("My heading is", drivetrain.heading(DEGREES))
    brain.screen.next_row()
    if ( reverse != 0 ):
        drivetrain.drive_for(REVERSE, distance, MM, wait=True)
    else:
        drivetrain.drive_for(FORWARD, distance, MM, wait=True)
    brain.screen.print("My heading is", drivetrain.heading(DEGREES))
    brain.screen.next_row()
    x1 = target_x
    y1 = target_y

def main():
    x1 = -1350
    y1 = 1420
    goto( -920,  920, 0)
    goto( -920,-1450, 0)
    goto(  750,-1400, 0) # blue in right zone
    goto(  500,-1150, 1)
#   goto(    0, -950, 0) # m = - 2/5
    goto( -600, -710, 0) # yellow in left zone
    goto(  400, -250, 1)
    goto(    0,    0, 0) # m = - 5/8
    goto( -600,  200, 0) # yellow in left zone
    goto(  400,  400, 1)
    goto(    0,  950, 0)
    goto( -600,  950, 0) # yellow in left zone
    goto(  920,  950, 1)
    goto(  920, 1500, 0)
    goto( -600, 1320, 0) # red in left zone
    goto(  600,  600, 1)
    goto(  600, -600, 1)
    goto( 1400,-1350, 1)
    goto( 1500, -900, 0) # red on balance
    goto( 1500,  100, 0)
