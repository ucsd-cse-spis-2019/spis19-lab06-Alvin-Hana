# This program demonstrates how to control a servo

# Import the relevant libraries
import RPi.GPIO as GPIO
import time

delayTarget = 1

LastTime = 0
 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
# set GPIO Pins
ServoPin = 7
BtnPin = 15                                        # GPIO pin for the servo

# set GPIO direction (IN / OUT)
GPIO.setup(ServoPin, GPIO.OUT)                      # Set ServoPin's mode to output
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# The servo is controlled using Pulse Width Modulation (PWM)
# The next few lines of code take care of the required setup for this functionality
# The details are not important; you should not modify this code
# --- Start of the PWM setup ---
    # Set PWM parameters
pwm_frequency = 50
duty_min = 2.5 * float(pwm_frequency) / 50.0
duty_max = 12.5 * float(pwm_frequency) / 50.0

    # Helper function to set the duty cycle
def set_duty_cycle(angle):
    return ((duty_max - duty_min) * float(angle) / 180.0 + duty_min)

    # Create a PWM instance
pwm_servo = GPIO.PWM(ServoPin, pwm_frequency)

# --- End of the PWM setup ---





# Main program 
if __name__ == '__main__':

    try:
        haveTurned = 0
        pressed = 0
        # This code repeats forever
        while True:
            # Check the current time
            currentTime = time.time()

            # Check if we have waited long enough
            if (currentTime - LastTime > delayTarget):
                print("Amount of time that has passed: {0}".format(currentTime-LastTime))
                if GPIO.input(BtnPin)==0:
                    if pressed == 0:
                        print("button pressed")
                        pwm_servo.start(set_duty_cycle(0))
                elif haveTurned == 0:
                    pressed = 0
                    pwm_servo.start(set_duty_cycle(180))
                    print ("Moving to angle 180")
                    haveTurned = 1
                else:
                    pressed = 0
                    pwm_servo.start(set_duty_cycle(0))
                    print ("Moving to angle 0")
                    haveTurned = 0

                LastTime = currentTime

            # Move the servo
#            angle = 0
#            pwm_servo.start(set_duty_cycle(angle))
#            print ("Moving to angle 0")
#            time.sleep(1)
                       
#            angle = 180
#            pwm_servo.start(set_duty_cycle(angle))
#            print ("Moving to angle 180")
#            time.sleep(1)

            
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program stopped by User")
        GPIO.cleanup()
