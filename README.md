# SubAI
A tool that uses AI to predict and classify internet subdomains.

# Subdomain Predictor and Classifier

This tool uses AI to predict and classify internet subdomains. Given a list of known subdomains, it can predict additional subdomains that might exist and are similar in structure and naming convention to the known subdomains. It can also classify the predicted subdomains based on their likely purpose or function. Being powered by AI helps it to generate subdomains that traditional tools can't.

The following subdomains were found by this tool with 30 subdomains as input.
```
Task output: 1. dclb02-dca1.example.com - Infrastructure
2. dclb04-sjc1.prod.example.com - Infrastructure
3. fusionjs-sync.example.com - Application
4. central-api.example.com - API
5. fantom-api.example.com - API
6. frontends-secondary.example.com - Frontend
7. elevatenetwork-c.example.com - Network
8. helpdesk.example.com - Support
9. bonjour-prod.example.com - Production
10. auth-production-dns.example.com - Authentication
11. cn-dca2.example.com - Country-specific
12. orders.example.com - E-commerce
13. engineering.example.com - Engineering
14. partners.example.com - Partnerships
15. activedirectory-prod.example.com - Active Directory
16. dclb02-dca2.prod.example.com - Infrastructure
17. jenkins-master02-sjc1.prod.example.com - Infrastructure
18. cn-staging-dca2.example.com - Country-specific
19. frontends-secondary.example.com - Frontend
20. elevatenetwork-c.example.com - Network
21. activedirectory-dca2.example.com - Active Directory
22. iadm-prod.example.com - Production
23. hcv-supplier-production.example.com - Supplier Management
24. call-logs.example.com - Logs
25. fantom-production.example.com - Production
26. bastion-secondary.example.com - Security
27. atg-pg-catalog-productiondb01-sjc1.prod.example.com - Database
28. ci-production.example.com - Continuous Integration
29. users.example.com - User Management
30. atg-customers.example.com - Customer Management
31. dclb05-dca1.example.com - Infrastructure
32. dclb06-sjc1.prod.example.com - Infrastructure
33. fusionjs-bot.example.com - Application
34. central-dev.example.com - Development
35. fantom-dev.example.com - Development
36. frontends-dev.example.com - Development
37. elevatenetwork-dev.example.com - Development
38. helpdesk-dev.example.com - Support
39. bonjour-dev.example.com - Development
40. auth-dev.example.com - Authentication
41. cn-dev.example.com - Country-specific
42. orders-dev.example.com - E-commerce
43. engineering-dev.example.com - Engineering
44. partners-dev.example.com - Partnerships
45. activedirectory-dev.example.com - Active Directory
46. jenkins-master-dev.example.com - Development
47. frontends-dev.example.com - Development
48. elevatenetwork-dev.example.com - Development
49. activedirectory-dev.example.com - Active Directory
50. iadm-dev.example.com - Development
```


## Features

- **Subdomain Prediction**: Predicts additional subdomains that might exist based on a list of known subdomains.
- **Subdomain Classification**: Classifies the predicted subdomains based on their likely purpose or function.

## Requirements

- Python 3.6 or later
- crewai library
- OpenAI API key

## Installation

- Clone this repository.
- Set your OpenAI API key as an environment variable: export OPENAI_MODEL_NAME='gpt-3.5-turbo'
- Run the script with your known subdomains.
