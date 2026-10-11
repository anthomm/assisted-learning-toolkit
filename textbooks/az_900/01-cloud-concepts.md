# Cloud concepts (25-30%)

This chapter introduces cloud computing as a way to access technology capabilities over the internet without owning and operating every part of the underlying infrastructure. It explains how deployment and service models change control, responsibility, and cost, then connects those choices to availability, adaptability, security, and day-to-day operations. The goal is to recognize what the cloud can provide—and what an organization must still design, configure, and manage.

## What cloud computing is

### Learning intent

Be able to explain cloud computing in plain language, distinguish public, private, and hybrid deployment models, and select a model for a stated need. Understand the shared responsibility model, consumption-based billing, common pricing approaches, and serverless computing as a cloud execution approach.

### Core concepts

**Cloud computing (`cc-define-cloud`).** Cloud computing delivers services such as compute, storage, databases, and networking over the internet. Instead of first buying and installing physical infrastructure, an organization can provision resources from a cloud provider. The defining idea is access to computing capability, not whether an application has a web interface.

**Shared responsibility (`cc-shared-responsibility`).** A cloud provider and customer divide operational and security duties. The provider operates the physical datacenter and supporting infrastructure; the customer remains accountable for its data, identities, and the parts of the service it controls. The division varies by service type: a virtual machine leaves the customer more to manage than a hosted application.

The table is a broad orientation, not a substitute for a service's terms or detailed control guidance. “Shared” indicates that both parties have related responsibilities; it does not mean every task is split evenly.

| Responsibility area | On-premises | IaaS | PaaS | SaaS |
| --- | --- | --- | --- | --- |
| Customer data, configurations, identities and users | Customer | Customer | Customer | Customer |
| Client devices | Customer | Customer | Customer | Shared |
| Applications | Customer | Customer | Shared | Shared |
| Network controls | Customer | Customer | Shared | Provider |
| Operating system | Customer | Customer | Provider | Provider |
| Physical hosts, physical network, datacenter | Customer | Provider | Provider | Provider |

**Cloud models (`cc-cloud-models`).** A *deployment model* describes how cloud resources are organized and who can use them; it is different from a service model such as IaaS or SaaS.

| Deployment model | What it means | Common trade-off |
| --- | --- | --- |
| Public cloud | A third-party provider offers cloud resources for use by customers. | Rapid provisioning and broad provider services, with less direct control of the underlying infrastructure. |
| Private cloud | A cloud environment is dedicated to one organization. It can be hosted on-site or by a third party. | More control over the environment, while the organization retains more responsibility for infrastructure and operations. |
| Hybrid cloud | Public and private cloud environments are connected and used together. | Greater flexibility in deciding where workloads and data run, with additional integration and management work. |

**Cloud model use cases (`cc-cloud-model-use-cases`).** Choose from requirements, not from a claim that one model is universally best. Public cloud can suit a team that needs to provision capacity quickly or avoid purchasing its own datacenter hardware. A private cloud can fit an organization that needs a dedicated environment and is prepared to retain greater infrastructure control and responsibility. A hybrid model can be useful when some workloads need to remain in a private environment while others benefit from public-cloud scale, or when public resources temporarily supplement private capacity. Security, legal obligations, skills, costs, and existing systems all affect the decision.

**Consumption model (`cc-consumption-model`).** Under a consumption-based approach, a customer pays for measured services it uses rather than purchasing all capacity in advance. Resources can often be added as needs grow and removed when they are no longer needed. This can reduce idle capacity and upfront infrastructure purchases, but “pay for what you use” does not mean cloud services are automatically inexpensive: unused resources, unexpectedly high demand and poor configuration can still create costs. Monitoring and deliberate capacity choices matter.

**Pricing models (`cc-pricing-models`).** In the AZ-900 comparison, purchasing and maintaining physical infrastructure is commonly presented as capital expenditure (CapEx), while metered cloud services are commonly presented as operational expenditure (OpEx). This is a budgeting distinction, not a promise that every cloud charge is variable. *Pay-as-you-go* charges follow service consumption. *Reservations* commit to qualifying usage for a defined term in return for a discount on matching usage; they can suit stable demand but may not fit uncertain or mismatched use. Terms, eligible services, and payment choices vary.

> **Verify:** Confirm current rates, eligible products, reservation terms, and billing choices in the [Azure pricing calculator](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator) and current product pricing information before making a purchasing decision. An estimate is not a guaranteed invoice.

**Serverless (`cc-serverless`).** Serverless is a cloud execution approach in which the provider manages the servers and much of the infrastructure operation, while the customer concentrates on application logic. It does not mean that servers do not exist. Azure Functions, for example, supports event-driven code such as responding to a file upload, a scheduled event, or a message. Hosting options and their scaling and billing behavior differ, so do not assume every serverless workload scales identically or is billed only when code runs.

