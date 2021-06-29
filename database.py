import DMC
import RGBDistance as Rgb


d_range_dmc = len(DMC.database_rgb)
dmc_list = []


def create_database(d_range, d_list):
    for x in range(d_range):
        new_color = (DMC.database_rgb[x][2], DMC.database_rgb[x][3], DMC.database_rgb[x][4])
        d_list.append(Rgb.RGBDistance(new_color))
