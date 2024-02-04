from controller import Robot, Motor, DistanceSensor

robot = Robot()

TIME_STEP = 64

ps_list = []
ps_names = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for idx, name in enumerate(ps_names):
    ps_list.append(robot.getDevice(name))
    ps_list[idx].enable(TIME_STEP)
    
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)


while robot.step(TIME_STEP) != -1:
    ps_values = []
    for ps in ps_list:
        ps_values.append(ps.getValue())
    
    left_obstacle = ps_values[5] > 80.0 or ps_values[6] > 80.0 or ps_values[7] > 80.0
    right_obstacle = ps_values[0] > 80.0 or ps_values[1] > 80.0 or ps_values[2] > 80.0
                     
    MAX_VELOCITY = 6.28
    
    left_speed = 0.5 * MAX_VELOCITY
    right_speed = 0.5 * MAX_VELOCITY
    
    if left_obstacle:
        right_speed *= -1
    elif right_obstacle:
        left_speed *= -1
    
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)  


