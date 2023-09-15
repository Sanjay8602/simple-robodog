from gpiozero import Robot, DistanceSensor
import time

# Define the robot with left and right motor pins
robot = Robot(left=(17, 18), right=(22, 23))

# Define the distance sensor for obstacle detection
distance_sensor = DistanceSensor(echo=24, trigger=25)

# Function to move the robot forward
def forward():
    robot.forward()
    print("Moving forward...")

# Function to move the robot backward
def backward():
    robot.backward()
    print("Moving backward...")

# Function to turn the robot left
def left():
    robot.left()
    print("Turning left...")

# Function to turn the robot right
def right():
    robot.right()
    print("Turning right...")

# Function to stop the robot
def stop():
    robot.stop()
    print("Stopping...")

# Function for obstacle avoidance
def obstacle_avoidance():
    while True:
        distance = distance_sensor.distance
        if distance < 20:  # Adjust this threshold as needed
            print("Obstacle detected!")
            stop()
            time.sleep(1)  # Pause briefly

            # Implement obstacle avoidance logic here
            # For example, turn right and then continue
            right()
            time.sleep(1)  # Adjust the turn duration as needed
            forward()
            time.sleep(1)  # Continue forward for a bit
        else:
            forward()

try:
    # Start obstacle avoidance thread
    obstacle_thread = Thread(target=obstacle_avoidance)
    obstacle_thread.start()

    while True:
        # Example 1: Move forward for 3 seconds, then stop
        forward()
        time.sleep(3)
        stop()
        time.sleep(1)

        # Example 2: Turn right for 1 second, then stop
        right()
        time.sleep(1)
        stop()
        time.sleep(1)

        # Example 3: Perform a sequence of movements
        forward()
        time.sleep(2)
        left()
        time.sleep(1)
        forward()
        time.sleep(2)
        right()
        time.sleep(1)
        stop()
        time.sleep(1)
        # Implement your robot dog's behavior here
        # You can use the movement functions defined above and add more logic as needed

except KeyboardInterrupt:
    stop()
