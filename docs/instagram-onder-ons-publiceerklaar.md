# Onder ons, publiceerklaar

De dinsdag-, donderdag- en zaterdagslots van @mijnpil.nu. Bijgewerkt 25 september
2026. Loopt tot en met 16 februari 2027. De uitlegqueue op maandag,
woensdag en vrijdag staat hier los van en heeft zijn eigen document.

In deze slots staan drie soorten posts: memes (Onder ons, id begint met m),
inhakers (id begint met i) en drie posts die bovenaan het profiel worden
vastgepind (id begint met p). Per post staat hieronder precies wat er moet gebeuren.

Alle beelden en stories staan al op de beeldhost. Er hoeft niets gebouwd of
gepusht te worden. De werkomgeving kan de host zelf niet bereiken, dus een
mislukte curl zegt niets: Instagram haalt de bestanden wel op.

## Vaste werkwijze per post

1. Zoek hieronder het kopje met de datum van vandaag in Europe/Amsterdam.
   Staat die datum er niet, dan is er vandaag niets te doen.
2. Feed: connector `instagram`, account `17841408082040893`. Gebruik de actie
   die bij de post staat (`create_image_post` of `create_carousel_post`) met de
   URL's en de letterlijke caption.
3. Staat er een eerste reactie bij, plaats die direct met `create_comment`,
   media_id is wat stap 2 teruggaf.
4. Staat er een story bij: actie `create_story` met video_url. Stories kennen
   geen caption. Mislukt de story, laat de feedpost dan staan en meld alleen de
   story. Staat er geen story bij, sla deze stap over.
5. Staat er bij de post "vastpinnen", meld dan in de pushmelding dat Alexander
   deze post handmatig bovenaan het profiel moet vastzetten. De API kan niet pinnen.

Vaste hashtags: #vrouwenonderelkaar #mijnpilnu. Die staan al in elke caption
hieronder, dus neem de caption letterlijk over en voeg niets toe.

---

# september 2026

## 2026-09-15 · m01 · dinsdag 20:00
Meme. Kleur: roze. Regel: De stopweek weet precies wanneer je op vakantie gaat.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m01.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m01-story.mp4

**Caption, letterlijk**

```
Drie weken niets aan de hand, en dan valt de stopweek precies op de dag dat je koffer dichtgaat.

Stuur 'm door naar wie volgende week mee op reis gaat.

#stopweek #anticonceptie #depil #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Even voor de duidelijkheid: de bloeding in je stopweek is een onttrekkingsbloeding en geen echte menstruatie. Bij veel combinatiepillen kun je die week overslaan, bijvoorbeeld voor een vakantie. Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-09-17 · m02 · donderdag 20:00
Meme. Kleur: indigo. Regel: Je menstruatie kent je agenda beter dan jij.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m02.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m02-story.mp4

**Caption, letterlijk**

```
Jij vergeet een afspraak. Zij niet.

Tag iemand die dit ook elke maand meemaakt.

#menstruatie #cyclus #vrouwengezondheid #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-09-19 · m03 · zaterdag 11:00
Meme. Kleur: lavendel. Regel: Je menstruatie wacht netjes tot je iets wits aanhebt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m03.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m03-story.mp4

**Caption, letterlijk**

```
Witte broek, witte jurk, witte bank. Ze weet het.

Stuur 'm door naar wie het toch nog een keer gaat proberen.

#menstruatie #cyclus #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-09-22 · m04 · dinsdag 20:00
Meme. Kleur: roze. Regel: De stopweek begint standaard op de dag dat je iets leuks hebt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m04.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m04-story.mp4

**Caption, letterlijk**

```
Nooit op een dinsdag waarop toch niets gebeurt.

Stuur 'm door naar wie dit weekend iets had gepland.

#stopweek #anticonceptie #depil #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Bij veel combinatiepillen kun je die week gewoon overslaan, zodat de bloeding opschuift naar een moment dat beter uitkomt. Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-09-24 · m05 · donderdag 20:00
Meme. Kleur: indigo. Regel: Je cyclus weet eerder dan jij wanneer het zwembadweer wordt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m05.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/m05-story.mp4

**Caption, letterlijk**

