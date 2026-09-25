# -*- coding: utf-8 -*-
"""Inhakers en de drie vast te pinnen posts, 25 september 2026.
Inhakers gebruiken het De Vraag-sjabloon, met de datum als kicker. Ze staan in
een memeslot en krijgen de vaste disclaimer als eerste reactie."""

D = ("Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of "
     "heb je klachten? Overleg met je huisarts of apotheker.")
ST = ["#vrouwenonderelkaar", "#mijnpilnu"]

INHAKERS = [
 {"id": "i01", "date": "2026-09-26", "field": "var(--peach)",
  "kicker": "26 september · wereld anticonceptiedag",
  "lines": ["Past je <em>anticonceptie</em>", "nog bij je leven", "van nu?"],
  "subject": "Wereld Anticonceptiedag: past je anticonceptie nog bij je leven van nu?",
  "caption": ("Vandaag is het Wereld Anticonceptiedag. Een goed moment voor een vraag die bijna "
   "niemand zichzelf stelt: past de anticonceptie die je ooit hebt gekozen nog bij je leven van nu?\n\n"
   "Veel vrouwen gebruiken jarenlang hetzelfde middel, terwijl er in de tussentijd genoeg verandert. "
   "Momenten om er opnieuw naar te kijken:\n\n"
   "Je vergeet vaker een pil dan je zou willen.\n"
   "Je hebt klachten die je inmiddels normaal bent gaan vinden.\n"
   "Je geeft borstvoeding, of je komt richting de overgang.\n"
   "Je wilt over een tijdje zwanger worden, of juist helemaal niet meer.\n\n"
   "Herken je jezelf hierin? Bespreek het bij je volgende afspraak met je huisarts.\n\n"
   "Bewaar 'm voor als je die afspraak maakt."),
  "tags": ["#wereldanticonceptiedag", "#anticonceptie", "#depil"] + ST, "first_comment": D},

 {"id": "i02", "date": "2026-10-17", "field": "var(--sky)",
  "kicker": "18 oktober · wereld menopauzedag",
  "lines": ["Merk je de <em>overgang</em>", "als je de pil", "slikt?"],
  "subject": "Wereld Menopauzedag: merk je de overgang als je de pil slikt?",
  "caption": ("Morgen is het Wereld Menopauzedag. Een vraag die we vaak tegenkomen: merk je de "
   "overgang eigenlijk wel als je de pil slikt?\n\n"
   "Vaak minder dan je zou verwachten. Een combinatiepil regelt je bloedingen en levert zelf "
   "hormonen, en kan daardoor klachten zoals een onregelmatige cyclus of opvliegers deels "
   "maskeren. Je kunt dus al in de overgang zitten zonder dat je het goed merkt.\n\n"
   "Ben je rond de 45 of ouder en gebruik je hormonale anticonceptie? Bespreek dan met je "
   "huisarts tot wanneer je die nog nodig hebt en wat een logisch moment is om te stoppen.\n\n"
   "Stuur 'm door naar wie hier ook mee bezig is."),
  "tags": ["#overgang", "#wereldmenopauzedag", "#anticonceptie"] + ST, "first_comment": D},

 {"id": "i03", "date": "2026-10-24", "field": "var(--mint)",
  "kicker": "vannacht gaat de klok een uur terug",
  "lines": ["Moet je <em>pil</em> nu", "een uur", "opschuiven?"],
  "subject": "Wintertijd: moet je pil een uur opschuiven?",
  "caption": ("Vannacht gaat de klok een uur terug. Moet je je pil dan ook anders gaan innemen?\n\n"
   "Nee, dat hoeft niet. Neem je pil gewoon op je vaste tijd volgens de nieuwe klok. Eén uur "
   "verschil valt ruim binnen de marge: bij de meeste pillen is die twaalf uur, en ook bij "
   "pillen met een krappere marge van drie uur zit je met één uur nog goed.\n\n"
   "Bewaar 'm voor maart, als de klok weer vooruit gaat."),
  "tags": ["#wintertijd", "#depil", "#anticonceptie"] + ST, "first_comment": D},

 {"id": "i04", "date": "2026-12-01", "field": "var(--blush)",
  "kicker": "1 december · wereld aidsdag",
  "lines": ["Beschermt de pil", "je ook tegen", "<em>soa's</em>?"],
  "subject": "Wereld Aidsdag: beschermt de pil ook tegen soa's?",
  "caption": ("Vandaag is het Wereld Aidsdag. Tijd voor een vraag met een kort antwoord: beschermt "
   "de pil je ook tegen soa's?\n\n"
   "Nee. De pil, de ring, de pleister, het spiraaltje en het staafje beschermen tegen "
   "zwangerschap, maar niet tegen soa's zoals chlamydia of hiv. Condooms zijn het enige "
   "anticonceptiemiddel dat daar wel tegen beschermt.\n\n"
   "Heb je een nieuwe partner, of twijfel je? Laat je testen bij je huisarts of bij het "
   "Centrum Seksuele Gezondheid van de GGD.\n\n"
   "Stuur 'm door naar wie dit wel even mag horen."),
  "tags": ["#wereldaidsdag", "#soa", "#condoom"] + ST, "first_comment": D},

 {"id": "i05", "date": "2026-12-12", "field": "var(--peach)",
  "kicker": "de feestdagen komen eraan",
  "lines": ["Valt je <em>stopweek</em>", "precies met", "kerst?"],
  "subject": "Feestdagen: valt je stopweek precies met kerst?",
  "caption": ("Kerst komt eraan. Tijd om even in je strip te kijken: valt je stopweek precies op "
   "de feestdagen?\n\n"
   "Bij veel combinatiepillen kun je de stopweek overslaan door meteen met een nieuwe strip te "
   "beginnen. De bloeding in je stopweek is een onttrekkingsbloeding en geen echte menstruatie, "
   "dus medisch gezien is daar geen bezwaar tegen.\n\n"
   "Let op: bij pillen met verschillende fases of met placebopillen in de strip werkt dit anders. "
   "Kijk in je bijsluiter of overleg met je huisarts als je het niet zeker weet.\n\n"
   "En check meteen of je genoeg strips in huis hebt, zeker als je een week doorslikt.\n\n"
   "Bewaar 'm voor je volgende strip."),
  "tags": ["#stopweek", "#feestdagen", "#depil"] + ST, "first_comment": D},
]

