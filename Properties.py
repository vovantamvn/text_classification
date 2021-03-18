class Properties:
    def __init__(self):
        self.types = ['the-thao',
                      'the-gioi',
                      'kinh-doanh',
                      'giai-tri',
                      'phap-luat',
                      'giao-duc',
                      'suc-khoe',
                      'doi-song',
                      'du-lich',
                      'khoa-hoc']

    def get_types(self):
        return self.types[:]

    def get_data_path_of_type(self, type: str):
        return './data/{}.txt'.format(type)

    def get_crawl_path_of_type(self, type: str):
        return './crawl/{}.txt'.format(type)