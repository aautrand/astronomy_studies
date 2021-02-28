import datetime

from astropy.io import fits
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body
from astropy.time import Time
from astroquery.jplhorizons import Horizons
import matplotlib.pyplot as plt

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


def reading_fits():
    """current getting fits from: https://pdsimage2.wr.usgs.gov/archive/lro-l-lamp-2-edr-v1.0/LROLAM_0001/DATA/2009187/
    This function was originally for tifs but couldnt fund much data from nasa and pds to warrant spending the time
    trying to decifer tifs.

    Cant open files. Why? had to move the file to the same directory as the app.

    """
    # https://pillow.readthedocs.io/en/stable/reference/Image.html

    f = fits.open("LAMP_ENG_0268577238_02.fit")
    print(f.info())
    print(f[0])
    #next is how to display a fits img.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # >print_loc('Astronomy!')
    reading_fits()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
