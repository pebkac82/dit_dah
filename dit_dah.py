import binascii

# import dits and dahs and split in to array for easy use
morse_code = "dah-dah-dah-dah-dah dah-di-di-dah di-di-di-di-dit dah-dah-di-di-dit dah-dah-di-di-dit " \
             "dah-dah-dah-dah-dah di-di-dah-dah-dah di-dah dah-di-di-di-dit dah-di-dah-dit di-di-di-di-dit " \
             "dah-dah-dah-di-dit dah-dah-di-di-dit di-di-di-di-dah di-di-di-di-dah dah-dah-di-di-dit di-di-di-di-dit " \
             "di-dah-dah-dah-dah di-di-di-dah-dah dah-dah-dah-di-dit dah-di-di-di-dit di-di-di-di-dit " \
             "di-di-di-dah-dah dah-dah-dah-di-dit dah-dah-di-di-dit di-dah-dah-dah-dah dah-di-di-di-dit dit " \
             "dah-di-di-di-dit dah-di-dit di-di-di-di-dah dah-di-dit di-di-di-di-dit dah-dah-dah-dah-dit " \
             "di-di-di-di-dit di-di-di-di-dit di-di-dah-dah-dah di-dah dah-dah-di-di-dit di-di-di-dah-dah " \
             "dah-dah-di-di-dit dah-di-di-di-dit di-di-di-di-dah dah-di-di-di-dit di-di-di-di-dah dah-dah-dah-di-dit " \
             "dah-di-di-di-dit dah-di-di-dit dah-di-di-di-dit di-dah di-di-di-di-dah dah-dah-dah-dah-dit " \
             "dah-dah-di-di-dit di-di-di-di-dah di-di-dah-dah-dah di-dah di-di-di-di-dit di-di-dah-dah-dah " \
             "di-di-di-di-dit di-dah-dah-dah-dah di-di-dah-dah-dah dah-di-di-di-dit di-di-di-di-dah di-dah " \
             "dah-dah-di-di-dit dah-dah-dah-dah-dah di-di-di-di-dit di-dah dah-dah-di-di-dit dah-di-di-di-dit " \
             "dah-di-di-di-dit di-dah dah-di-di-di-dit dah-di-dit di-di-dah-dah-dah di-dah-dah-dah-dah " \
             "di-di-dah-dah-dah di-di-di-di-dit di-di-dah-dah-dah di-di-di-di-dit di-di-di-di-dah dah-di-di-dit " \
             "di-di-di-di-dah di-di-di-di-dah dah-di-di-di-dit dah-di-di-dit dah-di-di-di-dit dah-di-di-di-dit " \
             "dah-dah-di-di-dit dah-dah-dah-dah-dah di-di-dah-dah-dah di-di-di-dah-dah di-di-di-di-dit dit " \
             "di-di-di-di-dah dit di-di-di-dah-dah dah-dah-dah-dah-dit dah-di-di-di-dit dah-di-di-di-dit " \
             "dah-di-di-di-dit dah-di-di-dit di-di-di-dah-dah di-di-di-di-dah dah-di-di-di-dit di-di-di-di-dah " \
             "di-di-di-di-dit di-di-di-di-dit di-di-di-dah-dah di-di-di-di-dah dah-di-di-di-dit dah-di-dah-dit " \
             "di-di-di-di-dah di-di-dah-dah-dah di-di-di-dah-dah di-di-di-dah-dah dah-dah-di-di-dit di-di-dah-dah-dah " \
             "di-di-di-di-dit di-di-di-di-dah dah-di-di-di-dit di-di-dah-dit di-di-di-di-dit di-di-di-di-dah " \
             "di-di-di-dah-dah dah-dah-dah-dah-dah di-di-di-di-dit dah-dah-dah-dah-dah di-di-di-di-dit di-dah " \
             "di-di-di-di-dit di-dah-dah-dah-dah dah-di-di-di-dit dah-di-dit di-di-di-di-dah di-di-di-dah-dah " \
             "di-di-di-di-dit di-dah-dah-dah-dah di-di-di-di-dah di-di-di-di-dit di-di-di-di-dah dah-di-di-dit " \
             "di-di-di-di-dit dah-dah-dah-dah-dit di-di-di-di-dah di-di-dah-dah-dah di-di-di-dah-dah di-di-di-di-dah " \
             "di-di-di-di-dit di-dah di-di-di-di-dah dah-di-dit dah-dah-di-di-dit dah-di-di-di-dit di-di-dah-dah-dah " \
             "di-dah di-di-dah-dah-dah di-dah-dah-dah-dah di-di-di-di-dah dah-di-di-di-dit dah-di-di-di-dit " \
             "dah-di-di-dit di-di-di-dah-dah dah-dah-dah-di-dit dah-di-di-di-dit dah-di-dah-dit di-di-dah-dah-dah " \
             "di-di-di-di-dit dah-di-di-di-dit di-di-dah-dah-dah dah-di-di-di-dit di-dah dah-dah-di-di-dit " \
             "di-dah-dah-dah-dah dah-di-di-di-dit dah-di-dah-dit di-di-di-di-dit dah-dah-dah-dah-dah di-di-di-di-dah " \
             "dah-di-dit dah-di-di-di-dit dah-di-di-di-dit di-di-di-di-dah dah-dah-dah-dah-dit di-di-di-di-dah " \
             "dah-dah-di-di-dit dah-di-di-di-dit dah-di-dit dah-di-di-di-dit di-dah-dah-dah-dah di-di-dah-dah-dah " \
             "di-di-di-di-dit di-di-dah-dah-dah di-di-di-di-dit di-di-di-di-dah dah-di-di-di-dit dah-dah-di-di-dit " \
             "di-dah di-di-di-di-dah dah-dah-di-di-dit di-di-dah-dah-dah dah-dah-dah-dah-dah dah-di-di-di-dit " \
             "dah-dah-di-di-dit dah-di-di-di-dit dah-dah-dah-dah-dit dah-di-di-di-dit dah-dah-di-di-dit " \
             "dah-di-di-di-dit di-di-di-di-dit dah-di-di-di-dit dah-di-dit dah-dah-di-di-dit dah-di-di-dit " \
             "di-di-di-di-dah di-di-di-dah-dah di-di-di-dah-dah di-dah-dah-dah-dah dah-di-di-di-dit " \
             "dah-dah-dah-dah-dit dah-di-di-di-dit di-di-di-dah-dah di-di-di-di-dah dah-di-di-dit di-di-di-di-dit " \
             "di-di-dah-dit dah-di-di-di-dit di-di-di-dah-dah dah-di-di-di-dit dah-di-dah-dit di-di-di-dah-dah " \
             "di-dah-dah-dah-dah di-di-di-di-dah di-di-di-dah-dah di-di-di-di-dah dah-di-di-dit di-di-dah-dah-dah " \
             "dah-di-dit dah-dah-di-di-dit dah-dah-dah-dah-dit di-di-di-dah-dah dah-dah-dah-dah-dah dah-dah-di-di-dit " \
             "di-di-di-di-dit di-di-di-di-dit di-di-dah-dit dah-di-di-di-dit dah-dah-dah-di-dit di-di-di-dah-dah " \
             "di-di-di-di-dah dah-dah-di-di-dit dah-di-di-di-dit di-di-di-dah-dah di-di-di-dah-dah di-di-di-di-dit " \
             "di-di-dah-dit dah-di-di-di-dit dah-di-dit di-di-di-dah-dah di-di-di-di-dah di-di-di-di-dah " \
             "dah-dah-dah-dah-dit di-di-di-dah-dah di-dah-dah-dah-dah dah-dah-di-di-dit dah-di-dit di-di-dah-dah-dah " \
             "dah-dah-dah-dah-dah dah-dah-di-di-dit di-di-di-di-dit dah-dah-di-di-dit dah-di-di-di-dit " \
             "di-di-di-dah-dah di-di-di-di-dah dah-dah-di-di-dit dah-di-di-di-dit dah-dah-di-di-dit di-dah " \
             "di-di-di-di-dah dah-di-di-dit di-di-di-di-dit di-dah dah-dah-di-di-dit di-di-di-di-dah di-di-di-dah-dah " \
             "di-di-di-di-dah dah-dah-di-di-dit dah-dah-dah-dah-dit dah-di-di-di-dit di-di-dah-dit dah-di-di-di-dit " \
             "dah-di-dit dah-di-di-di-dit dah-dah-dah-dah-dit di-di-di-di-dah di-di-di-di-dah di-di-di-di-dit " \
             "di-di-di-dah-dah dah-di-di-di-dit dah-dah-dah-di-dit di-di-di-di-dah dah-di-dah-dit dah-di-di-di-dit " \
             "dah-di-dit di-di-di-dah-dah dah-dah-dah-di-dit di-di-di-di-dit di-dah-dah-dah-dah di-di-di-di-dah " \
             "di-di-di-di-dit di-di-di-di-dah dah-di-di-di-dit dah-di-di-di-dit dit di-di-di-di-dit di-di-di-di-dit " \
             "dah-dah-di-di-dit di-di-di-di-dah dah-dah-di-di-dit dah-dah-di-di-dit di-di-di-di-dah di-dah " \
             "di-di-di-di-dah dah-dah-dah-dah-dah di-di-di-di-dah dit dah-dah-di-di-dit di-di-di-di-dit " \
             "di-di-di-di-dah di-di-dah-dit di-di-di-di-dit dah-dah-dah-dah-dit dah-di-di-di-dit dah-di-di-di-dit " \
             "di-di-di-di-dit dah-dah-dah-di-dit di-di-dah-dah-dah dah-di-di-di-dit di-di-di-dah-dah " \
             "dah-dah-dah-di-dit dah-dah-di-di-dit di-di-di-di-dit di-di-di-di-dah dah-dah-dah-dah-dah " \
             "di-di-di-di-dah dah-dah-di-di-dit dah-di-di-di-dit dit di-di-dah-dah-dah di-dah-dah-dah-dah " \
             "di-di-di-dah-dah di-dah-dah-dah-dah di-di-dah-dah-dah di-di-di-di-dit di-di-di-di-dit di-di-di-di-dah " \
             "dah-dah-di-di-dit di-dah-dah-dah-dah dah-dah-di-di-dit dah-di-di-di-dit di-di-di-dah-dah " \
             "dah-dah-dah-dah-dah di-di-di-di-dit dah-di-di-di-dit dah-di-di-di-dit di-di-di-dah-dah di-di-di-di-dit " \
             "di-di-dah-dah-dah dah-dah-di-di-dit di-dah di-di-di-di-dit dah-di-di-di-dit di-di-dah-dah-dah " \
             "di-dah-dah-dah-dah dah-di-di-di-dit di-dah di-di-dah-dah-dah di-dah-dah-dah-dah dah-dah-di-di-dit " \
             "dah-di-di-di-dit dah-dah-di-di-dit di-di-di-di-dit dah-dah-di-di-dit di-di-di-di-dit dah-dah-di-di-dit " \
             "dah-dah-dah-dah-dah di-di-di-dah-dah dah-dah-dah-di-dit di-di-di-di-dah di-di-dah-dah-dah " \
             "dah-di-di-di-dit di-dah dah-di-di-di-dit di-di-di-di-dah di-di-di-di-dah dit di-di-di-di-dah " \
             "dah-dah-dah-dah-dit dah-dah-di-di-dit di-dah-dah-dah-dah di-di-di-di-dah di-di-di-di-dit " \
             "di-di-di-dah-dah di-di-di-di-dit dah-dah-di-di-dit dah-dah-di-di-dit di-di-dah-dah-dah di-di-di-dah-dah " \
             "di-di-dah-dah-dah di-di-di-di-dah di-di-dah-dah-dah di-di-di-di-dit di-di-di-di-dit dah-di-di-di-dit " \
             "di-di-di-dah-dah di-di-di-di-dah di-di-di-di-dit di-di-di-di-dit di-di-di-di-dit di-dah di-di-di-di-dah " \
             "di-di-dah-dit di-di-di-di-dit dah-dah-dah-dah-dit di-di-di-di-dit di-dah di-di-di-dah-dah " \
             "di-di-dah-dah-dah dah-dah-di-di-dit di-dah di-di-di-dah-dah dah-dah-di-di-dit di-di-di-di-dit " \
             "di-di-di-di-dah di-di-di-dah-dah di-di-dah-dah-dah di-di-di-dah-dah di-di-di-di-dit dah-dah-di-di-dit " \
             "di-di-di-di-dah di-di-di-dah-dah dah-dah-di-di-dit di-di-dah-dah-dah dah-di-di-di-dit dah-dah-di-di-dit " \
             "dah-dah-dah-di-dit di-di-di-di-dah dah-di-dah-dit di-di-di-di-dah dah-dah-dah-dah-dah di-di-di-di-dit " \
             "dah-dah-di-di-dit di-di-di-di-dah di-di-dah-dit di-di-di-dah-dah dah-dah-di-di-dit di-di-di-dah-dah " \
             "di-di-di-di-dah di-di-di-dah-dah di-dah-dah-dah-dah di-di-di-dah-dah dah-dah-dah-dah-dah " \
             "di-di-di-di-dit di-dah-dah-dah-dah di-di-di-di-dah dah-dah-dah-dah-dit "
