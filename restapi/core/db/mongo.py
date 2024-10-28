import yaml
from motor.motor_asyncio import AsyncIOMotorClient
import os

# Lade die MongoDB-Konfiguration aus der YML-Datei
#config_path = os.path.join(os.path.dirname(__file__), "../../config/mongo_config.yml")
#with open(config_path, 'r') as config_file:
#    config = yaml.safe_load(config_file)

#mongo_host = config['mongodb']['host']
#mongo_port = config['mongodb']['port']
#mongo_db_name = config['mongodb']['database']
#mongo_user = config['mongodb']['username']
#mongo_password = config['mongodb']['password']
mongo_host = "localhost"
mongo_port = 27017
mongo_db_name = "Pyventure"
mongo_user = "root"
mongo_password = "example"

# Verbindung zu MongoDB herstellen
mongo_uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}"
client = AsyncIOMotorClient(mongo_uri)
db = client[mongo_db_name]
players_collection = db["players"]
