# Import necessary modules
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config


def train_nlu(data, configs):
    # Create a trainer that uses this config
    trainer = Trainer(config.load(configs))

    # Load the training data
    training_data = load_data(data)

    # Create an interpreter by training the model
    interpreter = trainer.train(training_data)

    return interpreter
    # initialize my model directory
    #model_directory = trainer.persist(model_dir, fixed_model_name='weather_nlu')


if __name__ == '__main__ ':
    train_nlu(('./data/data.json', 'config_spacy.yml'))
