from enum import *
import game_types

class PacketHeaderEnum(Enum):
	HANDSHAKE = b'S\x00\x00\x00\x00\x00\x00\x00'
	DISCONNECT_NOTIFY = b"S\x00\x00\x01\x00\x00\x00\x00"
	CLIENT_LOGIN_INFO = b'S\x01\x00\x00\x00\x00\x00\x00'
	LOGIN_RESPONSE = b'S\x05\x00\x00\x00\x00\x00\x00'
	CLIENT_USER_SESSION_INFO = b"S\x04\x00\x01\x00\x00\x00\x00"
	CLIENT_MINIFIGURE_LIST_REQUEST = b"S\x04\x00\x02\x00\x00\x00\x00"
	MINIFIGURE_LIST = b"S\x05\x00\x06\x00\x00\x00\x00"
	CLIENT_MINIFIGURE_CREATE_REQUEST = b"S\x04\x00\x03\x00\x00\x00\x00"
	MINIFIGURE_CREATION_RESPONSE = b"S\x05\x00\x08\x00\x00\x00\x00"
	CLIENT_DELETE_MINIFIGURE_REQUEST = b'S\x04\x00\x06\x00\x00\x00\x00'
	WORLD_INFO = b'S\x05\x00\x02\x00\x00\x00\x00'
	CLINET_ENTER_WORLD = b'S\x04\x00\x04\x00\x00\x00\x00'
	CLINET_LOAD_COMPLETE = b'S\x04\x00\x13\x00\x00\x00\x00'
	DETAILED_USER_INFO = b'S\x05\x00\x04\x00\x00\x00\x00'
	ROUTED_PACKET = b'S\x04\x00\x15\x00\x00\x00\x00'
	CLIENT_GAME_MESSAGE = b'S\x04\x00\x05\x00\x00\x00\x00'
	SERVER_GAME_MESSAGE = b'S\x05\x00\x0c\x00\x00\x00\x00'
	CLIENT_POSITION_UPDATES = b'S\x04\x00\x16\x00\x00\x00\x00'

class LoginResponseEnum(IntEnum):
	SUCCESS = 0x01
	BANNED = 0x02
	INVALID_PERM = 0x03
	INVALID_LOGIN_INFO = 0x06
	ACCOUNT_LOCKED = 0x07

class DisconnectionReasonEnum(IntEnum):
	UNKNOWN_ERROR = 0x00
	DUPLICATE_LOGIN = 0x04
	SERVER_SHUTDOWN = 0x05
	SERVER_CANNOT_LOAD_MAP = 0x06
	INVALID_SESSION_KEY = 0x07
	CHARACTER_NOT_FOUND = 0x09
	CHARACTER_CORRUPTION = 0x0a
	KICKED = 0x0b

class ItemLOTs(IntEnum):
	SHIRT_BRIGHT_RED = 4049
	SHIRT_BRIGHT_BLUE = 4083
	SHIRT_BRIGHT_YELLOW = 4117
	SHIRT_DARK_GREEN = 4151
	SHIRT_BRIGHT_ORANGE = 4185
	SHIRT_BLACK = 4219
	SHIRT_DARK_STONE_GRAY = 4253
	SHIRT_MEDIUM_STONE_GRAY = 4287
	SHIRT_REDDISH_BROWN = 4321
	SHIRT_WHITE = 4355
	SHIRT_MEDIUM_BLUE = 4389
	SHIRT_DARK_RED = 4423
	SHIRT_EARTH_BLUE = 4457
	SHIRT_EARTH_GREEN = 4491
	SHIRT_BRICK_YELLOW = 4525
	SHIRT_SAND_BLUE = 4559
	SHIRT_SAND_GREEN = 4593

	PANTS_BRIGHT_RED = 2508
	PANTS_BRIGHT_ORANGE = 2509
	PANTS_BRICK_YELLOW = 2511
	PANTS_MEDIUM_BLUE = 2513
	PANTS_SAND_GREEN = 2514
	PANTS_DARK_GREEN = 2515
	PANTS_EARTH_GREEN = 2516
	PANTS_EARTH_BLUE = 2517
	PANTS_BRIGHT_BLUE = 2519
	PANTS_SAND_BLUE = 2520
	PANTS_DARK_STONE_GRAY = 2521
	PANTS_MEDIUM_STONE_GRAY = 2522
	PANTS_WHITE = 2523
	PANTS_BLACK = 2524
	PANTS_REDDISH_BROWN = 2526
	PANTS_DARK_RED = 2527

