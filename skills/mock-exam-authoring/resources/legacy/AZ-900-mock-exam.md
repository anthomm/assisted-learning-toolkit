# AZ-900 Mock Exam: Microsoft Azure Fundamentals (50 questions)

Based on the skills measured as of July 20, 2026.

| Domain | Weight | Questions |
|---|---|---|
| Describe cloud concepts | 25–30% | 20 (26.7%): Q1–Q14, Q51–Q56 |
| Describe Azure architecture and services | 35–40% | 30 (40%): Q15–Q33, Q57–Q67 |
| Describe Azure management and governance | 30–35% | 25 (33.3%): Q34–Q50, Q68–Q75 |

Total: 75 questions. Q1–Q50 are the original set, and Q51–Q75 (Part 2) fill the remaining topics.

Each question has 4 options, and exactly one is correct. Try them all first, then check the answer key and explanations at the end of each section.

---

# Domain 1: Describe cloud concepts (Q1–Q14)

## Describe cloud computing (Q1–Q6)

**Q1.** Which statement best defines cloud computing?
- A) Buying and owning physical servers in your own datacenter
- B) Delivering computing services over the internet on demand, with pay-as-you-go pricing
- C) A private network that connects branch offices
- D) Installing software on a single local workstation

**Q2.** In the shared responsibility model, which item is ALWAYS the customer's responsibility regardless of service type (IaaS, PaaS, SaaS)?
- A) Physical datacenter security
- B) Physical network hardware
- C) Information and data, and the accounts, identities, and devices they use
- D) The host hypervisor

**Q3.** A company must keep sensitive data on hardware it fully controls on-premises, but wants to burst to Azure for peak workloads. Which cloud model fits?
- A) Public cloud
- B) Private cloud only
- C) Hybrid cloud
- D) Community cloud

**Q4.** Which scenario is the best use case for a PUBLIC cloud?
- A) A startup needs to launch quickly with no upfront hardware investment
- B) An organization must own and operate all hardware in its own facility
- C) A regulation prohibits any use of third-party infrastructure
- D) An air-gapped system with no internet connectivity

**Q5.** Which statement describes the consumption-based pricing model?
- A) You pay a fixed annual fee regardless of usage
- B) You buy hardware upfront and depreciate it over several years
- C) You pay only for the resources you use, with no upfront commitment
- D) You must reserve capacity for three years

**Q6.** Which statement about serverless computing is correct?
- A) You must provision and patch the virtual machines that run your code
- B) The cloud provider manages the infrastructure, and you are billed based on execution and consumption
- C) It means no servers exist anywhere in the architecture
- D) It is only available in a private cloud

### Answers and explanations: Cloud computing

**Q1 – B.** Cloud computing delivers compute, storage, databases, networking, and more over the internet on demand with pay-as-you-go pricing.
- A: that is traditional on-premises IT.
- C: that describes a WAN or VPN, not cloud computing.
- D: that is local software, not cloud.

**Q2 – C.** The customer always owns their data, the accounts and identities that access it, and the endpoint devices, in every service type.
- A: physical security is always the provider's.
- B: physical network hardware is the provider's.
- D: the hypervisor on the host is managed by the provider.

**Q3 – C.** Hybrid cloud combines on-premises or private infrastructure with public cloud, so sensitive data stays local while Azure absorbs peaks.
- A: public alone doesn't keep data on your own hardware.
- B: private only doesn't give you burst capacity from Azure.
- D: "Community cloud" is not one of the exam's cloud models (public, private, hybrid).

**Q4 – A.** Public cloud suits fast launches with no capital outlay and elastic scaling.
- B, C, D: each describes a need for full ownership, no third-party use, or isolation, which points to private or on-premises.

**Q5 – C.** Consumption-based pricing means you pay for what you use, with no upfront cost and no long-term commitment.
- A: a fixed fee is not consumption-based.
- B: this is CapEx on-premises purchasing.
- D: reserved capacity is a separate pricing option (reservations), not consumption-based.

**Q6 – B.** In serverless (such as Azure Functions), the provider manages the infrastructure and you pay for execution or consumption.
- A: that is IaaS.
- C: servers still exist, you just don't manage them.
- D: serverless is a public cloud capability.

## Describe the benefits of using cloud services (Q7–Q10)

**Q7.** Which feature allows an app to automatically add or remove resources as demand changes, improving both cost efficiency and performance?
- A) Geo-redundancy
- B) Elasticity (scalability)
- C) Data sovereignty
- D) Role-based access control

**Q8.** An organization wants its service to stay available even if a datacenter fails, and wants a contractual uptime guarantee. Which cloud benefit is this?
- A) High availability
- B) Cost predictability
- C) Manageability
- D) Governance

**Q9.** Which cloud benefit is delivered by using the pricing calculator and cost analysis to forecast spending accurately?
- A) Predictability
- B) Fault isolation
- C) Elasticity
- D) Passwordless sign-in

**Q10.** Which is an example of "manageability" in the cloud?
- A) Using a REST API, ARM template, or portal to manage resources and automate deployments at scale
- B) Replacing physical disks in a datacenter
- C) Negotiating a hardware support contract
- D) Hand-configuring each server through its local console

### Answers and explanations: Benefits

