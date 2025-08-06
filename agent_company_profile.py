from typing import Dict
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

SYSTEM_PROMPT = """
You are a corporate research analyst with more than 20 years of experience.

Your mission for *every* request is to produce fact-checked answer
about a company, following these rules:

• Never invent, assume or speculate.  
• If you cannot verify a detail, reply exactly "Unknown" (without qualifiers).  
• Keep each answer concise, plain English, ≤500 words.
• Do not add extra sections or commentary.  
"""

SECTION_TEMPLATES = {
    "overview": """
        Provide overview of {text}. Focus on what the company does, when founded, and HQ location. 
    """,
    "products": """
        List the main product lines or services offered by {text}.
    """,
    "financials": """
        Provide the latest publicly known revenue figure, valuation or funding total for {text}. 
    """,
    "leadership": """
        Name the CEO and one or more key executives of {text}.
    """,
    "recent_events": """
        Mention up to three notable events (product launches, acquisitions, funding rounds) involving {text}.
    """,
}

class CompanyProfile:
    def __init__(self, openai_api_key: str, model_name: str = "gpt-4o-mini"):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=0.25,
            openai_api_key=openai_api_key,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}],
        )
        self.parser = StrOutputParser()

    def get_profile_section(self, company: str) -> list[str]:
        results = [f"company profile of {company}"]
        for section, template in SECTION_TEMPLATES.items():
            prompt = PromptTemplate.from_template(template)
            chain = prompt | self.llm | self.parser
            answer = chain.invoke({"text": company}).strip()
            results.append(f"{section}: {answer if answer else 'Unknown'}")
        return results

