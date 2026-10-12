# AZ-104 coverage map

Working traceability map from the [Microsoft study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), skills measured as of April 17, 2026. Outcomes are interpreted in the author's words; IDs are internal and provisional. No mock exam is included, so the exam-question column is `—`. Status values: `todo`, `drafted`, or `reviewed`; `reviewed` requires human comparison with the source and references.

## Identities and governance (20–25%)

### Microsoft Entra users and groups

Source locator: study guide, "Manage Azure identities and governance" > "Manage Microsoft Entra users and groups".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `entra-create-users-groups` | Create directory users and groups for organizational access | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | 1, 2 | drafted | drafted |
| `entra-manage-properties` | Manage user and group properties and membership | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | 2, 3 | drafted | drafted |
| `entra-licenses` | Assign and manage Microsoft Entra licenses | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | 3, 4 | drafted | drafted |
| `entra-external-users` | Manage external identities and collaboration access | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | 5, 6 | drafted | drafted |
| `entra-sspr` | Configure self-service password reset for the intended users | direct | 01-identities-and-governance.md > Microsoft Entra users and groups | 7, 8 | drafted | drafted |

### Access to Azure resources with RBAC

Source locator: study guide, "Manage Azure identities and governance" > "Manage access to Azure resources".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `rbac-built-in-roles` | Select and manage suitable built-in Azure roles | direct | 01-identities-and-governance.md > Access to Azure resources with RBAC | 9, 10, 14, 15 | drafted | drafted |
| `rbac-scope-assignments` | Assign roles at an appropriate Azure scope | direct | 01-identities-and-governance.md > Access to Azure resources with RBAC | 9, 10, 11, 12, 13 | drafted | drafted |
| `rbac-interpret-access` | Interpret effective Azure role assignments | direct | 01-identities-and-governance.md > Access to Azure resources with RBAC | 12, 13, 14, 15, 22 | drafted | drafted |

### Subscriptions, governance, and cost control

Source locator: study guide, "Manage Azure identities and governance" > "Manage Azure subscriptions and governance".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `gov-azure-policy` | Implement and manage Azure Policy assignments and compliance | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | 16, 17, 18 | drafted | drafted |
| `gov-resource-locks` | Configure resource locks to prevent selected management actions | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | 19 | drafted | drafted |
| `gov-resource-tags` | Apply and manage resource tags for organization and reporting | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | 16, 17, 20 | drafted | drafted |
| `gov-resource-groups` | Create and manage resource groups for resource lifecycle | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | 21 | drafted | drafted |
| `gov-subscriptions` | Manage Azure subscriptions as administrative and billing boundaries | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | 22, 25 | drafted | drafted |
| `gov-cost-controls` | Use alerts, budgets, and Advisor recommendations to manage costs | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | 20, 23, 24 | drafted | drafted |
| `gov-management-groups` | Organize subscriptions with management groups | direct | 01-identities-and-governance.md > Subscriptions, governance, and cost control | 18, 25 | drafted | drafted |

## Storage (15–20%)

### Storage access and network controls

Source locator: study guide, "Implement and manage storage" > "Configure access to storage".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `storage-network-controls` | Configure storage firewall and virtual-network access restrictions | direct | 02-storage.md > Storage access and network controls | 26, 43 | drafted | drafted |
| `storage-sas` | Create and use scoped, time-limited SAS tokens | direct | 02-storage.md > Storage access and network controls | 27 | drafted | drafted |
| `storage-access-policies` | Configure stored access policies where the SAS type supports them | direct | 02-storage.md > Storage access and network controls | 28 | drafted | drafted |
| `storage-account-keys` | Manage storage account keys and their lifecycle | direct | 02-storage.md > Storage access and network controls | 29 | drafted | drafted |
| `files-identity-access` | Configure identity-based authorization for Azure Files | direct | 02-storage.md > Storage access and network controls | 30 | drafted | drafted |

### Storage accounts and data operations

Source locator: study guide, "Implement and manage storage" > "Configure and manage storage accounts".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `storage-account-create` | Create and configure storage accounts for workload needs | direct | 02-storage.md > Storage accounts and data operations | 31 | drafted | drafted |
| `storage-redundancy` | Select Azure Storage redundancy for required failure domains | direct | 02-storage.md > Storage accounts and data operations | 32 | drafted | drafted |
| `storage-object-replication` | Configure object replication for supported blob scenarios | direct | 02-storage.md > Storage accounts and data operations | 33 | drafted | drafted |
| `storage-encryption` | Configure storage account encryption and key options | direct | 02-storage.md > Storage accounts and data operations | 34 | drafted | drafted |
| `storage-data-tools` | Manage data with Storage Explorer and AzCopy | direct | 02-storage.md > Storage accounts and data operations | 35 | drafted | drafted |

### Azure Files and Blob Storage

