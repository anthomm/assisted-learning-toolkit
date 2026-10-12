# Virtual networking (15–20%)

Virtual network troubleshooting is a process of following the packet path and checking each control in order: address plan, route, security rule, name resolution, service endpoint or private link, and destination health. A correct setting at one layer cannot compensate for a failure at another.

## Virtual networks, subnets, and routing

### Learning intent

Create and configure virtual networks and subnets, peer networks, configure public IP addresses and user-defined routes, and troubleshoot connectivity.

### Core concepts

An **Azure virtual network (VNet)** is a private network boundary with one or more nonoverlapping IP address spaces. **Subnets** divide that address space for workload placement and policy. Reserve adequate ranges for expected growth and required platform use; Azure reserves addresses in each subnet, so do not plan to consume every address. A subnet is regional and belongs to one VNet.

**VNet peering** connects VNets using Microsoft's backbone, allowing private IP connectivity subject to routing, security, and address-space requirements. Peering is not automatically transitive: if VNet A peers with B and B peers with C, A does not thereby gain direct connectivity to C. Gateway transit or network appliances can support hub-and-spoke patterns, but must be configured intentionally.

A **public IP address** associates a public endpoint with an Azure resource, subject to the service's configuration and security controls. It is not inherently required for all outbound connectivity and does not replace a firewall. A **route table** contains system routes and optional user-defined routes (UDRs). A UDR can direct traffic to a virtual appliance, virtual network gateway, or another supported next hop. Effective routes show the route selected for a network interface.

### How it works, distinctions, limits, and defaults

When troubleshooting, verify that source and destination ranges do not overlap, the resource is in the intended subnet, peering is connected on both sides, and a route exists in both directions. A more specific route can win over a broader route; service routes and platform behavior should be checked in effective routes. NSGs and firewalls may still block permitted routes.

Peering does not itself configure DNS, security rules, or network virtual appliances. A public IP can expose a service to the internet if the attached resource listens and security allows it; prefer private connectivity when public exposure is unnecessary.

### Example or worked scenario

A VM in a spoke VNet cannot reach a database in a hub VNet. The administrator verifies address-space overlap, both peering states, gateway or appliance transit design, effective routes on the VM NIC, and NSG rules at the NIC and subnet. A successful ping is not assumed because the service may block ICMP; the actual application port and destination health are tested.

### Hands-on activity

In a sandbox, inspect a VNet address plan, subnet ranges, peering status, public IP associations, and effective routes for a network interface. If creating test VNets, choose nonoverlapping ranges and remove them after reviewing connectivity.

### Exam or practical application

Trace connectivity from source to destination and back. Identify the selected route, next hop, and every applicable security boundary. Treat public IP assignment, routing, peering, and authorization as separate parts of the design.

### Self-check questions

1. Does peering from A to B and B to C automatically provide transitive connectivity between A and C?

   **Answer:** No. Peering is not automatically transitive.

2. What does an effective route help an administrator determine?

   **Answer:** Which route is selected for traffic from a network interface and the associated next hop.

3. If a route permits a packet, is successful application connectivity guaranteed?

   **Answer:** No. Security rules, DNS, service health, and return routing can still prevent communication.

### Sources

