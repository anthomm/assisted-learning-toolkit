# Compute (20–25%)

Compute administration ranges from declarative resource deployment to maintaining individual virtual machines and managed application platforms. The operational choice is a balance among control, responsibility, scaling model, and service limits.

## Resource deployment with ARM and Bicep

### Learning intent

Read, modify, and deploy Azure Resource Manager (ARM) templates and Bicep files; understand parameters, dependencies, outputs, and how to export or convert deployments.

### Core concepts

**Azure Resource Manager (ARM)** is the management plane for deploying and managing Azure resources. An ARM JSON template declares the target resource types, API versions, properties, parameters, variables, dependencies, and outputs. **Bicep** is a declarative language that compiles to ARM JSON and offers a more concise syntax while retaining ARM deployment behavior.

Templates make deployments repeatable. Parameters vary values between environments; variables hold reusable expressions; outputs expose selected deployment results. Dependencies express ordering when ARM cannot infer it from resource references. A deployment's target scope matters: templates can deploy at resource-group, subscription, management-group, or tenant scope when supported by the deployment type and permissions.

An exported template can help document or reproduce an existing deployment, but it may omit operational intent, secrets, or configuration not represented by the export. Converting an ARM template to Bicep is supported by tooling, but generated output should be reviewed and tested. Use source control and parameter files carefully; never commit secrets.

### How it works, distinctions, limits, and defaults

Declarative deployment describes the desired resource state, not an imperative sequence for every action. A template deployment does not guarantee that all application-level setup is complete or that the resulting service is secure. Resource providers, API versions, permissions, quotas, and region availability affect success.

Review changes before deployment, especially replacements, destructive property changes, role assignments, and network exposure. Use incremental deployments where appropriate and understand the selected deployment mode and scope. Keep secrets in a managed secret store or secure deployment mechanism rather than template literals.

### Example or worked scenario

A team needs identical test and production network foundations. It creates a Bicep template for a virtual network and subnets, parameterizes address ranges and environment tags, and uses separate parameter values for each environment. A deployment preview and code review catch an unintended subnet change before it reaches production.

### Hands-on activity

In a test subscription, use the Azure portal or Azure CLI to validate and deploy a small Bicep template containing a resource group-scoped resource. Inspect deployment operations and outputs, then remove the test resource. Export a deployment and compare it with the original source; note any missing intent.

### Exam or practical application

When interpreting a template, identify its scope, parameters, resource type/API version, dependencies, and outputs. When asked to modify it, change the declarative property or parameter that represents the requirement, then validate the deployment and its permissions.

### Self-check questions

1. What is the relationship between Bicep and ARM templates?

   **Answer:** Bicep is a declarative language that compiles to ARM JSON templates and uses ARM for deployment.

2. Why might a resource need an explicit dependency?

   **Answer:** To ensure deployment ordering when a dependency is not already implied by a resource reference.

3. Is an exported template always a complete and safe source of truth for redeployment?

   **Answer:** No. It may omit intent or configuration, can require review, and should not be assumed to include secrets or all operational details.

### Sources

- [Azure Resource Manager templates overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)
- [Bicep overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)
- [ARM template structure and syntax](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax)
- [Deploy resources with Bicep and Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-cli)
- [Export template in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal)
- [Decompile an ARM template to Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile)

## Virtual machines and scale sets

### Learning intent

Create and configure virtual machines (VMs), select sizes and disks, protect host data, move VMs between supported scopes, and plan availability with zones, availability sets, and scale sets.

### Core concepts

An Azure VM is a compute resource with dependencies such as a virtual network interface, operating-system disk, optional data disks, and public or private IP configuration. Select an image, size, OS, authentication method, region, and availability design based on workload requirements. A VM **size** determines available CPU, memory, storage, and network characteristics; available sizes vary by region and quota. A managed disk abstracts the underlying storage account and offers selectable performance and redundancy characteristics.

**Encryption at host** encrypts VM-host caches and temporary disks in addition to managed disks where supported. It is a host-level protection option, not a replacement for disk encryption, key management, or access controls. Review supported VM sizes, regions, and dependencies before enabling it.

**Availability zones** place resources in separate physical locations within a supported region. **Availability sets** distribute VMs across fault and update domains within a datacenter. They are different placement approaches; neither makes an application highly available if its dependencies remain a single point of failure. **Virtual Machine Scale Sets (VMSS)** manage a group of VMs with coordinated deployment and scaling capabilities. Flexible and uniform orchestration modes have different behaviors; check the current design guidance.

