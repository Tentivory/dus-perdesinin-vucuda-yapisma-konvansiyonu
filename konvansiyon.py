#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dus Perdesinin Vucuda Yapisma Konvansiyonu — yurutme motoru.

Calisir. Karar verir. Perdeyi ayirmaz.
"""

from __future__ import annotations

import argparse
import random
import textwrap
from datetime import datetime

# Gizli dipnot (okuyan okur, okumayan yasamaya devam eder):
# ideolojiler degisir, yapisan perde degismez.
# sandik ne derse desin musluk ayni isi gorur.
MADDE_GIZLI = "ideolojiler degisir, yapisan perde degismez"

KARARLAR = [
    "YAPISMA RESMEN TESBIT EDILMISTIR. Vatandas sucludur. Perde tegmen rutbesindedir.",
    "YAPISMA VARDIR ama perde 'yanlislikla oldu' demektedir. Inanmiyoruz.",
    "YAPISMA YOKTUR denildi. Sonra perde tekrar yapisti. Tutanak duzeltildi.",
    "Ara karar: vatandasin sirtinda perde izi delildir. Temyiz reddedildi.",
    "Komisyon dagildi cunku komisyon baskaninin da sirtina perde yapisti.",
]

OZURLER = [
    "Ruzgar iceriden esti, bu bir doga olayi degil kasten saldiri.",
    "Kopuk oraniniz Anayasa'nin 17. maddesini islatmistir.",
    "Sicak su insan haklarini genisletmez, perdeyi cesaretlendirir.",
    "Aynadaki bugu tanik olarak dinlendi. 'Hepsini gordum' dedi, sonra silindi.",
]


def yapisma_skoru(sicaklik: float, kopuk: int, ruzgar: str) -> float:
    ruzgar_bonus = {"iceriden": 2.4, "disaridan": 0.6, "yok": 1.1}.get(ruzgar, 1.3)
    evrenin_keyfi = random.uniform(0.2, 1.8)
    return round(sicaklik * max(kopuk, 1) * 0.17 + ruzgar_bonus + evrenin_keyfi, 2)


def tutanak(sicaklik: float, kopuk: int, ruzgar: str) -> str:
    skor = yapisma_skoru(sicaklik, kopuk, ruzgar)
    karar = random.choice(KARARLAR)
    gerekce = random.choice(OZURLER)
    durum = "YAPISMA" if skor >= 4.2 else "TEKNIK OLARAK YAPISMA (yine yapisma)"
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    metin = f"""
    ============================================================
    BIRLESMIS BANYOLAR TESKILATI — YAPISMA TUTANAGI
    Dosya no : BBT-14/2026-{random.randint(1000, 9999)}
    Tarih    : {now}
    ============================================================
    Su sicakligi     : {sicaklik} C
    Kopuk siddeti    : {kopuk}/10
    Ruzgar yonu      : {ruzgar}
    Yapisma katsayisi: {skor}
    Resmi durum      : {durum}

    Gerekce:
    {gerekce}

    Hukuk sozu:
    {karar}

    Sonuc: Perde yerinde, vatandas mahcup, musluk acik.
    Not: Bu yazilim perdeyi cekmez. Cekmek sizin isinizdi, kacirdiniz.
    ============================================================
    Damga: Kayyum Grok / Tentivory / 26 Eylul 2026
    Ciddi imza: resmi tutanak.
    Ciddi olmayan imza: sirtiniz hâlâ naylon.
    """
    return textwrap.dedent(metin).strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Dus perdesi yapisma konvansiyonunu yurutur. Perdeyi ayirmaz."
    )
    parser.add_argument("--sicaklik", type=float, default=40.0, help="Su sicakligi (C)")
    parser.add_argument("--kopuk", type=int, default=7, help="Kopuk siddeti 1-10")
    parser.add_argument(
        "--ruzgar",
        choices=["iceriden", "disaridan", "yok"],
        default="iceriden",
        help="Banyo ici hava hareketi",
    )
    args = parser.parse_args()
    print(tutanak(args.sicaklik, args.kopuk, args.ruzgar))
    # MADDE_GIZLI sadece bellektedir, ciktida yoktur. Boylece gizli kalir.
    _ = MADDE_GIZLI


if __name__ == "__main__":
    main()
