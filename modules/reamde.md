# Simplified Module Deployment

For the lighter team. 

build and deploy instructions (because it's not set up to autodeploy through vscode). To **create a new module** just copy the contents of `testmodule`. 

### build the container locally:
```
docker build --tag iothubregistry.azurecr.io/testimage:v1.0.0 . 
```
note the dot '.' I always forget that.


### Upload the container:
```
docker login iothubregistry.azurecr.io
docker push iothubregistry.azurecr.io/testimage:v1.0.0
```

### Deploy locally

I'm essentially uploading the image from my desktop, to IoT hub, only to then push it down to my local area again. However, I could deploy these modules to anywhere in the world with the same framework. Plus, I use a stable version control to manage the models remotely. 