**Q7 – B.** Elasticity (a form of scalability) adds or removes resources automatically in line with demand.
- A: geo-redundancy copies data to another region and doesn't scale compute.
- C: data sovereignty is about where data lives legally.
- D: RBAC controls access, not capacity.

**Q8 – A.** High availability keeps services running through failures and is backed by SLAs.
- B: predictability is about forecasting cost and performance.
- C: manageability is about operating resources.
- D: governance is about policy and compliance.

**Q9 – A.** Predictability covers both cost (forecasting and monitoring spend) and performance.
- B: fault isolation is not the benefit being described.
- C: elasticity is about scaling.
- D: passwordless sign-in is an authentication method.

**Q10 – A.** Manageability in the cloud means managing and automating through the portal, CLI, APIs, templates, and monitoring.
- B, C, D: these are manual, on-premises-style tasks.

## Describe cloud service types (Q11–Q14)

**Q11.** Which service type gives you the most control over the operating system and runtime?
- A) SaaS
- B) PaaS
- C) IaaS
- D) Serverless

**Q12.** A developer wants to deploy a web application without managing the OS or web server patching. Which service type fits?
- A) IaaS
- B) PaaS
- C) On-premises
- D) Colocation

**Q13.** Microsoft 365 (for example, Exchange Online) is an example of which service type?
- A) IaaS
- B) PaaS
- C) SaaS
- D) Private cloud

**Q14.** A company needs to lift and shift a legacy application that requires a custom operating system configuration. Which service type is the best fit?
- A) SaaS
- B) PaaS
- C) Serverless functions
- D) IaaS

### Answers and explanations: Service types

**Q11 – C.** With IaaS you manage the OS, middleware, and apps. The provider manages only the underlying infrastructure.
- A: SaaS gives you the least control.
- B: PaaS has the provider manage the OS and runtime.
- D: serverless abstracts the infrastructure even further.

**Q12 – B.** PaaS (such as Azure App Service) lets you deploy code while Azure handles the OS and patching.
- A: IaaS requires you to patch the OS.
- C and D: you would manage hardware yourself.

**Q13 – C.** Microsoft 365 is SaaS, a complete application delivered over the internet.
- A and B: you don't manage infrastructure or a platform for it.
- D: private cloud is a deployment model, not a service type.

**Q14 – D.** IaaS (Azure VMs) gives full OS control, which is ideal for lift-and-shift with custom configuration.
- A: SaaS is a finished product.
- B and C: both restrict OS-level customization.

---

# Domain 2: Describe Azure architecture and services (Q15–Q33)

## Core architectural components (Q15–Q19)

**Q15.** What is a region pair in Azure?
- A) Two datacenters in the same building
- B) Two Azure regions within the same geography, paired for disaster recovery and platform updates
- C) Two subscriptions linked by billing
- D) Two availability zones in a single region

**Q16.** Which statement about availability zones is correct?
- A) They are physically separate locations within an Azure region, each with independent power, cooling, and networking
- B) They are separate Azure geographies
- C) They only exist for sovereign regions
- D) They are logical groupings of resource groups

**Q17.** Which Azure option is designed to meet specific compliance and legal requirements for government customers, with physical and logical isolation from the public Azure regions?
- A) Region pairs
- B) Sovereign regions such as Azure Government
- C) Availability sets
- D) Management groups

**Q18.** What is the correct hierarchy in Azure, from the highest level to the lowest?
- A) Subscription → Management group → Resource group → Resource
- B) Resource group → Subscription → Management group → Resource
- C) Management group → Subscription → Resource group → Resource
- D) Management group → Resource group → Subscription → Resource

**Q19.** Which statement about resource groups is correct?
- A) A resource can belong to multiple resource groups at once
- B) Resource groups are logical containers for resources, and each resource belongs to exactly one resource group
- C) Deleting a resource group leaves its resources intact
- D) Resource groups can contain other resource groups

### Answers and explanations: Core architecture

**Q15 – B.** Each Azure region is paired with another in the same geography, and platform updates are rolled out sequentially across the pair.
- A: that describes a datacenter.
- C: that is unrelated to billing.
- D: zones exist inside a single region.

**Q16 – A.** Availability zones are physically separate datacenter locations in a region with independent power, cooling, and networking.
- B: geographies are much larger.
- C: zones are not limited to sovereign regions.
- D: they are physical, not logical groupings.

**Q17 – B.** Sovereign regions (Azure Government, Azure operated by 21Vianet in China) are isolated instances for compliance and legal needs.
- A: pairs are for resiliency.
- C: availability sets are a VM-level feature.
- D: management groups organize subscriptions.

**Q18 – C.** The hierarchy is management group, then subscription, then resource group, then resource.
- A, B, D: each has the order wrong.

**Q19 – B.** A resource belongs to exactly one resource group, which is a logical container.
- A: a resource can't be in two groups.
- C: deleting a group deletes everything in it.
- D: resource groups can't be nested.

## Azure compute and networking (Q20–Q25)

**Q20.** You need to run a short, event-driven piece of code, such as responding to a queue message, without managing servers. Which service fits best?
- A) Azure Virtual Machines
- B) Azure Functions
- C) Azure Virtual Desktop
- D) Azure VPN Gateway