split_morse_code = morse_code.split()

# create morse alphabet dictionary
dits_dahs = {
    "di-dah": "A",
    "dah-di-di-dit": "B",
    "dah-di-dah-dit": "C",
    "dah-di-dit": "D",
    "dit": "E",
    "di-di-dah-dit": "F",
    "dah-dah-dit": "G",
    "di-di-di-dit": "H",
    "di-dit": "I",
    "di-dah-dah-dah": "J",
    "dah-di-dah": "K",
    "di-dah-di-dit": "L",
    "dah-dah": "M",
    "dah-dit": "N",
    "dah-dah-dah": "O",
    "di-dah-dah-dit": "P",
    "dah-dah-di-dah": "Q",
    "di-dah-dit": "R",
    "di-di-dit": "S",
    "dah": "T",
    "di-di-dah": "U",
    "di-di-di-dah": "V",
    "di-dah-dah": "W",
    "dah-di-di-dah": "X",
    "dah-di-dah-dah": "Y",
    "dah-dah-di-dit": "Z",
    "dah-dah-dah-dah-dah": "0",
    "di-dah-dah-dah-dah": "1",
    "di-di-dah-dah-dah": "2",
    "di-di-di-dah-dah": "3",
    "di-di-di-di-dah": "4",
    "di-di-di-di-dit": "5",
    "dah-di-di-di-dit": "6",
    "dah-dah-di-di-dit": "7",
    "dah-dah-dah-di-dit": "8",
    "dah-dah-dah-dah-dit": "9"
}

# decode morse => append hex-string to variable 
output_values = []
for dd in split_morse_code:
    if dd in dits_dahs:
        output_values.append(dits_dahs[dd])
    else:
        print("TableFlip")

# make string => hex-decode => strip away useless zero x 
# split in array => print position of flag in array for nice clean output otherwise check all output
string_value = ''.join(map(str, output_values))[2:]
string_decoded = (binascii.unhexlify(string_value.strip())).split()
print(string_decoded[1])