```
De eerste echt warme dag van het jaar staat blijkbaar ook in haar agenda.

Tag je zwemmaatje.

#cyclus #menstruatie #zomer #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-09-26 · i01 · zaterdag 11:00
Inhaker. Wereld Anticonceptiedag: past je anticonceptie nog bij je leven van nu?
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/i01.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/i01-story.mp4

**Caption, letterlijk**

```
Vandaag is het Wereld Anticonceptiedag. Een goed moment voor een vraag die bijna niemand zichzelf stelt: past de anticonceptie die je ooit hebt gekozen nog bij je leven van nu?

Veel vrouwen gebruiken jarenlang hetzelfde middel, terwijl er in de tussentijd genoeg verandert. Momenten om er opnieuw naar te kijken:

Je vergeet vaker een pil dan je zou willen.
Je hebt klachten die je inmiddels normaal bent gaan vinden.
Je geeft borstvoeding, of je komt richting de overgang.
Je wilt over een tijdje zwanger worden, of juist helemaal niet meer.

Herken je jezelf hierin? Bespreek het bij je volgende afspraak met je huisarts.

Bewaar 'm voor als je die afspraak maakt.

#wereldanticonceptiedag #anticonceptie #depil #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-09-29 · p1 · dinsdag 20:00
Vastpinnen. Vastgezet 1: wie we zijn. Na publicatie handmatig bovenaan het profiel vastzetten.
- Feed, `create_carousel_post`, image_urls in deze volgorde:
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/p1__1.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/p1__2.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/09/p1__3.jpg
- Geen story.

**Caption, letterlijk**

```
Wie zit er eigenlijk achter @mijnpil.nu? Een echte, geregistreerde apotheek, gevestigd in Hardenberg. We staan in het register van online aanbieders van het ministerie van VWS.

Online bestellen betekent bij ons niet dat er minder gecontroleerd wordt. Elke bestelling wordt samengesteld door een apothekersassistente en gecontroleerd door de apotheker.

Op dit account vind je heldere uitleg over anticonceptie, je cyclus en alles eromheen. En af en toe iets om naar je vriendinnen door te sturen.

#apotheek #anticonceptie #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

# oktober 2026

## 2026-10-01 · m19 · donderdag 20:00
Meme. Kleur: roze. Regel: Je laatste tampon ligt altijd los onderin je tas.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m19-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m19-a-story.mp4

**Caption, letterlijk**

```
Zonder verpakking, met een kruimel erop, maar hij is er.

Tag wie ook altijd de reddende engel is.

#menstruatie #tampon #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-10-03 · m31 · zaterdag 11:00
Meme. Kleur: indigo. Regel: Je huid weet precies wanneer je op de foto moet.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m31-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m31-a-story.mp4

**Caption, letterlijk**

```
Drie weken rust, en dan die ene dag.

Tag wie ook altijd op het verkeerde moment gefotografeerd wordt.

#hormonen #cyclus #huid #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-10-06 · p2 · dinsdag 20:00
Vastpinnen. Vastgezet 2: zo werkt bestellen. Na publicatie handmatig bovenaan het profiel vastzetten.
- Feed, `create_carousel_post`, image_urls in deze volgorde:
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p2__1.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p2__2.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p2__3.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p2__4.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p2__5.jpg
- Geen story.

**Caption, letterlijk**

```
Hoe werkt bestellen bij MijnPil.nu? In het kort: je bestelt de anticonceptie die je al gebruikt, en wij sturen het naar je toe.

Wij schrijven zelf niets voor. Bij je eerste bestelling vragen we een foto van je recept, of van een doosje met apotheeketiket, en die controleert de apotheker. Daarna kun je gewoon nabestellen zonder opnieuw iets aan te leveren, of je bestelling automatisch laten herhalen.

Op werkdagen voor 15:00 besteld is dezelfde dag verstuurd, en altijd discreet verzonden.

Alles begint via de link in onze bio.

#anticonceptie #depil #apotheek #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-10-08 · m13 · donderdag 20:00
Meme. Kleur: lavendel. Regel: Je ontdekt dat je strip op is op het moment dat je 'm nodig hebt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m13-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m13-a-story.mp4

**Caption, letterlijk**

```
Nooit een week eerder, altijd op de avond zelf.

Stuur 'm door naar wie dit ook maandelijks overkomt.

#depil #anticonceptie #herhaalrecept #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Praktische tip: zet een herinnering op de dag dat je aan je laatste strip begint. Dan heb je een week speling in plaats van een avond.
```