VAST = [
 {"id": "p1", "date": "2026-09-29", "theme": "indigo", "kicker": "over ons",
  "lines": ["Een echte apotheek.", "Alleen dan <em>online</em>."],
  "subject": "Vastgezet 1: wie we zijn",
  "slides": [
   ("1", "Een apotheek <em>in Hardenberg</em>",
    "MijnPil.nu is een echte apotheek, gevestigd in Hardenberg. We staan in het register van "
    "online aanbieders van het ministerie van VWS, in de categorie die receptgeneesmiddelen "
    "mag leveren.",
    "201905151830-Mijn-pil-visuals_Apotheek - green.png"),
   ("2", "Elke bestelling <em>gecontroleerd</em>",
    "Een apothekersassistente stelt je bestelling samen. Daarna controleert de apotheker alles "
    "en tekent af. Pas dan gaat je pakket de deur uit.",
    "201905151830-Mijn-pil-visuals_Verificatie akkoord - orange.png"),
  ],
  "caption": ("Wie zit er eigenlijk achter @mijnpil.nu? Een echte, geregistreerde apotheek, "
   "gevestigd in Hardenberg. We staan in het register van online aanbieders van het ministerie "
   "van VWS.\n\n"
   "Online bestellen betekent bij ons niet dat er minder gecontroleerd wordt. Elke bestelling "
   "wordt samengesteld door een apothekersassistente en gecontroleerd door de apotheker.\n\n"
   "Op dit account vind je heldere uitleg over anticonceptie, je cyclus en alles eromheen. "
   "En af en toe iets om naar je vriendinnen door te sturen."),
  "tags": ["#apotheek", "#anticonceptie"] + ST, "first_comment": None},

 {"id": "p2", "date": "2026-10-06", "theme": "roze", "kicker": "zo werkt het",
  "lines": ["Je anticonceptie,", "<em>thuisbezorgd</em>."],
  "subject": "Vastgezet 2: zo werkt bestellen",
  "slides": [
   ("1", "Je hebt al <em>een recept</em>",
    "Wij schrijven geen anticonceptie voor. Je bestelt wat je al gebruikt, of waarvoor je al "
    "een recept hebt.",
    "201905151830-Mijn-pil-visuals_Recept - red.png"),
   ("2", "De eerste keer: <em>een foto</em>",
    "Bij je eerste bestelling upload je een foto van je recept, of van een doosje met "
    "apotheeketiket. De apotheker controleert dat.",
    "201905151830-Mijn-pil-visuals_Verification foto 1 - purple.png"),
   ("3", "Snel en <em>discreet</em>",
    "Op werkdagen voor 15:00 besteld, dan versturen we het dezelfde dag. Altijd discreet "
    "verzonden.",
    "Pakketje-bezorgen_1-8.png"),
   ("4", "Daarna: gewoon <em>nabestellen</em>",
    "Bij een volgende bestelling hoef je niets opnieuw aan te leveren. Liever niet zelf "
    "opletten? Laat je bestelling dan automatisch herhalen.",
    "201905151830-Mijn-pil-visuals_Verification foto 2 - green.png"),
  ],
  "caption": ("Hoe werkt bestellen bij MijnPil.nu? In het kort: je bestelt de anticonceptie die je "
   "al gebruikt, en wij sturen het naar je toe.\n\n"
   "Wij schrijven zelf niets voor. Bij je eerste bestelling vragen we een foto van je recept, of "
   "van een doosje met apotheeketiket, en die controleert de apotheker. Daarna kun je gewoon "
   "nabestellen zonder opnieuw iets aan te leveren, of je bestelling automatisch laten herhalen.\n\n"
   "Op werkdagen voor 15:00 besteld is dezelfde dag verstuurd, en altijd discreet verzonden.\n\n"
   "Alles begint via de link in onze bio."),
  "tags": ["#anticonceptie", "#depil", "#apotheek"] + ST, "first_comment": None},

 {"id": "p3", "date": "2026-10-13", "theme": "lavendel", "kicker": "welkom",
  "lines": ["Van je eerste pil", "tot de <em>overgang</em>."],
  "subject": "Vastgezet 3: waar we het hier over hebben",
  "slides": [
   ("1", "<em>Anticonceptie</em>",
    "De pil, de ring, de pleister, het spiraaltje en de prik: wat het is, hoe het werkt en wat "
    "je kunt verwachten.",
    "Ring - 2.png"),
   ("2", "Hormoonvrije <em>anticonceptie</em>",
    "Liever zonder hormonen? Het koperspiraaltje en condooms, en wat je moet weten als je "
    "zonder hormonen wilt kiezen.",
    "Koppel-non-binair_1-8.png"),
   ("3", "<em>Menstruatie</em>",
    "Krampen, doorlekken, je cyclus bijhouden en wat wel en niet normaal is. De dingen die je "
    "elke maand meemaakt.",
    "Ongesteldheidsklachten-8.png"),
   ("4", "Intieme <em>gezondheid</em>",
    "Een schimmelinfectie, droogheid of een gevoelige huid. Zonder schaamte, want je bent echt "
    "niet de enige.",
    "Self-care-kleur-8.png"),
   ("5", "Zwanger worden <em>en overgang</em>",
    "Stoppen met de pil, je vruchtbare dagen en later de overgang. Wat je nodig hebt verandert, "
    "en wij bewegen mee.",
    "Sterke-vrouw-8.png"),
  ],
  "caption": ("Nieuw hier? Welkom bij MijnPil.nu. Hier vind je uitleg over alles wat met je "
   "cyclus en je hormonen te maken heeft, van je eerste pil tot de overgang: anticonceptie, "
   "hormoonvrije anticonceptie, menstruatie, intieme gezondheid, zwanger worden en de overgang.\n\n"
   "Op maandag, woensdag en vrijdag delen we uitleg waar je echt iets aan hebt. Op dinsdag, "
   "donderdag en zaterdag posts om naar je vriendinnen door te sturen, want sommige dingen "
   "herkent iedere vrouw.\n\n"
   "Wat we hier delen is algemene informatie en geen medisch advies. Heb je een vraag over je "
   "eigen situatie? Je huisarts is daar de beste plek voor.\n\n"
   "Post je zelf iets herkenbaars? Gebruik #vrouwenonderelkaar, de leukste delen we in onze "
   "stories."),
  "tags": ["#anticonceptie", "#cyclus"] + ST, "first_comment": None},
]
