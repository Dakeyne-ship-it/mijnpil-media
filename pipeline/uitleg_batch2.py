# -*- coding: utf-8 -*-
"""Uitlegbatch 2: 9 november 2026 tot en met 15 januari 2027.
Geschreven 25 september 2026. Vrijdag 25 december en 1 januari bewust vrij.

Elke reel heeft een `cover`: illustratie uit library/illustraties plus de regels
voor de omslag met boog. Rotatie per week: maandag Klare Taal (reel), woensdag
Mythe of feit of Anatomie (carrousel), vrijdag De Vraag (post) of Uit de DM (reel).
"""
ST = ["#vrouwenonderelkaar", "#mijnpilnu"]


def kt(i, date, subject, cover, scenes, caption, tags):
    return {"id": i, "date": date, "slot": "ma 19:30", "concept": "klare_taal",
            "format": "reel", "disclaimer": True, "subject": subject,
            "cover": {"img": cover, "lines": scenes[0]["lines"]},
            "scenes": scenes, "caption": caption, "tags": tags + ST}


def mf(i, date, subject, mythe, feit, bron, caption, tags):
    return {"id": i, "date": date, "slot": "wo 12:30", "concept": "mythe_feit",
            "format": "carousel", "disclaimer": True, "subject": subject,
            "mythe_lines": mythe, "feit_statement": feit, "feit_source": bron,
            "caption": caption, "tags": tags + ST}


def ana(i, date, subject, variant, caption, tags):
    return {"id": i, "date": date, "slot": "wo 12:30", "concept": "anatomie",
            "format": "carousel", "disclaimer": True, "subject": subject,
            "variant": variant, "caption": caption, "tags": tags + ST}


def dv(i, date, subject, lines, field, caption, tags):
    return {"id": i, "date": date, "slot": "vr 19:00", "concept": "de_vraag",
            "format": "image", "disclaimer": True, "subject": subject,
            "kicker": "Vraag van de week", "lines": lines, "field": field,
            "caption": caption, "tags": tags + ST}


def dm(i, date, subject, cover, cover_lines, vraag, antwoord, caption, tags):
    return {"id": i, "date": date, "slot": "vr 19:00", "concept": "uit_de_dm",
            "format": "reel", "disclaimer": True, "subject": subject,
            "cover": {"img": cover, "lines": cover_lines},
            "vraag": vraag, "antwoord": antwoord, "caption": caption, "tags": tags + ST}


def S(kind, lines, small=None):
    x = {"kind": kind, "lines": lines}
    if small:
        x["small"] = small
    return x


