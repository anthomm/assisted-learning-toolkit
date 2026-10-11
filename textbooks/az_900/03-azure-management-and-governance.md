# Azure management and governance (30-35%)

Azure gives organizations tools to understand what cloud resources cost, apply rules consistently, deploy resources repeatably, and detect problems before they become outages. It focuses on estimating, setting guardrails, deploying consistently, and responding to health signals.

## Costs in Azure

### Learning intent

Learn to recognize what can change an Azure bill, create a planning estimate with the Azure pricing calculator, use Microsoft Cost Management to inspect and manage spending, and use tags to organize resources and cost data. Remember that an estimate is a planning aid, while billing data records measured and rated use; neither a tag nor a budget by itself prevents all spending.

### Core concepts

**Factors that affect Azure costs (`mg-cost-factors`).** A cloud bill is the result of what you provision, how much you use it, and the applicable price and commercial terms. The service and configuration matter: for example, compute size, storage capacity or access pattern, database tier, and network design determine which meters apply. The quantity and duration of use matter too. A virtual machine left running for more hours generally incurs more compute usage than one stopped and deallocated sooner; storage can continue to incur charges even when a workload is idle. Transferred data, backups, monitoring, and other related services may contribute additional charges.

Location can affect the available products and their rates, so a configuration estimated in one region should not be assumed to cost the same in another. Discounts, negotiated prices, reservations, savings plans, and other eligible purchase choices can also change the effective price. Taxes, support, licensing, marketplace purchases, credits, and billing-specific arrangements may be accounted for differently from the resource-level cost view. Always identify which costs a particular estimate or report includes before using it as an invoice prediction.

A useful mental model is **configuration × measured consumption × applicable rate**, with billing adjustments and commercial terms layered on top. It is not a universal formula: products meter usage differently, and cost data may not match a finalized invoice.

**Azure pricing calculator (`mg-pricing-calculator`).** The Azure pricing calculator is a public, browser-based planning tool. Build an estimate by adding services, selecting product variants and region, and entering expected usage. The calculator displays the resulting estimated costs for the selected configuration. For some offerings it can show upfront and monthly amounts, and some services expose purchase options such as reserved capacity or savings plans. Signing in can let the calculator use negotiated or discounted prices associated with the account; the displayed public estimate is not necessarily the price a particular customer will pay.

Make calculator assumptions explicit: estimate the intended instance count and size, runtime, storage, transfer, and supporting services. Revisit the estimate as the design changes. It is not a quote, deployment, or spending cap; actual costs depend on actual usage and applicable account terms.

**Microsoft Cost Management (`mg-cost-management`).** Microsoft Cost Management provides FinOps-oriented tools to analyze, monitor, and optimize Microsoft cloud spending. Azure users can inspect cost data at available scopes such as billing accounts, subscriptions, resource groups, and management groups, subject to their access and agreement. Cost Analysis helps answer questions such as “Which services drove this month's increase?” or “How is spending distributed across teams?” Users can group and filter data, review trends, and export cost details for other analysis or processes.

Cost Management supports proactive tracking as well as retrospective analysis. Budgets let an authorized user set a spending or usage target and configure alerts when actual or forecast cost reaches defined thresholds. An alert notifies people or systems; it does not automatically stop resources or guarantee that the final bill stays below the target. Cost anomaly features can help surface unusual patterns, and scheduled alerts and exports can support recurring review and downstream reporting. Available features, scopes, and billing data depend on the account and current service capabilities.

Keep the distinction between **Cost Management** and **Billing** clear. Cost Management is for analyzing, managing, and optimizing cost. Billing experiences address the commercial billing relationship—such as invoices, payment methods, and credits—where applicable. The data and timing are related but not identical. In particular, invoices may include credits, taxes, or purchases that are not represented in the same way in Cost Management data. If reconciliation matters, use the appropriate billing documents and scope rather than treating a cost chart as an invoice.

**Tags (`mg-tags`).** A tag is a key-value pair of metadata attached to a resource, resource group, or subscription. For example, `Environment = Production` or `CostCenter = 1200` can support organization, automation, reporting, and cost attribution. Where billing data supports tags, teams can group costs by department, application, or project.

Tags are not a separate access-control system, and adding a tag does not itself change a resource's behavior. A resource also does not automatically inherit tags from its resource group or subscription. An organization can use Azure Policy to require or apply tags, and Cost Management supports tag inheritance and cost-allocation capabilities in supported contexts, but the existence of a parent tag alone does not guarantee child resources or every cost record carry it. Tags are plain text: do not put secrets, personal data, or other sensitive values in them. Agree on consistent key names and value conventions so reports remain useful.

### How it works, distinctions, limits, and defaults