## 2026-10-10 · m25 · zaterdag 11:00
Meme. Kleur: roze. Regel: Krampen wachten netjes tot je in de trein zit.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m25-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m25-a-story.mp4

**Caption, letterlijk**

```
Thuis niets, perron niets, deuren dicht en daar zijn ze.

Tag wie ook altijd in de spits begint.

#menstruatiepijn #krampen #menstruatie #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Krampen die je dag echt in de weg zitten horen er niet gewoon bij. Bespreek het een keer met je huisarts, er is vaak meer mogelijk dan vrouwen denken. Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-10-13 · p3 · dinsdag 20:00
Vastpinnen. Vastgezet 3: waar we het hier over hebben. Na publicatie handmatig bovenaan het profiel vastzetten.
- Feed, `create_carousel_post`, image_urls in deze volgorde:
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p3__1.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p3__2.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p3__3.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p3__4.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p3__5.jpg
  - https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/p3__6.jpg
- Geen story.

**Caption, letterlijk**

```
Nieuw hier? Welkom bij MijnPil.nu. Hier vind je uitleg over alles wat met je cyclus en je hormonen te maken heeft, van je eerste pil tot de overgang: anticonceptie, hormoonvrije anticonceptie, menstruatie, intieme gezondheid, zwanger worden en de overgang.

Op maandag, woensdag en vrijdag delen we uitleg waar je echt iets aan hebt. Op dinsdag, donderdag en zaterdag posts om naar je vriendinnen door te sturen, want sommige dingen herkent iedere vrouw.

Wat we hier delen is algemene informatie en geen medisch advies. Heb je een vraag over je eigen situatie? Je huisarts is daar de beste plek voor.

Post je zelf iets herkenbaars? Gebruik #vrouwenonderelkaar, de leukste delen we in onze stories.

#anticonceptie #cyclus #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-10-15 · m06 · donderdag 20:00
Meme. Kleur: indigo. Regel: Je menstruatie heeft nog nooit een vakantie overgeslagen.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m06-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m06-a-story.mp4

**Caption, letterlijk**

```
Trouwer dan welke reisgenoot ook.

Stuur 'm door naar wie je koffer deelt.

#menstruatie #vakantie #cyclus #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-10-17 · i02 · zaterdag 11:00
Inhaker. Wereld Menopauzedag: merk je de overgang als je de pil slikt?
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/i02.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/i02-story.mp4

**Caption, letterlijk**

```
Morgen is het Wereld Menopauzedag. Een vraag die we vaak tegenkomen: merk je de overgang eigenlijk wel als je de pil slikt?

Vaak minder dan je zou verwachten. Een combinatiepil regelt je bloedingen en levert zelf hormonen, en kan daardoor klachten zoals een onregelmatige cyclus of opvliegers deels maskeren. Je kunt dus al in de overgang zitten zonder dat je het goed merkt.

Ben je rond de 45 of ouder en gebruik je hormonale anticonceptie? Bespreek dan met je huisarts tot wanneer je die nog nodig hebt en wat een logisch moment is om te stoppen.

Stuur 'm door naar wie hier ook mee bezig is.

#overgang #wereldmenopauzedag #anticonceptie #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-10-20 · m36 · dinsdag 20:00
Meme. Kleur: lavendel. Regel: In het vliegtuig weet je lichaam precies hoe laat het thuis is.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m36-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m36-a-story.mp4

**Caption, letterlijk**

```
Jij zit in een andere tijdzone. Je lichaam niet.

Stuur 'm door naar wie binnenkort ver weg gaat.

#anticonceptie #depil #reizen #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Reis je een paar uur naar het oosten of westen? Vraag je apotheek even hoe je je inname het handigst verschuift, dan hoef je daar ter plekke niet over na te denken. Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-10-22 · m21 · donderdag 20:00
Meme. Kleur: roze. Regel: Je neemt altijd precies één tampon te weinig mee.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m21-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m21-a-story.mp4

**Caption, letterlijk**

```
Twee leek genoeg. Twee was niet genoeg.

Tag je noodcontact voor precies dit moment.

#menstruatie #tampon #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-10-24 · i03 · zaterdag 11:00
Inhaker. Wintertijd: moet je pil een uur opschuiven?
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/i03.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/i03-story.mp4

**Caption, letterlijk**

