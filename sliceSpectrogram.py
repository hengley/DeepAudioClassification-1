# Import Pillow:
import errno
import os.path

from PIL import Image

from config import spectrogramsPath, slicesPath


# Slices all spectrograms
def createSlicesFromSpectrograms(desiredSize):
    for filename in os.listdir(spectrogramsPath):
        if filename.endswith(".png"):
            sliceSpectrogram(filename, desiredSize)


# Creates slices from spectrogram
# Author_TODO Improvement - Make sure we don't miss the end of the song
def sliceSpectrogram(filename, desiredSliceSize):
    genre = filename.split("_")[0]  # Ex. Dubstep_19.png

    # Load the full spectrogram
    img = Image.open(spectrogramsPath + filename)

    # Compute approximate number of 128x128 samples
    width, height = img.size
    nbSamples = int(width / desiredSliceSize)
    width - desiredSliceSize  # Ques Why do this

    # Create path if not existing
    slicePath = slicesPath + "{}/".format(genre)
    if not os.path.exists(os.path.dirname(slicePath)):
        try:
            os.makedirs(os.path.dirname(slicePath))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    # For each sample
    for i in range(nbSamples):
        print("Creating slice: ", (i + 1), "/", nbSamples, "for", filename)
        # Extract and save 128x128 sample
        startPixel = i * desiredSliceSize
        imgTmp = img.crop((startPixel, 1, startPixel + desiredSliceSize, desiredSliceSize + 1))
        imgTmp.save(slicesPath + "{}/{}_{}.png".format(genre, filename[:-4], i))
