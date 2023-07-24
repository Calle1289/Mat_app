# Ingredienser
frukt = {"banan": {"pris": 5, "vikt": 180}}  # vikt i gram
mejeri = {
    "proteinmjölk": {"pris": 18.9, "vikt": 500},
    "ägg": {"pris": 39, "vikt": 540},
    "mjölk_röd": {"pris": 22.50, "vikt": 1000},
}
bakning = {
    "havregryn": {"pris": 17.9, "vikt": 750},
    "cacao": {"pris": 31.9, "vikt": 200},
    "jordnötssmör": {"pris": 47, "vikt": 340},
}
annat = {"proteinpulver": {"pris": 259, "vikt": 1000}}
kött = {"kyckling_innerfiler": {"pris": 63, "vikt": 700}}
grönsaker = {
    "gurka": {"pris": 10, "vikt": 277},
    "selleri": {"pris": 20, "vikt": 350},
    "babyplommontomater": {"pris": 20, "vikt": 250},
    "isbergssallad": {"pris": 12, "vikt": 440},
    "rödlök": {"pris": 3.6, "vikt": 150},
    "citron": {"pris": 7.9, "vikt": 200},
}

# Kategorier
ingredienser = frukt | mejeri | bakning | annat | kött | grönsaker

# Recept
recept = {
    "proteinbar": [
        ("cacao", 44),
        ("mjölk_röd", 365),
        ("havregryn", 182),
        ("proteinpulver", 336),
        ("ägg", 100),
        ("banan", 100),
        ("jordnötssmör", 128),
        ("kanel", 6),
    ],
    "kycklingsallad": [
        ("kyckling_innerfiler", 200),
        ("gurka", 50),
        ("babyplommontomater", 60),
        ("selleri", 30),
        ("isbergssallad", 80),
        ("rödlök", 75),
        ("citron", 10),
    ],
}
