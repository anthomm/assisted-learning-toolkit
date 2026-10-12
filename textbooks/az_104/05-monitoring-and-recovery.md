# Monitoring and recovery (10–15%)

Monitoring helps administrators detect conditions; recovery services help restore operations after data loss or a larger outage. Neither works well without a defined target: what must be observed, what threshold matters, who responds, and how quickly the workload must recover.

## Azure Monitor and Network Watcher

### Learning intent

Interpret Azure Monitor metrics, configure diagnostic logs, query and analyze logs, create alerts and action groups, use Azure Monitor Insights, and diagnose network paths with Network Watcher and Connection Monitor.

### Core concepts

**Azure Monitor** collects and analyzes telemetry. **Metrics** are numeric time-series measurements with dimensions, such as CPU percentage or request count. They are useful for trends and near-real-time alerting. **Logs** are records stored in a Log Analytics workspace or another supported destination; they support querying and correlation but require appropriate diagnostic settings and retention configuration. Resource diagnostic settings route selected logs and metrics to destinations; they do not enable every resource log automatically.

Log queries use **Kusto Query Language (KQL)** to filter, aggregate, join, and summarize records. Start with a time range, identify the correct table, filter early, and validate the units and dimensions before drawing conclusions. **Alert rules** evaluate metrics, logs, or activity conditions. An **action group** describes notification or automation actions; an **alert processing rule** can alter or suppress alert handling under specified conditions, such as a maintenance period. Separate detection logic from notification and response ownership.

**Azure Monitor Insights** provides curated monitoring views for supported resources such as VMs, storage accounts, and networks. It can surface relevant metrics and dependencies but does not eliminate the need to configure data collection, permissions, or alerting. **Network Watcher** offers diagnostics such as IP flow verify, next hop, connection troubleshoot, packet capture, and topology. **Connection Monitor** tests connectivity over time between sources and destinations and can alert on loss or latency.

### How it works, distinctions, limits, and defaults

Metrics and logs answer different questions; availability, granularity, retention, and cost vary by metric, log category, resource, and destination. Confirm that collection is enabled before relying on a chart. A metric anomaly is evidence to investigate, not proof of a root cause.

Alerts require more than a threshold: scope, condition, evaluation frequency, severity, action group, and operational ownership all matter. Avoid noisy thresholds and verify that an action group reaches a monitored contact. Network diagnostics should follow the actual source, destination, protocol, port, DNS, and route.

### Example or worked scenario

Users report intermittent slow responses from a web app. The operator checks request and server metrics, queries relevant logs over the incident window, and correlates a latency increase with a dependent service. An alert rule detects sustained latency and invokes an action group. Connection Monitor then identifies loss on a path to a private backend; Network Watcher tools help inspect route and filtering state.

### Hands-on activity

In a test resource group, inspect available metrics and diagnostic categories for a VM or storage account. Route a small set of logs to a test workspace, run a time-bounded KQL query, and create a test metric or log alert with a nonproduction action group. In a sandbox VNet, inspect Network Watcher connectivity tools and remove test settings after review.

### Exam or practical application

For each symptom, choose the telemetry that can observe it: metrics for numeric trends, logs for event/detail analysis, and network tools for reachability and path behavior. Trace alert evaluation through condition, scope, action group, and response procedure.

### Self-check questions

1. What is a common distinction between an Azure Monitor metric and a log?

   **Answer:** Metrics are numeric time-series measurements; logs are records that can be queried and correlated for detailed analysis.

2. Does creating an alert rule automatically notify an administrator?

   **Answer:** No. The rule must be configured with an action group or another response mechanism.

3. Which tool is suited to monitoring connectivity and latency between endpoints over time?

   **Answer:** Connection Monitor.

### Sources

