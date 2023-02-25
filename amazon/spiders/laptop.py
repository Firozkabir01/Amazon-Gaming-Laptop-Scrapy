import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LaptopSpider(CrawlSpider):
    name = "laptop"
    # allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/s?k=gaming+laptops&page=2&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=WXE2GAFRBDQY4E1HDG2D&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1677334392&ref=sr_pg_1"
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]'),
             callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]'),
             follow=True)
        )

    def parse_item(self, response):
        yield {
            'title': response.xpath('//span[@id="productTitle"]/text()').get().strip(),
            'price': response.xpath('//span[@class="a-price aok-align-center"]/span/text()').get(),
            'ratings': response.xpath('(//span[@id="acrCustomerReviewText"])[1]/text()').get(),
            'stars': response.xpath('(//a[@class="a-popover-trigger a-declarative"]/i/span)[1]/text()').get(),
            'shipping+tax': response.xpath('(//span[contains(text(), "Shipping & Import")])[1]/text()').get(),
            'brand': response.xpath('(//tr[@class="a-spacing-small po-brand"]/td/span)[2]/text()').get(),
            'series': response.xpath('(//tr[@class="a-spacing-small po-model_name"]/td/span)[2]/text()').get(),
            'screenSize': response.xpath('(//tr[@class="a-spacing-small po-display.size"]/td/span)[2]/text()').get(),
            'color': response.xpath('(//tr[@class="a-spacing-small po-color"]/td/span)[2]/text()').get(),
            'hard_disk_size': response.xpath('(//tr[@class="a-spacing-small po-hard_disk.size"]/td/span)[2]/text()').get(),
            'cpu_model': response.xpath('(//tr[@class="a-spacing-small po-cpu_model.family"]/td/span)[2]/text()').get(),
            'ram': response.xpath('(//tr[@class="a-spacing-small po-ram_memory.installed_size"]/td/span)[2]/text()').get(),
            'OS': response.xpath('(//tr[@class="a-spacing-small po-operating_system"]/td/span)[2]/text()').get(),
            'card_description': response.xpath('(//tr[@class="a-spacing-small po-graphics_description"]/td/span)[2]/text()').get(),
            'graphics_coprocessor': response.xpath('(//tr[@class="a-spacing-small po-graphics_coprocessor"]/td/span)[2]/text()').get()
        }
