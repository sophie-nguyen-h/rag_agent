# Template for RAG agent

Goal: set up an agent to find and summarize information from additional data source. These are tasks that are expected of the agent.
- Create a new corpus (if not already existed).
- Add a new document to an existing corpus.

## Set up
- Google account platform needed and payment information is required as storage and services will be charged.
- Set up a project.
- Start a new virtual environment
- Create a req.txt file to include the following packages (select the versions of interest)
    - GitPython==3.1.44
    - google-adk==1.6.1
    - google-cloud-aiplatform==1.102.0
    - google-cloud-storage==2.19.0
    - google-genai==1.25.0
- Install packages listed in req.txt
- Create an environment file to include the following information
    - GOOGLE_GENAI_USE_VERTEXAI=TRUE
    - GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
    - GOOGLE_CLOUD_LOCATION=LOCATION
- Create a child folder name agent.
- Create files agent.py and .env inside the agent folder.
- To organize tools, create a child folder tools inside agent and create a file for each tool.

# Agent instruction guideline
Instruction details
- Name
- Adjective to describe the agent, for example, e.g., helpful, collaborative.
- Tell the agent its main function and its scope of capabilities.
- Instruction on how to process the users' requests.
- List all the tools it is provided with (can list all the parameters needed for the tools) and specify when to use each tool.
- List all the subagents it is provided with.
- Communication guideline
    - Be clear and concise.
    - Explain or details to provide aditional information.

