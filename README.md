EIE3105-setup
=============
- [用Python下載檔案. Using Python Download files | by Gradient Drift | Medium](https://gradient-drift.medium.com/%E7%94%A8python%E4%B8%8B%E8%BC%89%E6%AA%94%E6%A1%88-451d1b6f5c10)
- [concurrent.futures --- 啟動平行任務 — Python 3.14.2 說明文件](https://docs.python.org/zh-tw/3/library/concurrent.futures.html)
- [python concurrent模块实现多线程 - 三只松鼠 - 博客园](https://www.cnblogs.com/shenh/p/14338173.html)

### TODOs
- [ ] merge [dirkarnez/EIE3105-STM32-Tools](https://github.com/dirkarnez/EIE3105-STM32-Tools)

### AVR
```
rm -rf  main.o   
rm -rf  main.d   
rm -rf "EIE3105_ATmega328P_Application.elf" "EIE3105_ATmega328P_Application.a" "EIE3105_ATmega328P_Application.hex" "EIE3105_ATmega328P_Application.lss" "EIE3105_ATmega328P_Application.eep" "EIE3105_ATmega328P_Application.map" "EIE3105_ATmega328P_Application.srec" "EIE3105_ATmega328P_Application.usersignatures"
Building file: main.c
Invoking: AVR/GNU C Compiler : 5.4.0
"avr-gcc.exe"  -x c -funsigned-char -funsigned-bitfields -DDEBUG  -I"%USERPROFILE%\Downloads\Atmel.ATmega_DFP.2.1.506\include"  -Og -ffunction-sections -fdata-sections -fpack-struct -fshort-enums -g2 -Wall -mmcu=atmega328p -B "%USERPROFILE%\Downloads\Atmel.ATmega_DFP.2.1.506\gcc\dev\atmega328p" -c -std=gnu99 -MD -MP -MF "main.d" -MT"main.d" -MT"main.o"   -o "main.o" "main.c"
Finished building: main.c
Building target: EIE3105_ATmega328P_Application.elf
Invoking: AVR/GNU Linker : 5.4.0
"avr-gcc.exe" -o EIE3105_ATmega328P_Application.elf  main.o   -Wl,-Map="EIE3105_ATmega328P_Application.map" -Wl,--start-group -Wl,-lm  -Wl,--end-group -Wl,--gc-sections -mmcu=atmega328p -B "%USERPROFILE%\Downloads\Atmel.ATmega_DFP.2.1.506\gcc\dev\atmega328p"
Finished building target: EIE3105_ATmega328P_Application.elf
"avr-objcopy.exe" -O ihex -R .eeprom -R .fuse -R .lock -R .signature -R .user_signatures  "EIE3105_ATmega328P_Application.elf" "EIE3105_ATmega328P_Application.hex"
"avr-objcopy.exe" -j .eeprom  --set-section-flags=.eeprom=alloc,load --change-section-lma .eeprom=0  --no-change-warnings -O ihex "EIE3105_ATmega328P_Application.elf" "EIE3105_ATmega328P_Application.eep" || exit 0
"avr-objdump.exe" -h -S "EIE3105_ATmega328P_Application.elf" > "EIE3105_ATmega328P_Application.lss"
"avr-objcopy.exe" -O srec -R .eeprom -R .fuse -R .lock -R .signature -R .user_signatures "EIE3105_ATmega328P_Application.elf" "EIE3105_ATmega328P_Application.srec"
"avr-size.exe" "EIE3105_ATmega328P_Application.elf"
   text    data     bss     dec     hex filename
    160       0       0     160      a0 EIE3105_ATmega328P_Application.elf
```
