# Simplified Module Deployment

For the lighter team. 

build and deploy instructions (because it's not set up to autodeploy through vscode)

### build the container locally:
```
docker build .
```
note the dot '.' I always forget that.

### Test it:

### Tag the image correctly:
docker tag {localimage}:{tag} {your container repository}.azurecr.io/{your image name}:{tag}

### Upload the container:
```
docker login {your container registry}.azurecr.io
docker push {your container repository}.azurecr.io/{tag}
```
