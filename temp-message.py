# Import Libraries
from sense_hat import SenseHat

# Initialise SenseHAT
sense = SenseHat()
sense.clear()

# Set colours for LEDs
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255,0,0)

# Set temperature factor - used to offset Pi temperature
correction_factor = 1

# Initialise main loop
while True:
  temp = sense.get_temperature()
  corrected_temp = temp/correction_factor   # Calculate corrected temperature using SenseHAT value and correction_factor
  
  # Print message using Pi LEDs based on corrected_temp value in relation to temp thresholds
  if corrected_temp >=26: # Hot threshold
    sense.show_message(f"HOT! {corrected_temp:.1f}C", text_colour = red)

  elif corrected_temp <= 18: # Cold threshold
    sense.show_message(f"COLD! {corrected_temp:.1f}C", text_colour = blue)
  else: # Any other temp threshold
    sense.show_message(f"Fine! {corrected_temp:.1f}C", text_colour = green)
  print(corrected_temp)