```
Vannacht gaat de klok een uur terug. Moet je je pil dan ook anders gaan innemen?

Nee, dat hoeft niet. Neem je pil gewoon op je vaste tijd volgens de nieuwe klok. Eén uur verschil valt ruim binnen de marge: bij de meeste pillen is die twaalf uur, en ook bij pillen met een krappere marge van drie uur zit je met één uur nog goed.

Bewaar 'm voor maart, als de klok weer vooruit gaat.

#wintertijd #depil #anticonceptie #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-10-27 · m52 · dinsdag 20:00
Meme. Kleur: indigo. Regel: Je herinnering gaat altijd af op het moment dat je net niet kan.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m52-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m52-a-story.mp4

**Caption, letterlijk**

```
Onder de douche, in de auto, midden in een gesprek.

Stuur 'm door naar wie 'm ook altijd wegdrukt.

#depil #anticonceptie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-10-29 · m32 · donderdag 20:00
Meme. Kleur: lavendel. Regel: Je humeur begint een dag eerder dan je cyclus.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m32-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m32-a-story.mp4

**Caption, letterlijk**

```
Achteraf snap je precies waarom je boos was op die deur.

Stuur 'm door naar wie jou die dag verdraagt.

#pms #hormonen #cyclus #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-10-31 · m14 · zaterdag 11:00
Meme. Kleur: perzik. Regel: Het doosje voelt vol tot je het openmaakt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m14-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/10/m14-a-story.mp4

**Caption, letterlijk**

```
Gewicht zegt niets.

Tag wie ook op gevoel inschat hoeveel er nog in zit.

#anticonceptie #depil #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

# november 2026

## 2026-11-03 · m08 · dinsdag 20:00
Meme. Kleur: roze. Regel: Je pil valt altijd op de enige plek waar je niet bij kan.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m08-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m08-a-story.mp4

**Caption, letterlijk**

```
Achter de wc, onder de kast, tussen de plint. Nooit gewoon op de grond.

Tag wie ook wel eens op haar knieën in de badkamer heeft gelegen.

#depil #anticonceptie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Pil echt kwijt? Bel even je apotheek, die kijkt in een minuut met je mee wat handig is. Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-11-05 · m26 · donderdag 20:00
Meme. Kleur: indigo. Regel: Je kruik ligt altijd in de kast waar je niet bij kan.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m26-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m26-a-story.mp4

**Caption, letterlijk**

```
Bovenste plank, achterin, achter de kerstspullen.

Stuur 'm door naar wie ook een opstapje nodig heeft.

#krampen #menstruatie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-07 · m22 · zaterdag 11:00
Meme. Kleur: lavendel. Regel: Je vindt overal tampons, behalve als je er een zoekt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m22-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m22-a-story.mp4

**Caption, letterlijk**

```
In je jas, in de auto, in die ene la. Nooit nu.

Stuur 'm door naar wie ook overal voorraad heeft, behalve bij zich.

#menstruatie #tampon #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-10 · m33 · dinsdag 20:00
Meme. Kleur: indigo. Regel: Je hebt geen idee welke dag het is, je cyclus wel.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m33-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m33-a-story.mp4

**Caption, letterlijk**

```
De enige agenda die altijd klopt.

Tag wie ook op haar cyclus navigeert.

#cyclus #menstruatie #hormonen #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-12 · m34 · donderdag 20:00
Meme. Kleur: roze. Regel: Je onderbroeken zijn onderverdeeld in twee categorieën, en jij weet precies welke.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m34-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m34-a-story.mp4

**Caption, letterlijk**

```
Iedereen heeft dit systeem, niemand heeft het ooit uitgelegd.

Stuur 'm door naar wie precies weet wat je bedoelt.

#menstruatie #cyclus #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-14 · m15 · zaterdag 11:00
Meme. Kleur: indigo. Regel: Je herhaalrecept valt altijd in de week dat je het al druk hebt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m15-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m15-a-story.mp4

**Caption, letterlijk**

```
Nooit in die ene rustige week.

Stuur 'm door naar wie haar agenda ook niet meer ziet zitten.

#herhaalrecept #apotheek #anticonceptie #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-17 · m09 · dinsdag 20:00
Meme. Kleur: lavendel. Regel: De pilstrip zit altijd in de tas die je vandaag niet meeneemt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m09-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m09-a-story.mp4

