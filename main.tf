# Insecure Terraform sample (for IaC scanning)
provider "azurerm" {
  features {}
}

# Hard-coded credentials (DO NOT DO THIS IN REAL LIFE)
variable "client_id" { default = "00000000-0000-0000-0000-000000000000" }
variable "client_secret" { default = "fake-insecure-plain-secret" }
variable "subscription_id" { default = "11111111-1111-1111-1111-111111111111" }
variable "tenant_id" { default = "22222222-2222-2222-2222-222222222222" }

resource "azurerm_resource_group" "demo" {
  name     = "insecure-demo-rg"
  location = "eastus"
  # Missing tags & lifecycle policies
}

resource "azurerm_storage_account" "demo" {
  name                     = "insecuredemostoreacct"
  resource_group_name      = azurerm_resource_group.demo.name
  location                 = azurerm_resource_group.demo.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  enable_https_traffic_only = false  # Insecure: should be true
  allow_blob_public_access = true    # Insecure
}