**Q21.** Which Azure feature automatically increases or decreases the number of identical VM instances based on demand?
- A) Availability set
- B) Azure Virtual Machine Scale Sets
- C) Azure DNS
- D) Azure Storage Explorer

**Q22.** Which Azure service provides a cloud-hosted Windows desktop and apps that users can access remotely, and which hosting option runs a web app without managing the OS?
- A) Azure Virtual Desktop for remote desktops, and Azure App Service for web apps
- B) Azure App Service for remote desktops, and Azure Virtual Desktop for web apps
- C) Azure Container Instances for remote desktops, and Azure Arc for web apps
- D) Azure Arc for remote desktops, and Azure VPN Gateway for web apps

**Q23.** What does an availability set protect against?
- A) Region-wide outages
- B) Hardware failures and planned maintenance within a datacenter by spreading VMs across fault domains and update domains
- C) Accidental deletion of a VM
- D) Subscription billing errors

**Q24.** Which Azure service gives you a private, dedicated connection from on-premises to Azure that does NOT travel over the public internet?
- A) Azure VPN Gateway
- B) Azure DNS
- C) Azure ExpressRoute
- D) Virtual network peering

**Q25.** What is the purpose of a private endpoint?
- A) It assigns a public IP address to a PaaS service
- B) It gives an Azure PaaS service a private IP address from your virtual network, so traffic stays on the Microsoft backbone
- C) It encrypts the storage account at rest
- D) It lets you resolve domain names publicly

### Answers and explanations: Compute and networking

**Q20 – B.** Azure Functions is serverless and event-driven, so you pay per execution.
- A: VMs need management.
- C: AVD provides remote desktops.
- D: VPN Gateway is networking.

**Q21 – B.** VM Scale Sets deploy and autoscale a group of identical VMs.
- A: availability sets don't scale.
- C: DNS resolves names.
- D: Storage Explorer is a file-management tool.

**Q22 – A.** Azure Virtual Desktop is a desktop and app virtualization service, and App Service is the PaaS web app host (the alternatives for hosting apps are containers or VMs).
- B: the services are swapped.
- C: ACI runs containers, and Arc manages hybrid resources.
- D: Arc and VPN Gateway don't host desktops or web apps.

**Q23 – B.** Availability sets spread VMs across fault domains (hardware) and update domains (maintenance).
- A: region-wide outages need region pairs or multi-region designs.
- C and D: unrelated.

**Q24 – C.** ExpressRoute is a private connection that bypasses the public internet.
- A: VPN Gateway uses encrypted tunnels over the public internet.
- B: DNS is name resolution.
- D: peering connects virtual networks to each other.

**Q25 – B.** A private endpoint places a private IP from your VNet on the service, keeping traffic private.
- A: that is the opposite.
- C: encryption is a separate feature.
- D: that describes Azure DNS.

## Azure storage services (Q26–Q29)

**Q26.** Which storage option provides fully managed file shares accessible via SMB and NFS?
- A) Azure Blob Storage
- B) Azure Files
- C) Azure Queue Storage
- D) Azure Table Storage

**Q27.** Which redundancy option copies your data synchronously three times across availability zones in the primary region, and also asynchronously to a secondary region?
- A) LRS
- B) ZRS
- C) GRS
- D) GZRS

**Q28.** Which blob access tier is the most cost-effective for data that is rarely accessed and can tolerate hours of retrieval latency?
- A) Hot
- B) Cool
- C) Cold
- D) Archive

**Q29.** You need to move 80 TB of data to Azure, but your network is slow. Which service is the best fit?
- A) Azure Data Box
- B) Azure Storage Explorer
- C) Azure Migrate
- D) AzCopy over the existing link

### Answers and explanations: Storage

**Q26 – B.** Azure Files offers managed SMB and NFS shares.
- A: Blob is object storage.
- C: Queue is messaging.
- D: Table is NoSQL key-value data.

**Q27 – D.** GZRS = ZRS in the primary region (three zones) plus async replication to a secondary region.
- A: LRS keeps three copies in a single datacenter.
- B: ZRS has no secondary region.
- C: GRS uses LRS in the primary and replicates to a secondary region, with no zone redundancy in the primary.

**Q28 – D.** Archive is offline storage, the cheapest to store, with hours of rehydration time.
- A: Hot is for frequent access.
- B: Cool is for infrequent access (30+ days) with online access.
- C: Cold is for rarely accessed data (90+ days) with online access and no rehydration delay.

**Q29 – A.** Data Box is a physical appliance shipped to move large data offline.
- B: it is a GUI tool, still limited by bandwidth.
- C: Azure Migrate assesses and migrates servers and apps.
- D: AzCopy would take far too long over a slow link.

## Azure identity, access, and security (Q30–Q33)

**Q30.** A user signs in with a fingerprint or FIDO2 key instead of typing a password. Which authentication method is this, and which service issues the identity?
- A) Passwordless authentication, with Microsoft Entra ID
- B) Single sign-on only, with Azure Policy
- C) Passwordless authentication, with Azure Monitor
- D) Basic authentication, with Microsoft Purview

**Q31.** A user is granted access only when they sign in from a compliant device and a trusted location. Which feature enforces this?
- A) Azure Policy
- B) Resource locks
- C) Microsoft Entra Conditional Access
- D) Azure Advisor

