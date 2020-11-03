from PIL import Image
import math


def generate_mhi(
        frames,
        width,
        height,
        min_brightness=48,
):
    mhi = Image.new('RGB', (width, height), 'black')
    mhi_pixels = mhi.load()
    gradient_diff = (255 - min_brightness) / (len(frames) - 1)
    i = 0

    for frame in frames:
        gradient = min(min_brightness + math.floor(i * gradient_diff),
                       255)
        gradient_rgb = (gradient, gradient, gradient)

        for x in range(width):
            for y in range(height):
                if frame[x, y][0] > 15:
                    mhi_pixels[x, y] = gradient_rgb
        i += 1
    return mhi
