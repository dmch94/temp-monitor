
# Import libraries
import BlynkLib, os
from time import time, sleep
from sense_hat import SenseHat

# Initialise SenseHAT
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = os.getenv("BLYNK_AUTH")

# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Process Timeout
INACTIVITY_TIMEOUT = 90  #  90 seconds
blynk.last_activity = time()   # attach last activity to the instance

# Set Temperature Factor - used to offset the heat from the Pi
temp_factor = 1.8

# Process Blynk Events
if __name__ == "__main__":
    print("Blynk application initialised. Processes running...")
    try:
        while True:
            blynk.run()  # Process Blynk events
            corrected_temp = round((sense.temperature)/temp_factor,1)   # Calculate corrected temperature
            blynk.virtual_write(0,corrected_temp)  # Send corrected temperature to virtual pin V0
            
            # Send additional temperature message to virtual pin v1 based on temperature thresholds
            if corrected_temp >=26:
                blynk.virtual_write(1,"Hot!")  
            elif corrected_temp <= 18:
                blynk.virtual_write(1,"Cold!") 
            else:
                blynk.virtual_write(1,"Fine")  
            now = time()

            #If there's been no activity, break out of loop
            if now - blynk.last_activity > INACTIVITY_TIMEOUT:
            	print(f"No process activity for {INACTIVITY_TIMEOUT} seconds. Programme exiting.")
            	break
            sleep(2)  # Add a short delay to avoid high CPU usage

    except KeyboardInterrupt:
        print("Blynk application manually stopped.")
