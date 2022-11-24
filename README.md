# personalstack: an Azure setup for the home office

_If you don't understand why you might need this, then you probably don't need this_

The tools in this repo are used in my home office, aka 'The Command Center'. I'm a tech enthusiast who likes to build things in my free time, and I also consult on how to build connected, data driven systems. I'll keep the documents on how to build in this repository.

## My goal is to have a home IoT twin system that is:
* Completely owned by me
* I control the data, and where it goes
* Extensible
* Free (minus the cloud compute costs, no PaaS subscriptions otuside of Azure)
    * I may consider having a 100% local version of this at some time.
    * Hosting costs should be kept in the ~$20-$30 range.
* Designed for a very lightweight team. A single mono-repo that contains the full IoT/Digital Twin framework.
* End to end


# Create the `personalstack` env

create with the `env.yaml` file:
```
conda env create -f env.yml
```

# Local environment variables
Create an `ev-vars.json` file in the `infra` folder. It will be used for many different purposes and will be used to keep your secrets as a document. It should have this format:

```
{
    "subscription": ""***",
    "AZURE_STORAGE_KEY": ""***",
    "AZURE_ACCOUNT_NAME": ""***",
    "AZURE_STATIC_CONTAINER": "***",
    "AZURE_DIGITAL_TWIN_NAME": "**"
    ...
}
```
run the `configure_env.py` to load the variables from the json to the env. 



