class Settings:
    def __init__(self):
        pass
    def askNumOfChannels(self):
        #ask the user for the number of channels (1-4).
        while True:
            try:
                num_channels = int(input("Enter the number of channels (1-4): "))
                if 1 <= num_channels <= 4:
                    return num_channels
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
    def askNumOfOrders(self):
        #ask the user for the number of orders (1-4).
        while True:
            try:
                num_orders = int(input("Enter the number of orders (1-64): "))
                if 1 <= num_orders <= 64:
                    return num_orders
                else:
                    print("Please enter a number between 1 and 64.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 64.")
    def askInstrument(self, channel):
        '''
        First, it asks you what instrument you want on channel 1. The options are sine and organ (each with optional release).
        It then sets up the channel. Channels typically have a C_h#mix variable, used for mixing the sine waves produced by the tone(freq, vol) function in Desmos. 
        So, a simple sine wave is: C_h#mix = [C_h#[t]].
        Then, to produce the actual sound, another variable, C_hannel# is used.
        Following the example: C_hannel1 = tone(C_h1mix).
        For adding release, its tone function uses mod(-t, 1) for the volume. For example, an instrument wave with release in channel 1: C_hannel1 = tone(C_h1mix, mod(-t, 1))
        The organ instrument uses C_h#mix = [C_h#[t], C_h#[t] * 2, C_h#[t] * 4, C_h#[t] * 6] for its equation.
        This process repeats for the other number of channels.
        It returns something like:
        C_h#mix = EQUATION\nC_hannel# = tone(C_h#mix, mod(-t, 1)) if release is true, or C_hannel# = tone(C_h#mix) if release is false.
        '''
        while True:
            instrument = input(f"Enter the instrument for channel {channel} (sine, organ): ").strip().lower()
            if instrument in ["sine", "organ"]:
                release = input("Do you want release? (yes/no): ").strip().lower()
                if release in ["yes", "y"]:
                    release = True
                elif release in ["no", "n"]:
                    release = False
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    continue
                
                if instrument == "sine":
                    return f'C_h{channel}mix = [C_h{channel}[t]]\n\nC_hannel{channel} = tone(C_h{channel}mix, mod(-t, 1))\n\n' if release else f'C_h{channel}mix = [C_h{channel}[t]]\n\nC_hannel{channel} = tone(C_h{channel}mix)\n\n'
                elif instrument == "organ":
                    return f'C_h{channel}mix = [C_h{channel}[t], C_h{channel}[t] * 2, C_h{channel}[t] * 4, C_h{channel}[t] * 6]\n\nC_hannel{channel} = tone(C_h{channel}mix, mod(-t, 1))\n\n' if release else f'C_h{channel}mix = [C_h{channel}[t], C_h{channel}[t] * 2, C_h{channel}[t] * 4, C_h{channel}[t] * 6]\n\nC_hannel{channel} = tone(C_h{channel}mix)\n\n'
            else:
                print("Invalid instrument. Please enter 'sine' or 'organ'.")
        #TODO: Make easier to add more instruments. (And add more instruments in general)