Moving a VM across resource groups, subscriptions, or regions is subject to resource-specific move support and dependency constraints. A region move is often a redeployment or replication workflow rather than a simple metadata change. Check the move matrix and plan downtime, IP/DNS changes, quotas, and dependent resources.

### How it works, distinctions, limits, and defaults

Disk performance and VM network throughput can be constrained by both the VM size and the disk tier. Changing a VM size can require deallocation and is limited by regional capacity. A VM's availability model must match application architecture: stateless replicas may scale horizontally, while stateful workloads need data replication and recovery planning.

Availability sets distribute placement within one datacenter; zones distribute across zone locations in a region. A scale set can support scale-out but does not automatically make an application resilient. Backup, patching, identity, and network security remain operational responsibilities.

### Example or worked scenario

A line-of-business service requires OS-level control and must tolerate planned maintenance. The team selects a VM size after measuring memory and network needs, places redundant instances across zones where the region and application allow it, and stores state in a separately resilient service. It checks quotas and capacity, configures backup, and tests application failover instead of assuming VM placement alone provides availability.

### Hands-on activity

In a sandbox, review VM sizes and disk SKUs without deploying. If authorized, deploy a small test VM with a managed identity and no unnecessary public endpoint; inspect its disk and availability configuration. Use a move validation operation before any cross-scope move, and delete the VM and disks after testing.

### Exam or practical application

Start with the requirement: capacity points to size, persistent storage to managed disks, physical-location failure to zones, planned maintenance within a datacenter to availability sets, and group lifecycle or autoscaling to VMSS. Verify that the region, SKU, quota, and dependencies support the requested design.

### Self-check questions

1. How do availability zones differ from availability sets?

   **Answer:** Zones are separate physical locations in a region; availability sets distribute VMs across fault and update domains within a datacenter.

2. Does a larger VM size guarantee better performance for every workload?

   **Answer:** No. The selected size must fit the workload, and storage, network, application, quota, and regional capacity can also constrain performance.

3. Is moving a VM to another region always a direct resource move?

   **Answer:** No. Regional moves often require a supported migration or redeployment approach and planning for dependencies and downtime.

### Sources

- [Sizes for virtual machines in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)
- [Managed disks overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)
- [Encryption at host](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption)
- [Availability options for virtual machines in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/availability)
- [Availability sets overview](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)
- [Availability zones overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)
- [Virtual Machine Scale Sets overview](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview)
- [Move operation support for resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-support-resources)
- [Move Azure VMs to another region](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-migrate)

## Azure container services

### Learning intent

Create and manage an Azure Container Registry (ACR), choose between Azure Container Instances (ACI) and Azure Container Apps for container workloads, and configure sizing and scaling appropriate to each.

### Core concepts

A **container image** packages an application and its dependencies. **Azure Container Registry** stores and distributes images. Configure registry access through appropriate identities and role assignments, use private networking where needed, and protect image supply chains with controlled builds and updates. An image registry stores artifacts; it does not run the container.

**Azure Container Instances** runs container groups without requiring VM or orchestrator administration. It fits simple, short-lived, or isolated container workloads. **Azure Container Apps** is a managed application platform for containerized services, with features for revisions, ingress, and event-driven scaling. Neither should be confused with managing a full Kubernetes cluster; choose a more orchestration-focused platform only when its capabilities are actually needed.

Container sizing concerns CPU and memory requests/limits and the workload's scale model. ACI container groups have resource and lifecycle characteristics that differ from Container Apps. Container Apps can scale based on supported triggers and configuration, but scale-to-zero behavior, replicas, concurrency, and minimum/maximum replicas depend on the app and rule settings.

### How it works, distinctions, limits, and defaults

Registry authentication, image pull permissions, ingress, secrets, and egress must all be configured intentionally. A container image can include vulnerabilities or secrets; scanning and controlled build pipelines are part of administration. Scaling compute does not necessarily scale a backing database or external dependency.

ACI is not a general-purpose orchestration layer; Container Apps supplies more application-level management. Service quotas, supported regions, networking features, and billing dimensions change, so check current service limits before sizing a production workload.

### Example or worked scenario

A scheduled conversion job runs for a few minutes and exits; ACI may suit its simple lifecycle. A customer-facing API needs revisions, ingress, and event-driven horizontal scaling; Container Apps may better match. Both pull images from a controlled registry, use managed identity where supported, and receive only required network access.

### Hands-on activity

Inspect an existing ACR's repositories, access configuration, and image tags. In a sandbox, deploy a simple non-sensitive test image to ACI or Container Apps, review logs, ingress, resource sizing, and scaling configuration, then delete the workload and any unused image.

