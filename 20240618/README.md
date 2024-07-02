# App Service with Terraform

Following the official how to

https://learn.microsoft.com/en-us/azure/app-service/provision-resource-terraform


export TF_VAR_AZURE_RESOURCE_GROUP=learn-7187536a-e164-403e-bbd3-18881f90ca8d

export TF_VAR_AZURE_APP_SERVICE_REPO_URL='https://github.com/KristianSalva/2023-25.IDT.UFS05'

terraform init

terraform import azurerm_resource_group.rg "/subscriptions/c1d60e68-fff0-4985-8539-5fc69e7362d8/resourceGroups/learn-7187536a-e164-403e-bbd3-18881f90ca8d"

az webapp log tail --name '...' --resource-group $TF_VAR_AZURE_RESOURCE_GROUP


node-red-dashboard

terraform destroy --target azurerm_linux_web_app.python_webapp
