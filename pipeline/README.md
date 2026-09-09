# Publicatiepijplijn

Rendert één post uit `queue.json`, zet het beeld op de publieke host, en print
wat er gepubliceerd moet worden.

## Een run

    export MIJNPIL_GH_TOKEN=<token uit claude/instagram-toegang-en-beeldhost.md>
    python3 pipeline/run.py

Zonder argumenten pakt hij de post van vandaag (Europe/Amsterdam). Staat er
niets voor vandaag in de queue, dan stopt hij met "NO POST TODAY".

    python3 pipeline/run.py --date 2026-09-14      # een specifieke dag
    python3 pipeline/run.py --date 2026-09-14 --dry-run   # renderen, niet pushen

## Wat er uit komt

Tussen `BEGIN PUBLISH` en `END PUBLISH` staat een JSON-blok met de post-id, de
publieke URL's, de caption inclusief hashtags, en de disclaimer die als eerste
reactie onder de post hoort. De aanroepende sessie publiceert dat via Windsor,
want daar is een MCP-tool voor nodig die dit script niet kan bereiken.

**Wacht na de push ongeveer 100 seconden** voordat je publiceert. GitHub Pages
moet eerst opnieuw bouwen, anders haalt Instagram een URL op die nog niet
bestaat.

## Benodigdheden

Python met Playwright en Chromium, plus ffmpeg. Beide staan standaard in de
werkomgeving. De lettertypen zitten in `fonts/`, dus er is geen npm nodig.

## Bestanden

    base.py       paginashell: merkpalet, Athiti en Roboto Slab, animatiebasis
    concepts.py   de zes beeldconcepten
    anim.py       animatie naar frames naar MP4
    produce.py    queue-item naar afgewerkte bestanden
    run.py        één run: renderen, pushen, printen wat er gepubliceerd wordt
    queue.json    de contentqueue

`REST` in `concepts.py` bepaalt hoelang een scherm stil blijft staan nadat het
laatste element is ingekomen. Staat op 1,5 seconde.
