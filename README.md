<img width="898" height="928" alt="image" src="https://github.com/user-attachments/assets/b60452d2-a8ee-4ade-9bb9-5a37ffe41b94" />

# EasyDev
A RP2040 Dev Board featuring 43 exposed pins along with 16 MB of flash storage! Can support up to (not recommended) 1A of power draw on VBUS! Features 29 programmable GPIO pins so that you have plenty of pins for plenty of connecting and tinkering and also a onboard NeoPixel-compatible addressable RGB LED with a exposed pin dedicated for connecting other addressable LEDs to the board without sacrificing a GPIO!

<img width="833" height="2069" alt="image" src="https://github.com/user-attachments/assets/8bcc80f9-b112-4536-bd4e-fd6323dd7293" />
<img width="997" height="653" alt="image" src="https://github.com/user-attachments/assets/84a811b0-3a2e-485e-9566-f25fc2c012cf" />

# Why?
I was thinking of making some PCBs, and I thought, why not try something advanced and also something that you have been wanting to do for a while now? And that's when I came up with the idea of making my own RP2040 dev board (basically a Raspberry Pi Pico) starting from scratch. So I did, and learned a lot along the way! Making this devboard will definitely change the way I make PCBs in the future especially because of all the things that I learned from designing this.

# Using the EasyDev Devboard:
Using EasyDev is pretty similar to using other devboards. To use it simply connect the USB port on the devboard to your computer via a USB-C to USB-C/A cable. Then, simply write code to it like you would to a normal devboard/Arduino. To write the code, you can use CircuitPython/Micropython to program it as those are commonly used programming languages for RP2040 devboard, but if you prefer Arduino IDE, you can also use it. Then, if your program needs any connecting to external components, use 2.54mm dupont jumper wires to connect the parts to your devboard!

# Assembly:
The EasyDev devboard comes preassembled <ins>except for the header pins.</ins> You will have to solder the header pins on yourself. The max temperature recommended for soldering is 350 Degrees Celsius, but you should keep the temperature as low as possible <ins> to avoid damaging the PCB,</ins> but not too low where the solder won't properly melt and flow smoothly.

# How it Works:
If you are curious of how this devboard works, well you are in the right spot! When you connect the devboard to your computer, power goes through something called a LDO (Low Dropout Regulator) which, in our case, will keep the voltage going to the rest of the board at 3.3V. But why 3.3V, you might ask. Well, this is because the chip/microcontroller that the devboard has uses 3.3V logic and can only take 3.3V of power, your USB port has 5V of power, directly wiring the USB pins to the chip would blow it up! Then the power goes through decoupling capacitors which are like tiny batteries and then the capacitors help keep stable voltages to the RP2040 chip in case the voltage drops.  Then, there are pins on the chip called GPIOs (General Purpose Input/Output) that you can control with code. Those pins are wired to the header pins on the left and right-hand side. And then the USB data lines are also connected to the RP2040 so that the computer and the devboard can communicate with each other and to upload code to the board. And after you program the board, you can connect parts to the pins like motors, LEDs, etc. using some wires and/or a breadboard!

# PCB
<img width="357" height="812" alt="image" src="https://github.com/user-attachments/assets/4324b94e-40e5-4377-8eb8-3b5cba6139c3" />
<img width="368" height="804" alt="image" src="https://github.com/user-attachments/assets/dbbbabc1-c3bb-45f5-ac07-e1dae72ddd32" />
<img width="411" height="885" alt="image" src="https://github.com/user-attachments/assets/3f3dc52b-1b3d-4618-b22b-2d0c28bc20d7" />

# Schematic
<img width="3507" height="2480" alt="image" src="https://github.com/user-attachments/assets/474bdac0-ee6f-4ab7-9759-d5cc6d549906" />