### Exam or practical application

First identify the registry requirement separately from runtime. Then compare the requested lifecycle and operational features: simple container execution suggests ACI; managed app revisions and configurable scale/ingress suggest Container Apps. Always include the image pull identity and network path.

### Self-check questions

1. Does ACR execute a container image?

   **Answer:** No. It stores and distributes images; a runtime such as ACI or Container Apps executes them.

2. Which service is more aligned with a simple isolated container group: ACI or Azure Container Apps?

   **Answer:** ACI.

3. If a Container App scales out, is its database guaranteed to scale with it?

   **Answer:** No. The database is a separate dependency with its own limits and scaling configuration.

### Sources

- [Azure Container Registry overview](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro)
- [Azure Container Instances overview](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-overview)
- [Azure Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview)
- [Set scaling rules in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)
- [Azure Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions)

## Azure App Service

### Learning intent

Provision an App Service plan and web app; configure scaling, certificates and TLS, custom domains, backups, networking, and deployment slots.

### Core concepts

**Azure App Service** hosts web applications and APIs on a managed platform. An **App Service plan** defines the compute resources, operating system, region, pricing tier, and scale capacity for one or more apps. Apps in the same plan share the plan's compute resources; scaling the plan affects its apps. Choose a tier based on required features, capacity, availability, and cost.

**Scale up** changes the plan's pricing tier or instance size; **scale out** changes the number of instances. Autoscale options and supported behavior depend on the plan tier and configuration. A custom domain requires domain ownership verification and appropriate DNS records. Configure TLS binding and certificates for HTTPS; certificate availability and renewal method depend on the chosen certificate and domain.

**Deployment slots** provide separate live app environments, commonly used to validate a release before swapping into production. Slot settings and app configuration must be reviewed because selected settings can remain bound to a slot while others move during a swap. **App Service backups** are configured with supported storage and schedule/retention options depending on plan and app configuration. Backups should be tested, monitored, and protected from unauthorized access.

Networking features include inbound access restrictions, virtual network integration for supported outbound connectivity, and private endpoints for private inbound access. These features have different directions and DNS requirements: an outbound integration path is not the same as a private endpoint to the app.

### How it works, distinctions, limits, and defaults

The plan is the compute boundary; the app is the workload configuration boundary. Apps sharing a plan can contend for resources and share cost. Scaling an app's plan may affect other apps on it. TLS protects transport only when the hostname, certificate, and binding are correct. DNS changes can take time to propagate.

Slots reduce deployment risk but do not replace application testing, database migration strategy, or rollback planning. Backup availability and content can depend on plan tier, app type, linked storage, and current platform behavior; verify requirements before relying on it.

### Example or worked scenario

A team operates an API with a custom hostname. It provisions a plan sized for expected traffic, binds a verified domain and TLS certificate, and uses a staging slot to validate releases. Inbound restrictions limit access, while VNet integration provides a path to a private backend. Before swapping, the team confirms slot-specific settings and verifies that backup recovery covers the app's configuration and content needs.

### Hands-on activity

In a test subscription, compare App Service plan tiers and inspect scale settings. Deploy a sample app, create a staging slot if supported, and review domain, TLS, networking, and backup blades without exposing a production app. Delete the plan and test resources afterward.

### Exam or practical application

Separate plan-level requirements (compute, tier, scale) from app-level settings (domain, TLS, deployment slot, backup, access). For private connectivity, identify whether the requirement is inbound to the app or outbound from the app to a backend.

### Self-check questions

1. What happens when several apps use the same App Service plan?

   **Answer:** They share the plan's compute resources; scaling the plan affects the apps hosted on it.

2. Is VNet integration primarily an inbound private endpoint to the app?

   **Answer:** No. It provides supported outbound connectivity from the app into a virtual network; a private endpoint addresses private inbound access.

3. What should be checked before swapping a staging slot into production?

   **Answer:** Validate the application and review slot-specific settings, dependencies, and any state or database changes that are not safely reversed by a slot swap.

### Sources

- [App Service overview](https://learn.microsoft.com/en-us/azure/app-service/overview)
- [App Service plans](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans)
- [Scale up an app in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up)
- [Scale instance count manually or automatically](https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up)
- [Configure a custom domain name](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)
- [Secure a custom DNS name with a TLS/SSL binding](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)
- [Back up an app in Azure](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)
- [App Service networking features](https://learn.microsoft.com/en-us/azure/app-service/networking-features)
- [Set up staging environments in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)
