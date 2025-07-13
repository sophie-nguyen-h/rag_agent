from vertexai import rag

def create_corpus(corpus_name: str) -> dict:
    """
    Create a new corpus with a specific name 'corpus_name'.
    
    Args:
        corpus_name (str): The display name for the new corpus.
        
    Return:
        dict: A dictionary containing the weather information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'report' key with a message that the new corpus was created.
              If 'error', includes an 'error_message' key with the error details.
    """
    
    print(f"--- Tool: call 'create_corpus' to create a new corpus with name {corpus_name}. ---")
    
    try:
        rag.create_corpus(
            display_name = corpus_name
        )
        
        print(f"--- Tool: 'create_corpus' successfully created a new corpus with name {corpus_name}. ---")
        return {
            'status': 'success',
            'report': f"A new corpus named {corpus_name} was created successfully."
        }

    except Error as e:
        
        print(f"--- Tool: 'create_corpus' can not create a new corpus with name {corpus_name}. Error message: {e}. ---")
        return {
            'status': 'error',
            'report': f"The new corpus can not be created. Error message: {e}."
        }