Source locator: study guide, "Implement and manage storage" > "Configure Azure Files and Azure Blob Storage".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `files-share` | Create and configure an Azure file share | direct | 02-storage.md > Azure Files and Blob Storage | 40 | drafted | drafted |
| `blob-container` | Create and configure a Blob Storage container | direct | 02-storage.md > Azure Files and Blob Storage | 37 | drafted | drafted |
| `blob-access-tiers` | Select blob access tiers for cost and retrieval needs | direct | 02-storage.md > Azure Files and Blob Storage | 38 | drafted | drafted |
| `blob-soft-delete` | Configure soft delete for blobs and containers | direct | 02-storage.md > Azure Files and Blob Storage | 39 | drafted | drafted |
| `files-snapshots-soft-delete` | Configure Azure Files snapshots and share soft delete | direct | 02-storage.md > Azure Files and Blob Storage | 36 | drafted | drafted |
| `blob-lifecycle` | Configure blob lifecycle rules for tiering and deletion | direct | 02-storage.md > Azure Files and Blob Storage | 41 | drafted | drafted |
| `blob-versioning` | Configure and use blob versioning | direct | 02-storage.md > Azure Files and Blob Storage | 42 | drafted | drafted |

## Compute (20–25%)

### Resource deployment with ARM and Bicep

Source locator: study guide, "Deploy and manage Azure compute resources" > "Automate deployment of resources by using ARM templates or Bicep files".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `iac-interpret` | Interpret ARM template or Bicep resources, parameters, and dependencies | direct | 03-compute.md > Resource deployment with ARM and Bicep | 44, 48 | drafted | drafted |
| `iac-modify-arm` | Modify an existing ARM template to meet deployment requirements | direct | 03-compute.md > Resource deployment with ARM and Bicep | 44 | drafted | drafted |
| `iac-modify-bicep` | Modify an existing Bicep file to meet deployment requirements | direct | 03-compute.md > Resource deployment with ARM and Bicep | 45 | drafted | drafted |
| `iac-deploy` | Deploy resources using ARM templates or Bicep | direct | 03-compute.md > Resource deployment with ARM and Bicep | 46, 48 | drafted | drafted |
| `iac-export-convert` | Export a deployment or convert an ARM template to Bicep | direct | 03-compute.md > Resource deployment with ARM and Bicep | 47 | drafted | drafted |

### Virtual machines and scale sets

Source locator: study guide, "Deploy and manage Azure compute resources" > "Create and configure virtual machines".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `vm-create` | Create and configure a virtual machine and its dependencies | direct | 03-compute.md > Virtual machines and scale sets | 49 | drafted | drafted |
| `vm-encryption-host` | Configure host encryption for supported virtual machines | direct | 03-compute.md > Virtual machines and scale sets | 52 | drafted | drafted |
| `vm-move` | Move a VM within supported resource-group, subscription, or region scenarios | direct | 03-compute.md > Virtual machines and scale sets | 55 | drafted | drafted |
| `vm-sizes` | Select VM sizes for workload capacity and available quotas | direct | 03-compute.md > Virtual machines and scale sets | 50 | drafted | drafted |
| `vm-disks` | Manage managed disks and their performance characteristics | direct | 03-compute.md > Virtual machines and scale sets | 51 | drafted | drafted |
| `vm-availability` | Deploy VMs across availability zones or availability sets | direct | 03-compute.md > Virtual machines and scale sets | 53 | drafted | drafted |
| `vm-scale-sets` | Deploy and configure Virtual Machine Scale Sets | direct | 03-compute.md > Virtual machines and scale sets | 54 | drafted | drafted |

### Azure container services

Source locator: study guide, "Deploy and manage Azure compute resources" > "Provision and manage containers in the Azure portal".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `containers-registry` | Create and manage an Azure Container Registry | direct | 03-compute.md > Azure container services | 56 | drafted | drafted |
| `containers-aci` | Provision a workload with Azure Container Instances | direct | 03-compute.md > Azure container services | 57 | drafted | drafted |
| `containers-apps` | Provision a workload with Azure Container Apps | direct | 03-compute.md > Azure container services | 58 | drafted | drafted |
| `containers-sizing-scaling` | Manage container sizing and scaling for ACI and Container Apps | direct | 03-compute.md > Azure container services | 59 | drafted | drafted |

### Azure App Service

Source locator: study guide, "Deploy and manage Azure compute resources" > "Create and configure Azure App Service".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `appservice-plan` | Provision an App Service plan for workload requirements | direct | 03-compute.md > Azure App Service | 60, 68 | drafted | drafted |
| `appservice-scaling` | Configure scaling for an App Service plan | direct | 03-compute.md > Azure App Service | 61, 68 | drafted | drafted |
| `appservice-create` | Create and configure an App Service app | direct | 03-compute.md > Azure App Service | 62 | drafted | drafted |
| `appservice-tls` | Configure certificates and TLS for App Service | direct | 03-compute.md > Azure App Service | 63 | drafted | drafted |
| `appservice-custom-domain` | Map a custom DNS name to an App Service app | direct | 03-compute.md > Azure App Service | 64 | drafted | drafted |
| `appservice-backup` | Configure backups for an App Service app | direct | 03-compute.md > Azure App Service | 65 | drafted | drafted |
| `appservice-networking` | Configure App Service networking settings | direct | 03-compute.md > Azure App Service | 66 | drafted | drafted |
| `appservice-slots` | Configure deployment slots for controlled app releases | direct | 03-compute.md > Azure App Service | 67 | drafted | drafted |

