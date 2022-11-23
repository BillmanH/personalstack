# Building the Azure Resources:

In the `infra` folder you will find `build_az.ps1`. I generally copy and paste it line by line into the terminal to make sure I'm configured correctly. Normally this part would be part of a build pipeline in ADO but I built this to run on my local machine out of simplicity. 
* You'll need to add yourself (and anyone else) data owner IAM roles to all of the resources. 

[Setting up the 3d Scenes](https://learn.microsoft.com/en-us/azure/digital-twins/quickstart-3d-scenes-studio). This should be automated, but the automation always seems to break for one reason or another. Eventually I end up running through the startup scripts here. 