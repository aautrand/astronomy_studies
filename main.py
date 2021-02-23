import datetime

from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body
from PIL import Image

from astroquery.jplhorizons import Horizons
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_loc(name):
    # Use a breakpoint in the code line below to debug your script.

    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    t = Time(datetime.datetime.now())
    loc = EarthLocation.of_address(address="")
    print(loc.lat, loc.lon)
    mm = Horizons(id="Mars")
    print(mm.__str__())
    with solar_system_ephemeris.set("builtin"):
        mars = get_body('mars', t, loc)

        print(mars)


def reading_tiffs():
    img = Image.open("MSL_Gale_Orthophoto_Mosaic_25cm_v3.tif")
    img.show()
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # >print_loc('Astronomy!')
    reading_tiffs()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
