# Identities and governance (20–25%)

Azure administration begins with two questions: **who is acting, and which resources may they change?** Governance adds the rules that keep those changes within an organization's boundaries. These capabilities operate at different layers: Microsoft Entra ID holds directory identities, Azure role-based access control (Azure RBAC) authorizes actions on Azure resources, and Azure Policy evaluates resource configuration against rules.

## Microsoft Entra users and groups

### Learning intent

Create and manage directory users and groups, understand licenses and external identities, and configure self-service password reset (SSPR) with the required prerequisites.

### Core concepts

A **user** is a directory identity. User properties such as display name, sign-in name, account state, and assigned directory roles have different purposes; changing a profile property does not by itself grant access to an Azure subscription. A **group** collects identities so membership and access can be managed consistently. Security groups are commonly used for access control; Microsoft 365 groups also support collaboration workloads. Membership can be assigned by an administrator or, where supported and licensed, evaluated dynamically from user attributes.

Product licenses enable particular capabilities; they are not Azure resource permissions. Assign a license to the intended users or groups, and verify the current service-plan and licensing requirements before enabling a feature. An **external user** is an identity from outside the organization's workforce directory that is invited or otherwise brought into collaboration. External collaboration settings and resource authorization are separate controls: invitation does not automatically grant access to every resource.

**SSPR** lets eligible users reset their own password after the organization configures the feature, registration and authentication methods, and applicable scope. It is not a substitute for administrator recovery procedures or strong authentication. Requirements vary with directory configuration and licensing.

### How it works, distinctions, limits, and defaults

Treat the directory and the Azure resource hierarchy as related but distinct systems. A user can exist in Entra ID without being assigned an Azure role. Group-based administration can reduce repeated assignments, but membership lifecycle and nested-group behavior must be checked for the consuming service. Minimize standing privileged access and review group owners and members.

### Example or worked scenario

A company hires 30 contractors for a migration. An administrator provisions named identities, places them in a contractor security group, grants that group a narrowly scoped role on the migration resource group, and configures the approved sign-in and external-collaboration requirements. The identity lifecycle team sets an end date and removes membership when the contract ends. The group assignment is easier to review than 30 independent resource grants.

### Hands-on activity

In a test tenant, create a nonprivileged test user and security group, inspect their properties and membership, then assign and remove a test license if available. Review the Entra external collaboration and SSPR configuration pages without changing production settings. Record which steps concern identity, licensing, or resource authorization.

### Exam or practical application

When a scenario asks who can sign in, look at identity and authentication configuration. When it asks whether a person can manage a resource, inspect Azure RBAC assignments. A guest invitation, group membership, license, and role assignment solve different problems.

### Self-check questions

1. Does adding a user to the Entra directory grant Contributor access to a subscription?

   **Answer:** No. An Azure role assignment at an applicable scope is needed.

2. What is the administrative benefit of assigning a role to a group?

   **Answer:** Permissions can be granted once and then managed through group membership, making access review and lifecycle changes more consistent.

3. Does inviting an external user automatically authorize that user to manage Azure resources?

   **Answer:** No. External identity access and Azure resource authorization are separate.

### Sources

- [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity/)
- [Create or delete users in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users)
- [Manage groups in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups)
- [Assign or unassign licenses for users in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users)
- [What is Microsoft Entra External ID?](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview)
- [Self-service password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks)

## Access to Azure resources with RBAC

### Learning intent

Select appropriate built-in roles, assign them at a suitable scope, and interpret effective role assignments without confusing directory roles with Azure resource roles.

### Core concepts

An Azure RBAC role definition is a set of allowed actions. A **role assignment** connects a security principal (user, group, service principal, or managed identity) to a role at a **scope**. The main scopes form an inheritance hierarchy: management group, subscription, resource group, and individual resource. An assignment at a parent scope normally applies to descendants unless the role definition or assignment conditions constrain it.

Built-in roles represent common permission sets. **Owner** can manage resources and access; **Contributor** can manage resources but cannot grant access; **Reader** can view resources. Service-specific roles, such as Storage Blob Data Reader, target particular data-plane operations. These names are useful orientation, not a reason to grant broad access. Choose the least-privileged role that permits the required task, and check its current actions and data actions in the role definition.

### How it works, distinctions, limits, and defaults

Azure management-plane permissions control operations on resource configuration; data-plane permissions control operations on data stored in a service. A management role does not necessarily imply data access. Effective authorization can be affected by inherited assignments, deny assignments, conditions, resource-specific behavior, and directory or service configuration. A role assignment is therefore not always the whole access story.

Scope is a security boundary and an operational choice. Subscription scope is convenient for cross-resource work but grants broad reach; a resource or resource-group scope limits blast radius. Role assignments can take time to propagate. Removing an assignment may not immediately terminate existing sessions or cached credentials.

### Example or worked scenario

