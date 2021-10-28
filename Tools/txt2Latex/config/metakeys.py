# Schlüssel für metaangaben, die im Titelblock eines Liedes Vorkommen dürfen. siehe auch die Definition in lib/Heuristik/Heuristik.py

metakeys = dict(  # Siehe auch liste in Heuristik.py
    ww='wuw',  # Worte und weise
    wuw='wuw',
    jahr='jahr',  # jahr des Liedes
    j='jahr',
    mel='mel',  # Autor der Melodie
    melodie='mel',
    weise='mel',
    melj='meljahr',  # Jahr der Melodie
    meljahr='meljahr',
    weisej='meljahr',
    weisejahr='meljahr',
    txt='txt',  # Autor des Textes
    text='txt',
    worte='txt',
    txtj='txtjahr',  # Jahr des Textes
    textj='txtjahr',
    txtjahr='txtjahr',
    textjahr='txtjahr',
    wortejahr='txtjahr',
    wortej='txtjahr',
    alb='alb',  # Album, auf dem das Lied erschienen ist.
    album='alb',
    lager='lager',  # Lager, auf dem / für das das Lied geschrieben
    tonart='tonart',  # originaltonart
    capo='capo',    # vorschlag für das setzen des Capos
    cap='capo',     # TODO: in Latex setzen
    key='tonart',
    bo='bo',  # Seite im Bock
    bock='bo',
    cp='cp',    # Seite iom Codex Pathomomosis
    codex='cp',
    pf1='pfi',  # Seite im Pfadiralala1
    pfi='pfi',
    pf='pfi',
    pf2='pfii',  # Seite im Pfadiralala2
    pfii='pfii',
    pf3='pfiii',  # Seite im Pfadiralala3
    pfiii='pfiii',
    pf4='pfiv',
    pfiiii='pfiv',
    pfiv='pfiv',
    pf4p='pfivp',
    pfiiiip='pfivp',
    pfivp='pfivp',
    ju='ju',  # Seite in der Jurtenburg
    jurten='ju',
    jurtenburg='ju',
    gruen='gruen',  # Seite Im Grünen (Liederbuch)
    grün='gruen',
    gruenes='gruen',
    grünes='gruen',
    kss4='kssiv',  # Seite in Kinder-Schoko-Songs 4
    kssiv='kssiv',
    kssiiii='kssiv',
    siru='siru',  # Seite in Die singende Runde
    biest='biest',  # Seite im Biest
    eg='eg',  # Seite im evangelischen Gesangbuch
    evg='eg',
    egp='egplus',  # Seite Im evangelischen Gesangbuch plus
    evgp='egplus',
    egplus='egplus',
    evgplus='egplus',
    tf='tf',
    turm='tf',
    turmfalke='tf',
    gb='gb',
    gnorken='gb',
    gnorkenbüdel='gb')
