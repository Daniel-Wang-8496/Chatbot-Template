from mindmeld.text_preparation.text_preparation_pipeline import TextPreparationPipelineFactory
from mindmeld.text_preparation.stemmers import Stemmer
from mindmeld.text_preparation.normalizers import Normalizer

class SpacyLemmatizer(Stemmer):

    def init(self):
        self.nlp = spacy.load('en_core_web_sm')

    def stem_word(self, word):
        doc = self.nlp(word)
        return " ".join([token.lemma for token in doc])

class Lowercase(Normalizer):

    def normalize(self, text):
        return text.lower()

def get_text_preparation_pipeline():
    """
    text_preparation_pipeline = TextPreparationPipelineFactory.create_from_app_path("./")
    text_preparation_pipeline.normalizers.append(Lowercase())
    text_preparation_pipeline.set_stemmer(SpacyLemmatizer())
    return text_preparation_pipeline
    """
