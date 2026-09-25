# mijnpil-media

Publieke beeldhost voor de Instagram-publicatie van **mijnpil.nu**.

Instagram accepteert geen upload: de Graph API haalt elk beeld op via een
publieke URL. Deze repository wordt via GitHub Pages geserveerd en levert die
URL's.

## Structuur

    docs/                   de publicatiedocumenten die de geplande taken lezen,
                            plus het overzicht van hoe alles draait
    ig/<jaar>/<maand>/      gerenderd beeld: .jpg voor feed en carrousel (1080 x 1350),
                            .mp4 voor reels en stories (1080 x 1920), -cover.jpg voor reelomslagen
    library/illustraties/   bronillustraties in de huisstijl, voor nieuwe posts
    pipeline/               de code en bronnen waarmee alles gemaakt wordt
    gbp/                    beeld voor Google Bedrijfsprofiel

In `ig/` staat alleen wat in een van de twee publicatiedocumenten voorkomt.

## Let op

Alles in deze repository is openbaar. Hier komt uitsluitend gerenderd
marketingbeeld in, nooit klantgegevens of ongepubliceerde content.

Bestanden ouder dan ongeveer een maand kunnen weg: zodra een post gepubliceerd
is, bewaart Instagram zijn eigen kopie.
