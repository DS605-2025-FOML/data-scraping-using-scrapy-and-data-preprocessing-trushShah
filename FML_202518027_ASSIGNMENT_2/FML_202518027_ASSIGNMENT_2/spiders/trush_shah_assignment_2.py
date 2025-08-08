import scrapy
from FML_202518027_ASSIGNMENT_2.items import Fml202518027Assignment2Item

class ProductSpider(scrapy.Spider):
    name = "Product_Books"
    start_urls = [
        'https://books.toscrape.com/'
    ]

    def parse(self, response):
        all_div_BOOKS = response.css('article.product_pod')


        for BOOKS_div in all_div_BOOKS:
            
            items = Fml202518027Assignment2Item()
            Title = BOOKS_div.css('.product_pod h3 a::attr(title)').extract_first()
            Price = BOOKS_div.css('p.price_color::text').extract_first()
            Rating = BOOKS_div.css('p.star-rating::attr(class)').extract_first()
            Availability = BOOKS_div.css('p.instock.availability::text').getall()[1].strip()

            items['Title'] = Title
            items['Price'] = Price
            items['Rating'] = Rating
            items['Availability'] = Availability

            yield items
            
        
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)