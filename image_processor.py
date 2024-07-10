class ImageProcessor:

  def apply_grayscale_filter(self, image_data):
    height, width, channels = image_data.shape
    grayscale_image = np.zeros((height, width))
    for y in range(height):
      for x in range(width):
        average = (image_data[y, x, 0] + image_data[y, x, 1] + image_data[y, x, 2]) / 3
        grayscale_image[y, x] = average
    return grayscale_image

image_data = load_image("image.jpg")
grayscale_image = image_processor.apply_grayscale_filter(image_data)
