# App Service with Terraform

Following the official how to

https://learn.microsoft.com/en-us/azure/app-service/provision-resource-terraform


export TF_VAR_AZURE_RESOURCE_GROUP=learn-e9ead29e-6810-4c56-81ef-8727bdb47c74

export TF_VAR_AZURE_APP_SERVICE_REPO_URL='https://github.com/KristianSalva/2023-25.IDT.UFS05'

terraform init

terraform import azurerm_resource_group.rg 'learn-e9ead29e-6810-4c56-81ef-8727bdb47c74'

az webapp log tail --name '...' --resource-group $TF_VAR_AZURE_RESOURCE_GROUP


node-red-dashboard

terraform destroy --target azurerm_linux_web_app.python_webapp