A support engineer must restart one virtual machine but must not change its network or grant access. First check whether an appropriate built-in VM operator role supplies the necessary actions. Assign it to a support group at the VM or tightly scoped resource-group level, then test the permitted operation and verify that unrelated actions remain denied.

### Hands-on activity

In a disposable resource group, inspect **Access control (IAM)** and list role assignments inherited from the subscription and management group. Compare Reader and Contributor role definitions. If a test identity is available, assign the narrowest suitable role, verify an allowed action, then remove the assignment.

### Exam or practical application

Read a scenario as a tuple: **principal + required operation + target + duration**. Match the operation to a role, then choose the lowest scope that includes the target resources. Do not mistake an Entra directory role for an Azure RBAC role.

### Self-check questions

1. Which common role allows resource management but not the ability to grant other users access: Owner or Contributor?

   **Answer:** Contributor.

2. If a user has Reader on a subscription, does assigning Contributor on one resource group remove the inherited Reader access elsewhere?

   **Answer:** No. The resource-group assignment adds permissions within its scope; the inherited subscription assignment still applies.

3. Why might a management-plane role not allow reading a blob's contents?

   **Answer:** Blob reads are data-plane operations and may require a data role or another service-specific authorization path.

### Sources

- [What is Azure role-based access control (Azure RBAC)?](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
- [Understand scope for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview)
- [Built-in Azure roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)
- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
- [Azure RBAC and Azure attribute-based access control (ABAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-overview)

## Subscriptions, governance, and cost control

### Learning intent

Organize resources and subscriptions, apply governance consistently with policy and locks, use tags thoughtfully, and use budgets, alerts, and Azure Advisor to manage costs.

### Core concepts

A **resource group** is a management container for resources that are commonly deployed, updated, and retired together. A resource belongs to one resource group at a time, and the group has a location for its metadata; contained resources can be in other regions. **Subscriptions** provide an administrative and billing boundary for Azure resources. **Management groups** let administrators organize subscriptions and apply governance across them. Together these scopes form a hierarchy; a policy or role assignment at a parent scope can affect descendants.

**Azure Policy** evaluates resources against definitions and assignments. Depending on its effect, a policy can audit, deny, append or modify configuration, or deploy related configuration when remediation is appropriate. An audit result reports noncompliance; it does not automatically correct a resource. Remediation tasks and permissions may be required for effects that modify existing resources. **Resource locks** provide an additional guard against deletion or changes: a Delete lock blocks deletion while allowing updates; a ReadOnly lock blocks writes. Locks do not replace access control and must be managed deliberately.

**Tags** are name/value metadata useful for ownership, environment, cost allocation, and automation. Tags do not automatically inherit from a resource group or subscription to its resources; policy can enforce or add tags. Cost Management supports analysis, budgets, and alerts. A budget is a monitoring and notification mechanism, not a hard spending cap. **Azure Advisor** provides recommendations across areas such as cost, reliability, security, operational excellence, and performance; recommendations need validation against the workload.

### How it works, distinctions, limits, and defaults

Use resource groups for lifecycle and administration, subscriptions for boundaries such as billing or environment separation, and management groups for cross-subscription governance. Moving resources between scopes can have service-specific restrictions and can affect dependencies or role assignments; inspect move guidance before proceeding.

Policy and locks answer different questions. Policy evaluates whether configuration meets a rule; a lock restricts certain management operations. Neither makes a poor role assignment safe. Cost alerts signal a threshold or forecast; they should be paired with owners, review cadence, and response actions.

### Example or worked scenario

A team operates development and production subscriptions. A management-group policy audits required cost-center tags, while production receives stricter location and SKU rules. Resource groups follow application lifecycles. Budgets alert each owner before expected monthly spend is exceeded; they do not stop deployment, so the team also reviews forecasts and Advisor recommendations.

### Hands-on activity

In a sandbox, create a resource group with an owner/environment tag, inspect policy compliance, and compare Delete and ReadOnly locks on a disposable resource. If the subscription allows it, create a low-value budget alert with a test contact. Remove temporary resources and review current costs before leaving the sandbox.

### Exam or practical application

For a governance scenario, identify the scope where a rule should apply and whether the requirement is to report, deny, modify, or protect. For a cost question, distinguish a budget alert from a spending limit, and treat Advisor as a recommendation source rather than an enforcement engine.

### Self-check questions

1. Will a tag on a resource group automatically appear on every resource in that group?

   **Answer:** No. Use policy or another management process to apply or maintain tags on resources.

2. Which control is designed to report resources that violate a configuration rule: Azure Policy or a resource lock?

   **Answer:** Azure Policy. A lock restricts certain management operations.

3. Does reaching an Azure budget automatically prevent further charges?

   **Answer:** No. Budgets provide monitoring and alerts; they do not hard-cap consumption.

### Sources

- [Azure resource manager overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- [Management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)
- [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
- [Remediate noncompliant resources with Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)
- [Lock your Azure resources to protect your infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)
- [Use tags to organize your Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources)
- [Create and manage budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview)
