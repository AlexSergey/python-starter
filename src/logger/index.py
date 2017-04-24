import logging

logging.basicConfig(filename='logging_app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s\n-----------\n')
logging.getLogger().addHandler(logging.StreamHandler())

logger = logging
