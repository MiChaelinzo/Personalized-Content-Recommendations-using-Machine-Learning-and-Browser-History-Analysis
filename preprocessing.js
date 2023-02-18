// Import the necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

// Define the function for preprocessing the user's browsing history
def preprocess_history(user_history):
    // Initialize the NLTK libraries
    nltk.download('punkt')
    nltk.download('stopwords')
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    
    // Loop through each document in the user's browsing history
    preprocessed_history = []
    for document in user_history:
        // Clean the document by removing any non-alphanumeric characters and converting to lowercase
        clean_document = ''.join(e for e in document if e.isalnum() or e.isspace())
        clean_document = clean_document.lower()
        
        // Tokenize the document into individual words
        tokenized_document = word_tokenize(clean_document)
        
        // Remove stop words from the document
        filtered_document = [word for word in tokenized_document if word not in stop_words]
        
        // Stem each word in the document
        stemmed_document = [stemmer.stem(word) for word in filtered_document]
        
        // Add the preprocessed document to the list of preprocessed history
        preprocessed_history.append(' '.join(stemmed_document))
    
    // Return the preprocessed user history
    return preprocessed_history
