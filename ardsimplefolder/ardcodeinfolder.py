import serial
import time
import simpleaudio as sa

# Replace with your Arduino's port
arduino = serial.Serial('/dev/cu.usbmodem14101', 9600, timeout=1)
time.sleep(2)  # Wait for the Arduino to reset

# Load the audio file
try:
    wave_obj = sa.WaveObject.from_wave_file("c.wav")
except Exception as e:
    print(f"Error loading audio file: {e}")
    arduino.close()
    exit(1)

print('Audio file loaded successfully.')

try:
    while True:
        # Read data from the Arduino
        if arduino.in_waiting > 0:
            distance_cm = arduino.readline().decode('utf-8').rstrip()
            print(distance_cm)  # Print the distance for debugging

            # Check if the light level is low (adjust the threshold as needed)
            if int(distance_cm) == 1:
                print('Playing sound using simpleaudio')
                play_obj = wave_obj.play()
                play_obj.wait_done()  # Wait until sound has finished playing
                time.sleep(1)  # Wait to prevent continuous sound playback

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    arduino.close()
