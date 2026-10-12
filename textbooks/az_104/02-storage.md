# Storage (15–20%)

Azure Storage is a set of services with distinct data models, protocols, and availability options. Administration means matching the service to the workload, limiting who and where can access it, and planning for the failures that protection features can and cannot recover from.

## Storage access and network controls

### Learning intent

Configure network boundaries and authorization for storage, including shared access signatures (SAS), stored access policies, account keys, and identity-based access for Azure Files.

### Core concepts

Azure Storage authorization can use Microsoft Entra identities, shared keys, SAS tokens, and service-specific mechanisms. Prefer identity-based authorization where it fits: assign a data role to a principal at the narrowest suitable scope, and use network rules as an additional boundary. **Storage firewalls and virtual network rules** restrict requests to approved network paths; a permitted identity does not automatically bypass those network restrictions.

A **SAS** is a signed, time-limited delegation of specific permissions to storage resources. Scope, permissions, start/expiry times, and allowed protocols should be minimized. A service SAS can be associated with a **stored access policy** for supported services, allowing administrators to change or revoke the policy that governs its SAS tokens. Not all SAS types support stored access policies. An account SAS and a user delegation SAS have different authority and signing requirements; use a user delegation SAS for Blob Storage when identity-based delegation is appropriate.

**Storage account keys** grant broad access to the account. Keep them secret, avoid embedding them in source code, and rotate them using the account's two-key lifecycle where applications can be updated safely. For **Azure Files**, identity-based SMB authentication can integrate with supported directory services and permit share/file authorization through identities; support depends on protocol, client, directory configuration, and deployment scenario. A storage account key is not equivalent to per-user identity authorization.

### How it works, distinctions, limits, and defaults

Authorization and network access are separate checks. A caller may have a valid role or SAS and still be blocked by firewall, routing, private endpoint, or public-network settings. Conversely, a reachable endpoint does not authorize data operations. SAS expiration policy, key rotation, logging, and secret handling should be part of operations rather than afterthoughts.

Private endpoints provide a private IP path to a storage service through a virtual network, but require correct DNS and routing. Service endpoints keep access on the Azure backbone and let a storage firewall allow selected subnets; they do not provide a private IP address for the service. Verify supported endpoint types and current data-exfiltration controls for the specific storage service.

### Example or worked scenario

A reporting job needs read-only access to one container for several hours. Prefer a managed identity with a container-scoped data role if the job runs in Azure and its service supports identity authorization. If a temporary external process requires a SAS, restrict it to the needed resource and read permission, use HTTPS, set a short expiry, and protect the token as a credential. Restricting the network path adds another layer.

### Hands-on activity

In a sandbox storage account, compare a role-based data assignment with a short-lived, read-only SAS. Test each from an allowed and disallowed network path, then revoke the assignment or token and review access configuration. Never paste live keys or SAS values into notes or source control.

### Exam or practical application

Determine whether a scenario needs resource access (role), a delegated temporary capability (SAS), broad account-level access (key), or SMB identity authorization (Azure Files). Then separately evaluate network restrictions, expiry, and revocation.

### Self-check questions

1. Does allowing a subnet through a storage firewall grant that subnet's users permission to read blobs?

   **Answer:** No. The firewall controls network reachability; authorization is still required.

2. Which credential generally has broader authority: an account key or a narrowly scoped SAS?

   **Answer:** An account key generally grants broad account-level authority; a SAS can be restricted by resource, permission, and time.

3. Are stored access policies available for every type of SAS?

   **Answer:** No. They apply only to supported service SAS scenarios; check the current service documentation.

### Sources

