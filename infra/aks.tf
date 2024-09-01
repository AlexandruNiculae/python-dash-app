# Define the provider
provider "azurerm" {
  features = {}
}

# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = "aksResourceGroup"
  location = "East US"
}

# Create a virtual network
resource "azurerm_virtual_network" "vnet" {
  name                = "aksVnet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  address_space       = ["10.0.0.0/8"]
}

# Create a subnet
resource "azurerm_subnet" "subnet" {
  name                 = "aksSubnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.240.0.0/16"]
}

# Create an AKS cluster
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "myAKSCluster"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "myakscluster"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_DS2_v2"
    vnet_subnet_id = azurerm_subnet.subnet.id
  }

  identity {
    type = "SystemAssigned"
  }

  # Adding additional node pools with labels
  agent_pool_profile {
    name       = "main"
    count      = 1
    vm_size    = "Standard_DS2_v2"
    os_type    = "Linux"
    vnet_subnet_id = azurerm_subnet.subnet.id
    node_labels = {
      role = "main"
    }
  }

  agent_pool_profile {
    name       = "jobs"
    count      = 1
    vm_size    = "Standard_DS2_v2"
    os_type    = "Linux"
    vnet_subnet_id = azurerm_subnet.subnet.id
    node_labels = {
      role = "jobs"
    }
  }

  network_profile {
    network_plugin    = "azure"
    dns_service_ip    = "10.2.0.10"
    service_cidr      = "10.2.0.0/24"
    docker_bridge_cidr = "172.17.0.1/16"
  }
}