BOT_NAME = 'lpb'

SPIDER_MODULES = ['lpb.spiders']
NEWSPIDER_MODULE = 'lpb.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'lpb.pipelines.LpbPipeline': 100,

}