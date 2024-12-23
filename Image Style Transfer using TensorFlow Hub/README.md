Image Style Transfer using TensorFlow Hub:
This project demonstrates advanced image style transfer techniques using TensorFlow Hub's pre-trained model. It allows users to transform a content image by applying styles from one or multiple style images with various blending techniques

Features
Single Style Transfer: Apply a single style image to a content image.
Blended Style Transfer: Blend two style images before applying them to the content image.
Sequential Style Transfer: Apply two style images sequentially on the content image.
Content-Style Blending: Blend the stylized output with the original content image for customized results.
Interactive Upload: Upload content and style images directly via Google Colab.
Customizable Blending Ratios: Adjust alpha values to control blending intensity.

Technologies Used
Python: Backend programming.
TensorFlow & TensorFlow Hub: For loading and utilizing the pre-trained style transfer model.
Matplotlib: Visualization of content, style, and output images.
OpenCV: Image manipulation and saving outputs.
Google Colab: Cloud-based execution for interactive user uploads

How It Works
Model: The application uses TensorFlow Hub's pre-trained style transfer model.
Content Image: The main image to which the styles will be applied.
Style Images: One or more images used to provide artistic style transformations.

Steps to Use
-Install Dependencies:
pip install tensorflow tensorflow_hub matplotlib opencv-python-headless
-Upload Images:
Content image (content.jpg).
One or more style images (style1.jpg, style2.jpg, etc.).
-Run the Notebook:
Upload the notebook or execute the code in Google Colab.
-Select Mode:
Single Style Transfer.
Blended Style Transfer.
Sequential Style Transfer.
Content-Style Blending.
-Set Blending Ratios:
Adjust alpha to control blending between images.
-View & Save Output:
Outputs are displayed in the notebook and saved as .jpg files.

Folder Structure:
style-transfer/
│
├── project.ipynb             # Main notebook with all implementation
├── content.jpg               # Example content image
├── style1.jpg                # Example style image 1
├── style2.jpg                # Example style image 2
├── stylized_output.jpg       # Output for single style transfer
├── stylized_output_blended.jpg   # Output for blended style transfer
├── stylized_output_sequential.jpg # Output for sequential style transfer
├── blended_output.jpg        # Output for content-style blending
└── README.md                 # Project documentation

