import markdown
import requests
import glob
from PIL import Image
import os
import json


def main():
    URL = "https://raw.githubusercontent.com/bitshares/awesome-bitshares/master/README.md"


    data = requests.get(URL).text
    html = markdown.markdown(data)

    html = html.replace('src="logo.svg"', 'src="./images/bitshares_logo.svg"')
    html = html.replace('<a href="', '<a target="_blank" href="')
    img = (
        '<center><p><img src="./images/bitshares_logo.svg" alt="BitShares Blockchain" align="center"'
        ' style="width:25vw"></p></center>'
    )
    # html = img + html.split("<h2>Awesome BitShares Blockchain</h2>")[1]
    # "BTS:BTC": [
    #     "gateio",
    #     "bittrex",
    #     "binance",  # WARN: requires NON-US VPN
    #     "poloniex",
    #     "hitbtc",
    # ],


    CEX = """
    <ul>
    <li><a class=".awesome" target="_blank" href="https://www.gate.io/trade/BTS_BTC">GateIO BTS:BTC</a></li>
    <li><a class=".awesome" target="_blank" href="https://www.gate.io/trade/BTS_USDT">GateIO BTS:USDT</a></li><br>
    <li><a class=".awesome" target="_blank" href="https://global.bittrex.com/trade/bts-btc">Bittrex BTS:BTC</a></li><br>
    <li><a class=".awesome" target="_blank" href="https://www.binance.com/en/trade/BTS_BTC">Binance BTS:BTC</a></li>
    <li><a class=".awesome" target="_blank" href="https://www.binance.com/en/trade/BTS_USDT">Binance BTS:USDT</a></li><br>
    <li><a class=".awesome" target="_blank" href="https://poloniex.com/spot/BTS_USDT">Poloniex BTS:USDT</a></li>
    <li><a class=".awesome" target="_blank" href="https://poloniex.com/spot/BTS_BTC">Poloniex BTS:BTC</a></li><br>
    <li><a class=".awesome" target="_blank" href="https://hitbtc.com/bts-to-btc">HitBTC BTS:BTC</a></li>
    </ul>
    """

    defaultpage = (
        "Warning: Being listed here is not endorsement nor does it provide any credibility"
        " to these projects. Even though the authors of this list have high quality"
        " standards, limited resources prevent them from keeping this list up-to-date with"
        " respect to their credibility. Use this list at your own risk and do your own"
        " research!"
    )

    html = ["<h3>" + i for i in html.split("<h3>")][1:]


    html = {i.split("</h3>")[0][4:]: i.split("</h3>", 1)[1] for i in html}


    text = (  # <link rel='stylesheet' href='main.css'></link>"
        '<DOCTYPE html>\n<html>\n<body>\n<link rel="stylesheet" href="main.css">\n<link'
        ' rel="stylesheet" href="awesomestyle.css">\n<script type="text/javascript"'
        ' src="tabs.js"></script>\n'
    )
    text += img

    for idx, htm in enumerate(html):
        if idx % 5 == 0:
            if idx:
                text += "</div>\n"
            text += (
                '<div class="awesometab" style="position:relative;flex: 1;display: flex;'
                ' width: 100%;">\n'
            )
        text += (
            '<button class="tablinks" onclick="switch_tab(event,'
            f" '{idx}')\">{htm}</button>\n"
        )
    text += "</div>\n"
    # print(idx)


    """
        <button class="tablinks" onclick="switch_tab(event, '1')">Pools</button>
        <button class="tablinks" onclick="switch_tab(event, '2')">Home</button>
        <button class="tablinks" onclick="switch_tab(event, '3')">Explorer</button>
        <button class="tablinks" onclick="switch_tab(event, '4')">Market Cap</button>
        <button class="tablinks" onclick="switch_tab(event, '5')">Links</button>
        <button class="tablinks" onclick="switch_tab(event, '6')">Team</button>
        <button class="tablinks" onclick="switch_tab(event, '7')">Nodes</button>
    </div>"""

    for idx, htm in enumerate(html):
        text += f'<div id="{idx}" class="tabcontent">'
        if htm != "Exchanges":
            text += html[htm].split("<h2")[0]
        else:
            text += "<center><h2>Bitshares Decentralized Exchanges</h3></center>"
            text += html[htm].split("<h2")[0]
            text += "<br><br><center><h2>Centralized Exchanges</h3></center>"
            text += CEX
        text += "</div>"

    text = text.replace("<a ", '<a class=".awesome" ')

    # print(text)


    # print(json.dumps(html, indent=4))


    # exit()

    text = text + "</body>\n</html>"


    print()

    with open("awesome.html", "w") as handle:
        handle.write(text)
        handle.close()

    print("generating GIF...")

    # exit()

    # filepaths
    fp_in = "./latency_maps/map_*.png"
    fp_out = "./images/map.gif"

    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif

    img_paths = sorted(glob.glob(fp_in))
    print(img_paths)

    while len(img_paths) > 20:
        to_remove = img_paths.pop(0)
        os.remove(to_remove)


    imgs = (Image.open(f) for f in sorted(glob.glob(fp_in)))
    img = next(imgs)  # extract first image from iterator
    img.save(
        fp=fp_out,
        format="GIF",
        append_images=imgs,
        save_all=True,
        duration=333 + (1 / 3),
        loop=0,
    )
