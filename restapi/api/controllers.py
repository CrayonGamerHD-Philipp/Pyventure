from restapi.core.models.player import Player
from restapi.core.db.mongo import players_collection
from bson import ObjectId
import bcrypt


class PlayerController:
    @staticmethod
    async def create_player(player_data: Player):
        # Passwort hashen
        hashed_password = bcrypt.hashpw(player_data.password.encode('utf-8'), bcrypt.gensalt())

        # Gehashtes Passwort in das Player-Dictionary einfügen
        player_dict = player_data.dict()
        player_dict['password'] = hashed_password.decode('utf-8')

        # Spieler in MongoDB speichern
        result = await players_collection.insert_one(player_dict)
        player_dict["_id"] = str(result.inserted_id)
        return player_dict

    @staticmethod
    async def get_player_by_id(player_id: int):
        """Findet einen Spieler anhand seiner ID"""
        player = await players_collection.find_one({"id": player_id})
        if player:
            player["_id"] = str(player["_id"])  # Konvertiere ObjectId zu String
        return player

    @staticmethod
    async def get_player_by_email(player_email: str):
        """Findet einen Spieler anhand seiner Email"""
        player = await players_collection.find_one({"email": player_email})
        if player:
            player["_id"] = str(player["_id"])  # Konvertiere ObjectId zu String
        return player

    @staticmethod
    async def delete_player(player_id: int):
        """Löscht einen Spieler anhand seiner ID"""
        result = await players_collection.delete_one({"id": player_id})
        return result.deleted_count > 0
