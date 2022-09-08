""" Textual analysis of search queries """


from nltk.sentiment import SentimentIntensityAnalyzer
from typing import List, Dict
import nltk
import json

sia = SentimentIntensityAnalyzer()

def extract_tokens(text: str) -> List[str]:
    """Extracts tokens from a given text.

    Args:
        text: A string containing the input text

    Returns:
        A list of tokens
    """

    # Sentence tokenization
    sentences = nltk.sent_tokenize(text)

    # Word tokenization
    w = [nltk.word_tokenize(sent) for sent in sentences]


    return {
        "sentences": sentences,
        "words": w,
    }

def grammatical_tagging(tokens: Dict) -> Dict:
    """Grammatical tagging of tokens.

    Args:
        tokens: A dictionary containing token data

    Requires:
        tokens["sentences"]: A list of sentence-tokenized tokens
        tokens["words"]: A list of word-tokenized tokens

    Returns:
        A list of tokens with grammatical tags
    """

    # Grammatical tagging
    tagged = [nltk.pos_tag(sent) for sent in tokens["words"]]

    return tagged
   
def entity_recognition(tokens: Dict):
    """Entity Recognition of tokens. 
    
    Args:
        tokens: A dictionary containing token data
    Requires:
        tokens["sentences"]: A list of sentence-tokenized tokens 
    Returns:
        A list of tokens with entity tags
    """

    entity_list = list()

    for sentence in tokens["sentences"]:
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))):
            if hasattr(chunk, 'label'):
                entity_list.append(chunk)



    return entity_list

def frequency_distribution(tokens: Dict):
    """Frequency distribution of tokens.

    Args:
        tokens: A dictionary containing token data

    Requires:
        tokens["sentences"]: A list of sentence-tokenized tokens
        tokens["words"]: A list of word-tokenized tokens

    Returns:
        A list of tokens with frequency distribution
    """

    # Frequency distribution
    freq_dist = nltk.FreqDist(tokens["words"][0])
    return freq_dist


def bi_and_tri_grams(tokens: Dict) -> Dict:
    """Extracts bi- and tri-grams from a given text.

    Args:
        tokens: A dictionary containing token data
    Requires:
        tokens: A dictionary containing token data
        tokens["words"]: A list of word-tokenized tokens
    Returns:
        A dict of bi- and tri-grams
    """

    # @TODO : Implement bi- and tri-grams
    return {
        "bi_grams": list(nltk.bigrams(tokens["words"][0])),
        "tri_grams": list(nltk.trigrams(tokens["words"][0]))
    }

def stopwords(tokens: Dict) -> List[str]:
    """ Extracts stopwords from a given text.
    Args:   
        tokens: A dictionary containing token data
    Requires:
        tokens["words"]: A list of word-tokenized tokens
    Returns:
        A list of stopwords
        """

    return [w for w in tokens["words"][0] if w in nltk.corpus.stopwords.words('english')]

def sentiment_analysis(text: str) -> Dict:
    """ Sentiment analysis of a given text.

    Args:
        text: A string containing the input text
    
    Returns:
        A dictionary containing the sentiment analysis polarity scores
    """

    # @TODO : Implement sentiment analysis
    return sia.polarity_scores(text)

# @TODO : Chunking seems really useful, try that.
# https://www.nltk.org/book/ch07.html

def pipeline(text: str) -> Dict:
    """ Calls all query enrichment modules and
    collects the enriched metadata to a single JSON object.
    which is returned.

    Args:
        text: A string containing the input text
    
    Returns:
        A JSON object containing the enriched metadata
    """

    metadata = {
        "tokens": extract_tokens(text),
        "tagged": grammatical_tagging(extract_tokens(text)),
        "entities": entity_recognition(extract_tokens(text)),
        "frequency_distribution": frequency_distribution(extract_tokens(text)),
        "bi_and_tri_grams": bi_and_tri_grams(extract_tokens(text)),
        "stopwords": stopwords(extract_tokens(text)),
        "sentiment_analysis": sentiment_analysis(text)
    }

    # @TODO Success checks

    return metadata