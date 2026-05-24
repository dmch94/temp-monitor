from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255,0,0)
correction_factor = 1.7
while True:
  temp = sense.get_temperature()
  corrected_temp = temp/correction_factor
  if corrected_temp >=26:
    sense.show_message(f"HOT! {corrected_temp:.1f}C", text_colour = red)

  elif corrected_temp <= 18:
    sense.show_message(f"COLD! {corrected_temp:.1f}C", text_colour = blue)
  else:
    sense.show_message(f"Fine! {corrected_temp:.1f}C", text_colour = green)
  print(corrected_temp)

