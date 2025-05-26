from settings import Settings as st
from parser import Parser as pr

parser_instance = pr()
settings_instance = st()


class Compiler:
    def __init__(self):
        pass

    def createFolders(self):
        print("--Creating folders and adding notes to output file...")
        #get the number of channels from the user
        num_channels = settings_instance.askNumOfChannels()
        try:
            with open("io/output.txt", "a") as file:
                file.write('\nfolder "SongData" {\ntable {\n')
                for i in range(1, num_channels + 1):
                    file.write(parser_instance.takeNotes(i))
                    file.write(' @{\ncolor:"#000000",\nhidden: true,\n}\n\n')
                file.write("}\n} @{ collapsed: true }\n\n")
                file.write('folder "Channels" {\n\n')
                for i in range(1, num_channels + 1):
                    file.write(settings_instance.askInstrument(i))
                file.write('\n} @{ collapsed: true }\n')
        except FileNotFoundError:
            return None

    def addHardcodedVals(self):
        print("--Adding hardcoded values to output file...")
        #add predefined note values to the io/output.txt file
        try:
            with open("io/output.txt", "a") as file:
                #settings and time slider
                file.write('settings @{\nrandomSeed: "",\nviewport: @{ xmin: -10, xmax: 10, ymin: -6.5625, ymax: 6.5625 },\n}\n\n"Converted to Desmos by Antiblue\'s Furnace to Desmos Converter...  V2!!!"\n\nt = 1 @{ slider: @{ loopMode: "LOOP_FORWARD", period: 40000, min: 1, max: 256, step: 1/256, },}\n\n')
                #note frequency data
                file.write('\nfolder "Notes" {\n\nB_0 = 30.87 @{ color: "#388c46" }\n\nC_1 = 32.7 @{ color: "#6042a6" }\n\nC_s1 = 34.65 @{ color: "#000000" }\n\nD_1 = 36.71 @{ color: "#c74440" }\n\nD_s1 = 38.89 @{ color: "#2d70b3" }\n\nE_1 = 41.2 @{ color: "#388c46" }\n\nF_1 = 43.65 @{ color: "#6042a6" }\n\nF_s1 = 46.25 @{ color: "#000000" }\n\nG_1 = 49 @{ color: "#c74440" }\n\nG_s1 = 51.91 @{ color: "#2d70b3" }\n\nA_1 = 55 @{ color: "#388c46" }\n\nA_s1 = 58.27 @{ color: "#6042a6" }\n\nB_1 = 61.74 @{ color: "#000000" }\n\nC_2 = 65.41 @{ color: "#2d70b3" }\n\nC_s2 = 69.3 @{ color: "#388c46" }\n\nD_2 = 73.42 @{ color: "#6042a6" }\n\nD_s2 = 77.78 @{ color: "#000000" }\n\nE_2 = 82.41 @{ color: "#c74440" }\n\nF_2 = 87.31 @{ color: "#2d70b3" }\n\nF_s2 = 92.5 @{ color: "#388c46" }\n\nG_2 = 98 @{ color: "#6042a6" }\n\nG_s2 = 103.83 @{ color: "#000000" }\n\nA_2 = 110 @{ color: "#c74440" }\n\nA_s2 = 116.54 @{ color: "#2d70b3" }\n\nB_2 = 123.47 @{ color: "#388c46" }\n\nC_3 = 130.81 @{ color: "#6042a6" }\n\nC_s3 = 138.59 @{ color: "#000000" }\n\nD_3 = 146.83 @{ color: "#c74440" }\n\nD_s3 = 155.56 @{ color: "#2d70b3" }\n\nE_3 = 164.81 @{ color: "#388c46" }\n\nF_3 = 174.61 @{ color: "#6042a6" }\n\nF_s3 = 185 @{ color: "#000000" }\n\nG_3 = 196 @{ color: "#c74440" }\n\nG_s3 = 207.65 @{ color: "#2d70b3" }\n\nA_3 = 220 @{ color: "#388c46" }\n\nA_s3 = 233.08 @{ color: "#6042a6" }\n\nB_3 = 246.94 @{ color: "#000000" }\n\nC_4 = 261.63 @{ color: "#c74440" }\n\nC_s4 = 277.18 @{ color: "#2d70b3" }\n\nD_4 = 293.66 @{ color: "#388c46" }\n\nD_s4 = 311.13 @{ color: "#6042a6" }\n\nE_4 = 329.63 @{ color: "#000000" }\n\nF_4 = 349.23 @{ color: "#c74440" }\n\nF_s4 = 369.99 @{ color: "#2d70b3" }\n\nG_4 = 392 @{ color: "#388c46" }\n\nG_s4 = 415.3 @{ color: "#6042a6" }\n\nA_4 = 440 @{ color: "#000000" }\n\nA_s4 = 466.16 @{ color: "#c74440" }\n\nB_4 = 493.88 @{ color: "#2d70b3" }\n\nC_5 = 523.25 @{ color: "#000000" }\n\nC_s5 = 554.37 @{ color: "#c74440" }\n\nD_5 = 587.33 @{ color: "#2d70b3" }\n\nD_s5 = 622.25 @{ color: "#388c46" }\n\nE_5 = 659.26 @{ color: "#6042a6" }\n\nF_5 = 698.46 @{ color: "#000000" }\n\nF_s5 = 739.99 @{ color: "#c74440" }\n\nG_5 = 783.99 @{ color: "#2d70b3" }\n\nG_s5 = 830.61 @{ color: "#388c46" }\n\nA_5 = 880 @{ color: "#6042a6" }\n\nA_s5 = 932.33 @{ color: "#000000" }\n\nB_5 = 987.77 @{ color: "#c74440" } } @{ collapsed: true }\n')
        except FileNotFoundError:
            return None