- [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/overview)
- [Metrics in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-platform-metrics)
- [Azure Monitor diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings)
- [Log Analytics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)
- [Kusto Query Language (KQL) overview](https://learn.microsoft.com/en-us/kusto/query/)
- [Azure Monitor alerts overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
- [Create and manage action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups)
- [Alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules)
- [Azure Monitor Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview)
- [What is Azure Network Watcher?](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-overview)
- [Monitor network connectivity with Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)

## Backup and disaster recovery

### Learning intent

Create the appropriate vault, configure and operate Azure Backup policies, restore protected data, configure Azure Site Recovery (ASR), perform a failover, and interpret backup reports and alerts.

### Core concepts

**Azure Backup** protects supported workloads using a backup policy that defines when recovery points are created and how long they are retained. A **Recovery Services vault** stores backup and Site Recovery configuration for supported workloads; an **Azure Backup vault** supports backup for other supported data sources and newer scenarios. Select the vault type from the workload's current support matrix rather than assuming the two are interchangeable.

A backup policy describes schedule and retention, subject to workload and vault capabilities. After enabling backup, monitor job status, retention, and alerts. A successful backup is not proven recoverable until a restore is tested. Restore choices can include restoring files, disks, or a VM, depending on the protected workload. Plan for identity, networking, keys, permissions, and application consistency during recovery.

**Azure Site Recovery** replicates supported workloads to another location or region and orchestrates recovery during a disruption. Replication and failover are distinct from backup: replication can reproduce unwanted changes or corruption, while backup provides retained recovery points. A **test failover** validates a recovery plan in an isolated network; a planned or unplanned failover changes the serving location. Commit and reprotect steps depend on the scenario and should be understood before production use.

Backup reports and alerts expose job health, protected-item coverage, and issues requiring attention. Configure reporting and notification paths, review failures, and assign an owner for remediation. Retention, data residency, network access, and costs are part of the protection design.

### How it works, distinctions, limits, and defaults

Recovery objectives should be explicit: **recovery point objective (RPO)** is the acceptable data-loss window; **recovery time objective (RTO)** is the acceptable restoration time. Backup frequency and replication behavior affect RPO; restore throughput, dependencies, and tested automation affect RTO. Service defaults do not automatically meet business objectives.

Vault redundancy, soft delete, immutability, encryption, private connectivity, and role separation can strengthen protection, but feature availability differs by workload and configuration. Prevent backup operators from having unnecessary delete or production privileges. Validate the actual restore or failover path and record the result.

### Example or worked scenario

A VM must recover from accidental deletion and from a regional outage. The team protects it with Azure Backup in a supported vault and tests restoring a VM or disks. It separately configures Site Recovery for regional continuity, defines a recovery plan and isolated test network, and performs a test failover. A quarterly review confirms backup alerts reach the on-call team and measured recovery times meet objectives.

### Hands-on activity

In a nonproduction subscription, inspect supported vault types for a test workload, create a short-retention backup policy, and enable protection. Monitor the first job and perform a documented test restore where possible. Separately review ASR prerequisites and perform only a test failover in an isolated environment. Clean up test replicas and vault resources according to product guidance.

### Exam or practical application

Use backup when the requirement is retained point-in-time recovery; use Site Recovery when the requirement is orchestrated continuity at a secondary location. Identify workload support, vault type, policy, recovery objective, and verification/reporting need. A failover plan should include dependencies and post-failover steps, not just the compute resource.

### Self-check questions

1. What is the main difference between Azure Backup and Site Recovery?

   **Answer:** Backup retains recovery points for restore; Site Recovery replicates workloads and orchestrates failover to support continuity.

2. How do RPO and RTO differ?

   **Answer:** RPO describes acceptable data loss measured as time; RTO describes acceptable time to restore service.

3. Does a successful backup job prove that the application can be recovered within its RTO?

   **Answer:** No. Recovery must be tested, including application dependencies and measured restoration time.

### Sources

- [Azure Backup documentation](https://learn.microsoft.com/en-us/azure/backup/)
- [Azure Backup vault overview](https://learn.microsoft.com/en-us/azure/backup/backup-vault-overview)
- [Recovery Services vault overview](https://learn.microsoft.com/en-us/azure/backup/backup-azure-recovery-services-vault-overview)
- [Azure Backup support matrix](https://learn.microsoft.com/en-us/azure/backup/backup-support-matrix)
- [Back up an Azure VM](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-first-look-arm)
- [Restore an Azure VM](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms)
- [Azure Backup reports](https://learn.microsoft.com/en-us/azure/backup/configure-reports)
- [Azure Site Recovery overview](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview)
- [Run a test failover in Azure Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-test-failover-to-azure)
- [Fail over and fail back virtual machines](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-failover)
