# AZ-900 coverage map

Working traceability map. Outcomes are interpreted from the source guide in the author's words; IDs are internal and provisional. Status: `todo`/`drafted`/`reviewed`. Exam questions are IDs tagged `objective:<id>`; `validate.py --coverage` checks both directions.

## Cloud concepts (25-30%)

### What cloud computing is

Source locator: study guide, "Describe cloud concepts" > "Describe cloud computing".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `cc-define-cloud` | Explain what cloud computing is and its defining characteristics | direct | 01-cloud-concepts.md > What cloud computing is | 1 | todo | drafted |
| `cc-shared-responsibility` | Explain who is responsible for what under the shared responsibility model | direct | 01-cloud-concepts.md > What cloud computing is | 2, 10 | todo | drafted |
| `cc-cloud-models` | Distinguish public, private, and hybrid clouds | direct | 01-cloud-concepts.md > What cloud computing is | 3, 8 | todo | drafted |
| `cc-cloud-model-use-cases` | Choose the appropriate cloud model for a scenario | direct | 01-cloud-concepts.md > What cloud computing is | 4 | todo | drafted |
| `cc-consumption-model` | Explain consumption-based billing and its trade-offs | direct | 01-cloud-concepts.md > What cloud computing is | 5, 11, 12 | todo | drafted |
| `cc-pricing-models` | Compare cloud pricing models (CapEx vs OpEx, pay-as-you-go, reservations) | direct; models inferred | 01-cloud-concepts.md > What cloud computing is | 6, 9 | todo | drafted |
| `cc-serverless` | Explain serverless computing and when it fits | direct | 01-cloud-concepts.md > What cloud computing is | 7 | todo | drafted |

### Why organizations use the cloud

Source locator: study guide, "Describe cloud concepts" > "Describe the benefits of using cloud services".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `cc-ha-scalability` | Describe high availability and scalability (vertical, horizontal, elasticity) | direct | 01-cloud-concepts.md > Why organizations use the cloud | 13, 14, 20 | todo | drafted |
| `cc-reliability-predictability` | Describe reliability and predictability (performance and cost) | direct | 01-cloud-concepts.md > Why organizations use the cloud | 15, 16, 19 | todo | drafted |
| `cc-security-governance` | Describe security and governance benefits of the cloud | direct | 01-cloud-concepts.md > Why organizations use the cloud | 17 | todo | drafted |
| `cc-manageability` | Describe manageability benefits (of the cloud and in the cloud) | direct | 01-cloud-concepts.md > Why organizations use the cloud | 18 | todo | drafted |

### Cloud service types: IaaS, PaaS, SaaS

Source locator: study guide, "Describe cloud concepts" > "Describe cloud service types".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `cc-iaas` | Describe infrastructure as a service | direct | 01-cloud-concepts.md > Cloud service types: IaaS, PaaS, SaaS | 21, 24, 25 | todo | drafted |
| `cc-paas` | Describe platform as a service | direct | 01-cloud-concepts.md > Cloud service types: IaaS, PaaS, SaaS | 22, 24, 26 | todo | drafted |
| `cc-saas` | Describe software as a service | direct | 01-cloud-concepts.md > Cloud service types: IaaS, PaaS, SaaS | 23, 24, 27 | todo | drafted |
| `cc-service-type-use-cases` | Match IaaS, PaaS, and SaaS to use cases | direct | 01-cloud-concepts.md > Cloud service types: IaaS, PaaS, SaaS | 21, 22, 27, 28 | todo | drafted |

## Azure architecture and services (35-40%)

### Azure's physical and organizational structure

