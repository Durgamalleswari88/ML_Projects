# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t4cU4mq5lbx1xkI2vcR-Th7Bdq2U6v_v
"""

!pip install tensorflow tensorflow_hub matplotlib opencv-python-headless

from google.colab import files

uploaded = files.upload()

from google.colab import files

uploaded = files.upload()

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained model from TensorFlow Hub
style_transfer_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

def show_image(image, title='Image'):
    plt.figure(figsize=(10, 10))
    plt.imshow(np.squeeze(image))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_style(content_image_path, style_image_path):
    # Load content and style images
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)

    # Perform style transfer
    stylized_image = style_transfer_model(tf.constant(content_image), tf.constant(style_image))[0]

    # Display the result
    show_image(content_image, title='Content Image')
    show_image(style_image, title='Style Image')
    show_image(stylized_image, title='Stylized Image')

    # Save the output
    output_path = 'stylized_output.jpg'
    tf.keras.preprocessing.image.save_img(output_path, np.squeeze(stylized_image))
    print(f"Stylized image saved to {output_path}")

# Apply style transfer
content_image_path = 'content.jpg'  # Replace with the path to your content image
style_image_path = 'style.jpg'      # Replace with the path to your style image
apply_style(content_image_path, style_image_path)

from google.colab import files

# Upload content image
uploaded_content = files.upload()  # Upload your content image
content_image_path = next(iter(uploaded_content))  # Get the uploaded content image path

# Upload multiple style images one by one
style_image_paths = []

print("Upload your style images one by one.")
while True:
    uploaded_style = files.upload()  # Upload one style image
    style_image_path = next(iter(uploaded_style))  # Get the uploaded style image path
    style_image_paths.append(style_image_path)

    # Ask if the user wants to upload another style image
    more_images = input("Do you want to upload another style image? (y/n): ")
    if more_images.lower() != 'y':
        break

# Print paths for verification
print("Content Image Path:", content_image_path)
print("Style Image Paths:", style_image_paths)

#Blending the Styles Before Style Transfer

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Load the pre-trained model from TensorFlow Hub
style_transfer_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(img_path, image_size=(256, 256)):
    """Function to load, resize, and preprocess the image."""
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, image_size)  # Resize the image
    img = img[tf.newaxis, :]  # Add batch dimension
    return img

def show_image(image, title='Image'):
    """Function to display an image."""
    plt.figure(figsize=(10, 10))
    plt.imshow(np.squeeze(image))
    plt.title(title)
    plt.axis('off')
    plt.show()

def blend_styles(style_image1, style_image2, alpha=0.5):
    """Function to blend two style images."""
    blended_style = (style_image1 * alpha) + (style_image2 * (1 - alpha))
    blended_style = tf.clip_by_value(blended_style, 0.0, 1.0)
    return blended_style

def apply_style(content_image_path, style_image_paths):
    """Function to apply blended style to the content image."""
    # Load content image
    content_image = load_image(content_image_path)

    # Load style images
    style_image1 = load_image(style_image_paths[0])
    style_image2 = load_image(style_image_paths[1])

    # Blend the styles (alpha controls the blending ratio)
    blended_style = blend_styles(style_image1, style_image2, alpha=0.5)

    # Perform style transfer
    stylized_image = style_transfer_model(tf.constant(content_image), tf.constant(blended_style))[0]

    # Display the images
    show_image(content_image, title='Content Image')
    show_image(style_image1, title='Style Image 1')
    show_image(style_image2, title='Style Image 2')
    show_image(blended_style, title='Blended Style')
    show_image(stylized_image, title='Stylized Image with Blended Styles')

    # Save the output image
    output_path = 'stylized_output_blended.jpg'
    tf.keras.preprocessing.image.save_img(output_path, np.squeeze(stylized_image))
    print(f"Stylized image saved to {output_path}")

# Apply style transfer using the uploaded images
apply_style(content_image_path, style_image_paths)

#Sequential Style Transfer

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Load the pre-trained model from TensorFlow Hub
style_transfer_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(img_path):
    """Function to load and preprocess the image."""
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]  # Add batch dimension
    return img

def show_image(image, title='Image'):
    """Function to display an image."""
    plt.figure(figsize=(10, 10))
    plt.imshow(np.squeeze(image))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_style(content_image_path, style_image_paths):
    """Function to apply two style images sequentially on the content image."""
    # Load content image
    content_image = load_image(content_image_path)

    # Load the first style image
    style_image1 = load_image(style_image_paths[0])

    # Perform style transfer with the first style image
    stylized_image = style_transfer_model(tf.constant(content_image), tf.constant(style_image1))[0]

    # Load the second style image
    style_image2 = load_image(style_image_paths[1])

    # Apply style transfer with the second style image on the already stylized image
    final_stylized_image = style_transfer_model(tf.constant(stylized_image), tf.constant(style_image2))[0]

    # Display the images
    show_image(content_image, title='Content Image')
    show_image(style_image1, title='Style Image 1')
    show_image(style_image2, title='Style Image 2')
    show_image(stylized_image, title='First Stylized Image')
    show_image(final_stylized_image, title='Final Stylized Image with Both Styles')

    # Save the final output image
    output_path = 'stylized_output_sequential.jpg'
    tf.keras.preprocessing.image.save_img(output_path, np.squeeze(final_stylized_image))
    print(f"Stylized image saved to {output_path}")

# Apply style transfer using the uploaded images
apply_style(content_image_path, style_image_paths)

#Blend the Stylized Image with the Content Image

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained model from TensorFlow Hub
style_transfer_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(img_path, image_size=(256, 256)):
    """Function to load, resize, and preprocess the image."""
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, image_size)  # Resize the image
    img = img[tf.newaxis, :]  # Add batch dimension
    return img

def show_image(image, title='Image'):
    """Function to display an image."""
    plt.figure(figsize=(10, 10))
    plt.imshow(np.squeeze(image))
    plt.title(title)
    plt.axis('off')
    plt.show()

def blend_images(content_image, stylized_image, alpha=0.5):
    """Function to blend the content image with the stylized image."""
    blended_image = content_image * (1 - alpha) + stylized_image * alpha
    blended_image = tf.clip_by_value(blended_image, 0.0, 1.0)  # Ensure the values are in the range [0, 1]
    return blended_image

def apply_style(content_image_path, style_image_path, alpha=0.5):
    """Function to apply style transfer and blend the results."""
    # Load content image and style image
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)

    # Perform style transfer
    stylized_image = style_transfer_model(tf.constant(content_image), tf.constant(style_image))[0]

    # Blend the content image with the stylized image
    blended_image = blend_images(content_image, stylized_image, alpha)

    # Display the images
    show_image(content_image, title='Content Image')
    show_image(style_image, title='Style Image')
    show_image(stylized_image, title='Stylized Image')
    show_image(blended_image, title='Blended Image with Content and Style')

    # Save the output image
    output_path = 'blended_output.jpg'
    tf.keras.preprocessing.image.save_img(output_path, np.squeeze(blended_image))
    print(f"Blended image saved to {output_path}")

# Example paths (replace with your uploaded image paths)
content_image_path = 'content.jpg'  # Replace with the path to your content image
style_image_path = 'style.jpg'      # Replace with the path to your style image

# Apply style transfer and blending
apply_style(content_image_path, style_image_path, alpha=0.7)  # You can change alpha value to adjust the blending intensity