Cost estimation and cost observation answer related but different questions. The calculator asks, “Given this proposed configuration and these assumptions, what might it cost?” Cost Management asks, “What cost data is available for the scope and period I can access, and how can I analyze or manage it?” Billing asks, “What are the charges, credits, and payment obligations in the billing relationship?” Use each for its purpose: estimate before deployment, inspect actual cost during operation, and reconcile with billing artifacts when needed.

The main cost drivers are not limited to a monthly service price. Consider the chosen service tier and resource size, the quantity provisioned, the time it runs, usage-based measures such as requests or data processed, data storage and transfer, region, and applicable discounts or commitments. A design that reduces one meter can increase another—for example, additional redundancy may raise storage or transfer requirements while improving resilience. Cost optimization is therefore a design trade-off, not simply choosing the smallest virtual machine.

| Tool or mechanism | Main question it answers | What it does not guarantee |
| --- | --- | --- |
| Azure pricing calculator | What is a planned configuration likely to cost under stated assumptions? | It does not deploy resources, lock in a price, or guarantee an invoice amount. |
| Cost Analysis | What cost data is available for this scope and period, and how is it distributed? | It is not necessarily the final invoice or a live meter with zero delay. |
| Budget and alert | Has spending or a forecast reached a threshold that people should review? | An alert is not a spending cap and does not automatically stop resources by default. |
| Tags | How can resources and supported cost records be classified or grouped? | Tags do not enforce permissions, inherit automatically, or guarantee complete billing coverage. |

Cost data and billing records can differ in timing and scope. Before reconciling differences, check the period, price terms, credits, taxes, and data definitions; do not promise an exact amount without confirming current prices and account terms.

> **Verify:** Calculator catalog options, negotiated-price behavior, Cost Management features, report scopes, and billing-data timing can change. Check the live calculator and the account's applicable Cost Management and billing experience before making a purchasing commitment.

### Example or worked scenario

A small product team plans a test environment with two virtual machines, managed storage, and a database. Before creating anything, the team uses the calculator to add each service, chooses the intended region and service tiers, enters the expected hours and capacity, and checks whether any applicable purchase options should be modeled. It records two scenarios: one for a continuously running test system and another for a system shut down outside working hours. The comparison makes the runtime assumption visible instead of hiding it inside one monthly total.

After deployment, the team applies `Application = CatalogDemo`, `Environment = Test`, and `CostCenter = 1200` tags according to its naming convention. In Cost Analysis, it filters to the test resource group, compares the current period with the prior period, and groups by service or tag where available. It sets a budget with an alert for the team mailbox, but treats the message as a prompt to investigate—not as an automatic shutoff. If actual cost is higher than expected, the team checks whether VMs ran longer, data transfer or storage grew, or the selected configuration differed from the estimate. It also checks the billing view when reconciling final charges.

### Hands-on activity

Use an authorized sandbox; no deployment is required.

1. Open the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/), add compute and storage, and vary region, runtime, or capacity. Record your assumptions and any costs not modeled.
2. In the portal, open Cost Analysis for an authorized scope and note the time range, grouping, and filters available.
3. Inspect budgets and alerts, if permitted, without creating one for production. Identify a sensible threshold and recipients for a test subscription.
4. Review resource tags and verify child resources actually have them; do not assume inheritance.

### Exam or practical application

When a question asks which option helps **estimate future Azure use**, choose the pricing calculator. When it asks how to **analyze spending, track trends, or set threshold notifications**, think Microsoft Cost Management. When the goal is to **classify resources or group supported cost information**, think tags. If the scenario says spending must stop at a precise cap, do not assume a budget alert is an enforcement mechanism; distinguish an alert from an action that actually changes or stops a workload.

For a practical review, state the estimate's region, product configuration, quantity, runtime, and purchase assumptions. Identify the billing scope and period when reading actual costs.

### Self-check questions

1. **A project wants a predeployment estimate for a planned set of Azure services. Which tool should it start with?**  
   **Answer:** The Azure pricing calculator. It models expected products and usage; it does not deploy them or guarantee the final bill.

2. **Name three factors that can change an Azure cost.**  
   **Answer:** Any three of service type/tier or size, quantity, runtime, usage volume, region, data transfer, storage, or applicable discounts and purchase terms.

3. **Will a Cost Management budget alert automatically stop the resources when a threshold is reached?**  
   **Answer:** No. A budget can trigger notifications or configured alert actions, but a budget is not by itself a resource shutoff or guaranteed spending cap.

4. **What is a tag, and what is one important limitation?**  
   **Answer:** A tag is key-value metadata used to classify resources and, in supported reports, organize costs. It does not automatically inherit from a parent resource group or subscription, and sensitive data should not be stored in it.

5. **Why might a Cost Analysis amount differ from a final invoice?**  
   **Answer:** Cost data and invoice processing serve different purposes and can differ in timing, scope, credits, taxes, purchases, and other billing adjustments. Check the relevant billing artifacts for invoice reconciliation.

