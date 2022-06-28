import os
import shutil

class PageProcesser():
    def pageProcess(self):
        source_dir = 'webpages_raw'
        target_dir = 'webpages_processed'
        file_names = []

        for dirpath, subdirs, files in os.walk(source_dir):
            for i in files:
                    file_names.append(os.path.join(dirpath, i))

        # Find index files and move + rename
        count = 1
        for i in file_names:
            if 'index' in i:
                shutil.move(os.path.join(i), f"{target_dir}/page{count}.html")
                count += 1
            else:
                os.remove(i)

        # Recursive directory removal
        try:
            for dirpath, subdirs, files in os.walk(source_dir):
                for i in subdirs:
                    os.rmdir(os.path.join(source_dir, i))
        except:
            pass