**Caption, letterlijk**

```
De ene tas heeft alles. Vandaag gebruik je de andere.

Stuur 'm door naar wie drie tassen heeft en nooit de juiste.

#depil #anticonceptie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-19 · m23 · donderdag 20:00
Meme. Kleur: indigo. Regel: Je cup ligt altijd te drogen op het moment dat je 'm nodig hebt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m23-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m23-a-story.mp4

**Caption, letterlijk**

```
Schoon, klaar, en aan de verkeerde kant van het huis.

Tag je cupvriendin.

#menstruatiecup #menstruatie #duurzaam #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-21 · m45 · zaterdag 11:00
Meme. Kleur: perzik. Regel: Je huilt om een reclame en weet precies waarom.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m45-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m45-a-story.mp4

**Caption, letterlijk**

```
Een verzekeringsreclame. Met een hond.

Tag wie jou die week het beste kent.

#pms #hormonen #cyclus #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-24 · m27 · dinsdag 20:00
Meme. Kleur: roze. Regel: De eerste dag valt altijd samen met de dag die je niet kunt verzetten.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m27-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m27-a-story.mp4

**Caption, letterlijk**

```
Presentatie, rijexamen, bruiloft. Kies maar.

Tag wie dit ook een keer heeft meegemaakt.

#menstruatie #cyclus #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-26 · m37 · donderdag 20:00
Meme. Kleur: perzik. Regel: Je hebt alles ingepakt, behalve het enige wat niet kan wachten.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m37-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m37-a-story.mp4

**Caption, letterlijk**

```
Drie paar schoenen wel.

Tag wie pas op het vliegveld nadenkt.

#reizen #anticonceptie #depil #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-11-28 · m53 · zaterdag 11:00
Meme. Kleur: roze. Regel: Je zet de herinnering vijf minuten later en dan is het ineens morgen.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m53-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/11/m53-a-story.mp4

**Caption, letterlijk**

```
Vijf minuten is een rekbaar begrip.

Tag wie dit ook doet en het ontkent.

#depil #pilvergeten #anticonceptie #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Pil een keer vergeten? Bij de combinatiepil ben je bij één vergeten pil meestal gewoon beschermd, maar het hangt af van waar je in de strip zit. Bel je apotheek als je twijfelt. Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

# december 2026

## 2026-12-01 · i04 · dinsdag 20:00
Inhaker. Wereld Aidsdag: beschermt de pil ook tegen soa's?
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/i04.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/i04-story.mp4

**Caption, letterlijk**

```
Vandaag is het Wereld Aidsdag. Tijd voor een vraag met een kort antwoord: beschermt de pil je ook tegen soa's?

Nee. De pil, de ring, de pleister, het spiraaltje en het staafje beschermen tegen zwangerschap, maar niet tegen soa's zoals chlamydia of hiv. Condooms zijn het enige anticonceptiemiddel dat daar wel tegen beschermt.

Heb je een nieuwe partner, of twijfel je? Laat je testen bij je huisarts of bij het Centrum Seksuele Gezondheid van de GGD.

Stuur 'm door naar wie dit wel even mag horen.

#wereldaidsdag #soa #condoom #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-12-03 · m07 · donderdag 20:00
Meme. Kleur: indigo. Regel: Het weekendje weg stond al geboekt, de stopweek wist dat allang.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m07-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m07-a-story.mp4

**Caption, letterlijk**

```
Geboekt in maart, geregeld in juni, en toch precies die week.

Stuur 'm door naar wie het weekend organiseert.

#stopweek #anticonceptie #weekendje #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-05 · m16 · zaterdag 11:00
Meme. Kleur: lavendel. Regel: Je badkamerkastje is optimistischer over je voorraad dan de werkelijkheid.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m16-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m16-a-story.mp4

**Caption, letterlijk**

```
Vol met van alles, leeg aan het enige wat je zoekt.

Tag wie haar kastje ook niet durft op te ruimen.

#herkenbaar #vrouwengezondheid #badkamer #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-08 · m24 · dinsdag 20:00
Meme. Kleur: roze. Regel: Er zit altijd een tampon in je jaszak, alleen niet in de jas van vandaag.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m24-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m24-a-story.mp4

**Caption, letterlijk**

```
Jassen hebben een eigen systeem en dat is niet het jouwe.

