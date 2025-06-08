# MediaPad
![image](https://github.com/user-attachments/assets/b44731e8-d304-489c-b45c-d39cc1c0c4b5)
# Overview
- The MediaPad is a macropad made for the Hackclub program Hackpad.
- The macroboard features multiple buttons to control Youtube-based media, including functions such as going to the previous video, rewinding, pausing, skipping 5 seconds, and going to the next video.
- Additionally, there is a rotary encoder to control the volume, and pressing it allows the volume to be locked to prevent accidental changes.
- Similarly, a board-lock button exists to lock the keys that move to a different video, allowing only the inputs related to volume or time changing within the current video
- Features an LED that could be used for debugging or other purposes if neccessary \
*Note that the Models folder is for models used in the KiCad PCB rendering
# Case
- Includes a plate for switch stability, and everything is held together by M3 screws with threading in the plastic through the 3D-printed parts, but not the PCB
- Plate is top-mounted
- Also includes a cover for the rotary encoder for visuals and use
![image](https://github.com/user-attachments/assets/bdb109ee-deb1-41be-a2a0-1f19b6428bd1)
# PCB
## Schematic:
![image](https://github.com/user-attachments/assets/38af3418-de60-4f4d-94e3-0baa274d7950)
## Front:
![image](https://github.com/user-attachments/assets/48c161c1-ef79-4b58-b64a-3a6336fb964d)
![image](https://github.com/user-attachments/assets/d74b9840-6a98-4e79-a058-533b9de38699)
## Back: 
Nothing to see here (except traces)
![image](https://github.com/user-attachments/assets/a3ad8c3c-b2c1-4024-85f1-6b7d86918749)
![image](https://github.com/user-attachments/assets/f72e8b03-88e5-41f2-9f59-c8abfd145bb8)
# Firmware
- Uses KMK with CircuitPython, as included in the code folder. Only the custom code is included in the production folder.
# Lessons Learned
- First time using Fusion!!!!!
- Learned a lot about keyboards and how they work, a full-sized keyboard would 100% be made in the future
- Learned how to add models to PCB
- Learned a lot about 3D modeling
# BOM
- (1) PCB
- (1) EC11 Rotary Encoder
- (1) Rotary Encoder Cap (3D printed part)
- (1) Case Bottom
- (1) Case Top
- (1) Case Plate
- (8) M3x16MM Screws
- (1) XIAO RP2040
- (6) Cherry MX Switches
- (6) DSA Keycaps
- (1) SK6812 MINI-E LED
