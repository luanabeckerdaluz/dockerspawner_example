# dockerspawner_example

### Folow these instructions to deploy jupyterhub using DockerSpawner

- docker network create jupyterhub
- docker build -t hub .
- docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd)/jupyterhub_config.py:/srv/jupyterhub/jupyterhub_config.py --network jupyterhub --name jupyterhub -p 8000:8000 hub

NOTE: This last command mounts `docker.sock` and `jupyterhub_config.py` inside container running inside `jupyterhub` docker network.