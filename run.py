from me2gpx.medat import load_from_dat_file
from me2gpx.gpx import GPXTrack


input_file = '1.dat'
output_file = '2.gpx'


def convert():
    with open(input_file, 'rb') as inputfile:
        points = load_from_dat_file(inputfile)
    track = GPXTrack(*points)
    with open(output_file, 'w') as outputfile:
        track.write(outputfile)

if __name__ == '__main__':
    convert()