**Q32.** Which statement describes Zero Trust?
- A) Trust everything inside the corporate network
- B) Never trust, always verify: assume breach and verify explicitly, using least-privilege access
- C) Trust any request that comes from a known IP address
- D) Replace all authentication with firewalls

**Q33.** Which Azure service provides a cloud security posture management (CSPM) and workload protection (CWP) solution that gives security recommendations and a secure score?
- A) Azure Advisor
- B) Microsoft Defender for Cloud
- C) Azure Service Health
- D) Azure Arc

### Answers and explanations: Identity and security

**Q30 – A.** Biometrics and FIDO2 keys are passwordless methods, and Microsoft Entra ID (formerly Azure AD) is the cloud directory/identity service providing them, plus SSO (one sign-in for many apps), MFA (two or more factors), and external identities (B2B/B2C guests). Entra Domain Services adds managed domain join, LDAP, and Kerberos without domain controllers.
- B: SSO is a different capability, and Policy enforces resource standards, not identities.
- C: Monitor collects telemetry.
- D: Purview is for data governance, and basic authentication is not passwordless.

**Q31 – C.** Conditional Access evaluates signals such as device, location, and risk, and then enforces access decisions.
- A: Policy governs resource configuration.
- B: locks prevent deletion or modification of resources.
- D: Advisor gives recommendations.

**Q32 – B.** Zero Trust means verify explicitly, use least-privilege access, and assume breach.
- A and C: these are the old perimeter-based models.
- D: firewalls alone are not Zero Trust.

**Q33 – B.** Defender for Cloud provides CSPM (secure score, recommendations) and CWP (threat protection).
- A: Advisor covers cost, reliability, performance, and operational excellence recommendations (with some security).
- C: Service Health reports Azure service issues.
- D: Arc manages hybrid resources.

---

# Domain 3: Describe Azure management and governance (Q34–Q50)

## Cost management (Q34–Q38)

**Q34.** Which factor can affect the cost of an Azure virtual machine?
- A) The color theme of the portal
- B) Region, VM size, and operating system licensing
- C) The number of tags applied
- D) The number of resource locks

**Q35.** Which tool estimates the cost of a planned Azure deployment before you build it?
- A) Azure Cost Management
- B) Azure Pricing Calculator
- C) Azure Monitor
- D) Azure Advisor

**Q36.** Which tool analyzes your actual spending, lets you set budgets, and sends alerts when spending exceeds thresholds?
- A) Azure Pricing Calculator
- B) Azure Policy
- C) Microsoft Cost Management
- D) Azure Service Health

**Q37.** What is the primary purpose of tags in Azure?
- A) To encrypt resources
- B) To apply metadata (name/value pairs) to resources for organization and cost reporting
- C) To prevent a resource from being deleted
- D) To assign access permissions

**Q38.** A VM will run continuously for the next three years. Which option lowers its cost the most compared with pay-as-you-go?
- A) Deleting its tags
- B) Azure Monitor alerts
- C) An Azure Reservation (reserved instance) with a 1- or 3-year commitment
- D) Moving it to a different resource group

### Answers and explanations: Cost

**Q34 – B.** Costs depend on the region, resource type and size, OS licensing, usage time, and bandwidth.
- A: portal theme has no cost effect.
- C: tags are free metadata.
- D: locks are free.

**Q35 – B.** The Pricing Calculator estimates costs before deployment.
- A: Cost Management analyzes costs that have been incurred.
- C: Monitor is for telemetry.
- D: Advisor gives recommendations.

**Q36 – C.** Microsoft Cost Management provides analysis, budgets, and alerts on actual spend.
- A: the calculator only estimates.
- B: Policy enforces rules.
- D: Service Health is for service incidents.

**Q37 – B.** Tags are name/value metadata used to organize resources and group costs (for example, by department).
- A: tags don't encrypt.
- C: that is a resource lock.
- D: that is RBAC.

**Q38 – C.** Reservations trade a 1- or 3-year commitment for large discounts versus pay-as-you-go (the Pricing Calculator can model this).
- A: tags are free metadata and don't change price.
- B: alerts don't affect price.
- D: resource groups don't affect price.

## Governance and compliance (Q39–Q42)

**Q39.** Which service provides a unified data governance solution, helping you discover, classify, and manage data across on-premises, multicloud, and SaaS?
- A) Microsoft Purview
- B) Azure Policy
- C) Azure Arc
- D) Microsoft Defender for Cloud

**Q40.** You need to ensure that all new resources are deployed only in West Europe and North Europe. What should you use?
- A) Resource locks
- B) Azure Policy
- C) Azure Advisor
- D) Azure Monitor alerts

**Q41.** You want to prevent anyone, including owners, from accidentally deleting a production database. What should you use?
- A) Azure Policy with the Audit effect
- B) A tag
- C) A resource lock (Delete)
- D) A budget

**Q42.** What is the difference between the ReadOnly and CanNotDelete lock levels?
- A) ReadOnly allows modification and deletion, and CanNotDelete blocks all changes
- B) CanNotDelete allows authorized users to read and modify but not delete, and ReadOnly allows read only, with no modification or deletion
- C) They are identical
- D) ReadOnly applies only to subscriptions

### Answers and explanations: Governance

