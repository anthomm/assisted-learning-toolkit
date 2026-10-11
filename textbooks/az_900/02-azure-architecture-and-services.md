# Azure architecture and services (35-40%)

This chapter maps the physical locations, organization, and services that make up Azure to everyday design choices. It introduces compute and networking, storage and migration, and identity and security concepts, emphasizing how to select a service based on a workload rather than memorize product names in isolation. Examples focus on the distinctions that help you explain a design and recognize the appropriate Azure building block.

## Azure's physical and organizational structure

### Learning intent

Be able to describe where Azure resources run and how Azure organizes them for management. Distinguish regions, region pairs, availability zones, and datacenters; then explain how resources, resource groups, subscriptions, and management groups form a hierarchy. The core practical idea is that physical resilience and management scope are related design concerns, but they are not the same thing: a governance hierarchy does not itself make an application highly available.

### Core concepts

**Regions (`as-regions`).** An Azure region is a geographic area containing one or more datacenters connected through a low-latency network. A region is a deployment location for regional Azure resources; which services, features, and capacities are available varies by region. The region selected for a resource can affect latency to users and other components, data residency, resilience options, and cost. A region name in the portal is a service location choice, not a guarantee that every Azure service is available there.

Some regions are associated with a second region in a *region pair*. Some services use the pair for geo-replication or disaster recovery, and Azure may stagger updates or prioritize recovery across the pair. Deployment in one member does not itself replicate an application or automatically fail it over. Many regions are unpaired, and some services offer geo-redundancy independently. Plan application recovery explicitly and verify each service's behavior.

A *geography* is a broad market and data-residency area that can contain multiple regions. Specialized or sovereign cloud environments address particular legal, compliance, or operational requirements. A public-cloud region name alone does not establish that a specific legal regime applies; confirm requirements and service availability with current Microsoft documentation and your compliance team.

**Availability zones (`as-availability-zones`).** In a region that supports them, availability zones are physically separate groupings of one or more datacenters. Each zone has independent power, cooling, and networking, with connectivity designed for low-latency communication across the region. Zones are intended to reduce the chance that a localized datacenter or infrastructure failure affects every copy of a workload. Not every region or Azure service supports zones, and the service may use a different subset or count of zones than the region offers.

A *zonal* resource is placed in one selected zone; a *zone-redundant* resource is distributed or replicated across multiple zones by the service. Zonal placement alone does not protect against failure of that zone: the solution needs instances in other zones and a failover design. Service-managed zone redundancy behavior varies. A resilient web tier can still depend on a single-zone database or network component.

**Datacenters (`as-datacenters`).** A datacenter is a physical facility that houses computing, networking, and storage hardware. Azure datacenters are operated as part of Microsoft's cloud infrastructure; customers usually consume Azure services rather than select a specific building. Availability zones abstract physical placement into a failure-isolation choice. For a service that does not expose zone controls, consult its reliability documentation instead of assuming that a resource is in one particular datacenter or zone.

**Resources and resource groups (`as-resources-rgs`).** A *resource* is a manageable Azure item, such as a virtual machine, virtual network, storage account, database, or web app. A *resource group* is a logical container for resources commonly managed together. It gives a shared scope for access control, policy, monitoring, tagging, and lifecycle operations. Group resources with a sensible common lifecycle; shared networking, for example, may need a different lifecycle from an application.

Every resource belongs to a resource group, and resource groups belong to one subscription. The resource group's location stores metadata about the group; the resources within it can be in other regions. Deleting a resource group is a consequential lifecycle action because it can delete resources in the group. Use deliberate naming, access controls, and safeguards before applying bulk operations.

**Subscriptions (`as-subscriptions`).** An Azure subscription is a management and deployment boundary for Azure resources and is associated with a billing arrangement. It provides a scope for access control, quotas, and governance policies. Organizations often separate subscriptions to reflect environments, teams, business units, or compliance boundaries, but a subscription is not the same thing as a Microsoft Entra directory and should not be confused with a resource group. A tenant can be associated with multiple subscriptions; a subscription trusts one Microsoft Entra tenant at a time for its identity directory context.

Subscriptions also have service-specific quotas, which may be adjustable or fixed; available capacity varies by region and resource type. A subscription helps organize and govern resources but does not by itself isolate their network traffic. Check service limits before large deployments.

**Management groups (`as-management-groups`).** Management groups provide a hierarchy above subscriptions for organizing and governing them at scale. Policies and role assignments can be applied at a management-group scope and inherited by descendant scopes, including subscriptions and their resources, subject to the feature and scope involved. This enables central administration without configuring every subscription independently. Subscriptions in one management-group hierarchy must use the same Microsoft Entra tenant.

**Resource hierarchy (`as-resource-hierarchy`).** The main governance hierarchy is:

`Microsoft Entra tenant (directory) → management groups → subscriptions → resource groups → resources`

Not every organization needs every optional level. Management groups may contain child management groups or subscriptions; a subscription contains resource groups; a resource group contains resources. Parent-scope policy and role assignments can apply down the tree. A resource group does not contain a subscription, and a management group is not a physical location. This hierarchy supports governance; region and zone placement describe where supported service resources run.

| Scope | Primarily helps you organize or control | Typical use |
| --- | --- | --- |
| Management group | Multiple subscriptions | Apply broad policy or access governance across a portfolio |
| Subscription | A deployment, quota, and billing-related scope | Separate production from development or isolate cost/governance boundaries |
| Resource group | Related resources with a common management lifecycle | Deploy and manage one application environment |
| Resource | An individual service instance | Configure a VM, storage account, network, or database |