Stuur 'm door naar wie ook drie jassen en nul tampons bij zich heeft.

#menstruatie #tampon #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-10 · m46 · donderdag 20:00
Meme. Kleur: lavendel. Regel: Je hebt nergens zin in, behalve in alles tegelijk.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m46-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m46-a-story.mp4

**Caption, letterlijk**

```
Uitgaan, op de bank liggen, verhuizen. Allemaal tegelijk.

Stuur 'm door naar wie dit gevoel kent.

#pms #hormonen #cyclus #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-12 · i05 · zaterdag 11:00
Inhaker. Feestdagen: valt je stopweek precies met kerst?
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/i05.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/i05-story.mp4

**Caption, letterlijk**

```
Kerst komt eraan. Tijd om even in je strip te kijken: valt je stopweek precies op de feestdagen?

Bij veel combinatiepillen kun je de stopweek overslaan door meteen met een nieuwe strip te beginnen. De bloeding in je stopweek is een onttrekkingsbloeding en geen echte menstruatie, dus medisch gezien is daar geen bezwaar tegen.

Let op: bij pillen met verschillende fases of met placebopillen in de strip werkt dit anders. Kijk in je bijsluiter of overleg met je huisarts als je het niet zeker weet.

En check meteen of je genoeg strips in huis hebt, zeker als je een week doorslikt.

Bewaar 'm voor je volgende strip.

#stopweek #feestdagen #depil #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-12-15 · m10 · dinsdag 20:00
Meme. Kleur: indigo. Regel: Je pilstrip ligt thuis precies op de plek waar je nooit kijkt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m10-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m10-a-story.mp4

**Caption, letterlijk**

```
Je hebt overal gezocht behalve daar, en daar lag hij.

Tag wie 'm ook altijd op de gekste plek terugvindt.

#depil #anticonceptie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-17 · m28 · donderdag 20:00
Meme. Kleur: roze. Regel: Krampen weten precies wanneer je moet staan.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m28-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m28-a-story.mp4

**Caption, letterlijk**

```
In de rij, in de tram, in de supermarkt.

Stuur 'm door naar wie vandaag ook op haar tanden bijt.

#menstruatiepijn #krampen #menstruatie #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Warmte helpt vaak meer dan je denkt, en bewegen ook. Blijft het elke maand zo? Dan is het een gesprek met je huisarts waard. Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2026-12-19 · m42 · zaterdag 11:00
Meme. Kleur: lavendel. Regel: Er bestaat geen discrete manier om een tampon mee te nemen, en toch probeer je het.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m42-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m42-a-story.mp4

**Caption, letterlijk**

```
Mouw, zak, telefoonhoesje. Het is nooit subtiel.

Stuur 'm door naar wie het ook elke keer weer probeert.

#menstruatie #tampon #werk #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-22 · m35 · dinsdag 20:00
Meme. Kleur: perzik. Regel: Je wasmachine kent jouw cyclus inmiddels ook.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m35-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m35-a-story.mp4

**Caption, letterlijk**

```
Elke maand dezelfde afspraak.

Tag wie ook maandelijks een extra wasje draait.

#menstruatie #cyclus #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-24 · m17 · donderdag 20:00
Meme. Kleur: lavendel. Regel: Je hebt nog één strip, en dat weet je pas op zondagavond.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m17-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m17-a-story.mp4

**Caption, letterlijk**

```
Precies als alles dicht is.

Stuur 'm door naar wie dit ook op zondag ontdekt.

#depil #apotheek #anticonceptie #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-26 · m38 · zaterdag 11:00
Meme. Kleur: roze. Regel: Op reis is je strip het enige wat je twee keer controleert.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m38-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m38-a-story.mp4

**Caption, letterlijk**

```
Paspoort, sleutels, strip. En dan nog een keer de strip.

Stuur 'm door naar wie ook drie keer in haar tas kijkt.

#reizen #depil #anticonceptie #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-29 · m47 · dinsdag 20:00
Meme. Kleur: perzik. Regel: De chocola in huis weet dat haar tijd gekomen is.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m47-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m47-a-story.mp4

**Caption, letterlijk**