### Sources

- [Describe Cost Management in Azure — AZ-900 Learn module](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/)
- [Overview of Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management)
- [Estimate costs with the Azure pricing calculator](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator)
- [Use tags to organize Azure resources and management hierarchy](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources)
- [Cost Management budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- [Cost analysis in Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)

## Governance and compliance

### Learning intent

Distinguish the role of Microsoft Purview in data governance, protection, and compliance from the role of Azure Policy in applying resource-governance rules, and from resource locks that protect against accidental control-plane changes. Learn to match each tool to the problem it solves, and understand why none of these tools replaces identity permissions or an organization's broader compliance program.

### Core concepts

**Microsoft Purview (`mg-purview`).** Microsoft Purview is a suite of integrated solutions that helps an organization govern, protect, and manage data across its data estate. Its broad capabilities include data governance, data security, and data compliance. Depending on the solution and configuration, Purview can help organizations gain visibility into data, manage sensitive information, address regulatory requirements, and apply data-protection practices. Examples of the product areas include Data Map and Unified Catalog for data governance, and compliance and information-protection solutions for data compliance and security.

Think of Purview in terms of **data**: understanding data assets, managing sensitive information and its lifecycle, and supporting governance and compliance processes. It does not mean every Azure resource has been configured securely, nor does it automatically make an organization compliant with a law or standard. Purview capabilities and licensing vary by solution. It is distinct from Azure Policy, which evaluates and governs Azure resources and requests against assigned policy rules.

Purview has evolved from older Azure Purview descriptions. Verify the current solution, supported data sources, and licensing for a specific catalog, security, or compliance need.

**Azure Policy (`mg-policy`).** Azure Policy helps enforce organizational standards and assess compliance at scale. A policy definition describes a rule, such as allowing deployments only in approved regions or requiring a tag. An administrator assigns the definition—or a group of definitions called an initiative—to a scope, such as a management group, subscription, resource group, or resource. A higher-level assignment can cover resources below it; exclusions and exemptions can be used when authorized and appropriate.

Policy rules use effects to determine the response to evaluation. Depending on the definition, a policy can audit a resource, deny a noncompliant create or update, modify a request, deploy related configuration, or support remediation of existing resources. The compliance view reports evaluation results and helps identify noncompliant resources. Some policies only report; they do not automatically repair every existing resource. Remediation behavior and permissions depend on the policy effect, assignment, and resource provider.

Policy is a way to govern **what resources are deployed or how they are configured**, and in some cases to evaluate or restrict actions in a request. It is not the same as granting a user permission to perform operations. Use Azure RBAC to manage access by assigning roles to identities at scopes. A user can have permission to make a request that Azure Policy then denies because the request conflicts with an assigned rule.

**Resource locks (`mg-locks`).** A management lock helps protect a subscription, resource group, or resource from accidental deletion or modification. The two common lock types are **CanNotDelete** (shown in the portal as **Delete**) and **ReadOnly** (shown in the portal as **Read-only**). A CanNotDelete lock allows authorized users to read and modify a resource but prevents deletion. A ReadOnly lock permits reads but blocks updates and deletes through the control plane.

A lock adds a restriction regardless of RBAC permissions; it grants no access. Parent locks are inherited, including by later resources, and the most restrictive applicable lock governs. Remove a lock before a blocked operation. Since ReadOnly locks can disrupt routine management calls, use them carefully.

### How it works, distinctions, limits, and defaults

The following comparison is useful when multiple governance controls sound similar. They can coexist; the best answer depends on whether the problem is access, standards, protection against accidental changes, or data oversight.

| Capability | Primary purpose | Typical question | Scope or target | Important boundary |
| --- | --- | --- | --- | --- |
| Azure RBAC | Grant permissions to an identity through role assignments | Who may perform this operation? | Azure management scopes and supported data-plane scopes | Permission can be constrained by scope and role, but it does not itself define the organization's desired configuration. |
| Azure Policy | Evaluate and enforce resource-governance rules | Is this resource or request compliant with our standards? | Policy-supported management scopes and resources | An audit policy reports rather than blocks; effects and remediation vary by definition. |
| Resource locks | Prevent accidental control-plane deletion or modification | How can we guard this resource against a mistaken management operation? | Subscription, resource group, or resource | A lock does not grant access or protect every operation on the data inside a service. |
| Microsoft Purview | Govern, protect, and manage data; support compliance processes | What data do we have, how is it classified or protected, and how do we manage data risk? | Data estate and Purview-supported solutions | Capabilities, data sources, and licensing vary; it is not a blanket Azure-resource configuration policy. |

Locks are not backups or data-plane access controls. They apply to control-plane operations, so a lock on a storage account does not necessarily prevent a data-plane user from deleting a blob. ReadOnly locks can also block management operations that use write-style API calls. Check service-specific effects before applying locks broadly.

Policy evaluates resources on relevant lifecycle and assignment events and periodically, so compliance is not always instantaneous. Existing resources might need a separate remediation task and suitable permissions; inspect the policy effect rather than assuming assignment fixes them.

> **Verify:** Microsoft Purview solutions, supported data sources, licensing, and portal names change over time. Similarly, Azure Policy effects and resource lock behavior can differ by resource provider and operation. Check the current service documentation before treating a rule or lock as a complete compliance or data-protection control.

### Example or worked scenario

A company requires production resources in approved regions, cost-center tags, deletion protection for a critical network resource, and governance for sensitive data.

An administrator assigns policies for allowed locations and required tags, then reviews compliance and remediates existing resources where supported. RBAC still determines who can create or modify resources. A CanNotDelete lock adds deletion protection to the critical network resource and is removed through a controlled process when needed. The data team evaluates Microsoft Purview for supported data assets; it does not replace resource policies or locks.

### Hands-on activity

Use a lab subscription or read-only browsing. Do not assign a deny policy or apply a lock to a shared or production resource.

1. In the portal, inspect built-in Azure Policy definitions for allowed locations or required tags. Read the effect and distinguish a definition, assignment, and initiative.
2. On a disposable lab resource, inspect the **CanNotDelete** and **ReadOnly** locks and their scope. Do not apply a lock to shared infrastructure.
3. Review the current Microsoft Purview overview and identify its data-governance, data-security, and data-compliance solution areas; confirm tenant availability before planning deployment.

### Exam or practical application

Choose **Azure Policy** when the requirement is to assess or enforce standards such as allowed regions, required tags, or configuration rules across a scope. Choose **RBAC** when the question is about which identity can perform an operation. Choose a **resource lock** when the requirement is protection from accidental control-plane deletion or modification, particularly when even an authorized role holder should encounter an extra barrier. Choose **Microsoft Purview** when the focus is governing, discovering, protecting, or managing data and related compliance processes.

Avoid confusing “compliant” with “secure in every respect.” A policy compliance result is evidence about specified rules; a lock protects a defined set of management operations; Purview supports data governance and protection; RBAC controls access. Real governance uses these controls in combination with monitoring, data protection, process, and human review.

### Self-check questions

1. **Which service is designed to apply a required-tag or allowed-region rule across a resource scope?**  
   **Answer:** Azure Policy. An assignment evaluates resources at its scope and applies the effect defined by the policy.

2. **A developer has Contributor access, but a resource has a CanNotDelete lock. Can the developer delete it through a normal Azure management operation?**  
   **Answer:** No. The lock adds a deletion restriction that applies even to users whose RBAC role would otherwise permit deletion. An authorized administrator must remove the lock first.

3. **What is the difference between Azure Policy and RBAC?**  
   **Answer:** RBAC grants or limits what an identity can do. Policy evaluates or governs whether a resource or request conforms to assigned standards. A permitted RBAC action can still be denied by policy.

4. **Does a lock on a storage account guarantee that no one can delete data in that account?**  
   **Answer:** No. Locks apply to control-plane management operations and do not generally block data-plane operations against stored data. Use appropriate data-plane access controls and protection mechanisms too.

5. **What is Microsoft Purview primarily for in this comparison?**  
   **Answer:** It provides integrated solutions for governing, protecting, and managing data and supporting data compliance. It is not a substitute for Azure Policy's resource rules or RBAC permissions.

### Sources

- [Learn about Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview)
- [Overview of Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
- [Lock your Azure resources to protect your infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)
- [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

## Managing and deploying resources

### Learning intent

Understand that Azure resources can be managed through a shared Azure Resource Manager layer using the portal, command-line tools, APIs, and templates. Distinguish the Azure portal from Azure CLI and Azure PowerShell, and distinguish those tools from Cloud Shell, which supplies a browser-accessible command environment. Learn what Azure Arc adds for hybrid and multicloud management, what infrastructure as code means, and how ARM templates and Bicep support repeatable deployments.

### Core concepts

**Azure portal (`mg-portal`).** The Azure portal is a browser-based graphical interface for creating and managing Azure resources. It provides service blades, dashboards, search, resource views, and access to management features. It is useful for discovery, visual inspection, and one-off changes, especially while learning a service. Portal actions are requests to Azure management services; using a graphical interface does not make an action inherently safer or exempt it from access controls, policies, locks, or costs.

The portal is one management option, not a separate deployment engine. The same Resource Manager capabilities are also exposed through Azure CLI, Azure PowerShell, REST APIs, and SDKs. An administrator can choose the interface that fits a task, then use role assignments and governance rules to control what happens.

**Cloud Shell, Azure CLI, and Azure PowerShell (`mg-shell-cli-powershell`).** Azure CLI and Azure PowerShell are command-line management tools. The Azure CLI uses commands beginning with `az`, such as `az group list`; it is cross-platform and can be used interactively or in scripts. Azure PowerShell is the collection of Microsoft PowerShell modules for Azure; the current recommended module is **Az**, with cmdlets such as `Get-AzResourceGroup`. PowerShell cmdlets commonly return structured .NET objects that can be piped into other PowerShell commands. The CLI commonly formats output as JSON by default and supports other output formats.

Azure Cloud Shell is an authenticated, browser-accessible terminal available in the Azure portal and at shell.azure.com. It offers a Bash or PowerShell experience and comes with common Azure command-line tools. It is an **environment**, not a third command language: choose Bash or PowerShell and run Azure CLI or Az PowerShell commands in that shell. Cloud Shell is hosted and maintained by Microsoft, so it can be convenient when you do not want to install tools locally. Cloud Shell uses persistent file storage for the user's files and also runs on a temporary host; the service documentation describes session timeout and storage requirements. The hosting machine is free to use, but the required storage account can incur ordinary storage charges.

| Choice | What it is | Typical fit | Key distinction |
| --- | --- | --- | --- |
| Azure portal | Browser-based graphical management interface | Explore resources, review configuration, perform guided tasks | A GUI that sends management requests; not the only way to manage Azure. |
| Azure CLI | Cross-platform command-line tool with `az` commands | Shell scripts, interactive administration, cross-platform automation | Commands commonly present results as JSON and can be composed in a shell. |
| Azure PowerShell | Azure's PowerShell modules and cmdlets, currently the Az module | PowerShell automation and object-based pipelines | Uses PowerShell cmdlets and objects; legacy AzureRM examples are not the current module. |
| Azure Cloud Shell | Hosted browser shell environment with Bash or PowerShell | Run CLI or PowerShell without local installation | An environment for tools, not a replacement name for CLI or PowerShell. |

**Azure Arc (`mg-arc`).** Azure Arc extends Azure management and governance capabilities to supported resources outside Azure, including eligible servers, Kubernetes clusters, databases, and virtualized environments. Arc represents supported non-Azure resources in Azure Resource Manager so that teams can use a familiar Azure management experience and selected Azure services across on-premises, edge, and other cloud environments. The exact management operations depend on the Arc-enabled resource type and its configuration.

Arc does not move an on-premises server into Azure or make every Azure service work identically everywhere. Onboarding, agents or extensions, network connectivity, and service prerequisites depend on resource type. Arc's control-plane representation does not change compute location, and attached Azure services can incur their own charges.

**Infrastructure as code (`mg-iac`).** Infrastructure as code (IaC) means defining infrastructure in machine-readable files and managing those definitions as code, commonly using source control, review, and automated deployment. Rather than repeat a sequence of manual actions, a team describes the intended resources and configuration, then uses tooling to deploy them. IaC helps with consistency, reuse, review, change history, and recreating environments. It does not remove the need for permissions, testing, secrets management, or careful review of planned changes.

IaC may be declarative or imperative; ARM templates and Bicep are declarative Azure options. Versioned files can be parameterized and reused across environments. Review changes before deployment, especially possible deletions, replacements, or exposure.

**Azure Resource Manager and ARM templates (`mg-arm`).** Azure Resource Manager (ARM) is Azure's deployment and management service. Requests from the portal, command-line tools, APIs, and SDKs pass through the management layer, which authenticates and authorizes requests before forwarding them to resource providers. ARM provides consistent management capabilities such as deployment, access control, tags, and locks. Azure's management scopes include management groups, subscriptions, resource groups, and resources; scope affects how broadly settings and deployments apply.

An **ARM template** is a JSON file that declares the Azure resources and properties to deploy. Templates can describe one resource or a larger solution, including dependencies, parameters, and outputs. Resource Manager orchestrates deployment ordering for dependent resources. A template can be deployed repeatedly to help keep environments consistent. ARM deployments can also be used at different scopes when supported by the template and deployment operation.

**Bicep** is a domain-specific declarative language for Azure resources. It offers a more concise authoring syntax than raw ARM template JSON while targeting the same Azure Resource Manager deployment platform. Bicep files are converted to ARM templates during deployment, so Bicep is not a different control plane. When comparing ARM and Bicep, compare authoring format and workflow, not whether they can deploy Azure resources.

### How it works, distinctions, limits, and defaults

Management interfaces and infrastructure definitions are complementary. The portal is convenient for exploration and guided tasks. CLI and PowerShell make commands repeatable and scriptable. Cloud Shell provides a browser-hosted place to run command-line tools. IaC files record intended infrastructure and can be reviewed or used in automation. All ultimately operate subject to identity, scope, policy, locks, provider support, and service-specific configuration.

| Dimension | ARM template | Bicep |
| --- | --- | --- |
| Authoring format | JSON | Azure-focused declarative language with a more concise syntax |
| Deployment destination | Azure Resource Manager | Azure Resource Manager; Bicep is compiled to an ARM template during deployment |
| Desired use | Declare resources and configuration for repeatable deployment | Declare resources and configuration with simpler authoring and type-aware tooling |
| Relationship | Native template format used by the deployment platform | Alternative authoring experience for ARM deployments, not a separate Azure management service |

A declarative template specifies target configuration, and ARM orchestrates represented dependencies. Repeatability does not guarantee success: provider behavior, API versions, permissions, current state, and external dependencies matter. Review changes and use ARM **what-if** when appropriate.

Cloud Shell's persistence depends on its configured storage, even though its host is temporary. Cloud Shell may be subject to inactivity timeout, and local installation may be more suitable for durable development, offline work, specialized extensions, or local automation. The shell choice also matters: Bash syntax and PowerShell syntax differ, even when the Azure operation is conceptually the same. Avoid copying commands between environments without checking quoting, variables, and pipeline behavior.

> **Verify:** Cloud Shell session behavior, storage prerequisites, installed tool versions, Azure CLI and Az module versions, ARM API versions, and Azure Arc resource capabilities can change. Use live documentation and check the selected subscription and tenant before running commands that create, modify, or delete resources.

### Example or worked scenario

A company wants a consistent development environment in two subscriptions and visibility into an on-premises Linux server. An engineer explores the portal, writes Bicep, reviews it in source control, previews changes, and deploys after checking subscription and scope.

An engineer uses Cloud Shell Bash and Azure CLI for investigation; another uses Az cmdlets in automation. The on-premises server is connected through Azure Arc but remains on-premises. Any attached monitoring or security service is assessed separately for prerequisites and cost.

### Hands-on activity

This activity uses read-only commands until the optional template preview. Confirm the active tenant and subscription; do not run deployment commands in a production scope.

1. In the portal, inspect an authorized resource group's subscription and location.
2. In Cloud Shell Bash, run `az account show --output table` and `az group list --output table` to check context and list visible groups. In PowerShell, compare `Get-AzContext` and `Get-AzResourceGroup`.
3. Read a small ARM template or Bicep sample and identify a resource, name, location, and configuration. Use `what-if` only in a lab after verifying the deployment context.
4. From Azure Arc documentation, identify a supported non-Azure resource and its onboarding prerequisites.

### Exam or practical application

If the question asks for a **browser GUI**, think Azure portal. If it asks for **commands or scripts**, Azure CLI or Azure PowerShell are both management tools; determine which syntax and shell the scenario specifies. If it asks for **a browser terminal with Bash or PowerShell and preinstalled tools**, think Cloud Shell. If it describes **governing or managing supported servers or clusters outside Azure through Azure**, think Azure Arc.

If the requirement is to create consistent environments from source-controlled definitions, think IaC. ARM templates are JSON declarations, while Bicep offers a more concise language that deploys through ARM. ARM itself is the management and deployment service, not merely the JSON template file. Make sure you distinguish the platform, a template format, the command-line tool, and the environment in which a tool runs.

### Self-check questions

1. **Is Azure Cloud Shell another command language like Azure CLI, or an environment for running tools?**  
   **Answer:** It is an environment. It offers Bash or PowerShell and can run tools such as Azure CLI or Azure PowerShell.

2. **What is one distinction between Azure CLI and Azure PowerShell?**  
   **Answer:** CLI uses `az` commands and commonly produces JSON output; Azure PowerShell uses Az cmdlets and structured PowerShell/.NET objects. Both can manage Azure resources.

3. **Does Azure Arc move an on-premises server into an Azure datacenter?**  
   **Answer:** No. Arc can project supported non-Azure resources into Azure Resource Manager for selected management capabilities; the workload remains where it is hosted.

4. **How do ARM templates and Bicep relate?**  
   **Answer:** Both are declarative IaC approaches for Azure Resource Manager. ARM templates use JSON; Bicep provides a more concise authoring language that is converted to an ARM template for deployment.

5. **What should you check before running a deployment command?**  
   **Answer:** Confirm the tenant, subscription, scope, permissions, template contents, and proposed changes. Use an appropriate preview such as what-if when available, and avoid unreviewed deployments to production.

### Sources

- [What is Azure Resource Manager?](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- [What is Azure Cloud Shell?](https://learn.microsoft.com/en-us/azure/cloud-shell/overview)
- [What is the Azure CLI?](https://learn.microsoft.com/en-us/cli/azure/what-is-azure-cli)
- [What is Azure PowerShell?](https://learn.microsoft.com/en-us/powershell/azure/what-is-azure-powershell)
- [Azure Arc overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)
- [Infrastructure as code with Azure Resource Manager templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)
- [What is Bicep?](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)
- [ARM template what-if operation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-what-if)

## Monitoring and advice

### Learning intent

Identify which Azure service helps answer a health, reliability, cost, performance, or application-diagnostics question. Distinguish Azure Advisor's recommendations from Azure Service Health's notices about Azure service issues and planned maintenance, Azure Monitor's telemetry-and-alerting platform, and Application Insights' application performance monitoring capabilities. Learn to choose signals and tools based on whether you are planning, investigating, or responding.

### Core concepts

**Azure Advisor (`mg-advisor`).** Azure Advisor analyzes resource configuration and usage telemetry to provide recommendations intended to help optimize Azure deployments. Recommendations are organized into areas such as cost, reliability, performance, security, and operational excellence. A recommendation identifies an opportunity and may suggest an action; Advisor does not automatically mean the action is safe for every workload or that implementing it is mandatory. Review context, dependencies, impact, and organizational requirements before applying a recommendation. Advisor is useful for proactive improvement—for example, spotting a cost-saving opportunity or a configuration that may affect reliability.

Advisor is not the same as monitoring an active incident. Its recommendations are generally optimization guidance based on available analysis. It does not replace resource telemetry, service incident notices, or an organization's operational review. Recommendations may take time to reflect a change after a team acts, and supported resource types vary.

**Azure Service Health (`mg-service-health`).** Azure Service Health gives personalized information about Azure service issues, planned maintenance, and health advisories that may affect the Azure services and regions an organization uses. It is intended to help Azure customers understand relevant events and configure alerts for issues or changes that matter to their subscriptions. This is different from a general global status page: a global status view is broad, while Service Health is tailored to the services, regions, and subscriptions relevant to the customer.

Microsoft's health experiences include related but distinct components. **Azure Status** presents global Azure service status. **Service Health** provides a personalized view of service-impacting communications and planned maintenance. **Resource Health** focuses on the health of an individual Azure resource, such as a particular virtual machine. Together, these views help answer different levels of “Is Azure healthy?” and “Is my resource affected?” questions.

**Azure Monitor (`mg-azure-monitor`).** Azure Monitor collects, analyzes, and acts on cloud and hybrid telemetry. Metrics are numerical measurements useful for trends and alerts; logs provide records and context; traces follow activity across components; events capture significant occurrences. Available signals depend on the source.

Azure Monitor includes tools to visualize and investigate collected data and to create alerts that notify people or trigger configured actions when conditions are met. An alert rule evaluates a signal or query and can create an alert instance when its condition is satisfied. Notification or action behavior depends on the configured action group and permissions. Monitoring is most effective when the team chooses useful signals, thresholds, scope, and response procedures rather than collecting data without a question to answer.

Log Analytics is an Azure Monitor experience for querying log and trace data in Log Analytics workspaces with Kusto Query Language (KQL). Azure Monitor also uses Azure Monitor workspaces for Prometheus and OpenTelemetry metrics, analyzed using Prometheus Query Language (PromQL). These are distinct workspace types and data stores. Do not assume that all telemetry uses the same workspace or query language. Azure Monitor provides the broad monitoring platform; Log Analytics is one component used to work with log data.

**Application Insights (`mg-app-insights`).** Azure Monitor Application Insights is an application performance monitoring feature of Azure Monitor. It helps developers and operators collect and analyze telemetry from applications so they can investigate availability, failures, performance bottlenecks, and behavior. Application Insights experiences include views such as application maps, live metrics, search, availability, failures, and performance. For supported scenarios, applications can use OpenTelemetry (OTel), a vendor-neutral observability framework, to instrument code and send telemetry for analysis. Setup depends on the language, hosting model, and supported instrumentation approach.

Application Insights is application-focused, while Azure Monitor covers a broader range of infrastructure, platform, and application telemetry. They are not competing choices: Application Insights is a capability in the Azure Monitor ecosystem. Monitoring data may contain sensitive information; instrumentation and data collection should follow applicable privacy, security, retention, and access requirements.

### How it works, distinctions, limits, and defaults

Use the following guide to choose a tool. Some products overlap in the portal, but each starts from a different operational question.

| Service or view | Main focus | Example question | Typical use |
| --- | --- | --- | --- |
| Azure Advisor | Best-practice recommendations for optimization | What changes might improve cost, reliability, performance, security, or operations? | Review recommendations and decide which actions fit. |
| Azure Status | Broad public view of Azure service status | Is there a widely reported Azure issue? | Check global status context; it may not show customer-specific impact. |
| Azure Service Health | Personalized Azure service issues, maintenance, and advisories | Is a service event or planned maintenance relevant to my subscriptions and regions? | Review targeted communications and configure alerts. |
| Resource Health | Health of a particular Azure resource | Is this specific VM or resource available, and what may have affected it? | Investigate individual resource availability. |
| Azure Monitor | Telemetry collection, analysis, visualization, and alerts | What does the measured behavior of my systems show, and should I be notified? | Monitor metrics, logs, traces, and events across supported sources. |
| Application Insights | Application performance and runtime behavior | Where are application failures or latency occurring? | Diagnose application availability, failures, transactions, and performance. |

These tools complement one another. For example, correlate an Advisor resize recommendation with Azure Monitor metrics, a Service Health maintenance notice, and the Resource Health state of an affected resource.

Azure Monitor is not automatically comprehensive: teams may need to enable diagnostic settings, instrumentation, destinations, and alert rules. Alerts depend on configured criteria and action groups; missing alerts do not prove there was no issue. Data can be delayed, sampled, or incomplete, so choose a suitable time range and query.

Application Insights requires instrumentation or a supported automatic collection path and a configured resource. OTel support varies by language and scenario. Avoid sending secrets or sensitive personal data; use appropriate data minimization and access controls.

> **Verify:** Monitoring capabilities, supported resource types, health views, instrumentation recommendations, data retention and ingestion behavior, and portal terminology can change. Validate current documentation for the language, service, region, and plan being used. Azure Monitor workspaces and Log Analytics workspaces are different workspace types; confirm which one is required by the data source.

### Example or worked scenario

A web application slows down. The on-call engineer checks Service Health for relevant incidents or maintenance, Resource Health for affected resources, and Azure Monitor metrics, logs, and alerts for evidence during the incident.

The developer uses Application Insights to investigate requests, failures, and dependencies, correlating telemetry with infrastructure evidence. After stabilization, the team reviews Advisor recommendations for longer-term improvements and assesses whether they fit the architecture.

### Hands-on activity

Use an existing demo or lab subscription. Do not create costly resources or send sensitive application data to a monitoring service.

1. In the portal, inspect Advisor recommendations for an authorized subscription and note why each should be evaluated before action.
2. Compare personalized Service Health notices with Azure Status, then open a resource's Resource Health view if available.
3. In Azure Monitor, locate metrics, logs, and alert rules. In a demo Application Insights resource, inspect availability, failures, or performance and identify the telemetry source.
4. Write an operational question and specify the signal, time range, view, and alert that could answer it.

### Exam or practical application

Match the noun in the requirement to the right tool. **Advice or optimization recommendations** points to Azure Advisor. **Azure outages, planned maintenance, or service-impacting notices personalized to a subscription** points to Azure Service Health. **A single resource's health** points to Resource Health. **Metrics, logs, alerts, and broad telemetry analysis** points to Azure Monitor. **Application requests, performance, availability tests, failures, and dependency diagnostics** points to Application Insights.

A common practical mistake is to use a recommendation service as an incident dashboard or to expect service-health notices to reveal application code-level latency. Start with the source that matches the question, then correlate sources. For example, combine a Service Health event with Monitor metrics and Application Insights request traces to understand both platform context and the user's application impact.

### Self-check questions

1. **Which Azure service provides recommendations for cost, reliability, performance, security, and operational excellence?**  
   **Answer:** Azure Advisor. Review its recommendations and decide whether they are appropriate before applying them.

2. **Which view is tailored to Azure service issues and maintenance that may affect the services and regions a subscription uses?**  
   **Answer:** Azure Service Health. Azure Status is the broad public view; Resource Health focuses on an individual resource.

3. **What is the difference between Azure Monitor and Application Insights?**  
   **Answer:** Azure Monitor is the broader telemetry and observability service. Application Insights is an application performance monitoring feature within Azure Monitor.

4. **Which data is typically queried with KQL in a Log Analytics workspace?**  
   **Answer:** Log and trace data collected in that workspace. Azure Monitor also has a distinct workspace type for Prometheus and OpenTelemetry metrics, which uses PromQL.

5. **Does the absence of an Azure Monitor alert prove that an application is healthy?**  
   **Answer:** No. An alert only fires when configured conditions and data sources detect its criteria. Missing instrumentation, incomplete signals, unsuitable thresholds, or configuration issues can all leave problems unalerted.

### Sources

- [Describe monitoring tools in Azure — AZ-900 Learn module](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/)
- [Introduction to Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview)
- [What is Azure Service Health?](https://learn.microsoft.com/en-us/azure/service-health/overview)
- [Azure Status overview](https://learn.microsoft.com/en-us/azure/service-health/azure-status-overview)
- [Resource Health overview](https://learn.microsoft.com/en-us/azure/service-health/resource-health-overview)
- [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/overview)
- [Log Analytics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)
- [Application Insights OpenTelemetry observability overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
- [Azure Monitor alerts overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
