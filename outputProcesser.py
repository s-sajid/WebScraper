import glob

class OutputProcceser():
    def outputProcess(self):
        read_files = glob.glob("output/*.txt")

        with open("output/outputText.txt", "wb") as outfile:
            for f in read_files:
                with open(f, "rb") as infile:
                    outfile.write(infile.read())