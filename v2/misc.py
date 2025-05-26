import os

class Misc:
    def __init__(self):
        pass
    def cleanup(self, postOutput):
        #delete the temporary files (MDremoved.txt, previous io/output.txt).
        print("--Cleaning up temporary files...")
        try:
            os.remove("MDremoved.txt")
            if not postOutput:
                print("--Resetting output file...")
                os.remove("io/output.txt")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"An error occurred: {e}")

    