# AZ-104 coverage map

Working traceability map from the [Microsoft study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), skills measured as of April 17, 2026. Outcomes are interpreted in the author's words; IDs are internal and provisional. No mock exam is included, so the exam-question column is `—`. Status values: `todo`, `drafted`, or `reviewed`; `reviewed` requires human comparison with the source and references.

## Identities and governance (20–25%)

### Microsoft Entra users and groups

Source locator: study guide, "Manage Azure identities and governance" > "Manage Microsoft Entra users and groups".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `entra-create-users-groups` | Create directory users and groups for organizational access | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | — | drafted | todo |
| `entra-manage-properties` | Manage user and group properties and membership | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | — | drafted | todo |
| `entra-licenses` | Assign and manage Microsoft Entra licenses | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | — | drafted | todo |
| `entra-external-users` | Manage external identities and collaboration access | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | — | drafted | todo |
| `entra-sspr` | Configure self-service password reset for the intended users | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | — | drafted | todo |

### Access to Azure resources with RBAC

Source locator: study guide, "Manage Azure identities and governance" > "Manage access to Azure resources".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `rbac-built-in-roles` | Select and manage suitable built-in Azure roles | direct | 01-identities-and-governance.md > Access to Azure resources with RBAC | — | drafted | todo |
| `rbac-scope-assignments` | Assign roles at an appropriate Azure scope | direct | 01-identities-and-governance.md > Access to Azure resources with RBAC | — | drafted | todo |
| `rbac-interpret-access` | Interpret effective Azure role assignments | direct | 01-identities-and-governance.md > Access to Azure resources with RBAC | — | drafted | todo |

### Subscriptions, governance, and cost control

Source locator: study guide, "Manage Azure identities and governance" > "Manage Azure subscriptions and governance".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `gov-azure-policy` | Implement and manage Azure Policy assignments and compliance | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | — | drafted | todo |
| `gov-resource-locks` | Configure resource locks to prevent selected management actions | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | — | drafted | todo |
| `gov-resource-tags` | Apply and manage resource tags for organization and reporting | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | — | drafted | todo |
| `gov-resource-groups` | Create and manage resource groups for resource lifecycle | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | — | drafted | todo |
| `gov-subscriptions` | Manage Azure subscriptions as administrative and billing boundaries | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | — | drafted | todo |
| `gov-cost-controls` | Use alerts, budgets, and Advisor recommendations to manage costs | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | — | drafted | todo |
| `gov-management-groups` | Organize subscriptions with management groups | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | — | drafted | todo |

## Storage (15–20%)

### Storage access and network controls

Source locator: study guide, "Implement and manage storage" > "Configure access to storage".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `storage-network-controls` | Configure storage firewall and virtual-network access restrictions | direct | 02-storage.md > Storage access and network controls | — | drafted | todo |
| `storage-sas` | Create and use scoped, time-limited SAS tokens | direct | 02-storage.md > Storage access and network controls | — | drafted | todo |
| `storage-access-policies` | Configure stored access policies where the SAS type supports them | direct | 02-storage.md > Storage access and network controls | direct; support varies by SAS type | drafted | todo |
| `storage-account-keys` | Manage storage account keys and their lifecycle | direct | 02-storage.md > Storage access and network controls | — | drafted | todo |
| `files-identity-access` | Configure identity-based authorization for Azure Files | direct | 02-storage.md > Storage access and network controls | — | drafted | todo |

### Storage accounts and data operations

Source locator: study guide, "Implement and manage storage" > "Configure and manage storage accounts".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `storage-account-create` | Create and configure storage accounts for workload needs | direct | 02-storage.md > Storage accounts and data operations | — | drafted | todo |
| `storage-redundancy` | Select Azure Storage redundancy for required failure domains | direct | 02-storage.md > Storage accounts and data operations | — | drafted | todo |
| `storage-object-replication` | Configure object replication for supported blob scenarios | direct | 02-storage.md > Storage accounts and data operations | — | drafted | todo |
| `storage-encryption` | Configure storage account encryption and key options | direct | 02-storage.md > Storage accounts and data operations | — | drafted | todo |
| `storage-data-tools` | Manage data with Storage Explorer and AzCopy | direct | 02-storage.md > Storage accounts and data operations | — | drafted | todo |

### Azure Files and Blob Storage

