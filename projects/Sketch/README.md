
# Image to Sketch Conversion using OpenCV

This Python script converts a given input image into a sketch-like effect using OpenCV. It follows a series of image processing steps to create the effect.

## Prerequisites

- Python
- OpenCV (Open Source Computer Vision Library)

You can install OpenCV using pip:

```bash
pip install opencv-python
```

## Usage

1. Clone or download the repository to your local machine.

2. Place your input image in the same directory as the script, or provide the full path to the image in the script.

3. Open a terminal and navigate to the script's directory.

4. Run the script:

```bash
python sketch.py
```

5. The script will process the image and create a sketch effect.

6. The resulting sketch image will be saved as "sketch.jpg" in the same directory.

7. You can view the generated sketch image or further process it as needed.

## Script Explanation

- The script loads the input image and converts it to grayscale, simplifying it.

- It then inverts the colors, turning dark areas into light and vice versa.

- A Gaussian blur is applied to the inverted image to smooth out details and noise.

- The blurred image is inverted again to restore the original orientation of colors.

- The final sketch effect is created by dividing the grayscale image by the inverted blurred image.

- You can adjust the intensity of the effect by changing the `scale` parameter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

