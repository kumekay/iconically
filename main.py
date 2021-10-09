import gc
import sys

import neopixel
import uasyncio as asyncio
from machine import Pin

gc.collect()

from icon import icon

PIXEL_PIN = 7
PIX_COUNT = 16 * 16

BRIGHTNESS = 0.5


async def main():
    pin = Pin(PIXEL_PIN, Pin.OUT)
    pixels = neopixel.NeoPixel(pin, PIX_COUNT)

    for p in range(PIX_COUNT):
        pixels[p] = [int(el * BRIGHTNESS) for el in icon[p * 3 : p * 3 + 3]]

    pixels.write()


try:
    asyncio.run(main())
except (KeyboardInterrupt, Exception) as e:
    sys.print_exception(e)
finally:
    asyncio.new_event_loop()
