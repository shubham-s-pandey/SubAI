# Warning control
import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew

import os
from utils import get_openai_api_key

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

# Initialize the agents and tasks
subdomain_predictor = Agent(
    role="Subdomain Predictor",
    goal="Given a list of known subdomains {known_subdomains}, predict additional subdomains that might exist, which are similar in structure and naming convention to the known subdomains.",
    backstory="You're an AI model trained on a large dataset of internet domain names. You've learned to recognize patterns and structures in domain names, and can generate new domain names that are similar to the ones you've seen before.",
    allow_delegation=False,
    verbose=True

)

subdomain_classifier = Agent(
    role="Subdomain Classifier",
    goal="Classify the predicted subdomains based on their likely purpose or function.",
    backstory="You're an AI model trained on a large dataset of internet domain names and their associated metadata. You've learned to recognize patterns in domain names and can predict their likely purpose or function.",
    allow_delegation=False,
    verbose=True
)

# Define the tasks
predict_subdomains = Task(
    description=(
        "1. Based on the {known_subdomains}, predict 50 more subdomains that are likely to exist and are similar in structure and naming convention to the known subdomains.\n"
        "2. Ensure the predicted subdomains are structured and organized for easy analysis.\n"
        "3. Handle any exceptions or errors during the prediction process."
    ),
    expected_output="A structured dataset containing the predicted subdomains.",
    agent=subdomain_predictor,
)


classify_subdomains = Task(
    description=(
        "1. Review the predicted subdomains and classify them based on their likely purpose or function.\n"
        "2. Ensure the classifications are structured and organized for easy analysis.\n"
        "3. Handle any exceptions or errors during the classification process."
    ),
    expected_output="A structured dataset containing the predicted subdomains and their classifications.",
    agent=subdomain_classifier,
)

# Initialize the crew and kickoff the tasks
crew = Crew(
    agents=[subdomain_predictor, subdomain_classifier],
    tasks=[predict_subdomains, classify_subdomains],
    verbose=2
)


# List of known subdomains
known_subdomains = [
    "dclb-dca1.example.com",
    "dclb03-sjc1.prod.example.com",
    "fusionjs-sync-bot.example.com",
    "central.example.com",
    "fantom.example.com",
    "frontends-all.example.com",
    "elevatenetwork.example.com",
    "email.example.com",
    "bonjour-qa.example.com",
    "auth-staging-dns.example.com",
    "cn-dca1.example.com",
    "eats.example.com",
    "eng.example.com",
    "empresas.example.com",
    "activedirectory.example.com",
    "dclb01-dca1.prod.example.com",
    "jenkins-master01-sjc1.prod.example.com",
    "cn-staging-dca1.example.com",
    "frontends-primary.example.com",
    "elevatenetwork-b.example.com",
    "activedirectory-dca1.example.com",
    "iadm.example.com",
    "hcv-supplier-staging.example.com",
    "call-prompts.example.com",
    "fantom-staging.example.com",
    "bastion-all.example.com",
    "atg-pg-catalog-stagingdb01-sjc1.prod.example.com",
    "ci.example.com",
    "drivers.example.com",
    "atg-partners.example.com"
]

# Kickoff the tasks with the known subdomains
result = crew.kickoff(inputs={"known_subdomains": known_subdomains})
