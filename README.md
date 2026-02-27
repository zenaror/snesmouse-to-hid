# SNES Mouse to USB HID
Esse código é praticamente identico ao original da Adafruit, [SNES Mouse to USB HID with CircuitPython](https://learn.adafruit.com/snes-mouse-to-usb-hid-with-circuitpython). 

Apenas realizei poucas alterações no código para poder permitir o uso com a placa RP2040 Zero.

A ligação permanece a mesma:

| Pino SNES | Pino RP2040 Zero |
|---|---|
| VCC | 3v3 |
| GND | GND |
| Clock | Pino 6 |
| Data | Pino 4 |
| Latch | Pino 5 |

Também criei um arquivo de `boot.py`, que desabilita o drive *CIRCUITPY* de ficar aparecendo. Também desabilita a comunicação Serial. Para ativar isso, basta soldar um fio (jumper) entre o pino 0 e o GND. 

Isso não impede de apertar o botão reset para colocar o CircuitPython em modo seguro, permitindo assim o drive e o serial serem reativados nesse modo. Pode ser útil se precisar fazer algum ajuste fino.
