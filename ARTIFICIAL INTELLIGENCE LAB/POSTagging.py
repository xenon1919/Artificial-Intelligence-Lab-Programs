import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Define the text
text = "John walked to the market to buy fresh vegetables. He carefully selected ripe tomatoes, crisp lettuce, and juicy oranges. After completing his shopping, he headed home, excited to prepare a delicious and healthy meal for his family."

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Initialize the set of stopwords
stop_words = set(stopwords.words('english'))

# Iterate through each sentence
for sentence in sentences:
    # Tokenize the sentence into words
    wordsList = word_tokenize(sentence)
    # Remove stopwords from the word list
    wordsList = [w for w in wordsList if not w in stop_words]
    # Tag the remaining words with their parts of speech
    tagged = nltk.pos_tag(wordsList)
    print(tagged)