- [Authorize access to blobs using Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory)
- [Grant limited access to Azure Storage resources using SAS](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
- [Define a stored access policy](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview#define-a-stored-access-policy)
- [Manage storage account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)
- [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)
- [Azure Files identity-based authentication](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)
- [Choose an Azure Files identity-based authentication option](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-auth-active-directory-enable)

## Storage accounts and data operations

### Learning intent

Create and configure storage accounts, select redundancy and replication options, understand encryption choices, and move or manage data with Storage Explorer and AzCopy.

### Core concepts

A **storage account** is the namespace and configuration boundary for supported Azure Storage services. Account configuration includes performance and redundancy choices, networking, security, and data-protection settings. Choose the account kind and performance tier that fit the required services and workload; options, features, and constraints vary by region and service.

**Redundancy** controls how copies are maintained. Locally redundant storage (LRS) keeps replicas within one datacenter in a region. Zone-redundant storage (ZRS) distributes copies across availability zones where supported. Geo-redundant options asynchronously replicate data to a paired secondary region; read-access variants provide a read endpoint for the secondary copy. These choices address different failure domains and recovery objectives. Replication is not the same as backup: deletion or corruption can be replicated.

**Object replication** asynchronously copies eligible blobs between source and destination accounts according to configured rules. It supports distribution or recovery scenarios but is not instantaneous and does not replace versioning, soft delete, or a backup plan. Storage encrypts data at rest by default; accounts can use Microsoft-managed keys or customer-managed keys where supported. Encryption at rest does not replace access control or secure transport.

**Azure Storage Explorer** provides a graphical way to inspect and manage supported storage resources. **AzCopy** is a command-line utility for data transfer and synchronization scenarios. Both still require authorization, correct endpoint/network access, and a transfer plan that accounts for scale, retries, and verification.

### How it works, distinctions, limits, and defaults

Select redundancy by failure domain and recovery requirement, not by label alone. Geographic replication is asynchronous, so a regional failure can involve a recovery point other than the latest write. Not every account type or service supports every redundancy option, and changing redundancy can involve service or cost constraints. Check the current feature matrix.

Encryption protects stored data from unauthorized disclosure if underlying media are accessed; a principal with valid service authorization can still read data. Customer-managed keys add key-management responsibilities and dependencies. Treat transfer utilities as clients, not as authorization systems.

### Example or worked scenario

A media team stores source images in a Blob account and needs copies in another region for downstream processing. It compares ZRS availability and geo-redundancy requirements, checks object-replication support and expected delay, and separately configures soft delete/versioning to recover from accidental overwrites. AzCopy handles an initial bulk transfer; a managed identity limits ongoing access.

### Hands-on activity

Create a low-cost test account only after checking current pricing. Compare available redundancy, encryption, and network settings in the portal. Upload a small test file with Storage Explorer, then transfer it with AzCopy using an identity-based sign-in. Verify the destination and remove the test account when finished.

### Exam or practical application

For account configuration, map each requirement to a setting: failure-domain coverage, key ownership, access method, network boundary, and data movement. If recovery from deletion is required, do not assume replication alone is sufficient.

### Self-check questions

1. What is the key difference between ZRS and geo-redundant storage?

   **Answer:** ZRS replicates across availability zones in a region; geo-redundancy asynchronously maintains a copy in a secondary region.

2. Does object replication necessarily copy a newly written blob immediately?

   **Answer:** No. It is asynchronous and replication time can vary.

3. Does encryption at rest prevent an authorized identity from reading a blob?

   **Answer:** No. Encryption at rest does not replace authorization controls.

### Sources

- [Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)
- [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
- [Object replication for block blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview)
- [Azure Storage encryption for data at rest](https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption)
- [Azure Storage Explorer](https://learn.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer)
- [Get started with AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)

## Azure Files and Blob Storage

### Learning intent

Create file shares and blob containers, select storage tiers, and configure protection and lifecycle features for Azure Files and Blob Storage.

### Core concepts

**Azure Files** provides managed file shares accessible over supported protocols, commonly SMB and NFS depending on configuration. Create a share with a suitable quota and performance option, then configure identity, network, and client access. Share snapshots provide point-in-time views useful for recovery; soft delete retains deleted shares for a configured period. Neither feature guarantees recovery from every failure or replaces a separately designed backup.

**Azure Blob Storage** stores object data in containers. A container is an organizational and access-control boundary; blobs carry the data. Access tiers such as hot, cool, cold, and archive (where supported) trade access cost, storage cost, and retrieval behavior. Archive data must be rehydrated before normal reads; tier availability and minimum retention or early-deletion charges vary by account and tier. Do not move data to a colder tier solely on access frequency without considering retrieval needs.

Blob **soft delete** retains deleted blobs or containers for a configured retention period. **Versioning** keeps previous blob versions as writes occur. **Lifecycle management** applies rule-based tiering or deletion based on age and other supported conditions. Azure Files has its own snapshots and soft-delete capabilities; do not assume Blob protection settings apply to file shares. Protection settings can interact, and lifecycle rules may delete older versions if configured to do so.

### How it works, distinctions, limits, and defaults

Soft delete provides a recovery window; versioning provides prior object states; snapshots provide point-in-time views. These are operational protections but may share account-level failure or administrative boundaries. Review retention, capacity, and recovery workflows. Test restoring representative content before relying on a feature.

Lifecycle management is asynchronous and conditions are evaluated over time, not necessarily at the exact moment a threshold is crossed. Some operations, tiers, account configurations, and protection features have mutual constraints. Verify current support and cost implications.

### Example or worked scenario

A design team collaborates through an Azure file share, while a publishing system stores product images as blobs. The file share uses identity-based SMB access and snapshots for convenient file recovery. The Blob account enables versioning and soft delete for accidental edits, and lifecycle rules move older, rarely accessed images to a lower-cost tier. Legal retention requirements are handled separately from these operational settings.

### Hands-on activity

In a sandbox, create a file share and a blob container, upload non-sensitive test data, and enable an available protection feature. Delete a test item and restore it using the documented workflow. Inspect tier and lifecycle options, then clean up the test data and resources.

### Exam or practical application

Map requirements to the right service and recovery mechanism: shared file-system access suggests Azure Files; object data suggests Blob Storage. Distinguish a share snapshot, blob version, soft-delete retention, and lifecycle action; each solves a different problem.

### Self-check questions

1. Which service is designed for a managed file share: Azure Files or Blob Storage?

   **Answer:** Azure Files.

2. What is one important difference between blob versioning and lifecycle management?

   **Answer:** Versioning preserves prior blob states; lifecycle management applies rules that can tier or delete eligible data.

3. Can archived blob data always be read immediately like hot-tier data?

   **Answer:** No. Archive data must generally be rehydrated, and access behavior and costs differ.

### Sources

- [Introduction to Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction)
- [Create an Azure file share](https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share)
- [Overview of Azure Files share snapshots](https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files)
- [Azure Files soft delete](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-enable-soft-delete)
- [Introduction to Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
- [Access tiers for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)
- [Soft delete for blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview)
- [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview)
- [Optimize costs by automating Azure Blob Storage access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)
