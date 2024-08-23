import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://nobero.com/products/men-oversized-t-shirt-6?variant=45387325014182',
        'https://nobero.com/products/men-oversized-t-shirt-6?variant=44029882761382',
        'https://nobero.com/products/wandersoul-oversized-t-shirt?variant=44967822196902',
        'https://nobero.com/products/less-scrolling-oversized-t-shirt?variant=44791975411878',
        'https://nobero.com/products/dimensions-oversized-t-shirt?variant=45483260018854',
        'https://nobero.com/products/limitations-oversized-t-shirt?variant=45724124938406'
    ]
    

    def parse(self, response):
        title = response.css('.leading-none::text').extract_first().strip()
        url = response.css('img::attr(srcset)').extract_first().strip()
        off = response.css('#variant-save-flat::text').extract_first().strip()
        MRP = response.css('span#variant-compare-at-price::text').get()
        last_7_days = response.css(r'.leading-\[0\.875rem\]::text').extract_first().strip()

        color_size_pairs = []
        options = response.css('select[name="id"] option')
        for option in options:
            color_size_variant = option.css('::text').get()
            if ' / ' in color_size_variant:
                color, size = color_size_variant.split(' / ')
                color_size_pairs.append({
                    'color': color.strip(),
                    'size': size.strip()
                })
       
        sizes = response.css('input.size-select-input::attr(value)').extract()
        unique_sizes = list(set(sizes))

        fit = response.css('div.product-metafields-values p::text').get()
        fabric = response.css('div.product-metafields-values:contains("Fabric") p::text').get().strip()
        neck = response.css('div.product-metafields-values:contains("Neck") p::text').get().strip()
        sleeve = response.css('div.product-metafields-values:contains("Sleeve") p::text').get().strip()
        pattern = response.css('div.product-metafields-values:contains("Pattern") p::text').get().strip()
        length = response.css('div.product-metafields-values:contains("Length") p::text').get().strip()

        # Create the item
        item = {
            'product': title,
            'url': url,
            'price': '₹400',
            'off': off,
            'MRP': '₹999',
            'last_7_days': last_7_days,
            'variants': color_size_pairs,
            'sizes': unique_sizes,
            'fit': fit,
            'fabric': fabric,
            'neck': neck,
            'sleeve': sleeve,
            'pattern': pattern,
            'length': length
        }
        
       
        
       
        # Optionally, yield the item for further processing or output
        yield item
        