```
Ze lag daar al weken rustig te wachten.

Tag wie haar voorraad ook op peil houdt.

#pms #cyclus #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2026-12-31 · m54 · donderdag 20:00
Meme. Kleur: indigo. Regel: De enige datum die je uit je hoofd kent, is die van je strip.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m54-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2026/12/m54-a-story.mp4

**Caption, letterlijk**

```
Verjaardagen niet, dit wel.

Stuur 'm door naar wie jouw verjaardag ook vergeet.

#depil #anticonceptie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

# januari 2027

## 2027-01-02 · m41 · zaterdag 11:00
Meme. Kleur: roze. Regel: Een witte stoel voelt in die week als een persoonlijke aanval.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m41-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m41-a-story.mp4

**Caption, letterlijk**

```
Wie ontwerpt die dingen.

Tag wie ook altijd de donkere stoel uitzoekt.

#menstruatie #herkenbaar #cyclus #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-05 · m29 · dinsdag 20:00
Meme. Kleur: perzik. Regel: Je pijnstillers liggen altijd in je andere tas.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m29-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m29-a-story.mp4

**Caption, letterlijk**

```
Samen met je pleisters en je goede voornemens.

Tag wie altijd wel iets bij zich heeft.

#krampen #menstruatie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-07 · m48 · donderdag 20:00
Meme. Kleur: lavendel. Regel: Je geduld raakt een week eerder op dan je strip.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m48-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m48-a-story.mp4

**Caption, letterlijk**

```
En dat is precies te voorspellen.

Stuur 'm door naar wie dit van je pikt.

#pms #hormonen #cyclus #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-09 · m18 · zaterdag 11:00
Meme. Kleur: perzik. Regel: De apotheek is altijd net dicht als je eraan denkt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m18-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m18-a-story.mp4

**Caption, letterlijk**

```
Je denkt er de hele dag niet aan, en dan om vijf over zes wel.

Tag wie ook altijd net te laat is.

#apotheek #herhaalrecept #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-12 · m56 · dinsdag 20:00
Meme. Kleur: indigo. Regel: Je weet in elke winkel precies waar het schap staat.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m56-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m56-a-story.mp4

**Caption, letterlijk**

```
Zonder te kijken, zonder te vragen.

Stuur 'm door naar wie jou hier ooit heen heeft gestuurd.

#menstruatie #herkenbaar #vrouwengezondheid #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-14 · m11 · donderdag 20:00
Meme. Kleur: perzik. Regel: Niets is zo onzeker als de vraag of je 'm vanochtend genomen hebt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m11-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m11-a-story.mp4

**Caption, letterlijk**

```
Je weet het zeker. Tot je even naar de strip kijkt.

Stuur 'm door naar wie hier ook wel eens over twijfelt.

#depil #pilvergeten #anticonceptie #vrouwenonderelkaar #mijnpilnu
```

**Eerste reactie eronder**

```
Twijfel je of je 'm genomen hebt? Je apotheek denkt hier zo met je mee, en dat is een betere bron dan je geheugen om half twaalf 's avonds. Let op: dit is algemene informatie en geen medisch advies. Twijfel je, of heb je klachten? Overleg met je huisarts of apotheker.
```

## 2027-01-16 · m49 · zaterdag 11:00
Meme. Kleur: lavendel. Regel: Alles is irritant, en de meeste dingen hebben niets gedaan.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m49-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m49-a-story.mp4

**Caption, letterlijk**

```
Sorry tegen de wasmachine, de buurman en die ene app.

Tag wie hier deze week begrip voor heeft.

#pms #hormonen #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-19 · m57 · dinsdag 20:00
Meme. Kleur: roze. Regel: De zelfscankassa vraagt altijd om controle bij precies dat ene product.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m57-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m57-a-story.mp4

**Caption, letterlijk**

```
Nooit bij de melk.

Tag wie dit ook een keer is overkomen.

#menstruatie #herkenbaar #boodschappen #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-21 · m30 · donderdag 20:00
Meme. Kleur: perzik. Regel: Je onderrug weet het eerder dan jij.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m30-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m30-a-story.mp4

**Caption, letterlijk**

```
Nog voor je app iets zegt.

Stuur 'm door naar wie het ook altijd in haar rug voelt.

#menstruatie #cyclus #krampen #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-23 · m20 · zaterdag 11:00
Meme. Kleur: indigo. Regel: Je voorraad raakt altijd op tijdens de drukste dag.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m20-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m20-a-story.mp4

**Caption, letterlijk**

