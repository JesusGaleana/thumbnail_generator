"""
This module provides functionality for a Flask application to generate and serve image thumbnails.
"""

import os
from flask import Flask, request, render_template, send_file
from PIL import Image
from utils.read_config_file import YamlDataLoader


app = Flask(__name__)
yaml_data_loader = YamlDataLoader(file_path="config.yml")
config_params = yaml_data_loader.read_yaml_file()
app.config["UPLOAD_FOLDER"] = config_params["upload_folder"]


def generate_thumbnail(image, size):
    """Generate a thumbnail of the provided image with the given size.

    Args: 
    image (File object): Representing the image to generate thumbnail from.
    size (Tuple): Containing the width and height of the thumbnail.
    
    Return: 
    img (PIL.Image.Image object): The generated thumbnail.
    """
    img = Image.open(image)
    img.thumbnail(size)
    return img


@app.route('/')
def index():
    """Render the principal page of the application.

    Returns: 
    render_template: Rendered HTML template.
    """
    return render_template(config_params["index_page"])


@app.route('/generate', methods=['POST'])
def generate():
    """Endpoint to generate image thumbnails.

    Returns: 
    render_template: Rendered HTML template displaying the result of thumbnail generation.
    """
    try:
        image = request.files['image']
        size = request.form.get('size', '100x100')
        width, height = map(int, size.split('x'))
    except KeyError:
        return "No image provided to generate the thumbnail", 400
    except ValueError:
        width = height = 100
    thumbnail = generate_thumbnail(image, size=(width, height))
    thumbnail.save(os.path.join(config_params["upload_folder"], config_params["filename"]))
    return render_template(config_params["result_page"], filename=config_params["filename"])


@app.route('/download/<filename>')
def viz_img(filename):
    """Serve the thumbnail image generated for visualization.

    Args:
    filename (str): Name of the image file to be served.
    
    Returns: 
    File object representing the image.
    """
    return send_file(os.path.join(config_params["upload_folder"], filename), mimetype='image/jpg')


@app.route('/download/<filename>')
def download(filename):
    """Endpoint to download the thumbnail image generated.

    Args:
    filename (str): Name of the file to be downloaded.
    
    Returns: 
    File object to be downloaded as an attachment.
    """
    return send_file(os.path.join(app.config["UPLOAD_FOLDER"], filename), as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
