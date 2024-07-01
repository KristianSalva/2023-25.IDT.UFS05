# App Service with Terraform

Following the official how to

https://learn.microsoft.com/en-us/azure/app-service/provision-resource-terraform


export TF_VAR_AZURE_RESOURCE_GROUP=learn-b20043d8-841b-4579-9168-c192bda2c02a

export TF_VAR_AZURE_APP_SERVICE_REPO_URL='https://github.com/KristianSalva/2023-25.IDT.UFS05'

terraform init

terraform import azurerm_resource_group.rg "/subscriptions/a597e5fe-3c45-4412-b944-53e730b31c57/resourceGroups/learn-b20043d8-841b-4579-9168-c192bda2c02a"

az webapp log tail --name '...' --resource-group $TF_VAR_AZURE_RESOURCE_GROUP


node-red-dashboard

terraform destroy --target azurerm_linux_web_app.python_webapp
