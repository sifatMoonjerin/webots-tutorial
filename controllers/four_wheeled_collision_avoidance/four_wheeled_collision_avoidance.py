from controller import Robot, Motor, DistanceSensor

robot = Robot()

TIME_STEP = 64

wheels = []
for i in range(1, 5):
    name = f'wheel_motor_{i}'
    wheels.append(robot.getDevice(name))

    
ds_left = robot.getDevice('ds_left')
ds_right = robot.getDevice('ds_right')
ds_left.enable(TIME_STEP)
ds_right.enable(TIME_STEP)

def updateSpeed(wheels, direction = 1):
    speed = 1 * direction
    for wheel in wheels:
        wheel.setPosition(float('inf'))
        wheel.setVelocity(speed)
    
avoid_obstacle_counter = 0

while robot.step(TIME_STEP) != -1:
    if avoid_obstacle_counter > 0:
        avoid_obstacle_counter -= 1
        if avoid_obstacle_counter == 80:
            updateSpeed(wheels[2:], 1)
        continue
        
    ds_left_val = ds_left.getValue()
    ds_right_val = ds_right.getValue()
    
    updateSpeed(wheels)
        
    if ds_left_val < 1000 or ds_right_val < 1000:
        avoid_obstacle_counter = 100
        updateSpeed(wheels, -1)

    pass
