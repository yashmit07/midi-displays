import rtmidi
from tkinter import Tk, Canvas

# Create the main window
root = Tk()
root.title("MIDI Color Display")

# Create canvas for color display
canvas = Canvas(root, width=600, height=200, bg='black')
canvas.pack(pady=20)

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
    print("No MIDI ports available.")
    exit()

section1End = 56
section2End = 64

def get_color(note):
    # Divide the keyboard into three sections
    if note < section1End:  # Lower section
        return "#FF0000"  # Red
    elif note < section2End:  # Middle section
        return "#00FF00"  # Green
    else:  # Upper section
        return "#0000FF"  # Blue

def check_midi():
    msg = midi_in.getmessage()
    if msg:
        message,  = msg
        if message[2] > 0:  # Note On with velocity > 0
            note = message[1]
            color = get_color(note)
            canvas.configure(bg=color)
            print(f"Note: {note}, Color: {color}")  # Debug print

    root.after(10, check_midi)

# Start checking for MIDI messages
check_midi()

try:
    root.mainloop()
except KeyboardInterrupt:
    print("\nClosing MIDI connection...")
finally:
    midi_in.close_port()
    midi_in.delete()