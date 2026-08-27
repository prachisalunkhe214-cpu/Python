traffic_light = input("Enter the color: ").lower()

if traffic_light == "red":
    print("Stop!")
elif traffic_light == "yellow":
    print("Slow down!")
elif traffic_light == "green":
    print("Go!")
else:
    print("Invalid color!")