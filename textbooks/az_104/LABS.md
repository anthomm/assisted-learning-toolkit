# AZ-104 labs and hands-on resources

Link-checked 2026-11-01 (all returned HTTP 200). These are official Microsoft resources, linked rather than copied. Labs run in your own Azure subscription and can create billable resources: use a disposable or sandbox subscription and delete resources when you finish.

| Resource | Type | Link | Own subscription | Chapter / topic | Outcome IDs |
|---|---|---|---|---|---|
| Lab 01 – Manage Microsoft Entra ID identities | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_01-Manage_Entra_ID_Identities.html) | yes | 1 › Microsoft Entra users and groups | `entra-create-users-groups`, `entra-manage-properties` |
| Lab 02a – Manage subscriptions and RBAC | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_02a_Manage_Subscriptions_and_RBAC_Entra.html) | yes | 1 › RBAC; subscriptions and governance | `rbac-built-in-roles`, `rbac-scope-assignments`, `gov-management-groups` |
| Lab 02b – Manage governance via Azure Policy | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_02b-Manage_Governance_via_Azure_Policy.html) | yes | 1 › Subscriptions, governance, and cost control | `gov-azure-policy`, `gov-resource-tags`, `gov-resource-locks` |
| Lab 07 – Manage Azure Storage | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_07-Manage_Azure_Storage.html) | yes | 2 › all three storage topics | `storage-account-create`, `storage-network-controls`, `blob-container`, `files-share` |
| Lab 03 – Manage resources with ARM templates | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_03b-Manage_Azure_Resources_by_Using_ARM_Templates.html) | yes | 3 › Resource deployment with ARM and Bicep | `iac-modify-arm`, `iac-deploy`, `iac-modify-bicep` |
| Lab 08 – Manage virtual machines | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_08-Manage_Virtual_Machines.html) | yes | 3 › Virtual machines and scale sets | `vm-create`, `vm-availability`, `vm-scale-sets` |
| Lab 09a – Implement web apps | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_09a-Implement_Web_Apps.html) | yes | 3 › Azure App Service | `appservice-create`, `appservice-slots`, `appservice-scaling` |
| Lab 09b – Implement Azure Container Instances | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_09b-Implement_Azure_Container_Instances.html) | yes | 3 › Azure container services | `containers-aci` |
| Lab 09c – Implement Azure Container Apps | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_09c-Implement-Azure-Container-Apps.html) | yes | 3 › Azure container services | `containers-apps` |
| Lab 04 – Implement virtual networking | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_04-Implement_Virtual_Networking.html) | yes | 4 › virtual networks; secure access; DNS | `network-vnets-subnets`, `network-nsg-asg`, `network-dns` |
| Lab 05 – Implement intersite connectivity | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_05-Implement_Intersite_Connectivity.html) | yes | 4 › Virtual networks, subnets, and routing; 5 › Network Watcher | `network-peering`, `network-udr`, `monitor-network-watcher` |
| Lab 06 – Implement network traffic management | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_06-Implement_Network_Traffic_Management.html) | yes | 4 › Name resolution and load balancing | `network-load-balancer` |
| Lab 10 – Implement data protection | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_10-Implement_Data_Protection.html) | yes | 5 › Backup and disaster recovery | `recovery-services-vault`, `recovery-backup-restore`, `recovery-site-recovery` |
| Lab 11 – Implement monitoring | lab | [open](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_11-Implement_Monitoring.html) | yes | 5 › Azure Monitor and Network Watcher | `monitor-log-analysis`, `monitor-alerts` |
| Learning path: Manage identities and governance | learning path | [open](https://learn.microsoft.com/en-us/training/paths/az-104-manage-identities-governance/) | modules vary | 1 | chapter 1 outcomes |
| Learning path: Implement and manage storage | learning path | [open](https://learn.microsoft.com/en-us/training/paths/az-104-manage-storage/) | modules vary | 2 | chapter 2 outcomes |
| Learning path: Deploy and manage compute resources | learning path | [open](https://learn.microsoft.com/en-us/training/paths/az-104-manage-compute-resources/) | modules vary | 3 | chapter 3 outcomes |
| Learning path: Configure and manage virtual networks | learning path | [open](https://learn.microsoft.com/en-us/training/paths/az-104-manage-virtual-networks/) | modules vary | 4 | chapter 4 outcomes |
| Learning path: Monitor and back up Azure resources | learning path | [open](https://learn.microsoft.com/en-us/training/paths/az-104-monitor-backup-resources/) | modules vary | 5 | chapter 5 outcomes |
| AZ-104 exam sandbox | exam practice | [open](https://go.microsoft.com/fwlink/?linkid=2226877) | no | all | — |
| AZ-104 practice assessment | exam practice | [open](https://aka.ms/AZ104-PA) | no | all | — |

The lab-to-outcome mapping lists the main outcomes each lab exercises, based on the lab task titles; it is not exhaustive. Lab 02a's task titles cover management groups, built-in and custom roles, and the Activity Log. A repository of all labs: <https://github.com/MicrosoftLearning/AZ-104-MicrosoftAzureAdministrator>.

## Gaps

- No official hands-on lab was found for Azure Files identity-based access, private endpoints, Azure Bastion, or Site Recovery failover beyond Lab 10's replication step. Use the learning paths and your own sandbox.
- Lab names or content may change when Microsoft updates the course; re-check links on each edition.
