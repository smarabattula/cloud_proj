# cloud_proj
Simple Cloud Demo using MiniKube
Using Python Flask app for a skeletal Text-to-image generator app.
Steps to run this application on a docker image:
1. Get a VM (NCSU VCL) or a local machine connected to internet running
2. Install Docker from docker website
3. Clone this repo into your proj folder
4. Navigate and run the docker build command `docker build -t flask-kubes-proj .` This generates the docker image
5. Now run the docker image in 2 ways:
    - `docker run -p 8000:5000 flask-kubes-proj` for normal mode
    - `docker run -d -p 8000:5000 --name my-flask-app flask-kubes-proj` for detatched (background mode)
6. Get you VM's public IP address Ex: 152.7.177.35. You can use `ip addr show` cmd to check the addresses!
7. The docker image runs on port 8000. Access it via `http://<VM_IP>8000`. In our case its http://152.7.177.35:8000.
