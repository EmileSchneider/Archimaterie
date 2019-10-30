# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class zefixUnternehmen(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    geschaeftssitz = scrapy.Field()
    status = scrapy.Field()
    adresse = scrapy.Field()
    plz = scrapy.Field()
    ort = scrapy.Field()
    rechtsform = scrapy.Field()
    handelsregisternr = scrapy.Field()
    chId = scrapy.Field()
    ehraId = scrapy.Field()
    hrauszugkanton = scrapy.Field()
    amt = scrapy.Field()
    revisionsstelle = scrapy.Field()
    unternehmenszweck = scrapy.Field()
    frueherefassungen = scrapy.Field()
