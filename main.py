import os
import yaml
from google.oauth2.service_account import Credentials

from agent_summary import AgentSummary
from spreedsheet_api import SpreadsheetAPI
from agent_company_profile import CompanyProfile

# Load configuration from YAML file
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Spreedsheet config
spreadsheet_id = config["spreadsheet"].get("spreadsheet_id")
company_name_sheet = config["spreadsheet"].get("company_name_sheet")
company_summary_sheet = config["spreadsheet"].get("company_summary_sheet")
credentials_config = config["spreadsheet"].get("credentials_config")
creds = Credentials.from_service_account_info(
    credentials_config, 
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

# OpenAI config
api_key = config["openai"].get("api_key")
model_name = config["openai"].get("model_name", "gpt-4o")

# Initialize objects
spreadsheet = SpreadsheetAPI(spreadsheet_id=spreadsheet_id, creds=creds)
company_profile = CompanyProfile(openai_api_key=api_key, model_name=model_name)
agent_summary = AgentSummary(api_key=api_key, model_name=model_name)

# get company names from the spreadsheet
company_list = spreadsheet.get_values(range_name=f"{company_name_sheet}!A2:A")

# iterate through company names, get their profiles, and summarize them finally writing the results to the spreadsheet
for index, company in enumerate(company_list):
    company_information = company_profile.get_profile_section(company=company)
    company_summary = agent_summary.refine_summarize(company_information)
    spreadsheet.write_value(range_name=f"{company_summary_sheet}!A{2 + index}:A{2 + index}", value=company)
    spreadsheet.write_value(range_name=f"{company_summary_sheet}!B{2 + index}:B{2 + index}", value=company_summary)
