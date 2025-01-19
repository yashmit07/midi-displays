import rtmidi
import time

# Create MIDI input
midi_in = rtmidi.MidiIn()

# List available ports
ports = midi_in.get_ports()
print("Available MIDI ports:")
for i, port in enumerate(ports):
    print(f"{i}: {port}")

# Let user choose port
if ports:
    port_num = int(input("Choose port number: "))
    midi_in.open_port(port_num)
    print(f"Opened port: {ports[port_num]}")
else:
    print("No MIDI ports available. Opening virtual port...")
    midi_in.open_virtual_port("My Virtual Port")

try:
    while True:
        msg = midi_in.get_message()
        if msg:
            message, _ = msg
            print(f"Note: {message[1]}, Velocity: {message[2]}")
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nClosing MIDI connection...")
    midi_in.close_port()
    midi_in.delete()