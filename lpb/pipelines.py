import re
import sqlite3


class LpbPipeline:
    conn = sqlite3.connect('lpb.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `lpb` (
                                                                        title varchar(100),
                                                                        description text,
                                                                        date text
                                                                        )''')
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            title = item['title']
            title = re.sub('"', "'", title).strip()
        except:
            title = ''
        try:
            description = item['description']
            description = re.sub('"', "'", description)
        except:
            description = ''
        try:
            date = item['date'].strip()
        except:
            date = ''

        self.cursor.execute(f'''select * from lpb where title = "{title}" and date = "{date}"''')
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(
                f'''insert into `lpb` (`title`, `description`, `date`) values ("{title}", "{description}", "{date}")''')
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
