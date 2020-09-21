import scrapy



class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = [
        'https://kopeyka.od.ua/napitki/kofe',
        'https://kopeyka.od.ua/napitki/kofe?start=20'
    ]

    def parse(self, response):
        for prod_div in response.css('div.prod'):
            link = prod_div.css('span.prod-ttl')
            print(link)
            title = link.css('::text').get().encode().decode()
            print(title)
            href = link.css('::attr(href)').get()
            print(href)
            raw_price = prod_div.css('ul.prod-price li.new-prc::text').get()

            price = raw_price

            yield {
                'title': title,
                'href': response.urljoin(href),
                'price_grivna': price,
                #'imgs': [response.urljoin(img) for img in img_urls],
            }
