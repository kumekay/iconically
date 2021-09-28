import gc
import sys

import neopixel
import uasyncio as asyncio
from machine import Pin

PIXEL_PIN = 8


async def main():
    pin = Pin(PIXEL_PIN, Pin.OUT)
    pixels = neopixel.NeoPixel(pin, 256)
    divider = 5
    while True:
        for t in range(16):
            for p in range(256):
                c = (t * 16 + p) % 255
                pixels[p] = (
                    c // divider,
                    (255 - c) // divider,
                    abs(127 - c) // divider,
                )

            pixels.write()
            await asyncio.sleep_ms(200)


try:
    asyncio.run(main())
except (KeyboardInterrupt, Exception) as e:
    sys.print_exception(e)
finally:
    asyncio.new_event_loop()
