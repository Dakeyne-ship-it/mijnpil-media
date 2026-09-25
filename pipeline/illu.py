# -*- coding: utf-8 -*-
"""Bibliotheekillustraties klaarmaken voor social.

- lavendel uit 2019 (#807fbc, schaduw #7372a9) naar het huidige lavendel
  (#9e9dce), met een zachte overgang zodat de randen niet rafelen
- een beeld in een vak van elke maat zetten door het egale achtergrondvlak door
  te trekken, nooit door het onderwerp bij te snijden
"""
import pathlib
import numpy as np
from PIL import Image

LIB = (pathlib.Path(__file__).parent.parent / "library" / "illustraties").resolve()
CACHE = (pathlib.Path(__file__).parent / "html" / "illu").resolve()
OUD = [np.array([0x80, 0x7f, 0xbc]), np.array([0x73, 0x72, 0xa9])]
NIEUW = np.array([0x9e, 0x9d, 0xce])


def herkleur(im):
    a = np.asarray(im.convert("RGB")).astype(float)
    delta = NIEUW - OUD[0]
    w = np.zeros(a.shape[:2])
    for ref in OUD:
        d = np.sqrt(((a - ref) ** 2).sum(-1))
        w = np.maximum(w, np.clip(1 - d / 45, 0, 1))
    a = a + w[..., None] * delta
    return Image.fromarray(np.clip(a, 0, 255).astype("uint8"))


def in_vak(naam, w, h, schaal=1.0, anker=1.0):
    """Beeld passend in w x h, achtergrond doorgetrokken. anker: verticale
    positie van het beeld in het vak (0 boven, 1 onder)."""
    src = Image.open(LIB / naam).convert("RGBA")
    wit = Image.new("RGBA", src.size, (255, 255, 255, 255))
    wit.alpha_composite(src)
    im = herkleur(wit)
    # witte of transparante marges eraf, dan is de meest voorkomende kleur het vlak
    a = np.asarray(im).astype(int)
    alfa = np.asarray(src)[..., 3].astype(int)
    vol = (alfa > 250) & (a < 250).any(-1)
    kol = np.where(vol.mean(0) > 0.5)[0]
    rij = np.where(vol.mean(1) > 0.5)[0]
    im = im.crop((kol.min() + 4, rij.min() + 4, kol.max() - 3, rij.max() - 3))
    kl, n = np.unique(np.asarray(im.resize((200, 200))).reshape(-1, 3), axis=0, return_counts=True)
    bg = tuple(int(x) for x in kl[n.argmax()])
    f = min(w / im.width, h / im.height) * schaal
    im = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
    vak = Image.new("RGB", (w, h), bg)
    vak.paste(im, ((w - im.width) // 2, round((h - im.height) * anker)))
    CACHE.mkdir(parents=True, exist_ok=True)
    out = CACHE / f"{pathlib.Path(naam).stem}_{w}x{h}.png".replace(" ", "_")
    vak.save(out)
    return out, "#%02x%02x%02x" % bg