**Q39 – A.** Microsoft Purview is the data governance, protection, and compliance solution.
- B: Policy governs Azure resource configuration.
- C: Arc extends management to non-Azure resources.
- D: Defender for Cloud is security posture and threat protection.

**Q40 – B.** Azure Policy can enforce allowed locations (and deny noncompliant deployments).
- A: locks don't restrict location.
- C: Advisor only recommends.
- D: alerts only notify.

**Q41 – C.** A CanNotDelete lock prevents deletion, even by owners, until the lock is removed.
- A: Audit only reports, it doesn't block.
- B: tags don't protect.
- D: budgets track spend.

**Q42 – B.** CanNotDelete lets authorized users read and modify but not delete. ReadOnly lets them read only.
- A: it is backwards.
- C: they differ.
- D: locks can apply to subscriptions, resource groups, or resources.

## Managing and deploying resources (Q43–Q46)

**Q43.** Which tool provides a browser-accessible shell authenticated to your Azure account, with Azure CLI and Azure PowerShell preinstalled?
- A) Azure Cloud Shell
- B) Azure Storage Explorer
- C) Azure Advisor
- D) Azure Data Box

**Q44.** Which service lets you manage on-premises, multicloud, and edge servers and Kubernetes clusters from Azure by projecting them into Azure Resource Manager?
- A) Azure Arc
- B) Azure Migrate
- C) Azure DNS
- D) Azure Traffic Manager

**Q45.** What is infrastructure as code (IaC)?
- A) Managing infrastructure by manually clicking through the portal
- B) Managing and provisioning infrastructure through machine-readable definition files, enabling repeatable, consistent deployments
- C) Writing applications in a low-code tool
- D) Backing up virtual machines

**Q46.** Which statement about Azure Resource Manager (ARM) and ARM templates is correct?
- A) ARM is the deployment and management layer for Azure, and ARM templates are declarative JSON files that define resources to deploy
- B) ARM templates can only deploy a single VM
- C) ARM is a billing tool
- D) ARM templates are imperative scripts that must be run line by line

### Answers and explanations: Management and deployment

**Q43 – A.** Cloud Shell is a browser-based shell with CLI and PowerShell.
- B: Storage Explorer is a file tool.
- C: Advisor gives recommendations.
- D: Data Box is a physical transfer device.

**Q44 – A.** Azure Arc extends Azure management and governance to resources running anywhere.
- B: Migrate is for migrations.
- C: DNS is for name resolution.
- D: Traffic Manager is for DNS-based traffic routing.

**Q45 – B.** IaC defines infrastructure in code files for repeatability and consistency.
- A: that is manual configuration.
- C and D: unrelated.

**Q46 – A.** ARM is the control plane for all Azure requests, and ARM templates are declarative JSON that deploy resources consistently.
- B: templates can deploy many resources.
- C: ARM is not a billing tool.
- D: templates are declarative, not imperative.

## Monitoring tools (Q47–Q50)

**Q47.** Which service gives personalized recommendations to improve reliability, security, performance, operational excellence, and cost?
- A) Azure Advisor
- B) Azure Service Health
- C) Azure Policy
- D) Microsoft Purview

**Q48.** You want to be notified about Azure service outages, planned maintenance, and health advisories that affect YOUR resources. Which service should you use?
- A) Azure Advisor
- B) Azure Service Health
- C) Azure Log Analytics only
- D) Azure Pricing Calculator

**Q49.** Which Azure Monitor capability lets you write queries to analyze log data collected from Azure resources?
- A) Log Analytics
- B) Azure Cloud Shell
- C) Azure Arc
- D) Azure Storage Explorer

**Q50.** You want to monitor a web application's performance, detect failures and slow response times, and trace dependencies. Which Azure Monitor feature should you use?
- A) Azure Monitor alerts only
- B) Application Insights
- C) Azure Service Health
- D) Azure Advisor

### Answers and explanations: Monitoring

**Q47 – A.** Advisor offers best-practice recommendations across five pillars: reliability, security, performance, operational excellence, and cost.
- B: Service Health reports incidents.
- C: Policy enforces rules.
- D: Purview is data governance.

**Q48 – B.** Service Health (with Azure status, Service Health, and Resource Health) provides personalized alerts about outages and maintenance affecting your resources.
- A: Advisor recommends improvements.
- C: Log Analytics queries logs.
- D: the calculator estimates costs.

**Q49 – A.** Log Analytics is the tool in Azure Monitor for querying logs using Kusto Query Language (KQL).
- B, C, D: none provides log querying.

**Q50 – B.** Application Insights is the APM feature of Azure Monitor that tracks requests, failures, performance, and dependencies.
- A: alerts only notify based on conditions.
- C: Service Health covers Azure platform issues.
- D: Advisor gives recommendations.

---

# Part 2: Additional questions (Q51–Q75)

These fill the remaining study-guide topics. They are grouped by domain and continue the numbering.

## Domain 1 additions: Cloud concepts (Q51–Q56)

**Q51.** A company is moving from buying servers every few years to renting cloud resources monthly. How does this change its spending?
- A) From operational expenditure (OpEx) to capital expenditure (CapEx)
- B) It eliminates all costs
- C) From capital expenditure (CapEx) to operational expenditure (OpEx)
- D) From variable costs to fixed costs

