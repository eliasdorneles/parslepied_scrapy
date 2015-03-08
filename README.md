Playing with Scrapy and Parslepy
================================

Toy experiment using [Scrapy][1] to build a simple crawler
decoupling scraping logic, delegated to [Parslepy][2].

#### Install the dependencies:

    pip install scrapy parslepy


#### Run it with:

    scrapy runspider youtube_channel.py -a parselet=video_parselet.json \
        -a channel=LongboardUK -o longboard_videos.jl

You can run it for any youtube channel:

    scrapy runspider youtube_channel.py -a parselet=video_parselet.json \
        -a channel=portadosfundos -o porta_videos.jl

And you can use the alternate parselet file that also scrapes tags:

    scrapy runspider youtube_channel.py -a parselet=video_with_tags_parselet.json \
        -a channel=portadosfundos -o porta_videos.jl


[1]: http://www.scrapy.org
[2]: http://github.com/redapple/parslepy