Source locator: study guide, "Describe Azure architecture and services" > "Describe the core architectural components of Azure".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `as-regions` | Describe regions, region pairs, and sovereign regions | direct | 02-azure-architecture-and-services.md > Azure's physical and organizational structure | 29, 37 | todo | drafted |
| `as-availability-zones` | Describe availability zones and zone-redundant options | direct | 02-azure-architecture-and-services.md > Azure's physical and organizational structure | 30 | todo | drafted |
| `as-datacenters` | Describe Azure datacenters | direct | 02-azure-architecture-and-services.md > Azure's physical and organizational structure | 31 | todo | drafted |
| `as-resources-rgs` | Describe resources and resource groups | direct | 02-azure-architecture-and-services.md > Azure's physical and organizational structure | 32, 36 | todo | drafted |
| `as-subscriptions` | Describe subscriptions and their role | direct | 02-azure-architecture-and-services.md > Azure's physical and organizational structure | 33 | todo | drafted |
| `as-management-groups` | Describe management groups | direct | 02-azure-architecture-and-services.md > Azure's physical and organizational structure | 34 | todo | drafted |
| `as-resource-hierarchy` | Explain how management groups, subscriptions, and resource groups nest | direct | 02-azure-architecture-and-services.md > Azure's physical and organizational structure | 35 | todo | drafted |

### Compute and networking

Source locator: study guide, "Describe Azure architecture and services" > "Describe Azure compute and networking services".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `as-compute-types` | Compare virtual machines, containers, and functions | direct | 02-azure-architecture-and-services.md > Compute and networking | 38 | todo | drafted |
| `as-vm-options` | Describe VM options: VMs, scale sets, availability sets, Azure Virtual Desktop | direct | 02-azure-architecture-and-services.md > Compute and networking | 39, 41 | todo | drafted |
| `as-vm-resources` | Identify resources required to run a VM | direct | 02-azure-architecture-and-services.md > Compute and networking | 40 | todo | drafted |
| `as-app-hosting` | Compare app hosting options (web apps, containers, VMs) | direct | 02-azure-architecture-and-services.md > Compute and networking | 42 | todo | drafted |
| `as-vnet-subnets-peering` | Describe virtual networks, subnets, and peering | direct; broad in source | 02-azure-architecture-and-services.md > Compute and networking | 43, 44 | todo | drafted |
| `as-dns-vpn-expressroute` | Describe Azure DNS, VPN Gateway, and ExpressRoute | direct; split from one source bullet | 02-azure-architecture-and-services.md > Compute and networking | 45, 46 | todo | drafted |
| `as-endpoints` | Define public and private endpoints | direct | 02-azure-architecture-and-services.md > Compute and networking | 47 | todo | drafted |

### Storage and data movement

Source locator: study guide, "Describe Azure architecture and services" > "Describe Azure storage services".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `as-storage-services` | Compare Azure Storage services (Blobs, Files, Queues, Tables, Disks) | direct | 02-azure-architecture-and-services.md > Storage and data movement | 48 | todo | drafted |
| `as-storage-tiers` | Describe access tiers | direct | 02-azure-architecture-and-services.md > Storage and data movement | 49 | todo | drafted |
| `as-storage-redundancy` | Describe redundancy options (LRS, ZRS, GRS, GZRS) | direct | 02-azure-architecture-and-services.md > Storage and data movement | 50, 55, 56 | todo | drafted |
| `as-storage-account-types` | Describe storage account options and types | direct | 02-azure-architecture-and-services.md > Storage and data movement | 51 | todo | drafted |
| `as-file-movement` | Identify tools for moving files (AzCopy, Storage Explorer, File Sync) | direct | 02-azure-architecture-and-services.md > Storage and data movement | 52, 53 | todo | drafted |
| `as-migration-options` | Describe migration options (Azure Migrate, Data Box) | direct | 02-azure-architecture-and-services.md > Storage and data movement | 54 | todo | drafted |

### Identity, access, and security