```
Niet op dag vier. Op dag twee.

Stuur 'm door naar wie dit ook elke keer verkeerd inschat.

#menstruatie #maandverband #tampon #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-26 · m58 · dinsdag 20:00
Meme. Kleur: lavendel. Regel: Je hebt voor elke tas een noodplan.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m58-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m58-a-story.mp4

**Caption, letterlijk**

```
Eentje in het vak, eentje in de rits, eentje ergens onderin.

Stuur 'm door naar wie altijd voorbereid is.

#menstruatie #herkenbaar #tampon #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-28 · m50 · donderdag 20:00
Meme. Kleur: roze. Regel: Je agenda en je zin om iets te doen lopen die week niet gelijk.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m50-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m50-a-story.mp4

**Caption, letterlijk**

```
Je hebt het allemaal zelf ingepland, dat is het vervelende.

Stuur 'm door naar wie ook wel eens iets afzegt.

#pms #cyclus #hormonen #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-01-30 · m39 · zaterdag 11:00
Meme. Kleur: perzik. Regel: Je koffer heeft altijd plek, behalve voor het kleinste doosje.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m39-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/01/m39-a-story.mp4

**Caption, letterlijk**

```
De föhn past wel.

Tag wie ook te groot inpakt en te klein vergeet.

#reizen #anticonceptie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

# februari 2027

## 2027-02-02 · m55 · dinsdag 20:00
Meme. Kleur: indigo. Regel: Je telefoon houdt je cyclus beter bij dan jij je afspraken.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m55-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m55-a-story.mp4

**Caption, letterlijk**

```
Eén van de twee is in elk geval op orde.

Tag wie ook op haar telefoon vertrouwt.

#cyclus #menstruatie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-02-04 · m44 · donderdag 20:00
Meme. Kleur: lavendel. Regel: De wasmand houdt bij welke week het is.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m44-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m44-a-story.mp4

**Caption, letterlijk**

```
Een rustige, betrouwbare kalender.

Stuur 'm door naar wie dit meteen snapt.

#menstruatie #cyclus #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-02-06 · m12 · zaterdag 11:00
Meme. Kleur: roze. Regel: De strip in je nachtkastje is altijd van vorige maand.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m12-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m12-a-story.mp4

**Caption, letterlijk**

```
Leeg, en toch ligt hij er nog steeds.

Tag wie haar nachtkastje ook nooit opruimt.

#depil #anticonceptie #herkenbaar #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-02-09 · m40 · dinsdag 20:00
Meme. Kleur: perzik. Regel: Je krampen wachten netjes tot de vergadering begint.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m40-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m40-a-story.mp4

**Caption, letterlijk**

```
Agendapunt één, en daar zijn ze.

Stuur 'm door naar wie vandaag ook een volle agenda heeft.

#krampen #werk #menstruatie #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-02-11 · m43 · donderdag 20:00
Meme. Kleur: indigo. Regel: Het spiegelkastje zit vol, en toch is er nooit wat je zoekt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m43-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m43-a-story.mp4

**Caption, letterlijk**

```
Wel drie soorten dagcrème.

Tag wie haar kastje ook eindelijk eens gaat uitzoeken.

#herkenbaar #badkamer #vrouwengezondheid #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-02-13 · m59 · zaterdag 11:00
Meme. Kleur: lavendel. Regel: Er ligt ergens in je huis een tampon die je nooit meer terugvindt.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m59-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m59-a-story.mp4

**Caption, letterlijk**

```
Hij duikt op bij de verhuizing.

Tag wie 'm ooit nog gaat vinden.

#menstruatie #herkenbaar #tampon #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.

## 2027-02-16 · m51 · dinsdag 20:00
Meme. Kleur: roze. Regel: Je cyclusapp is optimistischer over je regelmaat dan jij.
- Feed, `create_image_post`
  image_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m51-a.jpg
- Story, `create_story`
  video_url: https://dakeyne-ship-it.github.io/mijnpil-media/ig/2027/02/m51-a-story.mp4

**Caption, letterlijk**

```
Zij zegt woensdag. Jij weet wel beter.

Tag wie haar app ook niet helemaal gelooft.

#cyclus #menstruatie #hormonen #vrouwenonderelkaar #mijnpilnu
```

Geen eerste reactie. Deze post doet geen medische uitspraak.