Source locator: study guide, "Implement and manage storage" > "Configure Azure Files and Azure Blob Storage".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `files-share` | Create and configure an Azure file share | direct | 02-storage.md > Azure Files and Blob Storage | — | drafted | todo |
| `blob-container` | Create and configure a Blob Storage container | direct | 02-storage.md > Azure Files and Blob Storage | — | drafted | todo |
| `blob-access-tiers` | Select blob access tiers for cost and retrieval needs | direct | 02-storage.md > Azure Files and Blob Storage | — | drafted | todo |
| `blob-soft-delete` | Configure soft delete for blobs and containers | direct | 02-storage.md > Azure Files and Blob Storage | — | drafted | todo |
| `files-snapshots-soft-delete` | Configure Azure Files snapshots and share soft delete | direct | 02-storage.md > Azure Files and Blob Storage | — | drafted | todo |
| `blob-lifecycle` | Configure blob lifecycle rules for tiering and deletion | direct | 02-storage.md > Azure Files and Blob Storage | — | drafted | todo |
| `blob-versioning` | Configure and use blob versioning | direct | 02-storage.md > Azure Files and Blob Storage | — | drafted | todo |

## Compute (20–25%)

### Resource deployment with ARM and Bicep

Source locator: study guide, "Deploy and manage Azure compute resources" > "Automate deployment of resources by using ARM templates or Bicep files".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `iac-interpret` | Interpret ARM template or Bicep resources, parameters, and dependencies | direct | 03-compute.md > Resource deployment with ARM and Bicep | — | drafted | todo |
| `iac-modify-arm` | Modify an existing ARM template to meet deployment requirements | direct | 03-compute.md > Resource deployment with ARM and Bicep | — | drafted | todo |
| `iac-modify-bicep` | Modify an existing Bicep file to meet deployment requirements | direct | 03-compute.md > Resource deployment with ARM and Bicep | — | drafted | todo |
| `iac-deploy` | Deploy resources using ARM templates or Bicep | direct | 03-compute.md > Resource deployment with ARM and Bicep | — | drafted | todo |
| `iac-export-convert` | Export a deployment or convert an ARM template to Bicep | direct | 03-compute.md > Resource deployment with ARM and Bicep | direct | drafted | todo |

### Virtual machines and scale sets

Source locator: study guide, "Deploy and manage Azure compute resources" > "Create and configure virtual machines".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `vm-create` | Create and configure a virtual machine and its dependencies | direct | 03-compute.md > Virtual machines and scale sets | — | drafted | todo |
| `vm-encryption-host` | Configure host encryption for supported virtual machines | direct | 03-compute.md > Virtual machines and scale sets | — | drafted | todo |
| `vm-move` | Move a VM within supported resource-group, subscription, or region scenarios | direct | 03-compute.md > Virtual machines and scale sets | direct; region moves may require migration | drafted | todo |
| `vm-sizes` | Select VM sizes for workload capacity and available quotas | direct | 03-compute.md > Virtual machines and scale sets | — | drafted | todo |
| `vm-disks` | Manage managed disks and their performance characteristics | direct | 03-compute.md > Virtual machines and scale sets | — | drafted | todo |
| `vm-availability` | Deploy VMs across availability zones or availability sets | direct | 03-compute.md > Virtual machines and scale sets | — | drafted | todo |
| `vm-scale-sets` | Deploy and configure Virtual Machine Scale Sets | direct | 03-compute.md > Virtual machines and scale sets | — | drafted | todo |

### Azure container services

Source locator: study guide, "Deploy and manage Azure compute resources" > "Provision and manage containers in the Azure portal".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `containers-registry` | Create and manage an Azure Container Registry | direct | 03-compute.md > Azure container services | — | drafted | todo |
| `containers-aci` | Provision a workload with Azure Container Instances | direct | 03-compute.md > Azure container services | — | drafted | todo |
| `containers-apps` | Provision a workload with Azure Container Apps | direct | 03-compute.md > Azure container services | — | drafted | todo |
| `containers-sizing-scaling` | Manage container sizing and scaling for ACI and Container Apps | direct | 03-compute.md > Azure container services | — | drafted | todo |

### Azure App Service

Source locator: study guide, "Deploy and manage Azure compute resources" > "Create and configure Azure App Service".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `appservice-plan` | Provision an App Service plan for workload requirements | direct | 03-compute.md > Azure App Service | — | drafted | todo |
| `appservice-scaling` | Configure scaling for an App Service plan | direct | 03-compute.md > Azure App Service | — | drafted | todo |
| `appservice-create` | Create and configure an App Service app | direct | 03-compute.md > Azure App Service | — | drafted | todo |
| `appservice-tls` | Configure certificates and TLS for App Service | direct | 03-compute.md > Azure App Service | — | drafted | todo |
| `appservice-custom-domain` | Map a custom DNS name to an App Service app | direct | 03-compute.md > Azure App Service | — | drafted | todo |
| `appservice-backup` | Configure backups for an App Service app | direct | 03-compute.md > Azure App Service | — | drafted | todo |
| `appservice-networking` | Configure App Service networking settings | direct | 03-compute.md > Azure App Service | — | drafted | todo |
| `appservice-slots` | Configure deployment slots for controlled app releases | direct | 03-compute.md > Azure App Service | — | drafted | todo |

