class Parser:
    def __init__(self):
        pass
    def removeMetadata(self):
        #delete all lines until the one after that contains "----- ORDER 00".
        print("--Removing metadata...")
        try:
            with open("io/input.txt", "rt") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if "----- ORDER 00" in line:
                        break
                lines = lines[i+1:]
            with open("MDremoved.txt", "w") as file:
                file.writelines(lines)
        except FileNotFoundError:
            return None
    def takeNotes(self, channel):
        print(f"--Extracting notes from channel {channel}...")
        try:
            with open("MDremoved.txt", "rt") as file:
                lines = file.readlines()
                processed_lines = []
                previous_note = None
                
                for line in lines:
                    # Skip order lines
                    if "----- ORDER" in line:
                        continue
                    
                    # Extract note based on channel
                    if channel == 1:
                        current_note = line[4:7].strip()
                    elif channel == 2:
                        current_note = line[19:22].strip()
                    elif channel == 3:
                        current_note = line[34:37].strip()
                    elif channel == 4:
                        current_note = line[49:52].strip()
                    else:
                        processed_lines.append("ERR")
                        continue
                    
                    # Handle ... by replacing with previous note
                    if current_note == "...":
                        if previous_note:
                            current_note = previous_note
                    else:
                        previous_note = current_note
                    
                    # Format note and add to processed lines
                    formatted_note = current_note.replace("-", "_").replace("#", "_s")
                    if formatted_note == "OFF":
                        formatted_note = "0"
                    processed_lines.append(formatted_note)
                
                # Create return string
                result = f"C_h{channel} = ["
                result += ", ".join(processed_lines)
                result += "]"
                return result.replace("...", "0") #final countermeasure for the dreaded ellipsis
                
        except FileNotFoundError:
            return None