Source locator: study guide, "Describe Azure architecture and services" > "Describe Azure identity, access, and security".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `as-directory-services` | Describe Microsoft Entra ID and Entra Domain Services | direct | 02-azure-architecture-and-services.md > Identity, access, and security | 57, 66 | todo | drafted |
| `as-authentication-methods` | Describe SSO, MFA, and passwordless authentication | direct | 02-azure-architecture-and-services.md > Identity, access, and security | 58 | todo | drafted |
| `as-external-identities` | Describe external identities | direct | 02-azure-architecture-and-services.md > Identity, access, and security | 59 | todo | drafted |
| `as-conditional-access` | Describe Conditional Access | direct | 02-azure-architecture-and-services.md > Identity, access, and security | 60 | todo | drafted |
| `as-rbac` | Describe Azure RBAC | direct | 02-azure-architecture-and-services.md > Identity, access, and security | 61, 65 | todo | drafted |
| `as-zero-trust` | Describe Zero Trust | direct | 02-azure-architecture-and-services.md > Identity, access, and security | 62 | todo | drafted |
| `as-defense-in-depth` | Describe defense in depth | direct | 02-azure-architecture-and-services.md > Identity, access, and security | 63 | todo | drafted |
| `as-defender-for-cloud` | Describe the purpose of Microsoft Defender for Cloud | direct | 02-azure-architecture-and-services.md > Identity, access, and security | 64 | todo | drafted |

## Azure management and governance (30-35%)

### Costs in Azure

Source locator: study guide, "Describe Azure management and governance" > "Describe cost management in Azure".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `mg-cost-factors` | Identify factors that affect Azure costs | direct | 03-azure-management-and-governance.md > Costs in Azure | 67, 73 | todo | drafted |
| `mg-pricing-calculator` | Use the pricing calculator to estimate cost | direct | 03-azure-management-and-governance.md > Costs in Azure | 68, 74 | todo | drafted |
| `mg-cost-management` | Describe Cost Management capabilities | direct | 03-azure-management-and-governance.md > Costs in Azure | 69, 71 | todo | drafted |
| `mg-tags` | Describe the purpose of tags | direct | 03-azure-management-and-governance.md > Costs in Azure | 70, 72 | todo | drafted |

### Governance and compliance

Source locator: study guide, "Describe Azure management and governance" > "Describe features and tools in Azure for governance and compliance".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `mg-purview` | Describe the purpose of Microsoft Purview | direct | 03-azure-management-and-governance.md > Governance and compliance | 77 | todo | drafted |
| `mg-policy` | Describe the purpose of Azure Policy | direct | 03-azure-management-and-governance.md > Governance and compliance | 75, 78, 80 | todo | drafted |
| `mg-locks` | Describe the purpose of resource locks | direct | 03-azure-management-and-governance.md > Governance and compliance | 76, 79, 81 | todo | drafted |

### Managing and deploying resources

Source locator: study guide, "Describe Azure management and governance" > "Describe features and tools for managing and deploying Azure resources".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `mg-portal` | Describe the Azure portal | direct | 03-azure-management-and-governance.md > Managing and deploying resources | 82 | todo | drafted |
| `mg-shell-cli-powershell` | Describe Cloud Shell, Azure CLI, and Azure PowerShell | direct | 03-azure-management-and-governance.md > Managing and deploying resources | 83, 89 | todo | drafted |
| `mg-arc` | Describe the purpose of Azure Arc | direct | 03-azure-management-and-governance.md > Managing and deploying resources | 84, 90 | todo | drafted |
| `mg-iac` | Describe infrastructure as code | direct | 03-azure-management-and-governance.md > Managing and deploying resources | 85, 86, 88 | todo | drafted |
| `mg-arm` | Describe Azure Resource Manager and ARM templates | direct | 03-azure-management-and-governance.md > Managing and deploying resources | 87, 88, 91 | todo | drafted |

### Monitoring and advice

Source locator: study guide, "Describe Azure management and governance" > "Describe monitoring tools in Azure".

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|
| `mg-advisor` | Describe the purpose of Azure Advisor | direct | 03-azure-management-and-governance.md > Monitoring and advice | 92, 99 | todo | drafted |
| `mg-service-health` | Describe Azure Service Health | direct | 03-azure-management-and-governance.md > Monitoring and advice | 93, 94 | todo | drafted |
| `mg-azure-monitor` | Describe Azure Monitor, Log Analytics, and alerts | direct; broad in source | 03-azure-management-and-governance.md > Monitoring and advice | 95, 96, 100 | todo | drafted |
| `mg-app-insights` | Describe Application Insights | direct | 03-azure-management-and-governance.md > Monitoring and advice | 97, 98, 100 | todo | drafted |

## Known gaps

None recorded yet.
