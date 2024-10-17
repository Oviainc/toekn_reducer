# token_reducer.py

def token_reducer(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenization
    tokens = text.split()

    # Define stop words
    stop_words = set(['and', 'the', 'is', 'in', 'to', 'of'])

    # Apply reduction techniques
    reduced_tokens = [token for token in tokens if token not in stop_words]
    reduced_text = ' '.join(reduced_tokens)

    return reduced_text
