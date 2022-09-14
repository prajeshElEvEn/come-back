from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import argparse

parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args = parser.parse_args()
connection_string = args.connect
print("[*] Connecting to vehicle on: %s" % (connection_string))
vehicle = connect(connection_string, wait_ready=True)

def takeoff(target_altitude):
    print("[*] Arming motors.")
    while not vehicle.is_armable:
        print("[*] Waiting for vehicle to initialize...")
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    print("[*] Taking off.")
    vehicle.simple_takeoff(target_altitude)

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print("[+] Altitude: %f" % altitude)
        if altitude >= target_altitude - 1:
            print("[*] Altitude reached.")
            break
        time.sleep(1)

takeoff(10)
vehicle.airspeed = 7

print("[*] Going towards first point.")
point1 = LocationGlobalRelative(28.7514289, 77.4994955, 10)
vehicle.simple_goto(point1)

print("[*] Hovering for 30 seconds.")
time.sleep(30)

print("[*] Coming back to initial position.")
vehicle.mode = VehicleMode("RTL")

time.sleep(20)

print("[*] Disarming.")
vehicle.close()

