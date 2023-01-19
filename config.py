"""
╔╗ ╦╔╦╗╔═╗╦ ╦╔═╗╦═╗╔═╗╔═╗  ╔╗╔╔═╗╔╦╗╦ ╦╔═╗╦═╗╦╔═╔═╗
╠╩╗║ ║ ╚═╗╠═╣╠═╣╠╦╝║╣ ╚═╗  ║║║║╣  ║ ║║║║ ║╠╦╝╠╩╗╚═╗
╚═╝╩ ╩ ╚═╝╩ ╩╩ ╩╩╚═╚═╝╚═╝  ╝╚╝╚═╝ ╩ ╚╩╝╚═╝╩╚═╩ ╩╚═╝

LIQUIDITY POOL MAPPER
"""

# GLOBAL CONSTANTS

# True prints raw data in terminal
DEV = False
# Light or Dark Background
DARK_THEME = True
# Use these bitshares nodes to gather rpc data
NODES = [
    "wss://api.bts.mobi/wss",
    "wss://newyork.bitshares.im/ws",
    "wss://api.bitshares.info",
    "wss://bts.open.icowallet.net/ws",
    "wss://api.dex.trading/wss",
    "wss://eu.nodes.bitshares.ws/wss",
    "wss://api-us.61bts.com/wss",
    "wss://cloud.xbts.io/ws",
    "wss://dex.iobanker.com/wss",
    "wss://hongkong.bitshares.im/wss",
    "wss://bts.mypi.win/wss",
    "wss://public.xbts.io/wss",
    "wss://node.xbts.io/wss",
    "wss://btsws.roelandp.nl/wss",
    "wss://singapore.bitshares.im/wss",
    "wss://api.bts.btspp.io:10100/wss",
    "wss://api.btslebin.com/wss",
]
# menu option to exclude these from the map
DETACH = [
    "1.3.6008",  # NSNFT
    "1.3.6009",  # NUISHI
]
# menu option to network map only these pools
ATTACH = [
    # HONEST pools:
    "1.19.43",  # USD:BTS
    "1.19.65",  # BTC:USD
    "1.19.66",  # BTC:BTS
    "1.19.289",  # USDSHORT:USD
    "1.19.290",  # BTCSHORT:BTC
    "1.19.291",  # USDSHORT:BTS
    "1.19.292",  # BTCSHORT:BTS
    "1.19.293",  # BTCSHORT:USDSHORT
]
# PyVis Buttons
BUTTONS = ["physics", "edges", "nodes"]
# when making object rpc calls this many objects per call
CHUNK = 10
# viewport height of network map
HEIGHT = 90
# asset groups
COLOR = [
    "#8e7cc3",  # purple
    "#76a5af",  # teal
    "#6fa8dc",  # blue
    "#c27ba0",  # pink
    "#93c47d",  # green
    "#ffd966",  # yellow
    "#f6b26b",  # orange
    "#888888" if DARK_THEME else "#222222",  # grey
    "#bc9b05",  # gold
    "#e06666",  # red
]
# scale the line thickness
SCALE_WEIGHT = 80
# detach the unfunded pools from the network map
DETACH_UNFUNDED = False
