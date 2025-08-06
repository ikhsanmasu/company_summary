# agent_summary.py  –  versi bebas-warning (LangChain ≥ 0.2)
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_core.output_parsers import StrOutputParser

SUMMARY_TEMPLATE = """
Write a brief summary of the following:
{text}
BRIEF SUMMARY:
"""

SUMMARY_MAP_REDUCE_TMPL = """
Combine the following summaries into one coherent and concise summary:

{text}

Final summary:
"""

SUMMARY_REFINE_TMPL = """
You are a meticulous executive-level summarization assistant.

We have provided an existing summary up to a certain point: {existing_answer}
We now have the opportunity to refine that summary (only if needed) with the additional context below.
------------
{text}
------------
Using the new context, refine the original summary.
If the context is not useful, return the original summary.
Dont mention The original summary does not require refinement based on the new context provided, as there are no new significant details to incorporate.
Never assume, just use the provided context to refine the summary.
"""


class AgentSummary:
    def __init__(self, api_key: str, model_name: str = "gpt-4o"):
        self.llm = ChatOpenAI(
            model=model_name,
            api_key=api_key,
            temperature=0,
            max_tokens=800,
        )
        self.parser = StrOutputParser()

    def simple_summarize(self, text: str) -> str:
        if not text:
            return ""
        prompt = PromptTemplate.from_template(SUMMARY_TEMPLATE)

        chain = prompt | self.llm | self.parser
        return chain.invoke({"text": text}).strip()

    def map_reduce_summarize(self, pages: list[str]) -> str:
        if not pages:
            return ""
        docs = [Document(page_content=t) for t in pages]

        map_prompt    = PromptTemplate.from_template(SUMMARY_TEMPLATE)
        reduce_prompt = PromptTemplate.from_template(SUMMARY_MAP_REDUCE_TMPL)

        chain = load_summarize_chain(
            llm=self.llm,
            chain_type="map_reduce",
            map_prompt=map_prompt,
            combine_prompt=reduce_prompt,
        )

        return chain.invoke({"input_documents": docs})["output_text"].strip()

    def refine_summarize(self, pages: list[str]) -> str:
        if not pages:
            return ""
        docs = [Document(page_content=t) for t in pages]

        question_prompt = PromptTemplate.from_template(SUMMARY_TEMPLATE)
        refine_prompt   = PromptTemplate.from_template(SUMMARY_REFINE_TMPL)

        chain = load_summarize_chain(
            llm=self.llm,
            chain_type="refine",
            question_prompt=question_prompt,
            refine_prompt=refine_prompt,
        )

        return chain.invoke({"input_documents": docs})["output_text"].strip()
