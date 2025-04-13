import re
from typing import Any
from relevant_info import relevant_info
from rtmt import RTMiddleTier, Tool, ToolResult, ToolResultDirection

_search_tool_schema = {
    "type": "function",
    "name": "search",
    "description": """Get the current relevant information to the users question.
                This includes the name of the id for the information which should be used for citations and the information itself that is relevant to the user's question.""",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Detailed Search query of what information is needed. This should be a detailed query that is relevant to the user's question."
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}

# _grounding_tool_schema = {
#     "type": "function",
#     "name": "report_grounding",
#     "description": "Report use of a source from the knowledge base as part of an answer (effectively, cite the source). Sources " + \
#                    "appear in square brackets before each knowledge base passage. Always use this tool to cite sources when responding " + \
#                    "with information from the knowledge base.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "sources": {
#                 "type": "array",
#                 "items": {
#                     "type": "string"
#                 },
#                 "description": "List of source names from last statement actually used, do not include the ones not used to formulate a response"
#             }
#         },
#         "required": ["sources"],
#         "additionalProperties": False
#     }
# }

async def _search_tool(
    args: Any) -> ToolResult:
    print(f"Searching for '{args['query']}' in the knowledge base.")
    search_results = relevant_info(args["query"])
    
    # Send results to both server (for the LLM to use) and client (to display grounding files)
    # We'll make a copy for the server
    server_result = search_results
    
    # Return the client result with sources for display in the UI
    return ToolResult(search_results, ToolResultDirection.TO_CLIENT)

KEY_PATTERN = re.compile(r'^[a-zA-Z0-9_=\-]+$')

# TODO: move from sending all chunks used for grounding eagerly to only sending links to 
# the original content in storage, it'll be more efficient overall
# async def _report_grounding_tool(search_client: SearchClient, identifier_field: str, title_field: str, content_field: str, args: Any) -> None:
#     sources = [s for s in args["sources"] if KEY_PATTERN.match(s)]
#     list = " OR ".join(sources)
#     print(f"Grounding source: {list}")
#     # Use search instead of filter to align with how detailt integrated vectorization indexes
#     # are generated, where chunk_id is searchable with a keyword tokenizer, not filterable 
#     search_results = await search_client.search(search_text=list, 
#                                                 search_fields=[identifier_field], 
#                                                 select=[identifier_field, title_field, content_field], 
#                                                 top=len(sources), 
#                                                 query_type="full")
#     docs = []
#     async for r in search_results:
#         docs.append({"chunk_id": r[identifier_field], "title": r[title_field], "chunk": r[content_field]})
#     return ToolResult({"sources": docs}, ToolResultDirection.TO_CLIENT)

def attach_rag_tools(rtmt: RTMiddleTier) -> None:
    rtmt.tools["search"] = Tool(schema=_search_tool_schema, target=lambda args: _search_tool(args))
    #rtmt.tools["report_grounding"] = Tool(schema=_grounding_tool_schema, target=lambda args: _report_grounding_tool(search_client, identifier_field, title_field, content_field, args))