- [Virtual network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Create, change, or delete a virtual network](https://learn.microsoft.com/en-us/azure/virtual-network/manage-virtual-network)
- [Virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)
- [Public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)
- [Virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)
- [Diagnose a virtual machine routing problem](https://learn.microsoft.com/en-us/azure/virtual-network/diagnose-network-routing-problem)

## Secure access and private connectivity

### Learning intent

Create and interpret network security groups (NSGs) and application security groups (ASGs), evaluate effective rules, provide administrative access with Azure Bastion, and select service endpoints or private endpoints for PaaS connectivity.

### Core concepts

An **NSG** contains inbound and outbound allow/deny rules evaluated by priority. Rules can use address prefixes, ports, protocol, and service or application security groups. NSGs can be associated with subnets and network interfaces. **Application security groups** let rules refer to workload groups rather than repeatedly listing IP addresses; they are used within supported network designs and do not replace an NSG.

To investigate effective security, inspect rules applied at each association point, rule priority, default rules, and effective security rules on the NIC. A higher-priority matching rule can determine the outcome before a lower-priority rule. NSGs are stateful for established flows, but a new flow still needs a permitted direction and return path.

**Azure Bastion** provides managed remote connectivity to VMs over TLS through the Azure portal or supported clients, avoiding a public IP on each VM. Bastion itself requires a suitable deployment, subnet, SKU, and network configuration. It reduces exposed management endpoints but does not remove the need to secure identities and VM accounts.

A **service endpoint** extends a VNet subnet's identity to supported Azure services, so a service firewall can allow selected subnets while traffic reaches the service's public endpoint over the Azure backbone. A **private endpoint** assigns a private IP in a VNet to a specific service resource using Azure Private Link. Private endpoints usually require correct private DNS configuration. They are not interchangeable: the endpoint, DNS behavior, supported services, and security requirements differ.

### How it works, distinctions, limits, and defaults

If a rule appears correct but traffic fails, check for another NSG association, a higher-priority rule, a route or firewall issue, source address translation, and the destination's own access policy. Network Watcher tools can help identify effective rules and paths.

Service endpoints do not make a service private or remove its public endpoint; firewall configuration controls which networks can access it. Private endpoints do not automatically disable public network access on the service. Disable or restrict the public path separately when required, and confirm name resolution returns the intended private address from the client network.

### Example or worked scenario

A VM needs administrative access and must read a storage account without exposing either service broadly. The team uses Bastion for VM management, gives the VM a managed identity with a least-privileged storage data role, and chooses a private endpoint with private DNS when private IP-based service access is required. It separately restricts public network access and validates DNS and effective NSG rules.

### Hands-on activity

In a sandbox, inspect a VM's effective security rules and trace why a test port is allowed or denied. Compare the network path and DNS result for a service endpoint and a private endpoint in a test configuration. Verify that a private endpoint has correct DNS records and remove test resources afterward.

### Exam or practical application

Match the requirement: rule-based network filtering suggests NSG/ASG; browser-based VM administration without per-VM public IPs suggests Bastion; subnet-based service firewall access suggests service endpoints; a private IP for a specific PaaS resource suggests a private endpoint plus DNS planning.

### Self-check questions

1. Does a service endpoint assign a private IP address to the PaaS resource in the VNet?

   **Answer:** No. A private endpoint provides a private IP in the VNet; a service endpoint extends subnet identity to a supported service.

2. Does adding an NSG allow rule guarantee that traffic can reach the destination?

   **Answer:** No. Other NSGs, routes, firewalls, DNS, and destination configuration can still block the flow.

3. What additional configuration is commonly needed for private endpoint name resolution?

   **Answer:** Private DNS configuration that resolves the service name to the private endpoint address from the relevant clients.

### Sources

- [Network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
- [Application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups)
- [View effective security rules](https://learn.microsoft.com/en-us/azure/virtual-network/diagnose-network-traffic-filter-problem)
- [What is Azure Bastion?](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview)
- [Azure virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)
- [What is Azure Private Link?](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)
- [Azure private endpoint DNS values](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

## Name resolution and load balancing

### Learning intent

Configure Azure DNS, select internal or public load-balancing designs, and troubleshoot name resolution and load distribution.

### Core concepts

**Azure DNS** hosts DNS domains and records. A public DNS zone serves internet-visible records after its name servers are delegated at the domain registrar. A **private DNS zone** resolves names for linked VNets and supports private service resolution when configured with appropriate records and links. DNS records map names to addresses or other names; TTL controls caching duration, not the time required for every client to observe a change.

An **Azure Load Balancer** distributes TCP/UDP flows at layer 4 across healthy backend instances using a rule and health probe. A public load balancer has a public frontend; an internal load balancer uses a private frontend address. Backend pool membership, probe status, rules, NSGs, and return paths all affect results. A probe can mark a backend unavailable even when the VM is running if the application does not respond on the expected port or path.

### How it works, distinctions, limits, and defaults

DNS maps a name to an endpoint; it does not ensure the endpoint is reachable or healthy. Verify the resolver used by the client, zone links or delegation, record values, and cache/TTL behavior. Private DNS zone links and private endpoint records must be designed for the client VNets that need resolution.

A load-balancing rule defines frontend/backend ports and protocol; a health probe controls which backends receive new flows. Troubleshoot from the client inward: resolve the name, test the frontend, inspect the rule and backend pool, check probe health, then verify NSGs, routes, and application listeners. Load balancing is not the same as application-layer routing or global disaster recovery.

### Example or worked scenario

A two-VM application is reachable by private IP but not by its DNS name. The administrator checks the client resolver, private zone link, record, and TTL before changing the load balancer. Once name resolution works, an internal load-balancer probe remains unhealthy; checking the configured probe port reveals that the service listens on a different port.

### Hands-on activity

In a sandbox, inspect a public or private DNS zone, an internal load balancer frontend, backend pool, rule, and probe. Use name lookup from a VM in the intended VNet and compare it with lookup from an unlinked network. Avoid exposing a test backend publicly.

### Exam or practical application

Distinguish DNS failure from network or application failure. For load balancing, validate the frontend type, port mapping, backend health, probe, and path to each instance before changing unrelated NSGs.

### Self-check questions

1. What does a load-balancer health probe control?

   **Answer:** It determines whether a backend is considered healthy and eligible to receive new traffic under the associated rule.

2. Will creating a private DNS zone automatically make it resolvable from every VNet?

   **Answer:** No. The relevant VNets and DNS clients must be linked or otherwise configured to use the zone.

3. If DNS resolves to the expected load-balancer address, does that prove an application is healthy?

   **Answer:** No. Routing, security, load-balancer rules and probes, backend health, and application behavior still need verification.

### Sources

- [Azure DNS documentation](https://learn.microsoft.com/en-us/azure/dns/dns-overview)
- [Azure DNS private zones](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview)
- [Azure Load Balancer overview](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)
- [Azure Load Balancer health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-custom-probe-overview)
- [Troubleshoot Azure Load Balancer](https://learn.microsoft.com/en-us/troubleshoot/azure/load-balancer/load-balancer-troubleshoot)
