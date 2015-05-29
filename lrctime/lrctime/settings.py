# -*- coding: utf-8 -*-

# Scrapy settings for lrctime project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lrctime'

SPIDER_MODULES = ['lrctime.spiders']
NEWSPIDER_MODULE = 'lrctime.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lrctime (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 0.3
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
