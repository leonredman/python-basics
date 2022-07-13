# volume of a pyramid


def pyramid_volume(base_length, base_width, pyramid_height):
        
    #Base area = baselength x base width
    base_area = base_length * base_width

# returns the volume of a pyramid with a rectangular base.
    #volume = base area x height x 1/3
    volume = base_area * pyramid_height * 1/3
    return volume

print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(4.5, 2.1, 3.0))