**Q52.** Which Azure pricing model offers deep discounts for workloads that can be interrupted when Azure needs the capacity back?
- A) Pay-as-you-go
- B) Azure Spot pricing
- C) Reserved instances
- D) Free tier

**Q53.** Which cloud benefit describes a system's ability to recover from failures and continue to function?
- A) Elasticity
- B) Manageability
- C) Governance
- D) Reliability

**Q54.** Which is a security and governance benefit of using the cloud?
- A) Built-in compliance certifications, policy enforcement, and security tooling that you can apply consistently across resources
- B) No need to protect your data or identities
- C) The provider takes over all of your legal obligations
- D) Governance is no longer needed once you migrate

**Q55.** During peak demand you add more VM instances to share the load, rather than making a single VM larger. What is this called?
- A) Scaling up (vertical scaling)
- B) Scaling down
- C) Scaling out (horizontal scaling)
- D) Failover

**Q56.** Under the shared responsibility model, in a PaaS deployment (for example, Azure App Service), what remains the customer's responsibility?
- A) The physical hosts
- B) The operating system patching
- C) The physical network
- D) The application and its data

### Answers and explanations: Domain 1 additions

**Q51 – C.** Buying hardware is CapEx (upfront). Renting cloud resources as you consume them is OpEx (ongoing). This is the usual shift when moving to the cloud.
- A: it is the reverse.
- B: you still pay for what you use.
- D: the cloud typically makes costs more variable, not more fixed.

**Q52 – B.** Spot pricing uses Azure's unused capacity at steep discounts, but VMs can be evicted. It suits batch and fault-tolerant workloads.
- A: pay-as-you-go is full price per use with no discount.
- C: reservations give discounts for a 1- or 3-year commitment, with no interruptions.
- D: the free tier gives limited free usage and isn't a deep-discount model.

**Q53 – D.** Reliability is the ability of a system to recover from failures and keep working. The cloud supports it with decentralized, global datacenters.
- A: elasticity is scaling with demand.
- B: manageability is about operating resources.
- C: governance is about policies and compliance.

**Q54 – A.** Cloud platforms provide compliance certifications and tools such as policy, RBAC, and Defender for Cloud to apply consistent controls.
- B, C: you remain responsible for data, identities, and compliance.
- D: governance becomes more important, not less.

**Q55 – C.** Scaling out adds instances (horizontal). Scaling up makes one instance bigger.
- A: that is vertical scaling and is the opposite approach.
- B: scaling down reduces capacity.
- D: failover switches to a standby when something fails.

**Q56 – D.** In PaaS, the customer manages the application and its data (plus identities and access), while Azure manages the OS, runtime, hosts, and network.
- A, C: always the provider's.
- B: the provider patches the OS in PaaS.

## Domain 2 additions: Architecture and services (Q57–Q67)

**Q57.** What is an Azure datacenter?
- A) A logical grouping of subscriptions
- B) A physical facility with servers, networking, power, and cooling, grouped into regions
- C) A type of storage account
- D) A virtual network in a subscription

**Q58.** Which statement about subscriptions and management groups is correct?
- A) A subscription is a unit of management, billing, and scale, and management groups organize multiple subscriptions so policies and access can be applied across them
- B) Management groups hold resources directly, and subscriptions hold management groups
- C) A subscription can only ever contain one resource group
- D) Management groups are used to deploy virtual machines

**Q59.** Which of these resources are typically required (in addition to the VM itself) to create a virtual machine in Azure?
- A) A Cosmos DB account and a key vault
- B) A virtual network with a network interface, an OS disk, and a resource group
- C) A management group and a budget
- D) An Azure Policy and an ExpressRoute circuit

**Q60.** A team wants a lightweight, portable way to package an application and its dependencies and start it quickly, while sharing the host OS kernel. Which compute type fits?
- A) Containers
- B) Virtual machines with a full guest OS per instance
- C) Azure Functions only
- D) Azure Virtual Desktop

**Q61.** Which feature connects two Azure virtual networks so resources can communicate using private IP addresses over the Microsoft backbone?
- A) Subnet delegation
- B) Azure DNS
- C) Virtual network peering
- D) Azure Traffic Manager

**Q62.** What is a public endpoint for an Azure service?
- A) An address reachable over the internet, for example the public URL of a storage account
- B) A private IP address inside your virtual network
- C) A connection that never leaves your datacenter
- D) A subnet in a peered virtual network

**Q63.** Which storage account option offers the broadest feature set and is the recommended type for most scenarios (blobs, files, queues, tables)?
- A) Standard general-purpose v2
- B) Premium page blobs only
- C) Azure Disk snapshots
- D) A SQL managed instance

**Q64.** A user wants a graphical tool to upload and manage blobs, files, and queues from their desktop. Another admin needs to synchronize an on-premises Windows file server with Azure Files. Which tools match?
- A) Azure Storage Explorer, and Azure File Sync
- B) AzCopy, and Azure Migrate
- C) Azure Data Box, and Azure Storage Explorer
- D) Azure Migrate, and Azure Advisor

**Q65.** What does Azure role-based access control (RBAC) let you do?
- A) Block deletions with a lock
- B) Enforce resource naming standards
- C) Estimate costs
- D) Grant users, groups, and apps specific permissions at a given scope, following least privilege