ZoneChecksums = {
    1000: 0x20b8087c,
    1001: 0x26680a3c,
    1100: 0x49525511,
    1101: 0x538214e2,
    1102: 0x0fd403da,
    1150: 0x0fd403da,
    1151: 0x0a890303,
    1200: 0xda1e6b30,
    1201: 0x476e1330,
    1203: 0x10fc0502,
    1204: 0x07d40258,
	1250: 0x058d0191,
	1251: 0x094f045d,
	1300: 0x12eac290,
	1302: 0x0b7702ef,
	1303: 0x152e078a,
	1350: 0x04b6015c,
	1400: 0x8519760d,
	1402: 0x02f50187,
	1403: 0x81850f4e,
	1450: 0x03f00126,
	1600: 0x07c202ee,
	1601: 0x02320106,
	1602: 0x0793037f,
	1603: 0x043b01ad,
	1604: 0x181507dd,
	1700: 0x02040138,
	1800: 0x4b17a399,
	1900: 0x9e4af43c,
	2000: 0x4d692c74,
	2001: 0x09eb00ef
}

DefaultZoneSpawns = {1000 : [-624.13, 613.326233, -30.974],
		1001 : [-187.2391, 608.2743, 54.5554352],
		1100 : [522.9949, 406.040375, 129.992722],
		1101 : [35.0297, 365.780426, -201.578369],
		1102 : [-18.7062054, 440.20932, 37.5326424],
		1150 : [-18.7062054, 440.20932, 37.5326424],
		1151 : [25.0526543, 472.215027, -24.318882],
		1200 : [-40.0, 293.047, -16.0],
		1201 : [111.670906, 229.282776, 179.87793],
		1203 : [0.0, 0.0, 0.0],
		1204 : [-12.1019106, 212.900024, 191.147964],
		1250 : [-17.8299046, 440.509674, 30.0326862],
		1251 : [31.55009, 470.885254, 193.457321],
		1300 : [-329.965881, 302.470184, -470.232758],
		1302 : [-293.072571, 233.0, -4.16148],
		1303 : [0.0, 0.0, 0.0],
		1350 : [-19.713892, 440.20932, 26.935009],
		1400 : [390.284363, 229.452881, -511.350983],
		1402 : [-264.426575, 290.3452, 308.619049],
		1403 : [-1457.71826, 794.0, -332.2917],
		1450 : [-26.8431015, 425.11496, 53.7349777],
		1600 : [34.6352119, 1571.29309, 48.0321465],
		1601 : [-90.30964, 211.087067, -126.3196],
		1602 : [-163.2, 217.254913, 172.0],
		1603 : [9.18036652, 48.79997, 109.610374],
		1604 : [-99.80103, 231.916946, -162.67955],
		1700 : [-359.979156, 1066.328, -369.287781],
		1800 : [-241.965515, 92.78052, 557.327942],
		1900 : [165.355682, 1164.17822, -543.9093],
		2000 : [-446.79715, 171.158859, 1122.83545],
		2001 : [11.26009, 211.05188, 40.6721039]}

class MinifigureCreationResponseEnum(IntEnum):
	SUCCESS = 0x00
	ID_NOT_WORKING = 0x01
	NAME_NOT_ALLOWED = 0x02
	PREDEFINED_NAME_IN_USE = 0x03
	NAME_IN_USE = 0x04