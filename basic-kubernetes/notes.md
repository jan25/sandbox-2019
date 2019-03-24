
### Networking concepts

- within a pod containers talk on localhost
- pod IPs for internal cluster pod communication

- ClusterIP for Service for intra cluster networking

### How to expose service to external
- NodePort for exposing services to external
- LoadBalancer resource infront of Service for exposing it to external. Downside of this is we need 1 LB for each service
- Ingress controllers can do subdomain, path based routing and much more

