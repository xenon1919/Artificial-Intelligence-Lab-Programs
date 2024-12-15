import nltk
nltk.download('wordnet')
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Initialize stemmer and lemmatizer
porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

# List of words to process
words = ["running", "walked", "swimming", "cries", "horses", "mice", "happily", "faster", "geese", "better"]

# Stemming
stemmed_words = [porter_stemmer.stem(word) for word in words]
print("Stemmed words:", stemmed_words)

# Lemmatization
lemmatized_words = [wordnet_lemmatizer.lemmatize(word) for word in words]
print("Lemmatized words:", lemmatized_words)
