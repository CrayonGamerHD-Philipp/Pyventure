from fastapi import APIRouter, HTTPException
from restapi.api.controllers import PlayerController
from restapi.core.db.mongo import players_collection
from restapi.core.models.player import Player

router = APIRouter()

@router.get("/players/")
async def get_players():
    """Gibt alle Spieler zurück"""
    players = players_collection.find()
    result = []
    async for player in players:
        player["_id"] = str(player["_id"])  # Konvertiere ObjectId zu String
        result.append(player)
    return result

@router.get("/players/id/{player_id}")
async def get_player_by_id(player_id: int):
    """Gibt einen Spieler anhand der ID zurück"""
    player = await PlayerController.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/players/email/{player_email}")
async def get_player_by_email(player_email: str):
    """Gibt einen Spieler anhand der Email zurück"""
    player = await PlayerController.get_player_by_email(player_email)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.put("/players/")
async def create_user(player_data: Player):
    """Erstellt einen neuen Spieler"""
    new_player = await PlayerController.create_player(player_data)
    return new_player

@router.delete("/players/{player_id}")
async def delete_user(player_id: int):
    """Löscht einen Spieler anhand der ID"""
    success = await PlayerController.delete_player(player_id)
    if not success:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"detail": "Player deleted successfully"}
