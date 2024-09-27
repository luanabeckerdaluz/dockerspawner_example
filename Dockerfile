FROM jupyterhub/jupyterhub:5
RUN python3 -m pip install --no-cache dockerspawner
RUN python3 -m pip install --no-cache jupyterhub-dummyauthenticator