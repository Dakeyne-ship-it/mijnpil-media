# Publicatiepijplijn Instagram

Alles wordt vooraf gerenderd en op de beeldhost gezet. De geplande taken
renderen niets: ze lezen alleen de publicatiedocumenten in `docs/` en
publiceren via Windsor.

## Bronnen

    queue.json            uitlegpijler (ma, wo, vr), met per reel een omslag
    uitleg_batch2.py      tekst van uitlegbatch 2 (9 nov t/m 15 jan)
    memes_source.py       de regels van Onder ons
    inhakers.py           inhakers en de drie vast te pinnen posts
    build_meme_queue.py   bouwt queue-memes.json: volgorde op thema, kleur op rasterpositie
    queue-memes.json      di, do, za: memes, inhakers en vastgezette posts

## Beeld

    base.py        paginashell: merkpalet, Athiti en Roboto Slab
    concepts.py    alle sjablonen
    illu.py        bibliotheekillustraties klaarmaken (lavendel omzetten, vlak doortrekken)
    anim.py        animatie naar frames naar MP4
    produce.py     queue-item naar afgewerkte bestanden in out/production/

    python3 produce.py w09-ma m19          # losse posts
    python3 produce.py --omslag w05-ma     # alleen de reelomslag opnieuw

## Documenten

    build_uitleg_doc.py   -> docs/instagram-publiceerklaar-week-1-2.md
    build_meme_doc.py     -> docs/instagram-onder-ons-publiceerklaar.md

## Na een wijziging

1. Bron aanpassen, `build_meme_queue.py` draaien als de memeslots veranderen.
2. `produce.py` voor de betrokken posts, bestanden naar `ig/<jaar>/<maand>/`.
3. Beide documenten opnieuw bouwen, committen en pushen.

Pushen gaat met het token als header, zie `claude/instagram-toegang-en-beeldhost.md`.
Wacht na een push ongeveer 100 seconden voordat Instagram een nieuw bestand ophaalt.

## Tempo

`REST` in `concepts.py`, nu 1,0 seconde, bepaalt hoe lang een scherm stil staat
nadat het laatste element is ingekomen.