## Virtual networking (15–20%)

### Virtual networks, subnets, and routing

Source locator: study guide, "Implement and manage virtual networking" > "Configure and manage virtual networks in Azure".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `network-vnets-subnets` | Create and configure virtual networks and subnets | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | 69 | drafted | drafted |
| `network-peering` | Configure VNet peering and understand its routing behavior | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | 70, 71 | drafted | drafted |
| `network-public-ips` | Configure public IP addresses for supported Azure resources | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | 72 | drafted | drafted |
| `network-udr` | Configure user-defined routes and next hops | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | 70, 73, 74 | drafted | drafted |
| `network-connectivity-troubleshoot` | Troubleshoot virtual network connectivity and routing | direct | 04-virtual-networking.md > Virtual networks, subnets, and routing | 73, 75 | drafted | drafted |

### Secure access and private connectivity

Source locator: study guide, "Implement and manage virtual networking" > "Configure secure access to virtual networks".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `network-nsg-asg` | Create and configure NSGs and application security groups | direct | 04-virtual-networking.md > Secure access and private connectivity | 76, 77, 78 | drafted | drafted |
| `network-effective-rules` | Evaluate effective NSG security rules for a network interface | direct | 04-virtual-networking.md > Secure access and private connectivity | 75, 77 | drafted | drafted |
| `network-bastion` | Implement Azure Bastion for VM administration | direct | 04-virtual-networking.md > Secure access and private connectivity | 79, 80 | drafted | drafted |
| `network-service-endpoints` | Configure service endpoints for supported Azure PaaS services | direct | 04-virtual-networking.md > Secure access and private connectivity | 81 | drafted | drafted |
| `network-private-endpoints` | Configure private endpoints for supported Azure PaaS services | direct | 04-virtual-networking.md > Secure access and private connectivity | 82 | drafted | drafted |

### Name resolution and load balancing

Source locator: study guide, "Implement and manage virtual networking" > "Configure name resolution and load balancing".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `network-dns` | Configure Azure public and private DNS | direct | 04-virtual-networking.md > Name resolution and load balancing | 82, 83, 84 | drafted | drafted |
| `network-load-balancer` | Configure an internal or public Azure Load Balancer | direct | 04-virtual-networking.md > Name resolution and load balancing | 85 | drafted | drafted |
| `network-load-balancer-troubleshoot` | Troubleshoot load-balancer rules, probes, and backend health | direct | 04-virtual-networking.md > Name resolution and load balancing | 86 | drafted | drafted |

## Monitoring and recovery (10–15%)

### Azure Monitor and Network Watcher

Source locator: study guide, "Monitor and maintain Azure resources" > "Monitor resources in Azure".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `monitor-metrics` | Interpret Azure Monitor metrics for resource behavior | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | 87 | drafted | drafted |
| `monitor-log-settings` | Configure resource log collection and diagnostic settings | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | 88, 92 | drafted | drafted |
| `monitor-log-analysis` | Query and analyze Azure Monitor logs | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | 88, 89, 90 | drafted | drafted |
| `monitor-alerts` | Configure alert rules, action groups, and alert processing rules | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | 91, 95 | drafted | drafted |
| `monitor-insights` | Use Insights to monitor supported VMs, storage, and networks | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | 93 | drafted | drafted |
| `monitor-network-watcher` | Use Network Watcher and Connection Monitor to diagnose connectivity | direct | 05-monitoring-and-recovery.md > Azure Monitor and Network Watcher | 94, 95 | drafted | drafted |

### Backup and disaster recovery

Source locator: study guide, "Monitor and maintain Azure resources" > "Implement backup and recovery".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `recovery-services-vault` | Create a Recovery Services vault for a supported workload | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | 97 | drafted | drafted |
| `recovery-backup-vault` | Create an Azure Backup vault for a supported workload | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | 96 | drafted | drafted |
| `recovery-backup-policy` | Create and configure a backup policy | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | 98 | drafted | drafted |
| `recovery-backup-restore` | Perform backup and restore operations with Azure Backup | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | 99 | drafted | drafted |
| `recovery-site-recovery` | Configure Azure Site Recovery for supported resources | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | 100 | drafted | drafted |
| `recovery-failover` | Perform or test a failover to a secondary region | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | 100 | drafted | drafted |
| `recovery-reports-alerts` | Configure and interpret backup reports and alerts | direct | 05-monitoring-and-recovery.md > Backup and disaster recovery | 92 | drafted | drafted |

## Known gaps and review state

- All mapped objectives have a drafted book section, but the mapping and technical explanations have not yet been human-reviewed. Do not treat `drafted` as an assurance that the source outline is exhaustive.
- The mock exam (`mock_exams/az_104/az-104.exam.yaml`, 100 questions) is drafted and not yet human-reviewed. Outcomes with no question remain `todo`: none.
- Product support, service limits, portal workflows, and pricing can change. Verify version-sensitive decisions against the linked Microsoft Learn pages before applying them.
