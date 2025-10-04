import keyboard

print("Press any key to see its scan code...")

event = keyboard.read_event(suppress=False)
print(f"Key name: {event.name}")
print(f"Scan code: {event.scan_code}")
