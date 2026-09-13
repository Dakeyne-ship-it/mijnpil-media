# -*- coding: utf-8 -*-
"""The 59 approved Onder ons lines, as Alexander selected them on 13 sep 2026.

Each entry: (bronnummer, displayregels, captionopening, deelzin, tags, reactie)
The display lines are authored by hand: the renderer never wraps, so each line
here is exactly one line in the image. Keep them under about 26 characters,
otherwise the type drops below the size where the post still reads as a poster.
"""

D = ("Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of "
     "heb je klachten? Overleg met je huisarts of apotheker.")

POSTS = [
(1, ["<em>De stopweek</em>", "weet precies", "wanneer je op", "vakantie gaat."],
 "Drie weken niets aan de hand, en dan valt de stopweek precies op de dag dat je koffer dichtgaat.",
 "Stuur 'm door naar wie volgende week mee op reis gaat.",
 ["#stopweek", "#anticonceptie", "#depil"],
 "Even voor de duidelijkheid: de bloeding in je stopweek is een onttrekkingsbloeding "
 "en geen echte menstruatie. Bij veel combinatiepillen kun je die week overslaan, "
 "bijvoorbeeld voor een vakantie. " + D),

(2, ["<em>Je menstruatie</em>", "kent je agenda", "beter dan jij."],
 "Jij vergeet een afspraak. Zij niet.",
 "Tag iemand die dit ook elke maand meemaakt.",
 ["#menstruatie", "#cyclus", "#vrouwengezondheid"], None),

(3, ["<em>Je menstruatie</em>", "wacht netjes tot je", "iets wits aanhebt."],
 "Witte broek, witte jurk, witte bank. Ze weet het.",
 "Stuur 'm door naar wie het toch nog een keer gaat proberen.",
 ["#menstruatie", "#cyclus", "#herkenbaar"], None),

(4, ["<em>De stopweek</em>", "begint standaard", "op de dag dat je", "iets leuks hebt."],
 "Nooit op een dinsdag waarop toch niets gebeurt.",
 "Stuur 'm door naar wie dit weekend iets had gepland.",
 ["#stopweek", "#anticonceptie", "#depil"],
 "Bij veel combinatiepillen kun je die week gewoon overslaan, zodat de bloeding "
 "opschuift naar een moment dat beter uitkomt. " + D),

(5, ["<em>Je cyclus</em> weet eerder", "dan jij wanneer het", "zwembadweer wordt."],
 "De eerste echt warme dag van het jaar staat blijkbaar ook in haar agenda.",
 "Tag je zwemmaatje.",
 ["#cyclus", "#menstruatie", "#zomer"], None),

(6, ["<em>Je menstruatie</em>", "heeft nog nooit een", "vakantie overgeslagen."],
 "Trouwer dan welke reisgenoot ook.",
 "Stuur 'm door naar wie je koffer deelt.",
 ["#menstruatie", "#vakantie", "#cyclus"], None),

(7, ["Het weekendje weg", "stond al geboekt,", "<em>de stopweek</em>", "wist dat allang."],
 "Geboekt in maart, geregeld in juni, en toch precies die week.",
 "Stuur 'm door naar wie het weekend organiseert.",
 ["#stopweek", "#anticonceptie", "#weekendje"], None),

(8, ["<em>Je pil</em> valt altijd", "op de enige plek", "waar je niet bij kan."],
 "Achter de wc, onder de kast, tussen de plint. Nooit gewoon op de grond.",
 "Tag wie ook wel eens op haar knieën in de badkamer heeft gelegen.",
 ["#depil", "#anticonceptie", "#herkenbaar"],
 "Pil echt kwijt? Bel even je apotheek, die kijkt in een minuut met je mee wat "
 "handig is. " + D),

(9, ["<em>De pilstrip</em> zit altijd", "in de tas die je", "vandaag niet meeneemt."],
 "De ene tas heeft alles. Vandaag gebruik je de andere.",
 "Stuur 'm door naar wie drie tassen heeft en nooit de juiste.",
 ["#depil", "#anticonceptie", "#herkenbaar"], None),

(11, ["<em>Je pilstrip</em> ligt thuis", "precies op de plek", "waar je nooit kijkt."],
 "Je hebt overal gezocht behalve daar, en daar lag hij.",
 "Tag wie 'm ook altijd op de gekste plek terugvindt.",
 ["#depil", "#anticonceptie", "#herkenbaar"], None),

(13, ["Niets is zo onzeker", "als de vraag of je 'm", "<em>vanochtend</em>", "genomen hebt."],
 "Je weet het zeker. Tot je even naar de strip kijkt.",
 "Stuur 'm door naar wie hier ook wel eens over twijfelt.",
 ["#depil", "#pilvergeten", "#anticonceptie"],
 "Twijfel je of je 'm genomen hebt? Je apotheek denkt hier zo met je mee, en dat "
 "is een betere bron dan je geheugen om half twaalf 's avonds. " + D),

(15, ["<em>De strip</em> in je", "nachtkastje is altijd", "van vorige maand."],
 "Leeg, en toch ligt hij er nog steeds.",
 "Tag wie haar nachtkastje ook nooit opruimt.",
 ["#depil", "#anticonceptie", "#herkenbaar"], None),

(16, ["Je ontdekt dat", "<em>je strip op is</em>", "op het moment dat", "je 'm nodig hebt."],
 "Nooit een week eerder, altijd op de avond zelf.",
 "Stuur 'm door naar wie dit ook maandelijks overkomt.",
 ["#depil", "#anticonceptie", "#herhaalrecept"],
 "Praktische tip: zet een herinnering op de dag dat je aan je laatste strip begint. "
 "Dan heb je een week speling in plaats van een avond.", ),

(17, ["<em>Het doosje</em>", "voelt vol", "tot je het openmaakt."],
 "Gewicht zegt niets.",
 "Tag wie ook op gevoel inschat hoeveel er nog in zit.",
 ["#anticonceptie", "#depil", "#herkenbaar"], None),

(18, ["<em>Je herhaalrecept</em>", "valt altijd in de week", "dat je het al druk hebt."],
 "Nooit in die ene rustige week.",
 "Stuur 'm door naar wie haar agenda ook niet meer ziet zitten.",
 ["#herhaalrecept", "#apotheek", "#anticonceptie"], None),

(19, ["<em>Je badkamerkastje</em>", "is optimistischer", "over je voorraad", "dan de werkelijkheid."],
 "Vol met van alles, leeg aan het enige wat je zoekt.",
 "Tag wie haar kastje ook niet durft op te ruimen.",
 ["#herkenbaar", "#vrouwengezondheid", "#badkamer"], None),

(20, ["Je hebt nog", "<em>één strip</em>,", "en dat weet je pas", "op zondagavond."],
 "Precies als alles dicht is.",
 "Stuur 'm door naar wie dit ook op zondag ontdekt.",
 ["#depil", "#apotheek", "#anticonceptie"], None),

(21, ["<em>De apotheek</em>", "is altijd net dicht", "als je eraan denkt."],
 "Je denkt er de hele dag niet aan, en dan om vijf over zes wel.",
 "Tag wie ook altijd net te laat is.",
 ["#apotheek", "#herhaalrecept", "#herkenbaar"], None),

(22, ["<em>Je laatste tampon</em>", "ligt altijd los", "onderin je tas."],
 "Zonder verpakking, met een kruimel erop, maar hij is er.",
 "Tag wie ook altijd de reddende engel is.",
 ["#menstruatie", "#tampon", "#herkenbaar"], None),

(23, ["<em>Je voorraad</em>", "raakt altijd op", "tijdens de drukste dag."],
 "Niet op dag vier. Op dag twee.",
 "Stuur 'm door naar wie dit ook elke keer verkeerd inschat.",
 ["#menstruatie", "#maandverband", "#tampon"], None),

(26, ["Je neemt altijd", "precies <em>één tampon</em>", "te weinig mee."],
 "Twee leek genoeg. Twee was niet genoeg.",
 "Tag je noodcontact voor precies dit moment.",
 ["#menstruatie", "#tampon", "#herkenbaar"], None),

(27, ["Je vindt <em>overal</em>", "tampons, behalve", "als je er een zoekt."],
 "In je jas, in de auto, in die ene la. Nooit nu.",
 "Stuur 'm door naar wie ook overal voorraad heeft, behalve bij zich.",
 ["#menstruatie", "#tampon", "#herkenbaar"], None),

(28, ["<em>Je cup</em> ligt altijd", "te drogen op het", "moment dat je 'm", "nodig hebt."],
 "Schoon, klaar, en aan de verkeerde kant van het huis.",
 "Tag je cupvriendin.",
 ["#menstruatiecup", "#menstruatie", "#duurzaam"], None),

(29, ["Er zit altijd een", "tampon in <em>je jaszak</em>,", "alleen niet in de", "jas van vandaag."],
 "Jassen hebben een eigen systeem en dat is niet het jouwe.",
 "Stuur 'm door naar wie ook drie jassen en nul tampons bij zich heeft.",
 ["#menstruatie", "#tampon", "#herkenbaar"], None),

(30, ["<em>Krampen</em> wachten", "netjes tot je", "in de trein zit."],
 "Thuis niets, perron niets, deuren dicht en daar zijn ze.",
 "Tag wie ook altijd in de spits begint.",
 ["#menstruatiepijn", "#krampen", "#menstruatie"],
 "Krampen die je dag echt in de weg zitten horen er niet gewoon bij. Bespreek het "
 "een keer met je huisarts, er is vaak meer mogelijk dan vrouwen denken. " + D),

(31, ["<em>Je kruik</em> ligt altijd", "in de kast waar", "je niet bij kan."],
 "Bovenste plank, achterin, achter de kerstspullen.",
 "Stuur 'm door naar wie ook een opstapje nodig heeft.",
 ["#krampen", "#menstruatie", "#herkenbaar"], None),

(32, ["<em>De eerste dag</em>", "valt altijd samen met", "de dag die je niet", "kunt verzetten."],
 "Presentatie, rijexamen, bruiloft. Kies maar.",
 "Tag wie dit ook een keer heeft meegemaakt.",
 ["#menstruatie", "#cyclus", "#herkenbaar"], None),

(33, ["<em>Krampen</em> weten", "precies wanneer", "je moet staan."],
 "In de rij, in de tram, in de supermarkt.",
 "Stuur 'm door naar wie vandaag ook op haar tanden bijt.",
 ["#menstruatiepijn", "#krampen", "#menstruatie"],
 "Warmte helpt vaak meer dan je denkt, en bewegen ook. Blijft het elke maand zo? "
 "Dan is het een gesprek met je huisarts waard. " + D),

(34, ["<em>Je pijnstillers</em>", "liggen altijd", "in je andere tas."],
 "Samen met je pleisters en je goede voornemens.",
 "Tag wie altijd wel iets bij zich heeft.",
 ["#krampen", "#menstruatie", "#herkenbaar"], None),

(35, ["<em>Je onderrug</em>", "weet het eerder", "dan jij."],
 "Nog voor je app iets zegt.",
 "Stuur 'm door naar wie het ook altijd in haar rug voelt.",
 ["#menstruatie", "#cyclus", "#krampen"], None),

(36, ["<em>Je huid</em> weet precies", "wanneer je op de", "foto moet."],
 "Drie weken rust, en dan die ene dag.",
 "Tag wie ook altijd op het verkeerde moment gefotografeerd wordt.",
 ["#hormonen", "#cyclus", "#huid"], None),

(37, ["<em>Je humeur</em> begint", "een dag eerder", "dan je cyclus."],
 "Achteraf snap je precies waarom je boos was op die deur.",
 "Stuur 'm door naar wie jou die dag verdraagt.",
 ["#pms", "#hormonen", "#cyclus"], None),

(38, ["Je hebt geen idee", "welke dag het is,", "<em>je cyclus</em> wel."],
 "De enige agenda die altijd klopt.",
 "Tag wie ook op haar cyclus navigeert.",
 ["#cyclus", "#menstruatie", "#hormonen"], None),

(39, ["Je onderbroeken zijn", "<em>onderverdeeld</em> in", "twee categorieën, en", "jij weet precies welke."],
 "Iedereen heeft dit systeem, niemand heeft het ooit uitgelegd.",
 "Stuur 'm door naar wie precies weet wat je bedoelt.",
 ["#menstruatie", "#cyclus", "#herkenbaar"], None),

(40, ["<em>Je wasmachine</em>", "kent jouw cyclus", "inmiddels ook."],
 "Elke maand dezelfde afspraak.",
 "Tag wie ook maandelijks een extra wasje draait.",
 ["#menstruatie", "#cyclus", "#herkenbaar"], None),

(41, ["In het vliegtuig weet", "<em>je lichaam</em> precies", "hoe laat het thuis is."],
 "Jij zit in een andere tijdzone. Je lichaam niet.",
 "Stuur 'm door naar wie binnenkort ver weg gaat.",
 ["#anticonceptie", "#depil", "#reizen"],
 "Reis je een paar uur naar het oosten of westen? Vraag je apotheek even hoe je je "
 "inname het handigst verschuift, dan hoef je daar ter plekke niet over na te denken. " + D),

(43, ["Je hebt alles ingepakt,", "behalve <em>het enige</em>", "wat niet kan wachten."],
 "Drie paar schoenen wel.",
 "Tag wie pas op het vliegveld nadenkt.",
 ["#reizen", "#anticonceptie", "#depil"], None),

(44, ["Op reis is <em>je strip</em>", "het enige wat je", "twee keer controleert."],
 "Paspoort, sleutels, strip. En dan nog een keer de strip.",
 "Stuur 'm door naar wie ook drie keer in haar tas kijkt.",
 ["#reizen", "#depil", "#anticonceptie"], None),

(47, ["<em>Je koffer</em> heeft altijd", "plek, behalve voor", "het kleinste doosje."],
 "De föhn past wel.",
 "Tag wie ook te groot inpakt en te klein vergeet.",
 ["#reizen", "#anticonceptie", "#herkenbaar"], None),

(48, ["<em>Je krampen</em> wachten", "netjes tot de", "vergadering begint."],
 "Agendapunt één, en daar zijn ze.",
 "Stuur 'm door naar wie vandaag ook een volle agenda heeft.",
 ["#krampen", "#werk", "#menstruatie"], None),

(52, ["<em>Een witte stoel</em>", "voelt in die week als", "een persoonlijke aanval."],
 "Wie ontwerpt die dingen.",
 "Tag wie ook altijd de donkere stoel uitzoekt.",
 ["#menstruatie", "#herkenbaar", "#cyclus"], None),

(54, ["Er bestaat geen", "<em>discrete manier</em> om", "een tampon mee te", "nemen, en toch probeer", "je het."],
 "Mouw, zak, telefoonhoesje. Het is nooit subtiel.",
 "Stuur 'm door naar wie het ook elke keer weer probeert.",
 ["#menstruatie", "#tampon", "#werk"], None),

(55, ["<em>Het spiegelkastje</em>", "zit vol, en toch is er", "nooit wat je zoekt."],
 "Wel drie soorten dagcrème.",
 "Tag wie haar kastje ook eindelijk eens gaat uitzoeken.",
 ["#herkenbaar", "#badkamer", "#vrouwengezondheid"], None),

(56, ["<em>De wasmand</em>", "houdt bij", "welke week het is."],
 "Een rustige, betrouwbare kalender.",
 "Stuur 'm door naar wie dit meteen snapt.",
 ["#menstruatie", "#cyclus", "#herkenbaar"], None),

(62, ["<em>Je huilt</em> om een", "reclame en weet", "precies waarom."],
 "Een verzekeringsreclame. Met een hond.",
 "Tag wie jou die week het beste kent.",
 ["#pms", "#hormonen", "#cyclus"], None),

(63, ["Je hebt <em>nergens</em>", "zin in, behalve", "in alles tegelijk."],
 "Uitgaan, op de bank liggen, verhuizen. Allemaal tegelijk.",
 "Stuur 'm door naar wie dit gevoel kent.",
 ["#pms", "#hormonen", "#cyclus"], None),

(64, ["<em>De chocola</em> in huis", "weet dat haar tijd", "gekomen is."],
 "Ze lag daar al weken rustig te wachten.",
 "Tag wie haar voorraad ook op peil houdt.",
 ["#pms", "#cyclus", "#herkenbaar"], None),

(66, ["<em>Je geduld</em> raakt", "een week eerder op", "dan je strip."],
 "En dat is precies te voorspellen.",
 "Stuur 'm door naar wie dit van je pikt.",
 ["#pms", "#hormonen", "#cyclus"], None),

(67, ["<em>Alles</em> is irritant,", "en de meeste dingen", "hebben niets gedaan."],
 "Sorry tegen de wasmachine, de buurman en die ene app.",
 "Tag wie hier deze week begrip voor heeft.",
 ["#pms", "#hormonen", "#herkenbaar"], None),

(68, ["<em>Je agenda</em> en je zin", "om iets te doen lopen", "die week niet gelijk."],
 "Je hebt het allemaal zelf ingepland, dat is het vervelende.",
 "Stuur 'm door naar wie ook wel eens iets afzegt.",
 ["#pms", "#cyclus", "#hormonen"], None),

(69, ["<em>Je cyclusapp</em> is", "optimistischer over", "je regelmaat dan jij."],
 "Zij zegt woensdag. Jij weet wel beter.",
 "Tag wie haar app ook niet helemaal gelooft.",
 ["#cyclus", "#menstruatie", "#hormonen"], None),

(70, ["<em>Je herinnering</em> gaat", "altijd af op het", "moment dat je net", "niet kan."],
 "Onder de douche, in de auto, midden in een gesprek.",
 "Stuur 'm door naar wie 'm ook altijd wegdrukt.",
 ["#depil", "#anticonceptie", "#herkenbaar"], None),

(72, ["Je zet <em>de herinnering</em>", "vijf minuten later", "en dan is het", "ineens morgen."],
 "Vijf minuten is een rekbaar begrip.",
 "Tag wie dit ook doet en het ontkent.",
 ["#depil", "#pilvergeten", "#anticonceptie"],
 "Pil een keer vergeten? Bij de combinatiepil ben je bij één vergeten pil meestal "
 "gewoon beschermd, maar het hangt af van waar je in de strip zit. Bel je apotheek "
 "als je twijfelt. " + D),

(73, ["De enige datum die je", "uit je hoofd kent,", "is die van <em>je strip</em>."],
 "Verjaardagen niet, dit wel.",
 "Stuur 'm door naar wie jouw verjaardag ook vergeet.",
 ["#depil", "#anticonceptie", "#herkenbaar"], None),

(74, ["<em>Je telefoon</em> houdt", "je cyclus beter bij", "dan jij je afspraken."],
 "Eén van de twee is in elk geval op orde.",
 "Tag wie ook op haar telefoon vertrouwt.",
 ["#cyclus", "#menstruatie", "#herkenbaar"], None),

(75, ["Je weet in <em>elke winkel</em>", "precies waar", "het schap staat."],
 "Zonder te kijken, zonder te vragen.",
 "Stuur 'm door naar wie jou hier ooit heen heeft gestuurd.",
 ["#menstruatie", "#herkenbaar", "#vrouwengezondheid"], None),

(76, ["<em>De zelfscankassa</em>", "vraagt altijd om", "controle bij precies", "dat ene product."],
 "Nooit bij de melk.",
 "Tag wie dit ook een keer is overkomen.",
 ["#menstruatie", "#herkenbaar", "#boodschappen"], None),

(77, ["Je hebt voor", "<em>elke tas</em>", "een noodplan."],
 "Eentje in het vak, eentje in de rits, eentje ergens onderin.",
 "Stuur 'm door naar wie altijd voorbereid is.",
 ["#menstruatie", "#herkenbaar", "#tampon"], None),

(79, ["Er ligt ergens in je", "huis <em>een tampon</em> die", "je nooit meer", "terugvindt."],
 "Hij duikt op bij de verhuizing.",
 "Tag wie 'm ooit nog gaat vinden.",
 ["#menstruatie", "#herkenbaar", "#tampon"], None),
]