### How it works, distinctions, limits, and defaults

Keep physical placement (region → zones → datacenters) separate from governance (tenant → management groups → subscriptions → resource groups → resources). A resource has a place in both maps. Region pairs do not guarantee application replication or automatic failover; availability zones protect against some zone failures but are not regional disaster recovery. The component that detects failure, replicates data, routes traffic, and restores service depends on the service and architecture.

Resource Manager is Azure's consistent management layer across portal, CLI, PowerShell, APIs, and SDKs. Resource groups and subscriptions are management scopes; regions and zones are service locations. Region lists, service availability, quotas, and residency rules change, so validate them before deployment.

> **Verify:** Check the current region list, zone support, restricted-region access, and service reliability guidance.

### Example or worked scenario

A retailer separates production and nonproduction into subscriptions. A management group applies a region policy to both; a production scope adds stricter rules. The production subscription has separate resource groups for its ordering app and shared networking. The app uses a supported zone-resilient tier, while the team separately configures and tests database recovery in another region. Scopes govern and organize; they do not perform failover.

### Hands-on activity

In the portal, inspect **Subscriptions**, **Resource groups**, and—if permitted—**Management groups**. Compare a group's location with the regions of its resources; avoid making changes. Use the current Microsoft Learn region list to confirm service and zone availability. Optional read-only CLI: `az account show --output table` shows the active subscription; `az group list --output table` lists visible groups.

### Exam or practical application

For location scenarios, identify the requirement: latency, residency, a zone failure, or regional disaster recovery. For governance scenarios, select a scope that applies to the intended subscriptions or resources. Common traps are assuming a region pair automatically deploys a replica, treating a resource-group location as the location of all its resources, or confusing a management group with a physical location.

### Self-check questions

1. **Does deploying a VM in one region of a region pair automatically create a copy in the paired region?**  
   **Answer:** No. Pairing can support some service-level replication and recovery strategies, but deployment and application failover must be configured and tested.

2. **What is the difference between a zonal and a zone-redundant resource?**  
   **Answer:** A zonal resource is assigned to one selected zone. A zone-redundant resource is distributed or replicated across multiple zones by the service; exact behavior depends on the service.

3. **Can a resource group contain resources deployed to different Azure regions?**  
   **Answer:** Yes. The resource group's own location concerns its metadata; it does not force every resource in the group to use that region.

4. **Which scope is above subscriptions and is used to govern several subscriptions together?**  
   **Answer:** A management group.

5. **Put these scopes in parent-to-child order: resource group, management group, resource, subscription.**  
   **Answer:** Management group → subscription → resource group → resource.

### Sources