# BOM
Parts used for PCBA:
| Item # | Part Name                                   | JLC Part #    | Source | Cost (USD) | Link                                                                                                                                                 |
| -----: | :------------------------------------------ | :------------ | :----- | ---------: | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
|      1 | 1uF 25V X5R ±10% 0402 MLCC Capacitor        | **C52923**    | JLCPCB |    $0.2650 | [https://jlcpcb.com/partdetail/53938-CL05A105KA5NQNC/C52923](https://jlcpcb.com/partdetail/53938-CL05A105KA5NQNC/C52923)                             |
|      2 | 100nF 16V X7R ±10% 0402 MLCC Capacitor      | **C1525**     | JLCPCB |    $0.2915 | [https://jlcpcb.com/partdetail/1877-CL05B104KO5NNNC/C1525](https://jlcpcb.com/partdetail/1877-CL05B104KO5NNNC/C1525)                                 |
|      3 | 10µF 10V X5R ±10% 0603 MLCC Capacitor       | **C19702**    | JLCPCB |    $0.4080 | [https://jlcpcb.com/partdetail/20411-CL10A106KP8NNNC/C19702](https://jlcpcb.com/partdetail/20411-CL10A106KP8NNNC/C19702)                             |
|      4 | 33pF 50V C0G ±5% 0402 MLCC Capacitor        | **C1562**     | JLCPCB |    $0.1410 | [https://jlcpcb.com/partdetail/1914-0402CG330J500NT/C1562](https://jlcpcb.com/partdetail/1914-0402CG330J500NT/C1562)                                 |
|      5 | WS2812B-2020V6 RGB LED (Built-in IC)        | **C52917434** | JLCPCB |    $0.8118 | [https://jlcpcb.com/partdetail/Worldsemi-WS2812B_2020V6/C52917434](https://jlcpcb.com/partdetail/Worldsemi-WS2812B_2020V6/C52917434)                 |
|      6 | USB Type-C Connector (16P, Right Angle SMT) | **C165948**   | JLCPCB |    $0.9205 | [https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M12/C165948](https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M12/C165948)   |
|      7 | 5.1kΩ 0402 ±1% Resistor                     | **C25905**    | JLCPCB |    $0.0670 | [https://jlcpcb.com/partdetail/26648-0402WGF5101TCE/C25905](https://jlcpcb.com/partdetail/26648-0402WGF5101TCE/C25905)                               |
|      8 | 27Ω 0402 ±1% Resistor                       | **C138021**   | JLCPCB |    $0.1034 | [https://jlcpcb.com/partdetail/YAGEO-RC0402FR0727RL/C138021](https://jlcpcb.com/partdetail/YAGEO-RC0402FR0727RL/C138021)                             |
|      9 | 1kΩ 0402 ±1% Resistor                       | **C11702**    | JLCPCB |    $0.0800 | [https://jlcpcb.com/partdetail/12256-0402WGF1001TCE/C11702](https://jlcpcb.com/partdetail/12256-0402WGF1001TCE/C11702)                               |
|     10 | 10kΩ 0402 ±1% Resistor                      | **C60490**    | JLCPCB |    $0.1160 | [https://jlcpcb.com/partdetail/YAGEO-RC0402FR0710KL/C60490](https://jlcpcb.com/partdetail/YAGEO-RC0402FR0710KL/C60490)                               |
|     11 | 4×3mm SMT Tactile Switch                    | **C720477**   | JLCPCB |    $0.2760 | [https://jlcpcb.com/partdetail/XUNPU-TS_1088AR02016/C720477](https://jlcpcb.com/partdetail/XUNPU-TS_1088AR02016/C720477)                             |
|     12 | RP2040 Microcontroller                      | **C2040**     | JLCPCB |    $4.9250 | [https://jlcpcb.com/partdetail/RaspberryPi-RP2040/C2040](https://jlcpcb.com/partdetail/RaspberryPi-RP2040/C2040)                                     |
|     13 | NCP1117ST33T3G 3.3V LDO Regulator           | **C26537**    | JLCPCB |    $1.1680 | [https://jlcpcb.com/partdetail/onsemi-NCP1117ST33T3G/C26537](https://jlcpcb.com/partdetail/onsemi-NCP1117ST33T3G/C26537)                             |
|     14 | W25Q16JVUXIQ 16Mbit SPI Flash               | **C2843335**  | JLCPCB |   $10.1720 | [https://jlcpcb.com/partdetail/WinbondElec-W25Q16JVUXIQ/C2843335](https://jlcpcb.com/partdetail/WinbondElec-W25Q16JVUXIQ/C2843335)                   |
|     15 | 12MHz SMD Crystal                           | **C9002**     | JLCPCB |    $0.4750 | [https://jlcpcb.com/partdetail/YXC_CrystalOscillators-X322512MSB4SI/C9002](https://jlcpcb.com/partdetail/YXC_CrystalOscillators-X322512MSB4SI/C9002) |

# OLD PCB!!
<img width="775" height="850" alt="image" src="https://github.com/user-attachments/assets/6a81b15d-e1fa-40fa-b64f-182c5447a4d2" />