## Virtual networking (15–20%)

### Virtual networks, subnets, and routing

Source locator: study guide, "Implement and manage virtual networking" > "Configure and manage virtual networks in Azure".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `network-vnets-subnets` | Create and configure virtual networks and subnets | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | — | drafted | todo |
| `network-peering` | Configure VNet peering and understand its routing behavior | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | direct | drafted | todo |
| `network-public-ips` | Configure public IP addresses for supported Azure resources | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | — | drafted | todo |
| `network-udr` | Configure user-defined routes and next hops | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | — | drafted | todo |
| `network-connectivity-troubleshoot` | Troubleshoot virtual network connectivity and routing | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | — | drafted | todo |

### Secure access and private connectivity

Source locator: study guide, "Implement and manage virtual networking" > "Configure secure access to virtual networks".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `network-nsg-asg` | Create and configure NSGs and application security groups | direct | 04-virtual-networking.md > Secure access and private connectivity | — | drafted | todo |
| `network-effective-rules` | Evaluate effective NSG security rules for a network interface | direct | 04-virtual-networking.md > Secure access and private connectivity | — | drafted | todo |
| `network-bastion` | Implement Azure Bastion for VM administration | direct | 04-virtual-networking.md > Secure access and private connectivity | — | drafted | todo |
| `network-service-endpoints` | Configure service endpoints for supported Azure PaaS services | direct | 04-virtual-networking.md > Secure access and private connectivity | — | drafted | todo |
| `network-private-endpoints` | Configure private endpoints for supported Azure PaaS services | direct | 04-virtual-networking.md > Secure access and private connectivity | — | drafted | todo |

### Name resolution and load balancing

Source locator: study guide, "Implement and manage virtual networking" > "Configure name resolution and load balancing".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `network-dns` | Configure Azure public and private DNS | direct | 04-virtual-networking.md > Name resolution and load balancing | — | drafted | todo |
| `network-load-balancer` | Configure an internal or public Azure Load Balancer | direct | 04-virtual-networking.md > Name resolution and load balancing | direct | drafted | todo |
| `network-load-balancer-troubleshoot` | Troubleshoot load-balancer rules, probes, and backend health | direct | 04-virtual-networking.md > Name resolution and load balancing | — | drafted | todo |

## Monitoring and recovery (10–15%)

### Azure Monitor and Network Watcher

Source locator: study guide, "Monitor and maintain Azure resources" > "Monitor resources in Azure".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `monitor-metrics` | Interpret Azure Monitor metrics for resource behavior | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | — | drafted | todo |
| `monitor-log-settings` | Configure resource log collection and diagnostic settings | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | — | drafted | todo |
| `monitor-log-analysis` | Query and analyze Azure Monitor logs | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | — | drafted | todo |
| `monitor-alerts` | Configure alert rules, action groups, and alert processing rules | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | — | drafted | todo |
| `monitor-insights` | Use Insights to monitor supported VMs, storage, and networks | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | direct | drafted | todo |
| `monitor-network-watcher` | Use Network Watcher and Connection Monitor to diagnose connectivity | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | — | drafted | todo |

### Backup and disaster recovery

Source locator: study guide, "Monitor and maintain Azure resources" > "Implement backup and recovery".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `recovery-services-vault` | Create a Recovery Services vault for a supported workload | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | — | drafted | todo |
| `recovery-backup-vault` | Create an Azure Backup vault for a supported workload | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | — | drafted | todo |
| `recovery-backup-policy` | Create and configure a backup policy | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | — | drafted | todo |
| `recovery-backup-restore` | Perform backup and restore operations with Azure Backup | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | — | drafted | todo |
| `recovery-site-recovery` | Configure Azure Site Recovery for supported resources | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | — | drafted | todo |
| `recovery-failover` | Perform or test a failover to a secondary region | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | — | drafted | todo |
| `recovery-reports-alerts` | Configure and interpret backup reports and alerts | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | — | drafted | todo |

## Known gaps and review state

- All mapped objectives have a drafted book section, but the mapping and technical explanations have not yet been human-reviewed. Do not treat `drafted` as an assurance that the source outline is exhaustive.
- No exam questions are included in this textbook; all exam-question entries are therefore `—`.
- Product support, service limits, portal workflows, and pricing can change. Verify version-sensitive decisions against the linked Microsoft Learn pages before applying them.
