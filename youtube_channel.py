# -*- coding: utf-8 -*-

import StringIO

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import parslepy

from parslepy_functions import selector_handler


# This is kinda cumbersome, but I couldn't find a shorter way
# that works with Scrapy using -o output.json at command line
class FlexibleItem(scrapy.Item):
    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = scrapy.Field()
        super(FlexibleItem, self).__setitem__(key, value)


class ChannelVideosSpider(CrawlSpider):
    name = 'channel-videos'
    allowed_domains = ['youtube.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"), callback='parse_item'),
    )

    def __init__(self, parselet=None, channel=None, **kwargs):
        if not parselet or not channel:
            raise ValueError(
                'Please provide parselet and channel arguments (hint: use -a)')

        with open(parselet) as fp:
            self.parselet = parslepy.Parselet.from_jsonfile(
                fp, selector_handler=selector_handler)

        self.start_urls = ['https://www.youtube.com/user/%s/videos' % channel]
        super(ChannelVideosSpider, self).__init__(**kwargs)

    def apply_parselet(self, response):
        return self.parselet.parse(StringIO.StringIO(response.body))

    def parse_item(self, response):
        item = FlexibleItem(self.apply_parselet(response))

        # maybe it would be interesting if parslepy offered some way
        # of doing this kind of thing on the parselet -- no idea how, tho
        item['url'] = response.url

        return item
