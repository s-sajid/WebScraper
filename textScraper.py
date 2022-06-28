from bs4 import BeautifulSoup
import os

class TextScraper():
    def textScrape(self):
        target_dir = 'webpages_processed'

        _, _, files = next(os.walk(target_dir))
        file_count = len(files)
        count = 1

        while count <= file_count:
            source = f"{target_dir}/page{count}.html"

            with open(source) as html_file:
                soup = BeautifulSoup(html_file, 'lxml')

            text = soup.find_all(text=True)

            output = ''
            blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head', 
                'input',
                'script',
                'style'
            ]

            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t)
                    with open(f"output/outputText{count}.txt", 'w') as f:
                        f.write(output)
            f.close()
            count += 1