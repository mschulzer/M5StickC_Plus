# M5StickC_Plus
Also check out: 

https://github.com/m5stack/M5Stack_MicroPython/tree/master/MicroPython_BUILD/components/micropython/esp32/modules
https://gitlab.com/rcolistete/micropython-samples/-/blob/master/M5Stack/MicroPython_com_M5StickC_pt-br.md



esptool.py -p /dev/tty.usbserial-XXX -b 115200 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x1000 build-XXX/bootloader/bootloader.bin 0x8000 build-XXX/partition_table/partition-table.bin 0x10000 build-XXX/micropython.bin