- [Azure regions, region pairs, and nonpaired regions](https://learn.microsoft.com/en-us/azure/reliability/regions-paired)
- [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/en-us/azure/azure-sovereign-clouds/microsoft-sovereign-cloud)
- [List of Azure regions](https://learn.microsoft.com/en-us/azure/reliability/regions-list)
- [What are Azure Availability Zones?](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)
- [What is Azure Resource Manager?](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- [Manage resource groups with the Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal)
- [Organize resources with management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)
- [Azure subscription and service limits, quotas, and constraints](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits)

## Compute and networking

### Learning intent

Choose a compute model that matches how much infrastructure control an application needs, and identify the foundational VM resources that make a virtual machine usable. Explain the purpose of common VM availability and scaling options, app-hosting services, virtual networks and subnets, peering, DNS, VPN Gateway, ExpressRoute, and public/private endpoints. Focus on the workload requirement—control, portability, event response, managed operations, connectivity, or exposure—rather than assuming that one service is universally best.

### Core concepts

**Compute types (`as-compute-types`).** Azure offers multiple ways to run software. The level of control generally trades off against the amount of infrastructure the customer must manage.

| Model | What it runs | Who manages most of the host environment? | Good fit |
| --- | --- | --- | --- |
| Virtual machines | A guest operating system and software selected by the customer | Customer manages the OS and installed software; Azure manages physical infrastructure | Existing software, custom OS or network needs, lift-and-shift workloads |
| Containers | An application packaged with its dependencies in an image | Depends on the hosting service; a managed container platform can abstract hosts and orchestration | Portable services, microservices, repeatable packaging |
| Functions | Small units of code activated by triggers or events | Azure manages the execution infrastructure according to the selected hosting plan | Event-driven tasks, scheduled work, or small APIs |

A VM is a virtual computer with a guest operating system. It provides broad control but still requires maintenance such as patching, configuration, and software management. Containers package an app and its dependencies, but containers are not themselves a complete hosting service: choose a platform that runs and scales them. Functions let a developer focus on event-triggered code, while the platform handles much of the hosting and scaling work. “Serverless” means the customer does not manage the underlying servers in the same way; it does not mean that servers do not exist or that an application has no configuration, costs, or operational responsibilities.

**VM options (`as-vm-options`).** A standalone VM is suited to a workload needing a particular machine configuration. A *Virtual Machine Scale Set* manages a group of VMs and can scale the instance count based on demand or a schedule; load balancing and distribution features support applications that run across instances. An *availability set* logically distributes VMs across fault and update domains to reduce correlated maintenance or infrastructure failures, especially in regions without zones. Where supported and appropriate, Microsoft recommends considering scale sets with flexible orchestration for broad high-availability and scale capabilities; availability sets remain a distinct pattern. Neither an availability set nor a scale set guarantees application-level resilience if the application or data tier is a single point of failure.

*Azure Virtual Desktop* is a desktop and app virtualization service, not just a general-purpose application web-hosting option. It delivers Windows desktops or individual RemoteApps to users from host pools, including pooled or personal desktop approaches. It is useful when users need centrally managed remote desktops or published applications. It has its own service configuration, identity, networking, and VM cost considerations.

**VM resources (`as-vm-resources`).** A VM typically relies on a virtual network, a network interface attached to that network, an operating-system disk, and often one or more data disks. It can also use private and/or public IP addressing, network security groups (NSGs), monitoring, and identity or access configuration. A VM size determines a supported combination of compute, memory, and networking capacity; available sizes and features vary by region and workload. The OS image supplies the operating system, and credentials or keys are needed for administrative access. Consider data-disk separation where it suits the workload, and select a disk type and size for its performance and durability requirements. Each associated resource can have separate pricing or limits.

**App hosting (`as-app-hosting`).** Common choices include Azure App Service, container hosting, and VMs. App Service is a managed platform for web applications, mobile back ends, and REST APIs. It supports multiple language runtimes and custom containers while abstracting much of the server administration. Azure Container Apps is a managed platform for containerized applications, including APIs, microservices, jobs, and event-driven workloads, with platform features for ingress and scaling. Azure Kubernetes Service (AKS) offers managed Kubernetes when the application needs Kubernetes APIs and orchestration control; it is not identical to a platform that hides Kubernetes details. VMs offer the greatest control but require the most guest-OS operations. Azure Functions is a separate event-driven/serverless compute choice, even though functions can also run on some container platforms.

| Hosting choice | Control and management emphasis | Typical scenario |
| --- | --- | --- |
| App Service | Managed web-app platform; less host management | Web app or REST API using a supported runtime |
| Container Apps | Managed container platform with scaling and application-focused features | Containerized API, microservice, background job |
| AKS | Managed Kubernetes control plane; customer works with Kubernetes concepts | Kubernetes orchestration, portability or fine-grained cluster requirements |
| Virtual machines | Customer controls guest OS and software | Legacy or specialized software requiring machine-level control |
| Functions | Event-driven code with triggers and bindings | React to queue, timer, HTTP, or other supported events |

**Virtual networks, subnets, and peering (`as-vnet-subnets-peering`).** An Azure Virtual Network (VNet) is a logically isolated network boundary for Azure resources. It has an address space defined with IP address ranges and can be segmented into *subnets*. Subnets group resources and support traffic controls or service-specific configuration; they are not necessarily separate VNets. Address ranges must be planned to avoid overlap with connected networks, especially when peering or hybrid connectivity is planned.

VNet peering connects two VNets over Microsoft's network so their resources can communicate using private IP addresses, subject to routes, security rules, and peering settings. Local peering links VNets in the same region; global peering connects across regions. Peering is not the same as merging subscription ownership or removing the need for network security. VNet peering is not transitive by default: if VNet A peers with B and B peers with C, that alone does not mean A can reach C. Centralized transit requires an appropriate hub-and-spoke or other routing design.

**DNS, VPN Gateway, and ExpressRoute (`as-dns-vpn-expressroute`).** DNS translates names into IP addresses. Azure DNS provides public DNS hosting and private DNS zones for name resolution in virtual networks; Azure DNS Private Resolver can support resolution between Azure private zones and on-premises DNS environments without operating DNS VMs. DNS resolves names; it does not itself create a network route or grant access.

Azure VPN Gateway connects VNets or connects an Azure VNet with an on-premises network using encrypted VPN tunnels. Common patterns include site-to-site connections for network-to-network, point-to-site connections for individual remote clients, and VNet-to-VNet connections. These VPN connections use the public internet as transport for encrypted tunnels in common hybrid setups. ExpressRoute extends an on-premises network to Microsoft cloud through a connectivity provider and a private connection that does not traverse the public internet. It can offer more consistent network characteristics for eligible use cases, but it requires connectivity-provider arrangements and appropriate circuit and routing design. Neither VPN nor ExpressRoute automatically configures the application’s DNS, routes, or security rules.

| Need | Typical service | Key distinction |
| --- | --- | --- |
| Publish and resolve public DNS records | Azure Public DNS | DNS hosting for internet-facing domains |
| Resolve private names within connected VNets | Azure Private DNS | Private zone and VNet-link configuration |
| Encrypted connection over internet | VPN Gateway | Tunnel-based connectivity; site-to-site or point-to-site patterns |
| Provider-backed private connectivity | ExpressRoute | Private connection to Microsoft cloud, not a VPN tunnel over the public internet |

**Public and private endpoints (`as-endpoints`).** A *public endpoint* is reachable through a public IP address and the public network path, subject to the service's authentication and network controls. A *private endpoint* is a network interface with a private IP address from a VNet subnet, connected through Azure Private Link to a supported service. It lets a client reach that service through a private IP path. Private endpoints require correct DNS configuration for clients to resolve the service name to the intended private address, and the service owner may need to approve the connection.

Don't confuse private endpoints with *service endpoints*. A service endpoint extends VNet identity and routes traffic to a supported Azure service over the Azure backbone, while the service continues to use its service endpoint address; a private endpoint places a private IP network interface into your VNet for the service connection. Microsoft recommends Private Link/private endpoints for many private access scenarios, but the correct option depends on architecture and service support. A private endpoint does not by itself disable every public path to the service; configure the service's network access controls as required.

### How it works, distinctions, limits, and defaults

Choose compute by balancing control with managed operations. VMs allow guest-OS control but require patching and configuration; App Service reduces server management for supported web workloads; managed container platforms fit containerized apps; Functions fit event-triggered code. These are guidelines, not rigid rules. High availability and autoscaling differ: scaling changes instance count, while resilience depends on fault isolation, application behavior, data replication, and traffic distribution. Availability-set, scale-set, and zone capabilities vary by service and region.

For networking, distinguish DNS name resolution, routing, traffic filtering, and connectivity. A DNS record is not a route; a VNet or private endpoint does not grant authorization. Peering is not transitive by default. A private endpoint requires appropriate DNS and service network controls.

> **Verify:** VM sizes, zones, and supported endpoint services change; check current service guidance.

> **Conflict:** The Azure Virtual Desktop overview says the classic service retires on September 30, 2026, but that date has passed as of October 11, 2026 and the page does not confirm the post-retirement state. Verify current lifecycle and migration guidance before relying on classic resources.

### Example or worked scenario

A retailer initially moves a legacy Windows app to VMs because it needs OS control. VMs sit in a VNet with separate application and database subnets and narrowly scoped NSG rules. The modernized public API later moves to App Service or a managed container platform; a file-upload process may use Functions. Branch offices connect through VPN Gateway, while ExpressRoute is evaluated for a private provider connection. Each component is matched to its own needs.

### Hands-on activity

In the portal, inspect a VNet's address space, subnets, peerings, and DNS settings, then inspect a VM's size, NIC, disks, and IP configuration (read-only). Optional CLI: `az network vnet list --output table` and `az vm list-sizes --location <region> --output table` list visible VNets and available VM sizes. For a lab, use a disposable subscription and remove resources when finished.

### Exam or practical application

Match workload clues: guest OS control → VM; managed web app → App Service; containerized app without Kubernetes control requirements → Container Apps; Kubernetes API → AKS; event trigger → Functions. For networking, decide whether the problem is name resolution, VNet connectivity, encrypted hybrid access, private cloud-service access, or public exposure. VM basics include a VM, network interface/VNet, OS disk, and commonly optional data disks and security controls.

### Self-check questions

1. **Which compute option gives you the most control over the guest operating system?**  
   **Answer:** An Azure virtual machine; the customer still has to configure and maintain its guest OS and software.

2. **When might you choose Azure Functions rather than a VM?**  
   **Answer:** For code that responds to events or triggers, such as a scheduled task or file-upload processing, when a serverless execution model fits.

3. **Does peering VNet A to B and B to C automatically provide transitive connectivity from A to C?**  
   **Answer:** No. Peering is not transitive by default; a suitable routing or transit design is needed.

4. **How does a private endpoint differ from a public endpoint?**  
   **Answer:** A private endpoint uses a private IP address in a VNet to connect to a supported service through Private Link. A public endpoint is addressed through a public network endpoint, with access governed by service controls.

5. **Which service is commonly used for a private connectivity-provider circuit between an on-premises network and Microsoft cloud?**  
   **Answer:** ExpressRoute. A VPN Gateway instead establishes encrypted VPN tunnels, commonly over the public internet for hybrid connectivity.

### Sources

- [Choose an Azure compute service](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree)
- [Overview of virtual machines in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/overview)
- [Azure Virtual Machine Scale Sets overview](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview)
- [Availability sets overview](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)
- [What is Azure Virtual Desktop?](https://learn.microsoft.com/en-us/azure/virtual-desktop/overview)
- [Overview of Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/overview)
- [Azure Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview)
- [Azure Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)
- [What is Azure Virtual Network?](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Azure Virtual Network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)
- [Azure DNS overview](https://learn.microsoft.com/en-us/azure/dns/dns-overview)
- [About Azure VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways)
- [Azure ExpressRoute overview](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)
- [What is a private endpoint?](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
- [Azure virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

## Storage and data movement

### Learning intent

Match a data workload to the right Azure Storage service, access tier, redundancy pattern, account type, and data-movement tool. Understand that these are separate choices: the service describes how an application works with the data; the tier expresses access economics for supported blob data; redundancy describes the copies and failure domains; and an account type governs supported services and performance characteristics. For moving data, distinguish network copy utilities, file synchronization, migration planning, and offline bulk transfer.

### Core concepts

**Azure Storage services (`as-storage-services`).** Azure Storage groups several managed storage services behind storage accounts, while VM disks and some specialized services have their own resource models. Select the service based on the data shape and access pattern.

| Service | Data model and common purpose | Typical clue |
| --- | --- | --- |
| Blob Storage | Object storage for unstructured text and binary data; supports data-lake capabilities | Images, backups, logs, documents, analytics data |
| Azure Files | Managed file shares accessible through SMB and, for supported configurations, NFS | Shared folder or application expects a file-system share |
| Queue Storage | Messages that decouple application components or hold asynchronous work | A worker needs to process a backlog independently |
| Table Storage | Schemaless NoSQL key/attribute data | Simple structured entities without a relational database requirement |
| Managed disks | Block storage volumes for Azure VMs | OS or data disk attached to a VM |

Blob Storage stores objects in containers and is not a conventional mounted file share. Azure Files provides shared file-system semantics and can be mounted by clients. Queue Storage is a message store, not a general document database. Table Storage is a NoSQL option, not a relational SQL database. Managed disks are block-level storage used with VMs and are managed by Azure; they are distinct from blobs even though Azure Storage as a platform also offers Blob Storage. Some closely related services (such as Azure Elastic SAN and Azure NetApp Files) serve more specialized storage needs.

**Storage access tiers (`as-storage-tiers`).** Access tiers help tune Blob Storage costs according to access frequency and latency expectations. The Hot tier is for data read or changed frequently; it typically has higher storage cost and lower access cost. Cool is for infrequent access with an online, immediately available retrieval model, and Cold is for rarer access while still online. Archive is an offline tier for rarely accessed data where retrieval latency of hours can be acceptable; data generally must be rehydrated before normal online reads. Moving data between tiers, early deletion, retrieval, and transaction costs can affect total cost, so compare the full workload rather than storage price alone.

| Tier | Access pattern | Online availability | Cost trade-off and planning point |
| --- | --- | --- | --- |
| Hot | Frequent access or active data | Yes | Higher storage cost, lower access costs |
| Cool | Infrequent access | Yes | Lower storage and higher access costs; minimum-retention rules apply |
| Cold | Rare access, but fast retrieval is still required | Yes | Lower storage than cool, higher access costs; minimum-retention rules apply |
| Archive | Very infrequent access and flexible retrieval time | No (offline) | Lowest-cost storage tier among these in many comparisons; rehydration and retention conditions matter |
| Smart tier | Data's hot/cool/cold usage pattern is managed automatically where supported | Tier dependent | Platform-selected movement can simplify optimization; verify availability and costs |

Tier availability and supported blob types depend on account and feature configuration. Archive is not interchangeable with cool/cold: the online tiers are immediately accessible, whereas archived data needs a rehydration step. Access tiers are a Blob Storage data-management choice, not a replacement for choosing an account redundancy option.

> **Verify:** The current Microsoft Learn tier page includes Hot, Cool, Cold, Archive, and Smart tier terminology; availability, supported account types, retrieval behavior, and exam-guide emphasis can change, so check the current page and service region before using newer tier names in a design.

**Storage redundancy (`as-storage-redundancy`).** Azure Storage maintains copies of data for durability and availability, with selectable redundancy options. The key dimensions are whether copies stay within one datacenter or span zones in the primary region, whether data is replicated to a secondary region, and whether reads from that secondary region are available before failover.

| Option | Replication pattern | Main protection | Secondary-region read access? |
| --- | --- | --- | --- |
| LRS (locally redundant storage) | Multiple copies in one physical datacenter in the primary region | Some local hardware failures | No secondary region |
| ZRS (zone-redundant storage) | Synchronous copies across availability zones in the primary region | A failure affecting one zone | No secondary region |
| GRS (geo-redundant storage) | LRS in primary region plus asynchronous replication to a secondary region | Regional disaster, after/with failover behavior | Not by default before failover |
| RA-GRS (read-access geo-redundant storage) | GRS replication plus read access to the secondary region | Regional disaster with secondary reads available | Yes |
| GZRS (geo-zone-redundant storage) | ZRS in primary region plus asynchronous replication to a secondary region | Zone failure in primary and regional disaster | Not by default before failover |
| RA-GZRS | GZRS plus read access to the secondary region | Zone and regional failure with secondary reads | Yes |

LRS is generally the lowest-cost option and protects against local hardware failures but not the loss of the datacenter. ZRS spans zones within the primary region and supports continued service through some zone failures. GRS and GZRS add asynchronous replication to another region; an outage may mean the secondary copy is behind the primary. The `RA-` variants allow read access to the secondary region even when it has not become primary. Exact supported options vary by storage type, region, and account kind.

Redundancy is not backup. If an application or user deletes or overwrites data, those changes can be replicated to other copies. Use suitable backup, versioning, soft-delete, or recovery arrangements for accidental deletion and logical corruption. For regional disaster recovery, plan how to redirect application traffic and verify service-specific failover; replication by itself does not switch every dependent component to the secondary region.

**Storage account types (`as-storage-account-types`).** A storage account provides a namespace and shared configuration for storage resources such as blobs, files, queues, and tables. Standard general-purpose v2 is the recommended account type for many common scenarios because it supports these core services. Premium accounts are specialized for particular performance and storage models, including block blobs, file shares, or page blobs; they do not necessarily support every service available in general-purpose v2. The account type affects the supported redundancy choices and pricing. Choose it from workload needs and validate the feature matrix before deployment.

An account-level redundancy setting applies across storage services in that account. If different data needs different resilience or performance settings, separate accounts may be appropriate. Some storage account properties and types cannot simply be switched in place; migrating data may require creating a new account and copying data.

> **Verify:** Do not rely on remembered account labels or assume that premium, legacy, and general-purpose offerings have identical feature support; consult the current account-type comparison before creating an account.

**File movement tools (`as-file-movement`).** Choose a transfer method based on dataset size, network capacity, direction, and whether the activity is a one-time copy or ongoing synchronization.

| Tool | Best suited to | How to think about it |
| --- | --- | --- |
| AzCopy | Scriptable command-line copy or synchronization to, from, and between supported Azure Storage locations | Useful for controlled transfers and automation over a network |
| Azure Storage Explorer | Graphical browsing and management of supported storage resources | Useful for interactive upload, download, and inspection; it is a client tool, not a migration planning service |
| Azure File Sync | Keeping Windows Server file caches synchronized with a central Azure file share | Hybrid file-server solution; can tier infrequently used data to the cloud |
| Azure Storage Mover | Managed high-scale file migration to Azure Storage | Designed to orchestrate, monitor, and scale transfers for supported scenarios |

AzCopy transfers data; Storage Explorer gives an interactive graphical interface; File Sync keeps file shares coordinated between servers and Azure Files. They solve related but different problems. File Sync is not a general-purpose migration inventory service and does not synchronize arbitrary Blob containers like a file share. Check identity, permissions, network reachability, and supported source and target types before a transfer.

**Migration options (`as-migration-options`).** Azure Migrate helps discover and assess workloads, build a migration plan, and coordinate migration using tools for servers, databases, web apps, and other workloads. It supports migration and modernization pathways; it is not the same product as a file-copy command. Azure Data Box addresses large offline data transfers: Microsoft ships a secure device to the customer, data is copied locally, and the device is returned for upload or export processing. It is helpful when network bandwidth is limited or a dataset is too large for practical online transfer. The specific device models, capacity, availability, and order process change over time.

### How it works, distinctions, limits, and defaults

Choose storage first by data shape, then access pattern, redundancy, and transfer method. Blob is object storage; Files is a shared file system; Queue stores messages; Table stores NoSQL entities; managed disks provide VM block volumes. For supported blobs, tiers balance storage charges against retrieval, transaction, and latency costs. Archive is offline, unlike online Hot, Cool, and Cold.

Redundancy is not backup: replicated deletions or overwrites can affect copies. Zone replication addresses failures within a primary region; geo-replication adds an asynchronous secondary copy, and application failover still needs planning. Account-type, service, tier, and redundancy compatibility varies. Azure Migrate assesses and coordinates workload migration; Data Box transfers bulk data offline; AzCopy copies data; File Sync maintains hybrid file shares.

> **Verify:** Check current tiers, account-type support, regional availability, pricing, and Data Box device lifecycle.

### Example or worked scenario

A media company stores video objects in Blob Storage, shared production folders in Azure Files, processing messages in Queue Storage, and VM disks as managed disks. Hot data moves to cooler online tiers when reads decline; only material that can tolerate offline retrieval is considered for Archive. File Sync keeps office caches connected to an Azure file share. For resilience, the company selects zone or geo-redundancy based on the failure it must survive and separately protects against deletion. Data Box may support an initial bulk import; File Sync or AzCopy serves different follow-on needs.

### Hands-on activity

Inspect a test or authorized storage account in the portal. Record its account type, region, redundancy, and network controls; then inspect the access tier of a test blob. Do not modify production settings. Optional read-only CLI: `az storage account list --output table` and `az storage account show --name <account-name> --resource-group <resource-group> --output json`. Use a test container and approved identity for any transfer.

### Exam or practical application

Select by data model: shared folder → Azure Files; unstructured object → Blob; asynchronous message → Queue; NoSQL key/attribute data → Table; VM volume → managed disk. Frequent blob access suggests Hot; immediate but infrequent access suggests Cool or Cold; offline flexible-latency data may suit Archive. LRS stays in one datacenter, ZRS spans zones, GRS/GZRS add a secondary region, and RA variants add secondary read access. Distinguish replication from backup.

### Self-check questions

1. **Which service fits an application that needs a shared file share mounted by multiple clients?**  
   **Answer:** Azure Files, using a supported protocol such as SMB or NFS for the scenario.

2. **Is Archive an online Blob access tier for immediate retrieval?**  
   **Answer:** No. Archive is offline; data must be rehydrated before normal online access.

3. **What is the key difference between ZRS and GZRS?**  
   **Answer:** ZRS copies data across availability zones in the primary region. GZRS combines zone redundancy in the primary region with asynchronous replication to a secondary region.

4. **Which option adds read access to a geo-replicated secondary region?**  
   **Answer:** The read-access variants, RA-GRS or RA-GZRS.

5. **A company needs continuous synchronization between Windows file servers and a central Azure file share. Which tool is designed for this?**  
   **Answer:** Azure File Sync.

6. **Which product helps plan and assess workload migration, and which option physically ships bulk data?**  
   **Answer:** Azure Migrate helps assess and plan workload migration; Azure Data Box uses a shipped device for offline bulk transfer.

### Sources

- [Introduction to Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)
- [Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)
- [Data redundancy in Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
- [Access tiers for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)
- [What is Azure Files?](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction)
- [Introduction to Azure Queue Storage](https://learn.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction)
- [Introduction to Table storage](https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-overview)
- [Overview of Azure Disk Storage](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)
- [Copy or move data by using AzCopy v10](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)
- [What is Azure File Sync?](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction)
- [About Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview)
- [Microsoft Azure Data Box overview](https://learn.microsoft.com/en-us/azure/databox/data-box-overview)
- [Introduction to Azure Storage Mover](https://learn.microsoft.com/en-us/azure/storage-mover/service-overview)
- [Get started with Storage Explorer](https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer)

## Identity, access, and security

### Learning intent

Explain how Microsoft Entra ID and Microsoft Entra Domain Services support different identity needs; distinguish authentication from authorization; recognize single sign-on (SSO), multifactor authentication (MFA), and passwordless methods; and describe external identities, Conditional Access, Azure RBAC, Zero Trust, defense in depth, and Microsoft Defender for Cloud. The key is to layer controls: verify identities, grant only the necessary permissions, evaluate context, protect workloads and data, and monitor for risk.

### Core concepts

**Directory services (`as-directory-services`).** Microsoft Entra ID is Microsoft's cloud identity and access management service for users, groups, applications, devices, and resources. An organization uses a Microsoft Entra tenant (directory) to manage identity objects and access policies. Azure subscriptions use a directory as their identity context, while Azure RBAC controls authorization to Azure resource scopes. Microsoft Entra ID is not simply a cloud-hosted Windows domain controller; modern cloud sign-in and access management are its primary role.

Microsoft Entra Domain Services is a managed domain service for applications that still need traditional Active Directory Domain Services (AD DS) protocols and features such as domain join, Group Policy, LDAP, and Kerberos/NTLM. It reduces the need to deploy and maintain domain controllers for supported legacy workloads. It integrates with Microsoft Entra ID, which acts as the source of authority for identities, but it is not a replacement for every AD DS deployment or for Microsoft Entra ID's modern cloud identity functions.

| Service | Main purpose | Typical fit |
| --- | --- | --- |
| Microsoft Entra ID | Cloud identity, sign-in, authentication, and access-policy foundation | Users and apps accessing cloud and integrated services |
| Microsoft Entra Domain Services | Managed domain protocols and legacy AD-compatible capabilities | Cloud workloads dependent on LDAP, Kerberos/NTLM, domain join, or Group Policy |

**Authentication methods (`as-authentication-methods`).** Authentication answers “Who are you?”; authorization answers “What are you allowed to do?” Microsoft Entra ID supports passwords, authenticator-based sign-in, passkeys, certificate-based methods, and other methods, subject to configuration and service capability. The exact authentication method available for first factor, MFA, self-service password reset, or recovery varies; consult the current method matrix rather than assuming every method can be used for every purpose.

*Single sign-on (SSO)* allows a user to authenticate once and then access multiple applications without re-entering credentials for each app, subject to the applications' sign-in sessions and policies. SSO improves user experience and can reduce password prompts, but it does not remove the need to secure the sign-in session or control authorization to each resource.

*MFA* requires more than one verification factor in a sign-in. Factors are commonly described as something you know, have, or are. A password plus a second proof can make stolen passwords less sufficient on their own; however, not all MFA methods offer the same phishing resistance. Passwordless authentication lets a user sign in without a conventional password, using supported methods such as passkeys or authenticator mechanisms. A passwordless method can also satisfy strong authentication requirements depending on configuration. Avoid equating “passwordless” with “no authentication” or treating every method as equally resistant to phishing.

| Method or concept | What it means | Why it matters |
| --- | --- | --- |
| SSO | One authenticated session can be used across integrated apps | Reduces repeated sign-in prompts; app access still follows policy |
| MFA | More than one proof is required | Reduces reliance on a password alone |
| Passwordless | Sign-in without entering a conventional password | Can improve usability and reduce password-related risk; method security varies |

**External identities (`as-external-identities`).** Microsoft Entra External ID supports secure access for people outside an organization. For business-to-business (B2B) collaboration, a partner or guest can use an external identity to collaborate in the organization's workforce tenant, with access limited to what is granted. For customer identity and access management (CIAM), an organization can use an external-tenant configuration to manage consumer or business-customer sign-up and sign-in experiences separately from its workforce directory. The distinction is audience and tenant purpose: workforce collaboration with invited partners is not the same scenario as customer sign-in to a public-facing application.

External users should receive only the permissions needed for the collaboration or application. Invitation, federation, self-service registration, authentication method, terms, and lifecycle settings depend on the configuration. A guest identity is not automatically an administrator or a trusted user for all resources.

**Conditional Access (`as-conditional-access`).** Microsoft Entra Conditional Access is a policy engine that evaluates signals and applies access controls after first-factor authentication. Policies can consider the user or group, application, device, location, and risk signals, then require an action such as MFA, require a compliant device, or block access. It is often expressed as an “if this context, then that control” rule. For example, require MFA when an employee accesses a sensitive application from an unfamiliar context.

Conditional Access is not a replacement for authentication or a firewall, and it is not intended as the first-line defense against every type of attack. Policies need to be tested carefully to avoid unintended lockouts, and exclusions should be narrow and monitored. Licensing and feature availability affect which signals and controls are available.

**Azure role-based access control (`as-rbac`).** Azure RBAC is Azure Resource Manager's authorization system for managing access to Azure resources. A role assignment combines three parts: a *security principal* (user, group, service principal, or managed identity), a *role definition* (the allowed actions), and a *scope* (where those permissions apply). Azure built-in roles include broad roles such as Owner and narrower roles such as Reader or service-specific contributor roles; custom roles can be created when built-ins do not meet a need.

Common scopes are management group, subscription, resource group, and individual resource. A role assignment at a parent scope can be inherited by descendant resources. Use the narrowest practical scope and least-privilege role. Azure RBAC is not the same as Microsoft Entra directory roles: RBAC governs Azure resource access; directory roles administer identity and tenant functions. A user can authenticate successfully yet lack permission to create or modify an Azure resource.

**Zero Trust (`as-zero-trust`).** Zero Trust is a security model built around “never trust, always verify.” It assumes that location on an internal network does not automatically make a request safe. The three common principles are:

- **Verify explicitly:** authenticate and authorize access using available identity, device, location, and risk context.
- **Use least privilege:** grant only the minimum access needed and only for as long as needed.
- **Assume breach:** design controls to detect compromise, limit movement and impact, and support response.

Zero Trust is not one product or a single network appliance. It is a way to combine identity, devices, network, applications, data, infrastructure, and monitoring controls. It encourages continuous evaluation as conditions change.

**Defense in depth (`as-defense-in-depth`).** Defense in depth uses multiple layers of security controls so that failure of one control does not immediately expose the entire system. A simplified Azure-oriented view includes physical security operated by the cloud provider, identity and access controls, perimeter and network protections, compute and application hardening, data protection, and detection/response. The cloud provider and customer share responsibilities; the exact division depends on the service model. For example, Azure operates datacenter facilities, while the customer configures resource access, workload settings, and data permissions.

The layers should be complementary, not redundant checkboxes. MFA protects sign-in; RBAC limits actions; NSGs and private endpoints constrain network exposure; encryption protects data in transit or at rest; backup supports recovery; monitoring and Defender for Cloud can help identify risk. No single layer guarantees that a workload cannot be compromised.

**Microsoft Defender for Cloud (`as-defender-for-cloud`).** Defender for Cloud is a cloud security platform for assessing and improving security posture and protecting workloads across Azure and supported hybrid or multicloud environments. Its capabilities include cloud security posture management (CSPM), workload protection (CWPP), and security support across development workflows. It surfaces recommendations, security findings, and threat-protection capabilities depending on environment, plan, and configuration. It helps teams identify risks and improve protections; it does not automatically remediate every finding or replace the team's secure design and operations.

### How it works, distinctions, limits, and defaults

Treat identity, policy, authorization, network controls, and monitoring as distinct layers. Authentication proves identity; Conditional Access evaluates context and can require MFA or block; Azure RBAC authorizes actions on Azure resources. A user may sign in successfully yet lack permission to change a resource. Use the least-privileged principal, role, and scope. Parent-scope assignments can be inherited by descendants.

Conditional Access policies need careful testing to avoid lockouts; licensing and configuration affect signals and controls. Entra ID supports modern cloud identity, while Domain Services serves compatible legacy AD protocol needs. Defender for Cloud recommendations depend on onboarding and enabled plans and do not automatically fix every issue.

> **Verify:** Microsoft Entra naming, Defender portal experiences, plans, licensing, available authentication methods, and preview states change; consult current Learn guidance.

### Example or worked scenario

A company gives supplier guests access to one project through Entra External ID B2B collaboration. It assigns a group a narrow Azure RBAC role at the project resource group and uses Conditional Access to require MFA for the application. An app uses a managed identity rather than a stored password to access a storage service. A private endpoint limits the network path, and Defender for Cloud helps surface posture recommendations. Backup and recovery remain separately planned.

### Hands-on activity

In an authorized test tenant, inspect Entra **Users**, **Groups**, **Authentication methods**, and **External identities**. In the Azure portal, review a resource group's **Access control (IAM)** assignments and identify principal, role, and scope without changing them. Inspect Conditional Access policies in report-only mode where available, then review Defender for Cloud recommendations. Do not invite users, assign roles, or enable production policies as practice.

### Exam or practical application

Separate authentication from authorization: SSO shares sign-in across integrated apps; MFA uses multiple proofs; passwordless omits a conventional password; RBAC governs Azure resource actions. Use Domain Services for supported legacy AD protocols, External ID for partners or customers, and Conditional Access for context-based controls. Zero Trust means verify explicitly, use least privilege, and assume breach. Defender for Cloud helps improve posture and protect supported workloads; it is not a directory, firewall, or automatic fix for all risks.

### Self-check questions

1. **What are the three components of an Azure RBAC role assignment?**  
   **Answer:** Security principal, role definition, and scope.

2. **An application needs LDAP and Kerberos but cannot be modernized. Which service may provide managed domain capabilities?**  
   **Answer:** Microsoft Entra Domain Services, subject to workload compatibility and service requirements.

3. **Does MFA decide whether a signed-in user may delete a resource group?**  
   **Answer:** No. MFA is an authentication control. Azure RBAC determines whether the principal is authorized for that Azure operation at the applicable scope.

4. **What are the three Zero Trust principles?**  
   **Answer:** Verify explicitly, use least privilege, and assume breach.

5. **What is Conditional Access for?**  
   **Answer:** Evaluating sign-in context and applying controls such as requiring MFA or blocking access according to policy.

6. **What is Microsoft Defender for Cloud's general purpose?**  
   **Answer:** Help assess and improve cloud security posture and protect supported workloads across Azure and supported hybrid or multicloud environments.

### Sources

- [What is Microsoft Entra?](https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra)
- [Overview of Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview)
- [Microsoft Entra authentication overview](https://learn.microsoft.com/en-us/entra/identity/authentication/overview-authentication)
- [What is single sign-on in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on)
- [Microsoft Entra External ID overview](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview)
- [Microsoft Entra Conditional Access overview](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)
- [What is Azure role-based access control (Azure RBAC)?](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
- [Zero Trust as a security foundation](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview)
- [Introduction to Azure security](https://learn.microsoft.com/en-us/azure/security/fundamentals/overview)
- [Microsoft Defender for Cloud overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
- [Azure Virtual Network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [What is a private endpoint?](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
