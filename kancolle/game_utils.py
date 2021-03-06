# -*- coding: utf-8 -*-

# Ship attribute
SHIP_LV = 'Lv'       # 等级
SHIP_HP = 'HP'       # HP
SHIP_FP = 'FP'       # 装甲
SHIP_TP = 'TP'       # 雷装
SHIP_AA = 'AA'       # 对空
SHIP_AR = 'AR'       # 火力
SHIP_EV = 'EV'       # 回避
SHIP_ASW = 'ASW'     # 反潜
SHIP_LOS = 'LOS'     # 索敌
SHIP_LUK = 'LUK'     # 运
SHIP_EQUIP = 'EQUIPS' # 装备
SHIP_EVBASE = 'EVbase'
SHIP_ASWBASE = 'ASWbase'
SHIP_LOSBASE = 'LOSbase'

# equip type (can equip)
EQTYPE_MAINGUNS = 1
EQTYPE_MAINGUNSAA = 101
EQTYPE_MAINGUNM = 2
EQTYPE_MAINGUNL = 3
EQTYPE_SECGUN = 4
EQTYPE_SECGUNAA = 104
EQTYPE_TORPEDO = 5
EQTYPE_FIGHTER = 6
EQTYPE_DIVEBOMBER = 7
EQTYPE_TORPBOMBER = 8
EQTYPE_CARRIERSCOUT = 9
EQTYPE_SEAPLANE = 10
EQTYPE_SEAPLANEBOMBER = 11
EQTYPE_RADARS = 12
EQTYPE_RADARL = 13
EQTYPE_SONARS = 14
EQTYPE_DEPTHCHARGE = 15
EQTYPE_ENGINE = 17
EQTYPE_TYPE3SHELL = 18
EQTYPE_APSHELL = 19
EQTYPE_AAGUN = 21
EQTYPE_MIDGETSUB = 22
EQTYPE_REPAIR = 23
EQTYPE_LANDINGCRAFT = 24
EQTYPE_AUTOGYRO = 25
EQTYPE_ASWPLANE = 26
EQTYPE_BULGEM = 27
EQTYPE_BULGEL = 28
EQTYPE_SEARCHLIGHTS = 29
EQTYPE_DRUM = 30
EQTYPE_SRF = 31
EQTYPE_TORPEDOSS = 32
EQTYPE_STARSHELL = 33
EQTYPE_FCF = 34
EQTYPE_SCAMP = 35
EQTYPE_AAFD = 36
EQTYPE_WG42 = 37
EQTYPE_MAINGUNXL = 38
EQTYPE_PICKET = 39
EQTYPE_SONARL = 40
EQTYPE_FLYINGBOAT = 41
EQTYPE_SEARCHLIGHTL = 42
EQTYPE_RATION = 43
EQTYPE_OILDRUM = 44
EQTYPE_SEAPLANEFIGHTER = 45
EQTYPE_LANDINGTANK = 46
EQTYPE_LANDBOMBER = 47
EQTYPE_INTERCEPTOR = 48
EQTYPE_TRANSPORTITEM = 50
EQTYPE_SUBRADAR = 51
EQTYPE_JETBOMBER = 57
EQTYPE_JETSCOUT = 59
EQTYPE_RADARXL = 93
EQTYPE_CARRIERSCOUT2 = 94
EQTYPE_OTHER = 99

# artillery spot/night battle/other combat type
EQ_B_MAINGUN = 1
EQ_B_SECGUN = 2
EQ_B_RECON = 3
EQ_B_RADAR = 4
EQ_B_APSHELL = 5
EQ_B_SONAR = 6
EQ_B_DEPTHCHARGE = 7
EQ_B_TORPEDO = 8
EQ_B_TYPE3SHELL = 9
EQ_B_LC1 = 10
EQ_B_LC2 = 11
EQ_B_LC3 = 12
EQ_B_DEPTHCHARGE2 = 13
EQ_B_NIGHTFIGHTER = 14
EQ_B_NIGHTBOMBER = 15
EQ_B_NIGHTBOMBER2 = 16
EQ_B_NIGHTCREW = 17
EQ_B_OTHER = 0

# anti-air type
EQ_A_HAGUN = 1
EQ_A_AAFD = 2
EQ_A_HAFD = 3
EQ_A_MAINGUNL = 4
EQ_A_TYPE3SHELL = 5
EQ_A_AIRRADAR = 6
EQ_A_AAGUN = 7
EQ_A_GUN = 8
EQ_A_XLGUN = 9

# For CV types ship:
CV_TYPE = []

def get_var(pack, name):
    if isinstance(pack, dict) and name in pack:
        return pack[name]
    return None

def is_carrier(ship):
    return get_var(ship, 'type') in CV_TYPE