**Q66.** What is the defense-in-depth model?
- A) Using a single strong firewall at the network edge
- B) Using a layered approach to security: physical, identity and access, perimeter, network, compute, application, and data
- C) Encrypting only the data layer
- D) Relying on the provider alone for security

**Q67.** An organization wants to run legacy apps that need domain join, LDAP, and Kerberos without managing domain controllers, and also lets partners sign in with their own accounts. Which pair of capabilities fits?
- A) Azure Policy and resource locks
- B) Microsoft Entra Domain Services and Microsoft Entra External ID (external identities)
- C) Azure Arc and Azure Migrate
- D) Azure Monitor and Azure Advisor

### Answers and explanations: Domain 2 additions

**Q57 – B.** An Azure datacenter is a physical facility. Datacenters are grouped into availability zones and regions.
- A, C, D: these are logical constructs, not physical facilities.

**Q58 – A.** Subscriptions are the billing, access, and scale boundary, and management groups sit above them to apply governance consistently.
- B: it is the reverse.
- C: a subscription can hold many resource groups.
- D: management groups don't deploy resources.

**Q59 – B.** A VM needs a resource group, a virtual network and subnet, a network interface, and an OS disk (plus optionally a public IP and an NSG).
- A, C, D: these are unrelated to VM creation.

**Q60 – A.** Containers share the host OS kernel, are lightweight, and start quickly. VMs include a full guest OS, which makes them heavier.
- B: heavier and slower.
- C: Functions are event-driven code, not a packaging format.
- D: AVD delivers desktops.

**Q61 – C.** Peering links virtual networks, with traffic carried privately on the Microsoft backbone.
- A: subnet delegation grants a service permission in a subnet.
- B: DNS resolves names.
- D: Traffic Manager routes traffic by DNS.

**Q62 – A.** A public endpoint is internet-reachable.
- B: that is a private endpoint.
- C and D: not what a public endpoint is.

**Q63 – A.** General-purpose v2 supports blobs, files, queues, and tables, and it's the standard recommendation (premium types are for low-latency specialized needs).
- B: premium page blobs are specialized and narrow.
- C: snapshots aren't an account type.
- D: SQL managed instance is a database service.

**Q64 – A.** Storage Explorer is the GUI tool, and Azure File Sync syncs on-premises Windows file servers with Azure Files. (AzCopy is a command-line tool, and Azure Migrate assesses and migrates servers, databases, and apps.)
- B: AzCopy is not graphical, and Migrate isn't a sync tool.
- C: Data Box is a physical transfer device.
- D: Migrate and Advisor don't match.

**Q65 – D.** RBAC assigns roles (such as Reader, Contributor, Owner) to security principals at a scope (management group, subscription, resource group, or resource).
- A: that is locks.
- B: that is Azure Policy.
- C: that is the Pricing Calculator or Cost Management.

**Q66 – B.** Defense in depth uses multiple layers so that a breach of one layer doesn't compromise everything.
- A and C: a single layer is the opposite of the concept.
- D: security is a shared responsibility.

**Q67 – B.** Entra Domain Services provides managed domain services (domain join, LDAP, Kerberos/NTLM). External identities let partners and customers collaborate and sign in with their own accounts.
- A: neither provides domain services or external sign-in.
- C: Arc and Migrate cover hybrid management and migration.
- D: Monitor and Advisor provide telemetry and recommendations.

## Domain 3 additions: Management and governance (Q68–Q75)

**Q68.** What is the Azure portal?
- A) A command-line tool only
- B) A web-based unified console for building, managing, and monitoring Azure resources
- C) A billing-only website
- D) An on-premises hardware appliance

**Q69.** Which statement about Azure CLI and Azure PowerShell is correct?
- A) Both can manage Azure resources from the command line and in scripts, and CLI uses az commands while PowerShell uses cmdlets
- B) Azure CLI works only on Windows
- C) PowerShell cannot be used to automate Azure
- D) They can't be used in Cloud Shell

**Q70.** What is the key difference between Azure Policy and Azure RBAC?
- A) Policy controls who can access resources, and RBAC controls resource properties
- B) They are the same feature
- C) Policy controls what resource configurations are allowed, and RBAC controls what actions users can perform
- D) RBAC applies only to storage

**Q71.** You want to be emailed when the CPU of a VM exceeds 90% for 10 minutes. Which feature should you configure?
- A) Azure Monitor alerts with an action group
- B) Azure Policy
- C) A resource lock
- D) A tag

**Q72.** Which of the following can increase your Azure bill?
- A) Using resource groups
- B) Outbound data transfer (egress), larger VM sizes, and premium storage tiers
- C) Adding tags
- D) Using the Azure portal

**Q73.** What is the main benefit of deploying with ARM templates (infrastructure as code)?
- A) Manual configuration of each resource
- B) Templates only work on one subscription
- C) Resources can't be changed after deployment
- D) Repeatable, consistent deployments with idempotent behavior, where the same template yields the same result

**Q74.** Which Azure Service Health component shows issues with an individual resource such as a single VM?
- A) Azure status
- B) Resource Health
- C) Azure Advisor
- D) Cost Management

**Q75.** You apply a CanNotDelete lock to a resource group. What happens to the resources inside it?
- A) They inherit the lock, so they can't be deleted
- B) They are unaffected
- C) They are deleted
- D) They become read-only automatically