### How it works, distinctions, limits, and defaults

Keep three labels separate: the **deployment model** (public/private/hybrid) describes the environment; the **service model** (IaaS/PaaS/SaaS) describes the stack the provider operates; the **billing model** describes how charges are calculated. A public-cloud customer might use a PaaS database and pay according to measured usage—one label does not determine the others.

Moving a workload to the cloud does not hand off all security obligations. Customers still protect data, manage access, configure services, and monitor what they control. Provider-managed infrastructure does not make a workload secure by default; the boundary depends on the service and its configuration.

> **Conflict:** Microsoft's AZ-900 cloud-compute learning unit (dated 2024) describes identity and access as shared for PaaS and SaaS, explaining that the customer manages users, roles, and policies while the provider operates the authentication platform. Microsoft's Shared Responsibility article (dated 2026) lists “identities and users” and access management among customer responsibilities across cloud types. These descriptions use different levels of detail and their broad wording does not align exactly. A useful operational distinction is between operating an identity service and configuring the organization's users, roles, and access controls; verify the responsibility for the specific service and feature rather than treating “shared” as a blanket answer.

### Example or worked scenario

A small retailer is preparing a one-week online promotion. It needs additional capacity during the campaign, does not want to purchase servers that may sit idle afterward, and already has an internal policy requiring sensitive finance records to stay in its private environment.

The retailer could host the campaign site in public cloud, scale it back afterward, and retain the finance workload privately in a hybrid design. PaaS suits developers who want to avoid OS patching; a legacy application requiring OS-level changes may call for IaaS. Consumption-based charges can follow campaign usage, while reservations are better evaluated for steady eligible demand than a short uncertain peak. In each case, the retailer manages its data, identities, and applicable controls.

### Exam or practical application

For a scenario, identify the key requirement: OS control points to IaaS, infrastructure upkeep in a dedicated environment to private cloud, and connected private/public resources to hybrid. For costs, distinguish owned infrastructure from metered services and reservations from pay-as-you-go. For security, identify the service model and specific control.

### Self-check questions

1. A team wants to keep full control of a server operating system while avoiding ownership of physical hosts. Which arrangement best fits?

   **Answer:** IaaS in a cloud environment. The provider manages the physical hosts; the customer manages the guest operating system and much of the workload stack.

2. What is the key difference between a private cloud and a hybrid cloud?

   **Answer:** A private cloud is dedicated to one organization. A hybrid cloud connects and uses private and public cloud environments together.

3. Does consumption-based billing guarantee that costs will be low?

   **Answer:** No. It ties charges to measured use, but waste, unexpected demand, or poor configuration can still make costs high.

4. What does “serverless” mean, and what does it not mean?

   **Answer:** The provider manages much of the server infrastructure so the customer can focus on application logic; it does not mean that no servers exist.

### Sources

- [Describe cloud computing — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/)
- [What is cloud computing — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/3-what-cloud-compute)
- [Shared responsibility model (AZ-900 learning unit) — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model)
- [Define cloud models — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models)
- [Describe the consumption-based model — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model)
- [Shared responsibility in the cloud — Microsoft Learn](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)
- [What are Azure Reservations? — Microsoft Learn](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations)
- [Azure pricing calculator — Microsoft Learn](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator)
- [Azure Functions overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)

## Why organizations use the cloud

### Learning intent

Describe how cloud services can help an organization maintain service availability, adjust capacity, plan performance and cost, strengthen security and governance practices, and manage resources more effectively. Understand that these are capabilities to design and use—not automatic outcomes guaranteed by choosing a cloud provider.

### Core concepts

**High availability and scalability (`cc-ha-scalability`).** *High availability* is the design goal of keeping a service usable when failures or disruptions occur. Availability commitments are service-specific and are described in applicable service-level agreements (SLAs). An SLA is not a substitute for a resilient design: the organization must select suitable services, configure redundancy where available, and plan for recovery.

*Scalability* is the ability to adjust resources to meet changing demand. **Vertical scaling** changes the capacity of an individual resource—for example, selecting a virtual machine with more compute capacity. **Horizontal scaling** changes the number of resource instances, such as adding or removing application instances. Scaling *out* adds capacity; scaling *in* removes it. *Elasticity* is the ability to adjust capacity as demand rises and falls, often by automating scale actions. Whether a particular resource can scale, how quickly it can do so, and whether the action is automatic depend on the service and its configuration.

