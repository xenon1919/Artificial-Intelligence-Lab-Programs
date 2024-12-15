import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Add text
text = "The quick brown fox jumped. over the lazy dog. A small, fluffy cat watched " \
       "from a distance. In the nearby trees, birds chirped happily as the sun began to set. The wind " \
       "gently rustled the leaves, creating a soothing melody in the peaceful forest."
print("Text:", text)

# Convert text to lowercase and split into a list of words
tokens = word_tokenize(text.lower())
print("Tokens:", tokens)

# Remove stop words
english_stopwords = stopwords.words('english')
tokens_wo_stopwords = [t for t in tokens if t not in english_stopwords]
print("Text without stop words:", " ".join(tokens_wo_stopwords))
