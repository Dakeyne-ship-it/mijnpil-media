# Instagram: hoe het draait

Bijgewerkt 25 september 2026. Twee pijlers, zes posts per week:

- **Uitleg** op maandag, woensdag en vrijdag, gepland tot en met vrijdag 15 januari 2027.
  Vrijdag 25 december en 1 januari zijn bewust vrij.
- **Onder ons** op dinsdag, donderdag en zaterdag, gepland tot en met dinsdag
  16 februari 2027. In deze slots staan ook de inhakers en de drie vast te pinnen posts.

## De documenten

Alles staat in de map `docs/` van de repo `Dakeyne-ship-it/mijnpil-media`, en als kopie
in de map `claude/` op de computer van Alexander.

| Document | Gelezen door |
|---|---|
| `instagram-publiceerklaar-week-1-2.md` | de uitlegtaken (ma, wo, vr) |
| `instagram-onder-ons-publiceerklaar.md` | de Onder ons-taken (di, do, za) |
| `instagram-publicatie-hoe-het-draait.md` | dit overzicht, door niemand automatisch |

De geplande taken lezen eerst de versie in de repo en vallen terug op de lokale kopie
als GitHub niet bereikbaar is. Wijzigingen hoeven dus alleen in de repo.

## De geplande taken

| Taak | Schema | Rol |
|---|---|---|
| Instagram mijnpil.nu, maandag 19:30 | `CRON_TZ=Europe/Amsterdam 30 19 * * 1` | reel |
| Instagram mijnpil.nu, woensdag 12:30 | `CRON_TZ=Europe/Amsterdam 30 12 * * 3` | carrousel |
| Instagram mijnpil.nu, vrijdag 19:00 | `CRON_TZ=Europe/Amsterdam 0 19 * * 5` | post of reel |
| Onder ons, dinsdag 20:00 | `CRON_TZ=Europe/Amsterdam 0 20 * * 2` | meme, inhaker of vaste post |
| Onder ons, donderdag 20:00 | `CRON_TZ=Europe/Amsterdam 0 20 * * 4` | meme, inhaker of vaste post |
| Onder ons, zaterdag 11:00 | `CRON_TZ=Europe/Amsterdam 0 11 * * 6` | meme, inhaker of vaste post |
| Instagram mijnpil.nu, reacties | `CRON_TZ=Europe/Amsterdam 0 9,21 * * *` | reacties beantwoorden en modereren |

De tijdzone staat in de cron zelf, dus wintertijd op 25 oktober gaat vanzelf goed.

**Een uitlegrun** zoekt de post van vandaag, publiceert hem via Windsor (reels met
`cover_url`), zet de disclaimer als eerste reactie en rapporteert het bereik.

**Een Onder ons-run** zoekt de post van vandaag, publiceert hem (`create_image_post`, of
`create_carousel_post` bij een vaste post), plaatst de eerste reactie als die erbij
staat, plaatst de story als die erbij staat, en meldt bij een vaste post dat die
handmatig vastgepind moet worden.

**Een reactierun** volgt `claude/instagram-reactiebeleid.md`. Verwijderen gebeurt nooit,
spam wordt verborgen.

## Wat je in het raster ziet

Elke categorie heeft een eigen herkenbare tegel, zodat het raster wisselt:

| Categorie | Tegel |
|---|---|
| Onder ons (meme) | kleurvlak met een gekanteld kaartje, regel gecentreerd, logo op het kaartje |
| Reel (Klare Taal, Uit de DM, De Cyclus) | illustratie uit de bibliotheek, titel onder een witte boog |
| Mythe of feit | blush met doorgestreepte mythe, dan indigo met het feit |
| Anatomie van… | diagram op millimeterpapier |
| De Vraag en inhakers | licht kleurvlak met cirkelmotief, grote vraag |
| Vastgezet | kleurvlak met label en titel, logo in een witte pil |

Regels die hierbij horen:

- **Niets in de linkeronderhoek.** Daar legt Instagram het weergavetal over de miniatuur.
- **Niets bovenin een story.** Daar staan de naam van de afzender en de voortgangsbalk.
  De kicker staat daarom direct boven de vraag.
- **Reelomslagen binnen de 3:4-uitsnede** (y 240 tot 1680 van 1920). De boog begint pas
  onder de illustratie, zodat het figuur helemaal zichtbaar blijft.
- **Memekleur op rasterpositie.** Een meme krijgt nooit de kleur van een tegel ernaast,
  erboven of eronder, en nooit dezelfde kleur als de vorige meme.
- **Weekafstemming.** Een meme gaat nooit over het onderwerp van de uitlegposts of de
  inhaker van die week. De botsingen staan per week in `BOTS` in
  `pipeline/build_meme_queue.py`.
- **Illustraties** komen uit `library/illustraties/`. Het oude lavendel wordt automatisch
  omgezet naar het huidige. Niet gebruiken: de bezorgbus, want die heeft nog het oude logo.
  Niet twee keer dezelfde vrouw in reels die dicht bij elkaar staan.

## Inhakers

| Datum | Id | Haak |
|---|---|---|
| za 26 sep | i01 | Wereld Anticonceptiedag |
| za 17 okt | i02 | Wereld Menopauzedag (18 okt) |
| za 24 okt | i03 | Wintertijd |
| di 1 dec | i04 | Wereld Aidsdag |
| za 12 dec | i05 | Stopweek en de feestdagen |

Voor de volgende batch: Valentijnsdag, 8 maart, de zomertijd eind maart en 28 mei
Wereld Menstruatiedag.

## De drie vastgezette posts

| Datum | Id | Onderwerp |
|---|---|---|
| di 29 sep | p1 | Een echte apotheek in Hardenberg, elke bestelling gecontroleerd |
| di 6 okt | p2 | Zo werkt bestellen: recept, foto, snel en discreet, nabestellen |
| di 13 okt | p3 | Van je eerste pil tot de overgang: de vijf thema's |

Na publicatie handmatig vastpinnen. Instagram zet de laatst vastgepinde post meestal vooraan. Wil je van links naar rechts p1, p2, p3, maak dan na 13 oktober de vastzetting van alle drie ongedaan en pin ze opnieuw in de volgorde p3, p2, p1.

## Uitlegbatch 2 (9 november tot en met 15 januari)

Maandag Klare Taal, woensdag Mythe of feit of Anatomie, vrijdag De Vraag of Uit de DM.
Anticonceptie blijft de kern, met uitstapjes naar cyclus, intieme gezondheid en
kinderwens. Nieuwe Anatomie-platen: de ring en de minipil.

## Wat er wanneer moet gebeuren

**Eind november:** de cijfers van de eerste twee maanden bekijken, per categorie. Wat
telt: bereik buiten de volgers, doorsturen per bereik, bewaren per bereik en nieuwe
volgers per post.

**Half december:** uitlegbatch 3 schrijven voor vanaf 18 januari, en besluiten of Onder
ons doorloopt na 16 februari. Van de tachtig geschreven regels zijn er negenenvijftig in
gebruik.

**Eén keer per week, handmatig:** kijken wat er onder #vrouwenonderelkaar is gepost en
het beste daarvan in stories delen met credit.

## Openstaand

De reels hebben geen audio: de Instagram-API kan gelicentieerde muziek niet meesturen.
DM's zijn niet automatisch te lezen: Windsor heeft geen toegang tot de inbox.