**Reliability and predictability (`cc-reliability-predictability`).** *Reliability* concerns a workload's ability to recover from failure and continue to provide its intended function. A design may use redundancy or regional distribution, but cloud infrastructure alone does not ensure that an application is reliable; architecture, configuration, and recovery planning matter. *Predictability* means planning with greater confidence about workload behavior and costs. Performance predictability can benefit from monitoring, load balancing, and autoscaling. Cost predictability can benefit from measuring usage, analyzing trends, setting budgets, and estimating planned deployments. These practices inform decisions; actual demand and charges can differ from estimates.

**Security and governance (`cc-security-governance`).** Cloud environments provide tools and provider capabilities that organizations can use to apply security and governance controls consistently. For example, templates can standardize deployments, and auditing can help identify resources that do not match an organization's baseline. The customer must still define requirements, assign appropriate access, configure controls, protect data, and respond to findings. Governance is the system of policies and practices used to keep resources aligned with business, security, and compliance requirements; it is not a guarantee that every deployment is compliant.

**Manageability (`cc-manageability`).** Microsoft Learn distinguishes *management of the cloud* from *management in the cloud*. Management **of** the cloud is about operating or automating the resources themselves—for example, scaling based on demand, deploying from templates, monitoring resource health, or setting alerts. Management **in** the cloud is about the tools used to administer cloud resources, such as a web portal, command-line interface, APIs, and PowerShell. These tools can make operations repeatable and visible, but teams still need roles, processes, monitoring, and skills to use them effectively.

### How it works, distinctions, limits, and defaults

Availability, reliability, scalability, and elasticity are related but distinct. A scalable service can still have a single point of failure; replication may improve availability without increasing processing capacity. Reliability includes failure recovery, high availability focuses on maintaining access, and elasticity describes capacity changing with demand.

Predictability can mean anticipating performance as demand changes or forecasting cost. Scaling can support both, but does not replace monitoring. Autoscaling rules, limits, startup time, and billing effects are service-specific; estimates use assumptions, while bills reflect actual usage and current prices.

Cloud security is shared: the provider operates underlying facilities and offers security capabilities, while the customer decides who can access data and how workloads are configured. Automation improves consistency only when templates, policies, and alerts reflect the organization's requirements.

### Example or worked scenario

A ticketing company can add application instances horizontally during a popular sale and scale them back afterward. Monitoring and load balancing help the team observe and distribute demand, but it must test startup times, database capacity, and failure recovery. Finance and engineering can compare estimates with usage, standardize deployments with templates, and alert operators to health problems. These practices improve visibility and control but do not eliminate outages or cost surprises.

### Exam or practical application

When asked to classify a cloud benefit, look for the core action in the scenario: keeping a workload operating amid disruptions suggests high availability; recovering and continuing after failure suggests reliability; changing capacity suggests scalability; automatically following demand up and down suggests elasticity. Better estimates of operating expenses are cost predictability; confidence that a workload meets demand is performance predictability. For manageability, ask whether the scenario is automating resource operation (management **of** the cloud) or using a tool or interface to administer resources (management **in** the cloud). Do not interpret “cloud benefit” as “automatic guarantee.”

### Self-check questions

1. A team adds more identical application instances to handle a traffic spike. Is this vertical or horizontal scaling?

   **Answer:** Horizontal scaling; the team is changing the number of instances.

2. How does reliability differ from scalability?

   **Answer:** Reliability is about recovering from failure and continuing to function. Scalability is the ability to adjust resources to meet demand.

3. Give one example each of management of the cloud and management in the cloud.

   **Answer:** Automatically replacing or scaling resources is management of the cloud. Administering resources through a portal, CLI, API, or PowerShell is management in the cloud.

4. Does using a cloud provider guarantee that an organization meets its security and compliance obligations?

   **Answer:** No. Provider capabilities can help, but the customer must configure and operate its controls and meet its own obligations.

### Sources

- [Describe the benefits of using cloud services — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)
- [High availability and scalability in the cloud — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/2-high-availability-scalability-cloud)
- [Reliability and predictability in the cloud — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/3-reliability-predictability-cloud)
- [Security and governance in the cloud — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/4-security-governance-cloud)
- [Manageability in the cloud — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/5-manageability-cloud)
- [Azure Well-Architected Framework — Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/)
- [Overview of Cost Management — Microsoft Learn](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management)

## Cloud service types: IaaS, PaaS, SaaS

### Learning intent

Explain Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS); compare the responsibilities they leave with the customer; and match each type to a practical need. The central distinction is how much of the technology stack the provider operates on the customer's behalf.

### Core concepts

**Infrastructure as a Service (`cc-iaas`).** IaaS provides computing infrastructure—such as virtual machines, storage, and networking—as services. The provider operates the physical datacenter, physical hosts, and network infrastructure; the customer has substantial control over and responsibility for the guest operating system, configuration, applications, and data. It offers the most flexibility of the three, with more operational work; it can fit a workload requiring customer control of its OS or configuration.

