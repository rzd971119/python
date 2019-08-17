from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
def interprete():
    trainer = Trainer(config.load("config_spacy.yml"))
    training_data = load_data('demo-rasa.json')
    interpreter = trainer.train(training_data)
    return interpreter