import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from typing import Dict

async def get_title_and_summary(chunk: str, url: str) -> Dict[str, str]:
    """Extract title and summary without using DeepInfra API other than using Local LLM."""
    
    system_prompt = """You are an AI that extracts titles and summaries from web content chunks.
    Return a JSON object with 'title' and 'summary' keys.
    For the title: If this seems like the start of a document, extract its title. If it's a middle chunk, derive a descriptive title.
    For the summary: Create a concise summary of the main points in this chunk.
    Keep both title and summary concise but informative."""

    user_prompt = f"URL: {url}\n\nContent:\n{chunk[:256]}..."
    
    model = ChatOllama(model="deepseek-r1:1.5b", base_url="http://localhost:11434/")

    try:
        chat_template = ChatPromptTemplate.from_template(
            "{system_prompt}\n\n{user_prompt}"
        )
        
        chain = chat_template | model | StrOutputParser()
        response = await chain.ainvoke({"system_prompt": system_prompt, "user_prompt": user_prompt})
        
        try:
            jres = json.loads(response)  # Ensure valid JSON
        except json.JSONDecodeError:
            print("Invalid JSON response:", response)
            return {"title": "Error", "summary": "Invalid response format"}
        
        print(jres)
        return jres

    except Exception as e:
        print(f"Error getting title and summary: {e}")
        return {"title": "Error processing title", "summary": "Error processing summary"}
