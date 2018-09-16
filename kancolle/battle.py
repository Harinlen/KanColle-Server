# -*- coding: utf-8 -*-

import math

# from . import game_data
import ship_data
import equip_data
import game_utils

USER_PROVIDE = [
    game_utils.SHIP_HP,
    game_utils.SHIP_LV,
    game_utils.SHIP_AR,
    game_utils.SHIP_TP,
    game_utils.SHIP_AA,
    game_utils.SHIP_FP,
    game_utils.SHIP_LUK,
    game_utils.SHIP_EQUIP]

EQUIP_ENHANCE = [
    game_utils.SHIP_LV,
    game_utils.SHIP_HP,
    game_utils.SHIP_FP,
    game_utils.SHIP_TP,
    game_utils.SHIP_AA,
    game_utils.SHIP_AR,
    game_utils.SHIP_EV,
    game_utils.SHIP_ASW,
    game_utils.SHIP_LOS,
    game_utils.SHIP_LUK]

def scaleValue(ship, value, valueBase):
    base_line = ship[valueBase]
    ship[value] = math.floor((ship[value] - base_line) / 99 * \
        ship[game_utils.SHIP_LV] + base_line)
    return ship

def scaleShip(ship):
    # Scale three value: EV, ASW, LOS
    ship = scaleValue(ship, game_utils.SHIP_EV, game_utils.SHIP_EVBASE)
    ship = scaleValue(ship, game_utils.SHIP_ASW, game_utils.SHIP_ASWBASE)
    ship = scaleValue(ship, game_utils.SHIP_LOS, game_utils.SHIP_LOSBASE)
    return ship

def setEquip(ship):
    # Get the equipment data.
    equip_ids = game_utils.get_var(ship, game_utils.SHIP_EQUIP)
    equip_list = []
    for equip_id in equip_ids:
        equip = {}
        if equip_id > 0 and equip_id in equip_data.EQDATA:
            equip = equip_data.EQDATA[equip_id]
        # Add to the equip list.
        equip_list.append(equip)
        # Add the data of equip to the ship.
        for enhance_item in EQUIP_ENHANCE:
            if enhance_item in equip:
                ship[enhance_item] += equip[enhance_item]
    ship[game_utils.SHIP_EQUIP] = equip_list
    return ship

def fullFillPlayer(ships):
    player_ships = []
    for ship in ships:
        ship_raw_data = game_utils.get_var(ship_data.KANCOLLE_SHIP_DATA, ship['id']).copy()
        # Check the ships data.
        for provide_item in USER_PROVIDE:
            if not provide_item in ship:
                print("No provided item")
                return None
        # Append the data which is not in ship.
        for item in ship_raw_data:
            if not item in ship:
                ship[item] = ship_raw_data[item]
        ship = scaleShip(ship)
        # Set the equipment.
        ship = setEquip(ship)
        # Add ship to the list.
        player_ships.append(ship)
    return player_ships

def fullFillEnemy(ships):
    enemy_ships = []
    for ship in ships:
        ship = game_utils.get_var(ship_data.KANCOLLE_SHIP_DATA, ship['id']).copy()
        # Set the equipment.
        ship = setEquip(ship)
        # Add ship to the list
        enemy_ships.append(ship)
    return enemy_ships

def getAttack(ships):
    ship_with_attacks = []
    for ship in ships:
        if game_utils.is_carrier(ship):
            # Should be something else.
            ship['attack'] = ship[game_utils.SHIP_AR] + 5
        else:
            ship['attack'] = ship[game_utils.SHIP_AR] + 5
        ship_with_attacks.append(ship)
    return ship_with_attacks

def startBattle(fleet1 = {}, fleet2 = {}):
    # Extract ships.
    fleet1_ship = game_utils.get_var(fleet1, 'ships')
    fleet2_ship = game_utils.get_var(fleet2, 'ships')
    if fleet1_ship is None or fleet2_ship is None:
        return None
    fleet1_ship = fullFillPlayer(fleet1_ship)
    fleet2_ship = fullFillEnemy(fleet2_ship)
    if fleet1_ship is None or fleet2_ship is None:
        return None
    
    # -- Battle Phase --
    # Shelling 1
    fleet1_ship = getAttack(fleet1_ship)
    fleet2_ship = getAttack(fleet2_ship)
    # Decide the attack sequence.
    
    return fleet1_ship

if __name__ == '__main__':
    fleet1 = {'ships': [
            {'id': 50, 'HP': 19, 'Lv': 3, 'AR': 8, 'TP': 45, 'AA': 34, 'FP': 12, 'LUK': 10,
             'EQUIPS': [2, 28], 'fuel': 20, 'ammo': 25},
            {'id': 50, 'HP': 19, 'Lv': 3, 'AR': 8, 'TP': 45, 'AA': 34, 'FP': 12, 'LUK': 10,
             'EQUIPS': [2, 28], 'fuel': 20, 'ammo': 25}]}
    fleet2 = {'ships': [
            {'id': 1501}, {'id': 1501}, {'id': 1501}]}
    startBattle(fleet1, fleet2)
    