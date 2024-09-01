# Define the provider
provider "azurerm" {
  features = {}
}

# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = "myResourceGroup"
  location = "East US"
}

# Create a container registry
resource "azurerm_container_registry" "acr" {
  name                = "myContainerRegistry"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"

  admin_enabled = true
}