**Platform as a Service (`cc-paas`).** PaaS provides a managed platform on which the customer builds, deploys, or runs applications. The provider manages the physical infrastructure and platform components such as the operating system and runtime. The customer focuses more on application code, data, and service configuration. It can fit a team building and deploying an application without maintaining servers or the operating system.

**Software as a Service (`cc-saas`).** SaaS provides a ready-to-use application operated by the provider. The provider manages most of the application stack and its infrastructure; the customer typically manages its data, users, access choices, and how the application is used. Email, messaging, and productivity applications are common examples. SaaS offers quick access to a complete application, with less infrastructure and software control than IaaS or PaaS.

The table summarizes the broad pattern; exact responsibility depends on the service and configuration.

| Service type | Provider primarily manages | Customer primarily manages | Typical choice when… |
| --- | --- | --- | --- |
| IaaS | Physical facilities, hosts, and underlying network | Operating system, much of configuration, applications, data, and access | You need control over the operating system or want to move a customizable workload. |
| PaaS | Infrastructure, operating system, runtime, and managed platform | Application code, data, and service-level configuration | You want to build or run an application without operating its platform. |
| SaaS | Infrastructure, platform, and ready-made application | Data, users, access settings, and appropriate use | You need a complete application rather than a platform to build on. |

**Service-type use cases (`cc-service-type-use-cases`).** Ask what the organization wants to manage. Choose IaaS when retaining lower-level control—especially over the operating system—is important and the team can take on patching and maintenance. Choose PaaS when the priority is developing or deploying applications while delegating infrastructure and platform upkeep. Choose SaaS when the requirement is to use a complete application with minimal infrastructure management. Real solutions can combine service types; a single organization can use SaaS for collaboration, PaaS for a custom application, and IaaS for a legacy workload.

### How it works, distinctions, limits, and defaults

Think of a stack: facilities and hardware, virtualization and networking, operating system and runtime, application, then data and user configuration. Moving from IaaS through PaaS to SaaS generally shifts more operation to the provider and reduces customer infrastructure work, but also reduces customization of provider-managed layers. Customers still have duties in every model.

IaaS differs from on-premises hosting because the provider operates the physical host and datacenter even while the customer manages a VM's OS. PaaS is distinguished by provider-managed platform components; SaaS is a provider-operated application. Across all three, customers manage data and accounts and must understand applicable access, network, and security controls. SaaS reduces infrastructure work, not identity or data-governance duties; IaaS does not place the physical datacenter under customer control.

> **Verify:** Individual cloud services may combine features or expose configuration choices that change the practical responsibility boundary. Consult the service's current documentation and responsibility guidance rather than inferring every control solely from the label IaaS, PaaS, or SaaS.

### Example or worked scenario

A nonprofit wants to launch a public-facing donation website. Its developers are comfortable maintaining application code but do not want to patch a web server operating system. A PaaS web-hosting service is a plausible fit: the provider operates the underlying platform, while the nonprofit focuses on its application and data. The nonprofit still configures access, protects donor information, and monitors the application.

An older finance application needing a custom OS component may fit IaaS, while staff email and document collaboration may fit SaaS. The nonprofit can use different service types for different workloads rather than choosing a single label for the organization.

### Exam or practical application

Use the responsibility boundary to classify service types: customer-managed guest OS on a cloud VM indicates IaaS; provider-managed OS/runtime with customer-deployed code indicates PaaS; a provider-operated business application indicates SaaS. Minimal infrastructure work points to SaaS for a complete product or PaaS for a customer's own app. OS control points to IaaS.

### Self-check questions

1. Which service type best fits a development team that wants to deploy its own code but not patch the operating system?

   **Answer:** PaaS, because the provider manages the operating system and managed platform while the team focuses on its application.

2. In IaaS, who typically patches and maintains the guest operating system?

   **Answer:** The customer. The provider manages the physical infrastructure, but the guest OS is part of the customer-managed workload.

3. A company uses a hosted email product without operating its own mail servers or application. Which service type is this?

   **Answer:** SaaS, a ready-to-use application operated by the provider.

4. Does choosing SaaS remove every customer security responsibility?

   **Answer:** No. Customers continue to manage their data, identities, users, access settings, and other controls applicable to their use of the service.

### Sources

- [Describe cloud service types — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)
- [Describe Infrastructure as a Service — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service)
- [Describe Platform as a Service — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/3-describe-platform-service)
- [Describe Software as a Service — Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/4-describe-software-service)
- [Shared responsibility in the cloud — Microsoft Learn](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)
