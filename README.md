# Thumbnail Generator
This is a Flask application that allows users to generate and serve image thumbnails.


## Features
- Generate thumbnails of images uploaded by users.
- Customize thumbnail size.
- Download generated thumbnails.
- Serve images for visualization.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/JesusGaleana/thumbnail_generator.git
```
2. Go to poject folder.   

3. Start the services into docker-compose file and run the application:
```bash
docker-compose up
```

## Usage
1. Access the application in your browser at http://localhost:8088.
2. Upload an image.
3. Optionally, customize the thumbnail size. Ex. 200x200
4. Click on "Generate Thumbnail" to generate the thumbnail.
5. Download the generated thumbnail or view it in the browser.

## Configuration
Configuration parameters such as upload folder location or HTML templates can be set in the config.yml file.  
This configuration is only for developer.

## Infrastructure
For now, this application is  hosted into docker container, you can see the infrastructure diagram bellow:  

![Docker-infrastructure-diagram](Documentation/infrastructure-diagram.png)  

### Migration to Cloud
This application can hosted into cloud services such as AWS, the services and the diagram that could be in the cloud are bellow:  

- EC2: With this cloud computing service we can host the application for thumbnail generator.
- S3: With this cloud storage service we can host the user uploaded images and generated images.
- Route 53: With this service we can create a domain to access to EC2 machine IP and the web application.

![Cloud-infrastructure-diagram](Documentation/cloud-infrastructure-diagram.png)  


## License
This project is licensed under the MIT License - see the LICENSE file for details.