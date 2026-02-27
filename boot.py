import storage
import usb_cdc
import digitalio
import board

# Configura o GP0
switch = digitalio.DigitalInOut(board.GP0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# Se GP0 estiver conectado ao GND (soldado), switch.value será False
if not switch.value:
    storage.disable_usb_drive()
    usb_cdc.disable()