POSTS = [
# ------------------------------------------------------------ week 9
kt("w09-ma", "2026-11-09", "De anticonceptiering", "Ring - 3.png", [
    S("open", ["De <em>ring</em>,", "in het kort"]),
    S("mint", ["Drie weken in,", "één week uit"], "In de week zonder ring komt de bloeding."),
    S("peach", ["Je brengt 'm", "zelf in"], "Net zo makkelijk als een tampon."),
    S("pink", ["Eruit gevallen?"], "Afspoelen met lauw water en binnen drie uur terugdoen."),
    S("end", ["Niet elke dag", "<em>iets onthouden</em>"], "Daarom kiezen veel vrouwen ervoor."),
  ],
  "De anticonceptiering in het kort. Het is een zacht, buigzaam ringetje dat je zelf inbrengt en "
  "dat drie weken blijft zitten. Daarna haal je hem eruit, en in de week zonder ring komt je "
  "bloeding. Daarna begin je met een nieuwe.\n\n"
  "Het grote voordeel: je hoeft niet elke dag aan een pil te denken. Valt de ring er toch een keer "
  "uit, spoel hem dan af met lauw water en doe hem binnen drie uur terug. Duurde het langer, kijk "
  "dan in de bijsluiter wat je moet doen.\n\n"
  "Bewaar 'm als je twijfelt tussen de pil en de ring.",
  ["#anticonceptiering", "#anticonceptie", "#nuvaring"]),

mf("w09-wo", "2026-11-11", "Spiraaltje zonder kinderen",
   ["Een spiraaltje is", "alleen voor vrouwen", "met kinderen."],
   "Een spiraaltje kan <b>ook als je nog geen kinderen</b> hebt.",
   "Dat idee is achterhaald. Het plaatsen kan bij vrouwen die nog niet zwanger zijn geweest wat "
   "gevoeliger zijn, maar het spiraaltje werkt net zo goed. Je huisarts bespreekt met je wat past.",
   "Een spiraaltje alleen als je al kinderen hebt? Dat hoor je nog vaak, maar het klopt niet. Een "
   "spiraaltje is ook een goede keuze als je nog nooit zwanger bent geweest.\n\n"
   "Het plaatsen kan dan wat gevoeliger zijn, omdat de baarmoedermond nog wat nauwer is. Aan de "
   "werking verandert dat niets. En er zijn verschillende maten, dus je huisarts kan kijken welke "
   "het beste bij je past.\n\n"
   "Dacht jij dit ook?",
   ["#spiraaltje", "#anticonceptie", "#hormoonspiraal"]),

dm("w09-vr", "2026-11-13", "Overgegeven na je pil", "Hoofdpijn-voller-8.png",
   ["Overgegeven", "na je <em>pil</em>?"],
   "Ik moest vanochtend overgeven, een uurtje nadat ik mijn pil had genomen. Werkt hij nog?",
   "Moest je binnen <b>drie tot vier uur</b> na je pil overgeven? Dan telt het alsof je die pil "
   "bent vergeten.",
   "Overgeven kort na je pil is een vraag die we vaak krijgen, zeker in griepseizoen. Moest je "
   "binnen drie tot vier uur na inname overgeven, of heb je flinke diarree, dan heeft je lichaam "
   "de pil misschien niet goed opgenomen. Dan telt hij als vergeten.\n\n"
   "Wat je dan precies moet doen staat in je bijsluiter, want dat hangt af van je pil en van waar "
   "je in de strip zit. Twijfel je, overleg dan met je huisarts.\n\n"
   "Stuur 'm door naar wie net de griep heeft gehad.",
   ["#depil", "#pilvergeten", "#anticonceptie"]),

# ------------------------------------------------------------ week 10
kt("w10-ma", "2026-11-16", "Hormoonspiraal of koperspiraal", "Spiraaltje - 4.png", [
    S("open", ["Hormoon of", "<em>koper</em>?"]),
    S("mint", ["Hormoonspiraal"], "Geeft lokaal een beetje hormoon af. Je menstruatie wordt meestal lichter."),
    S("peach", ["Koperspiraal"], "Werkt zonder hormonen. Je menstruatie wordt vaak wat heviger."),
    S("pink", ["Allebei", "jarenlang"], "Hoe lang precies hangt af van het type."),
    S("end", ["Wat past", "<em>bij jou</em>?"], "Bespreek het met je huisarts."),
  ],
  "Hormoonspiraal of koperspiraal? Ze lijken op elkaar, maar werken anders. De hormoonspiraal "
  "geeft plaatselijk een kleine hoeveelheid hormoon af. Veel vrouwen krijgen daardoor een lichtere "
  "menstruatie, en soms blijft die helemaal weg.\n\n"
  "De koperspiraal werkt zonder hormonen. Je eigen cyclus blijft dus gewoon doorgaan, maar je "
  "menstruatie kan wel wat heviger of langer worden, vooral in de eerste maanden.\n\n"
  "Allebei blijven ze jarenlang zitten en hoef je er niets voor te onthouden. Welke het beste bij "
  "je past, bespreek je met je huisarts.",
  ["#spiraaltje", "#koperspiraal", "#hormoonspiraal"]),

ana("w10-wo", "2026-11-18", "De ring op ware grootte", "ring",
    "Anatomie van de anticonceptiering. Hij is groter dan veel mensen denken, ongeveer vijf en een "
    "halve centimeter doorsnee, maar zo dun en buigzaam dat je hem gewoon samenknijpt om in te "
    "brengen.\n\n"
    "Drie weken blijft hij zitten, daarna volgt een week zonder ring. In die week komt de bloeding, "
    "net als in de stopweek van de pil. Valt hij er een keer uit, spoel hem af en doe hem binnen "
    "drie uur terug.\n\n"
    "Bewaar 'm als je erover nadenkt.",
    ["#anticonceptiering", "#anticonceptie", "#nuvaring"]),

dv("w10-vr", "2026-11-20", "Prikpil en vruchtbaarheid",
   ["Word je minder", "vruchtbaar van", "de <em>prikpil</em>?"], "var(--mint)",
   "Word je minder vruchtbaar van de prikpil? Niet blijvend. Maar het kan na je laatste prik wel "
   "langer duren voordat je weer vruchtbaar bent dan bij de pil, soms een jaar of langer.\n\n"
   "Dat maakt de prikpil minder handig als je binnen afzienbare tijd zwanger wilt worden. Heb je "
   "een kinderwens voor de komende tijd, bespreek dan met je huisarts welk middel beter past.\n\n"
   "Stuur 'm door naar wie de prikpil gebruikt.",
   ["#prikpil", "#vruchtbaarheid", "#kinderwens"]),

# ------------------------------------------------------------ week 11
kt("w11-ma", "2026-11-23", "Condooms: wat vaak misgaat", "Koppel-2-8.png", [
    S("open", ["3 dingen die", "vaak misgaan", "met <em>condooms</em>"]),
    S("mint", ["Verkeerd", "bewaard"], "Warmte en een portemonnee maken ze zwakker. Let op de houdbaarheid."),
    S("peach", ["Glijmiddel", "op oliebasis"], "Dat tast latex aan. Kies water of siliconen."),
    S("pink", ["Twee over", "elkaar"], "Meer wrijving, meer kans dat er een scheurt."),
    S("end", ["Goed gebruikt", "<em>beschermt het</em>"], "Ook tegen soa's."),
  ],
  "Condooms zijn betrouwbaar, maar alleen als je ze goed gebruikt. Drie dingen die vaak misgaan.\n\n"
  "Een condoom dat maanden in een portemonnee of een warme auto zit, wordt zwakker. Bewaar ze "
  "koel en kijk op de houdbaarheidsdatum.\n\n"
  "Glijmiddel op oliebasis, zoals babyolie of massageolie, tast latex aan. Gebruik glijmiddel op "
  "water- of siliconenbasis.\n\n"
  "En twee condooms over elkaar is niet dubbel veilig. Door de wrijving scheurt er juist eerder "
  "een.\n\n"
  "Stuur 'm door naar wie dit nog niet wist.",
  ["#condoom", "#veiligvrijen", "#anticonceptie"]),

mf("w11-wo", "2026-11-25", "Zwanger de eerste keer",
   ["De eerste keer", "kun je niet", "zwanger worden."],
   "Ook <b>de allereerste keer</b> kun je zwanger worden.",
   "Wat telt is of je vruchtbaar bent op dat moment, niet of het de eerste keer is. Zonder "
   "anticonceptie is er altijd een kans.",
   "Een van de hardnekkigste mythes: de eerste keer kun je niet zwanger worden. Dat klopt niet. "
   "Zodra je een eisprong hebt, kun je zwanger worden, of het nu de eerste keer is of de "
   "honderdste.\n\n"
   "Het is dus goed om al vóór de eerste keer na te denken over anticonceptie, en over condooms "
   "voor de bescherming tegen soa's.\n\n"
   "Stuur 'm door naar wie het misschien nog moet horen.",
   ["#anticonceptie", "#eerstekeer", "#veiligvrijen"]),

dv("w11-vr", "2026-11-27", "Zwanger tijdens je menstruatie",
   ["Kun je zwanger", "worden tijdens je", "<em>menstruatie</em>?"], "var(--peach)",
   "Kun je zwanger worden tijdens je menstruatie? De kans is klein, maar niet nul.\n\n"
   "Zaadcellen kunnen tot vijf dagen in je lichaam overleven. Heb je een korte cyclus, dan kan je "
   "eisprong vroeg komen, soms maar een paar dagen na het einde van je menstruatie. Seks aan het "
   "eind van je menstruatie kan dan toch tot een zwangerschap leiden.\n\n"
   "Wil je niet zwanger worden, gebruik dan ook tijdens je menstruatie anticonceptie.\n\n"
   "Bewaar 'm voor later.",
   ["#menstruatie", "#vruchtbaredagen", "#anticonceptie"]),

# ------------------------------------------------------------ week 12
kt("w12-ma", "2026-11-30", "Het staafje", "Staafje - 1.png", [
    S("open", ["Het <em>staafje</em>,", "in het kort"]),
    S("mint", ["In je", "bovenarm"], "Zo groot als een lucifer, net onder de huid."),
    S("peach", ["Drie jaar", "beschermd"], "Een van de betrouwbaarste middelen die er zijn."),
    S("pink", ["Bloedingen zijn", "onvoorspelbaar"], "Minder, vaker of helemaal niet. Dat verschilt."),
    S("end", ["Eruit kan", "<em>altijd</em>"], "Je vruchtbaarheid komt snel terug."),
  ],
  "Het staafje in het kort. Het is een klein, buigzaam staafje, ongeveer zo groot als een lucifer, "
  "dat de huisarts net onder de huid van je bovenarm plaatst. Het geeft een hormoon af en "
  "beschermt je drie jaar lang.\n\n"
  "Het is een van de betrouwbaarste vormen van anticonceptie, omdat je er niets voor hoeft te "
  "onthouden. Wat je wel moet weten: je bloedingspatroon wordt onvoorspelbaar. Sommige vrouwen "
  "bloeden minder of helemaal niet, anderen juist vaker.\n\n"
  "Wil je stoppen, dan kan het staafje er altijd uit en komt je vruchtbaarheid snel terug.",
  ["#staafje", "#implanon", "#anticonceptie"]),

mf("w12-wo", "2026-12-02", "De pil en je humeur",
   ["Van de pil krijgt", "iedereen een", "slecht humeur."],
   "De meeste vrouwen merken <b>geen verschil</b> in hun stemming.",
   "Een deel van de vrouwen merkt wel stemmingsklachten. Herken je dat, dan is dat serieus en een "
   "goede reden om met je huisarts naar een ander middel te kijken.",
   "Van de pil word je somber of prikkelbaar, toch? Voor de meeste vrouwen klopt dat niet: zij "
   "merken geen verschil in hun stemming.\n\n"
   "Maar een deel van de vrouwen merkt het wel. Somberheid, prikkelbaarheid of minder zin in "
   "dingen kunnen samenhangen met hormonale anticonceptie. Herken je dat bij jezelf, dan hoef je "
   "daar niet mee door te lopen. Een ander middel kan heel anders uitpakken.\n\n"
   "Bespreek het met je huisarts.",
   ["#depil", "#hormonen", "#stemming"]),

dm("w12-vr", "2026-12-04", "Alcohol en de pil", "Blije-vrouwen.png",
   ["Alcohol en", "<em>de pil</em>"],
   "Het is bijna december en dus veel borrels. Werkt mijn pil nog als ik drink?",
   "Alcohol zelf heeft <b>geen invloed</b> op de werking van de pil. Let wel op overgeven.",
   "Werkt de pil nog als je drinkt? Ja. Alcohol zelf heeft geen invloed op de betrouwbaarheid van "
   "de pil.\n\n"
   "Wat wel uitmaakt: moet je binnen drie tot vier uur na je pil overgeven, dan telt die pil als "
   "vergeten. En na een lange avond is het ook makkelijk om je pil de volgende ochtend te "
   "vergeten. Een wekker helpt.\n\n"
   "Stuur 'm door naar je borrelgenoten.",
   ["#depil", "#feestdagen", "#anticonceptie"]),

# ------------------------------------------------------------ week 13
kt("w13-ma", "2026-12-07", "Anticonceptie na een bevalling", "Sterke-vrouw_1-8.png", [
    S("open", ["Anticonceptie", "na een", "<em>bevalling</em>"]),
    S("mint", ["Je kunt snel", "weer vruchtbaar zijn"], "Soms al voordat je eerste menstruatie terug is."),
    S("peach", ["Borstvoeding", "telt niet zomaar"], "Alleen onder strikte voorwaarden beschermt het je."),
    S("pink", ["Niet elk middel", "past meteen"], "Zeker bij borstvoeding is dat maatwerk."),
    S("end", ["Bespreek het", "<em>op tijd</em>"], "Met je verloskundige of huisarts."),
  ],
  "Anticonceptie na een bevalling is iets om op tijd over na te denken, want je kunt al snel "
  "weer vruchtbaar zijn. Soms al voordat je eerste menstruatie terug is.\n\n"
  "Borstvoeding beschermt je alleen onder strikte voorwaarden: je baby is jonger dan zes maanden, "
  "krijgt alleen borstvoeding, dag en nacht, en je menstruatie is nog niet terug. Voldoe je daar "
  "niet aan, dan is het geen betrouwbare anticonceptie.\n\n"
  "Niet elk middel past direct na een bevalling of tijdens borstvoeding. Bespreek met je "
  "verloskundige of huisarts wat voor jou een goede keuze is.",
  ["#borstvoeding", "#anticonceptie", "#kraamtijd"]),

ana("w13-wo", "2026-12-09", "De minipil, 28 dagen door", "minipil",
    "Anatomie van de minipil. Waar een gewone strip een stopweek heeft, slik je de minipil elke "
    "dag door. Achtentwintig pillen, en na de laatste begin je meteen aan de volgende strip.\n\n"
    "De minipil bevat maar één hormoon en geen oestrogeen. Daardoor is hij ook een optie voor "
    "vrouwen die geen oestrogeen mogen of willen. Je bloedingen kunnen onregelmatig worden of "
    "helemaal wegblijven. Dat is bij de minipil normaal.\n\n"
    "Bewaar 'm voor later.",
    ["#minipil", "#depil", "#anticonceptie"]),

dv("w13-vr", "2026-12-11", "De pil en tijdzones",
   ["Pil op reis in", "een andere", "<em>tijdzone</em>?"], "var(--sky)",
   "Op reis in een andere tijdzone? Neem je pil dan gewoon om de 24 uur, dus op hetzelfde moment "
   "als thuis. Dat kan betekenen dat je hem op je bestemming midden op de dag of 's nachts moet "
   "nemen.\n\n"
   "Handiger is om het tijdstip een paar dagen voor vertrek stap voor stap op te schuiven, zodat "
   "je nooit meer dan de toegestane marge te laat bent. Bij de meeste pillen is die marge twaalf "
   "uur, bij sommige minipillen drie uur. Kijk in je bijsluiter welke voor jou geldt.\n\n"
   "Bewaar 'm voor je volgende reis.",
   ["#depil", "#reizen", "#anticonceptie"]),

# ------------------------------------------------------------ week 14
kt("w14-ma", "2026-12-14", "Een soa-test", "Bespreken.png", [
    S("open", ["Een <em>soa-test</em>,", "zo gaat het"]),
    S("mint", ["Vaak merk je", "niets"], "Chlamydia geeft lang niet altijd klachten."),
    S("peach", ["Huisarts", "of GGD"], "Bij de GGD is het soms gratis, bijvoorbeeld onder de 25."),
    S("pink", ["Meestal", "plassen of een swab"], "Soms ook bloed, afhankelijk van de test."),
    S("end", ["Nieuwe partner?", "<em>Test je</em>"], "Het is snel geregeld."),
  ],
  "Een soa-test klinkt spannender dan het is. En het is vaker nodig dan je denkt, want veel soa's, "
  "zoals chlamydia, geven lang niet altijd klachten.\n\n"
  "Je kunt je laten testen bij je huisarts of bij het Centrum Seksuele Gezondheid van de GGD. Bij "
  "de GGD is het in sommige situaties gratis, bijvoorbeeld als je jonger bent dan 25. Meestal gaat "
  "het om plassen in een potje of een swab, soms ook om bloed.\n\n"
  "Heb je een nieuwe partner gehad, of twijfel je? Laat je testen.",
  ["#soa", "#soatest", "#veiligvrijen"]),

mf("w14-wo", "2026-12-16", "Afscheiding",
   ["Afscheiding", "betekent dat er", "iets mis is."],
   "Afscheiding is <b>normaal</b> en verandert tijdens je cyclus.",
   "Rond je eisprong is het vaak helder en rekbaar, daarna dikker. Laat het checken als het "
   "anders ruikt, van kleur verandert of jeukt.",
   "Afscheiding hoort bij je lichaam. Het houdt je vagina schoon en vochtig, en het verandert "
   "tijdens je cyclus. Rond je eisprong is het vaak helder en rekbaar, in de rest van je cyclus "
   "wat dikker of juist minder.\n\n"
   "Het wordt pas een signaal als er iets verandert: een andere geur, een andere kleur, of als het "
   "jeukt of branden geeft. Dan is het goed om het te laten checken.\n\n"
   "Stuur 'm door naar wie dit ook nooit uitgelegd kreeg.",
   ["#afscheiding", "#intiemegezondheid", "#cyclus"]),

dm("w14-vr", "2026-12-18", "Hevig bloeden met een koperspiraal", "Doorlekken-schaamte-8.png",
   ["Heviger bloeden", "met een <em>koperspiraal</em>?"],
   "Sinds ik een koperspiraal heb, is mijn menstruatie veel heftiger. Is dat normaal?",
   "In de eerste maanden <b>vaak wel</b>. Wordt het niet minder of is het heel heftig, ga dan "
   "naar je huisarts.",
   "Heviger of langer menstrueren is een bekend gevolg van een koperspiraal, vooral in de eerste "
   "maanden. Bij veel vrouwen wordt het daarna wat rustiger.\n\n"
   "Gaat het niet over, verlies je zoveel bloed dat het je dagelijks leven in de weg zit, of voel "
   "je je slap en moe? Ga dan naar je huisarts. Soms is een ander middel een betere keuze.\n\n"
   "Stuur 'm door naar wie net een koperspiraal heeft.",
   ["#koperspiraal", "#spiraaltje", "#menstruatie"]),

# ------------------------------------------------------------ week 15
kt("w15-ma", "2026-12-21", "PMS", "Stemmings-wisselingen-8.png", [
    S("open", ["<em>PMS</em>,", "wat is het nou?"]),
    S("mint", ["De week", "vóór je menstruatie"], "Daar zitten de klachten, en daarna zakken ze weg."),
    S("peach", ["Lichaam", "en hoofd"], "Van gevoelige borsten tot prikkelbaar of somber."),
    S("pink", ["Wat vaak", "helpt"], "Genoeg slaap, bewegen en minder cafeïne."),
    S("end", ["Heel heftig?", "<em>Bespreek het</em>"], "Er is meer mogelijk dan je denkt."),
  ],
  "PMS staat voor premenstrueel syndroom: klachten in de dagen tot een week vóór je menstruatie, "
  "die wegzakken zodra je menstruatie begint. Denk aan gevoelige borsten, een opgeblazen gevoel, "
  "hoofdpijn, maar ook prikkelbaarheid of somberheid.\n\n"
  "Wat bij veel vrouwen helpt: genoeg slapen, regelmatig bewegen en minder cafeïne. Het helpt ook "
  "om een paar maanden bij te houden wanneer je klachten hebt, zodat je het patroon ziet.\n\n"
  "Zijn je klachten zo heftig dat ze je leven elke maand op zijn kop zetten? Bespreek het met je "
  "huisarts. Er is meer mogelijk dan je denkt.",
  ["#pms", "#cyclus", "#menstruatie"]),

mf("w15-wo", "2026-12-23", "Pil op de minuut",
   ["Je moet de pil", "op de minuut", "precies innemen."],
   "Bij de meeste pillen heb je <b>twaalf uur marge</b>.",
   "Bij sommige minipillen is die marge drie uur. Kijk in je bijsluiter welke voor jou geldt. "
   "Een vast moment helpt wel om hem niet te vergeten.",
   "Moet je de pil echt op de minuut innemen? Nee. Bij de meeste pillen, zowel combinatiepillen "
   "als de gebruikelijke minipil, heb je twaalf uur marge. Ben je binnen die tijd, dan ben je "
   "gewoon beschermd.\n\n"
   "Er zijn wel minipillen met een marge van drie uur. Kijk in je bijsluiter welke voor jou "
   "geldt.\n\n"
   "Een vast moment kiezen blijft slim, niet omdat het op de minuut moet, maar omdat je hem dan "
   "minder snel vergeet. Zeker in de drukke feestweken.",
   ["#depil", "#minipil", "#anticonceptie"]),

# ------------------------------------------------------------ week 16
kt("w16-ma", "2026-12-28", "Menstruatiepijn die niet normaal is", "Hoofdpijn-buikpijn-8.png", [
    S("open", ["Wanneer is", "<em>menstruatiepijn</em>", "niet normaal?"]),
    S("mint", ["Als het je", "leven stillegt"], "School, werk of afspraken afzeggen hoort er niet bij."),
    S("peach", ["Als pijnstillers", "niet helpen"], "Of als je steeds meer nodig hebt."),
    S("pink", ["Als het erger", "wordt"], "Of als je ook pijn hebt buiten je menstruatie."),
    S("end", ["Ga naar", "<em>je huisarts</em>"], "Soms zit er iets achter, zoals endometriose."),
  ],
  "Menstruatiepijn is heel gewoon, maar er is een grens. Het is niet normaal als je elke maand "
  "school, werk of afspraken moet afzeggen, als pijnstillers niet genoeg helpen, of als de pijn "
  "steeds erger wordt.\n\n"
  "Ook pijn buiten je menstruatie, pijn bij het vrijen of pijn bij plassen of poepen tijdens je "
  "menstruatie zijn redenen om aan de bel te trekken. Soms zit er een aandoening achter, zoals "
  "endometriose, en dat wordt nog vaak laat ontdekt.\n\n"
  "Herken je dit? Ga naar je huisarts. Je pijn mag serieus genomen worden.",
  ["#menstruatiepijn", "#endometriose", "#menstruatie"]),

mf("w16-wo", "2026-12-30", "Een tampon kwijtraken",
   ["Een tampon kan", "kwijtraken in", "je lichaam."],
   "Een tampon kan <b>nergens heen</b>.",
   "De opening van je baarmoedermond is veel te klein. Hij kan wel hoog zitten. Kom je er echt "
   "niet bij, dan helpt je huisarts je.",
   "Een tampon die ergens in je lichaam verdwijnt? Dat kan niet. Je vagina loopt dood bij de "
   "baarmoedermond, en die opening is veel te klein voor een tampon.\n\n"
   "Wat wel kan: dat hij hoog zit of dat het touwtje naar binnen is geschoven. Ontspan, ga op je "
   "hurken zitten en probeer het rustig. Lukt het echt niet, ga dan naar je huisarts. Die haalt "
   "hem er zo uit, en dat is voor hen heel gewoon.\n\n"
   "Stuur 'm door naar wie hier stiekem weleens bang voor was.",
   ["#tampon", "#menstruatie", "#intiemegezondheid"]),

# ------------------------------------------------------------ week 17
kt("w17-ma", "2027-01-04", "De menstruatiecup", "Sport-8.png", [
    S("open", ["De <em>cup</em>,", "3 dingen die", "je wilt weten"]),
    S("mint", ["Vouwen en", "inbrengen"], "Hij vouwt zich binnen weer open en sluit af."),
    S("peach", ["Tot twaalf uur", "achter elkaar"], "Kijk in de bijsluiter wat voor jouw cup geldt."),
    S("pink", ["Uitkoken", "na je menstruatie"], "Tussendoor is afspoelen met water genoeg."),
    S("end", ["Even oefenen,", "<em>daarna makkelijk</em>"], "Geef het een paar cycli."),
  ],
  "Een menstruatiecup: drie dingen die je wilt weten voordat je begint.\n\n"
  "Je vouwt de cup, brengt hem in en binnen vouwt hij zich weer open. Zo sluit hij af en vangt hij "
  "je bloed op. De meeste cups kun je tot twaalf uur achter elkaar dragen. Kijk in de bijsluiter "
  "wat voor jouw cup geldt.\n\n"
  "Tussendoor spoel je hem af met water. Na je menstruatie kook je hem een paar minuten uit.\n\n"
  "De eerste keren is het even oefenen, en dat is normaal. Geef het een paar cycli.",
  ["#menstruatiecup", "#menstruatie", "#duurzaam"]),

mf("w17-wo", "2027-01-06", "Schimmelinfectie en hygiëne",
   ["Een schimmelinfectie", "krijg je door", "slechte hygiëne."],
   "Een schimmelinfectie heeft <b>niets met vies zijn</b> te maken.",
   "Het ontstaat als het evenwicht in je vagina verstoord raakt, bijvoorbeeld door antibiotica of "
   "hormonen. Te veel wassen met zeep kan het juist erger maken.",
   "Een schimmelinfectie komt door slechte hygiëne? Nee. Er leeft altijd een beetje schimmel in je "
   "vagina, en meestal houdt je lichaam dat prima in evenwicht.\n\n"
   "Het gaat mis als dat evenwicht verstoord raakt. Bijvoorbeeld door antibiotica, door "
   "hormonale veranderingen of door te veel wassen met zeep. Gewoon water is voor je vulva "
   "genoeg.\n\n"
   "Heb je het voor het eerst, of komt het steeds terug? Laat het dan checken door je huisarts.",
   ["#schimmelinfectie", "#intiemegezondheid", "#vrouwengezondheid"]),

dv("w17-vr", "2027-01-08", "Vitamines en de pil",
   ["Heb je extra", "<em>vitamines</em> nodig", "als je de pil slikt?"], "var(--blush)",
   "Heb je extra vitamines nodig als je de pil slikt? Voor de meeste vrouwen niet. Met een "
   "gevarieerd eetpatroon krijg je binnen wat je nodig hebt.\n\n"
   "Er is één uitzondering waar je wel op moet letten: wil je zwanger worden, begin dan al vóór "
   "je stopt met anticonceptie met foliumzuur. Dat verkleint de kans op een open ruggetje bij je "
   "baby.\n\n"
   "Twijfel je of een supplement zinvol is voor jou? Bespreek het met je huisarts.",
   ["#depil", "#vitamines", "#foliumzuur"]),

# ------------------------------------------------------------ week 18
kt("w18-ma", "2027-01-11", "Van de pil naar een spiraaltje", "Spiraaltje - 2.png", [
    S("open", ["Van de pil", "naar een", "<em>spiraaltje</em>"]),
    S("mint", ["Eerst een", "afspraak"], "De huisarts bespreekt welk spiraaltje past."),
    S("peach", ["Plaatsen duurt", "een paar minuten"], "Vraag gerust naar pijnstilling."),
    S("pink", ["Pil nog even", "doorslikken?"], "Dat hangt af van het moment. Je huisarts zegt het je."),
    S("end", ["Daarna jaren", "<em>niets onthouden</em>"], "Geen strip meer nodig."),
  ],
  "Overstappen van de pil naar een spiraaltje. Het begint met een afspraak bij je huisarts, die "
  "met je bespreekt of een hormoonspiraal of een koperspiraal beter past.\n\n"
  "Het plaatsen zelf duurt maar een paar minuten. Het kan gevoelig zijn, dus vraag gerust naar "
  "pijnstilling. Of je de pil nog een paar dagen moet doorslikken, hangt af van wanneer het "
  "spiraaltje wordt geplaatst. Dat hoor je van je huisarts.\n\n"
  "Daarna hoef je jarenlang nergens meer aan te denken.",
  ["#spiraaltje", "#depil", "#anticonceptie"]),

mf("w18-wo", "2027-01-13", "Spiraaltje plaatsen en pijn",
   ["Een spiraaltje", "plaatsen doet", "altijd veel pijn."],
   "Hoe het voelt <b>verschilt sterk</b> per vrouw.",
   "Sommige vrouwen voelen een korte kramp, anderen vinden het echt pijnlijk. Je mag altijd "
   "vragen naar pijnstilling. Bespreek het vooraf met je huisarts.",
   "Doet een spiraaltje plaatsen altijd veel pijn? Dat verschilt sterk. Sommige vrouwen voelen "
   "alleen een korte kramp, anderen vinden het echt pijnlijk. Allebei is normaal.\n\n"
   "Wat helpt: vooraf bespreken wat je kunt verwachten, en vragen naar pijnstilling. Dat mag "
   "altijd, en het wordt steeds vaker aangeboden. Neem ook even de tijd na de plaatsing voordat je "
   "weer vertrekt.\n\n"
   "Hoe was het bij jou?",
   ["#spiraaltje", "#anticonceptie", "#vrouwengezondheid"]),

dm("w18-vr", "2027-01-15", "Hoe weet je of je ovuleert", "Vrouwen-vraag.png",
   ["Hoe weet je", "of je <em>ovuleert</em>?"],
   "Wij willen zwanger worden. Hoe weet ik eigenlijk wanneer ik ovuleer?",
   "Let op je <b>afscheiding</b>: helder en rekbaar betekent vaak dat je eisprong eraan komt. "
   "Een ovulatietest geeft meer zekerheid.",
   "Hoe weet je of je ovuleert? Je lichaam geeft vaak signalen. Rond je eisprong wordt je "
   "afscheiding helder en rekbaar, een beetje als rauw eiwit. Sommige vrouwen voelen ook een "
   "zeurende pijn aan één kant van hun onderbuik.\n\n"
   "Meer zekerheid geeft een ovulatietest. Die meet de hormoonpiek die een dag of twee vóór je "
   "eisprong komt, zodat je weet wanneer je het meest vruchtbaar bent.\n\n"
   "En goed om te weten: gebruik je de pil, dan heb je geen eisprong.",
   ["#eisprong", "#kinderwens", "#ovulatietest"]),
]
