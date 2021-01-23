# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class PhysicianPipeline:
    def process_item(self, item, spider):
        # if item['Title']:
        #     item['Title'] = item['Title'].upper()
        if item['Comments']:
            item['Comments'] = [x.strip() for x in item['Comments']]
        if item['Content']:
            item['Content'] = ' '.join([x for x in item['Content']])
            
            start = item['Content'].find('</a>')
            ending = item['Content'].find('<p class="comment-disclaimer">')            
            
            item['Content'] = item['Content'][start:ending]
            pattern = re.compile('</*[ap]>')
            item['Content'] = re.sub(pattern, '', item['Content'])

        return item