### Answers and explanations: Domain 3 additions

**Q68 – B.** The portal is the web-based console for managing Azure.
- A: that's the CLI or PowerShell.
- C: it isn't billing-only.
- D: it's not hardware.

**Q69 – A.** Both are cross-platform and scriptable. CLI uses `az` commands and PowerShell uses cmdlets (for example, `Get-AzVM`), and both are available in Cloud Shell.
- B: the CLI is cross-platform.
- C: PowerShell is a standard automation tool for Azure.
- D: both are preinstalled in Cloud Shell.

**Q70 – C.** Policy governs resource configuration and compliance (what's allowed). RBAC governs user permissions (who can do what).
- A: it's reversed.
- B: they differ.
- D: RBAC applies across resource types.

**Q71 – A.** Azure Monitor alerts trigger on metric thresholds, and action groups define notifications such as email.
- B, C, D: none sends notifications on metrics.

**Q72 – B.** Egress, VM size, storage tier, and region all influence cost.
- A, C, D: resource groups, tags, and the portal are free.

**Q73 – D.** ARM templates are declarative and idempotent, giving consistent, repeatable deployments.
- A: that's what IaC avoids.
- B: templates can target multiple subscriptions and resource groups.
- C: resources can be updated by redeploying.

**Q74 – B.** Resource Health reports the health of individual resources. Azure status shows global service health, and Service Health shows issues affecting your subscriptions and regions.
- A: global status, not per resource.
- C: Advisor gives recommendations.
- D: Cost Management is about spend.

**Q75 – A.** Locks are inherited by child resources, so the resources can't be deleted while the lock is in place.
- B: inheritance applies.
- C: a lock doesn't delete anything.
- D: that is the ReadOnly lock level.

---

# Answer key

| Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 11 | C | 21 | B | 31 | C | 41 | C |
| 2 | C | 12 | B | 22 | A | 32 | B | 42 | B |
| 3 | C | 13 | C | 23 | B | 33 | B | 43 | A |
| 4 | A | 14 | D | 24 | C | 34 | B | 44 | A |
| 5 | C | 15 | B | 25 | B | 35 | B | 45 | B |
| 6 | B | 16 | A | 26 | B | 36 | C | 46 | A |
| 7 | B | 17 | B | 27 | D | 37 | B | 47 | A |
| 8 | A | 18 | C | 28 | D | 38 | C | 48 | B |
| 9 | A | 19 | B | 29 | A | 39 | A | 49 | A |
| 10 | A | 20 | B | 30 | A | 40 | B | 50 | B |

| Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|
| 51 | C | 56 | D | 61 | C | 66 | B | 71 | A |
| 52 | B | 57 | B | 62 | A | 67 | B | 72 | B |
| 53 | D | 58 | A | 63 | A | 68 | B | 73 | D |
| 54 | A | 59 | B | 64 | A | 69 | A | 74 | B |
| 55 | C | 60 | A | 65 | D | 70 | C | 75 | A |

## Topic coverage checklist (from the study guide)

- **Cloud computing:** definition (Q1), shared responsibility (Q2, Q56), cloud models and use cases (Q3, Q4), consumption-based model (Q5, Q51), pricing models (Q52, Q38), serverless (Q6)
- **Benefits:** high availability and scalability (Q7, Q8, Q55), reliability and predictability (Q9, Q53), security and governance (Q54), manageability (Q10)
- **Service types:** IaaS, PaaS, SaaS and use cases (Q11–Q14)
- **Core architecture:** regions, region pairs, sovereign regions (Q15, Q17), availability zones (Q16), datacenters (Q57), resources and resource groups (Q19), subscriptions and management groups (Q58), hierarchy (Q18)
- **Compute and networking:** compute types (Q20, Q60), VM options: Scale Sets, availability sets, AVD (Q21–Q23), VM resources (Q59), application hosting (Q22, Q60), virtual networks, subnets, peering (Q61), Azure DNS (Q25 explanation, Q62), VPN Gateway and ExpressRoute (Q24), public and private endpoints (Q25, Q62)
- **Storage:** services (Q26), tiers (Q28), redundancy (Q27), account options and types (Q63), file movement tools: AzCopy, Storage Explorer, File Sync (Q64), migration: Azure Migrate, Data Box (Q29, Q64)
- **Identity and security:** Entra ID, SSO, MFA, passwordless (Q30), Entra Domain Services and external identities (Q67), Conditional Access (Q31), RBAC (Q65), Zero Trust (Q32), defense in depth (Q66), Defender for Cloud (Q33)
- **Cost management:** cost factors (Q34, Q72), pricing calculator (Q35), Cost Management (Q36), tags (Q37), reservations (Q38)
- **Governance:** Purview (Q39), Policy (Q40, Q70), resource locks (Q41, Q42, Q75)
- **Management and deployment:** portal (Q68), Cloud Shell, CLI and PowerShell (Q43, Q69), Arc (Q44), IaC (Q45), ARM and templates (Q46, Q73)
- **Monitoring:** Advisor (Q47), Service Health (Q48, Q74), Azure Monitor, Log Analytics (Q49), alerts (Q71), Application Insights (Q50)

Note: Azure DNS appears only in Q61/Q62 distractors and the Q25 context, so review its purpose (name resolution for domains) separately.
