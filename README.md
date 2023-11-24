# cloud_proj
Simple Cloud Demo using MiniKube
Using Python Flask app for a skeletal Text-to-image generator app.

## Steps to build docker image on Docker Hub:

1. Get a VM (NCSU VCL) or a local machine connected to internet running

2. Install Docker from docker website

3. Clone this repo into your proj folder

4. You can login to you docker hub account for public hosting (imp for k8s part) `docker login`. Enter username and password. Sign up if you don't have an account!

5. Navigate and run the docker build command `docker build -t <docker_hub_userid>/flask-kubes-proj .` This generates the docker image!

## Steps to run the docker image on port

1. Now run the docker image in 2 ways: (8000 is an example port here, can mention your own port)
    - `docker run -p 8000:5000 flask-kubes-proj` for normal mode
    - `docker run -d -p 8000:5000 --name my-flask-app flask-kubes-proj` for detatched (background mode)
2. Get you VM's public IP address Ex: 152.7.177.35. You can use `ip addr show` cmd to check the addresses!

3. The docker image runs on port 8000. Access it via `http://<VM_IP>8000`. In our case its http://152.7.177.35:8000.

## Using Kubernetes for Orchestrating services

1. Install minikube (reference this link for all commands `https://www.linuxbuzz.com/install-minikube-on-ubuntu/` follow upto step 5 to install minikube and kubectl)

2. Run `kubectl apply -f deployment.yaml`. This will create a kubernetes deployment

3. Run `kubectl apply -f services.yaml`. This will create kubernetes services, where we wrote that the app will be exposed on 'NodePort' and we use HorizontalPodAutoscaler to scale up/down

4. Get ip address of minikube's NodePort using `minikube ip`

5. Now the application will run on your local machine on <minikube_node_ip>, listening on port that we specified on services.yaml's nodePort and port fields! (I set it to `32001`)

6. Visit your app locally, my machine had `http://192.168.49.2:32001/`

7. Load test it using Locust or another load generating script!

