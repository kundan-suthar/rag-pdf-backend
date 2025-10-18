from fastapi import APIRouter,   HTTPException
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from app.utils.embeddings import embeddingModel, index
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
router = APIRouter()

class QueryRequest(BaseModel):
    query:str

@router.post("/")
async def QueryRequest(data:QueryRequest):
    try:
        userQuery = data.query
        queryVector = embeddingModel.embed_query(userQuery)
        result = index.query(
            vector=queryVector,
            top_k=3,
            include_metadata=True
        )
        if not result["matches"]:
            return {"No relevent information found in provided doc."}
        
        context = "\n".join([match["metadata"]["text"] for match in result["matches"]])
        
        promptTemplate = ChatPromptTemplate.from_messages([
            ("system", """You are a PDF Q&A assistant. Answer questions using ONLY the provided context. If the answer is not in the context, respond: "I did not find the answer in the given PDF." Never use external knowledge."""),
            ("user", "Context: {context}\n\nQuestion: {question}")
        ])
        llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        output_parser = StrOutputParser()  
        chain = promptTemplate | llm | output_parser
        result =chain.invoke({
            "context": context,
            "question": userQuery
        })
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=e, )