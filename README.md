# simple-robodog
This Python code controls a robot using the Raspberry Pi GPIO pins, specifically utilizing the gpiozero library for hardware control. The robot can move forward, backward, turn left, and turn right. Additionally, it has obstacle avoidance capabilities. Here's a breakdown of the code:

Import Libraries: The code starts by importing the necessary libraries:

gpiozero: This library is used for controlling the motors of the robot and reading data from sensors.
time: It is used for adding delays in the code.
Robot and Sensor Initialization:

Robot: An instance of the Robot class is created to control the robot's motors. The motor pins are specified for both the left and right motors.
DistanceSensor: An instance of the DistanceSensor class is created to interface with a distance sensor. The echo and trigger pins are specified for the sensor.
Movement Functions:

Several functions are defined for controlling the robot's movements. These include forward(), backward(), left(), right(), and stop(). Each function sets the appropriate motor actions and prints a corresponding message.
Obstacle Avoidance Function:

The obstacle_avoidance() function is a continuous loop that checks the distance measured by the distance sensor.
If an obstacle is detected (distance < 20 units, you can adjust this threshold), it stops the robot, prints a message, and implements obstacle avoidance logic. In this example, it turns right and then moves forward for a bit.
If no obstacle is detected, it continues moving forward.
Main Program:

The main program starts with a try block.
It creates a separate thread for the obstacle_avoidance() function to run concurrently with other robot movements.
Inside an infinite loop (while True), it demonstrates various robot movements:
Example 1: Move forward for 3 seconds and then stop.
Example 2: Turn right for 1 second and then stop.
Example 3: Perform a sequence of movements (forward, left, forward, right) with delays between each action.
The program can be expanded by adding more logic for your robot's behavior inside this loop.
Keyboard Interrupt Handling:

The program can be terminated gracefully by pressing Ctrl+C. When a keyboard interrupt is detected (except KeyboardInterrupt:), it calls the stop() function to stop the robot.
This code provides a basic framework for controlling a robot with obstacle avoidance capabilities using Raspberry Pi GPIO pins. You can customize and expand upon it to create more complex robot behaviors
