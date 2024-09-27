from dockerspawner import DockerSpawner

# Set dummy auth
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.Authenticator.allowed_users = {"user1", "user2"}
c.Authenticator.admin_users = {"user1"}

# DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner
c.DockerSpawner.image = 'jupyter/base-notebook:latest'
c.DockerSpawner.http_timeout = 600
c.DockerSpawner.start_timeout = 600
c.DockerSpawner.debug = True
c.DockerSpawner.remove = True

# DockerSpawner Network
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = 'jupyterhub'
c.JupyterHub.hub_ip = '0.0.0.0' # Set hub to listen on all ips when it is in a container
c.JupyterHub.hub_connect_ip = 'jupyterhub' # Used to connect to the hub (container name)

# DockerSpawner Resources
c.DockerSpawner.cpu_limit = 2
c.DockerSpawner.mem_limit = "2G"
