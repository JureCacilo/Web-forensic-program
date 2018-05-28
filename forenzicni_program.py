print("Welcome to our CSI forensic program.")
print("Our CSI lab succesfully extracted the DNA of the criminal.\n"
      " Its now our job to crack up the DNA code and find the criminal!.\n")


#dna_code = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
criminal = {} # a dictionary for the criminal characteristics


# Human characteristics
hair_color = {
    "black":"CCAGCAATCGC",
    "brown": "GCCAGTGCCG",
    "blonde": "TTAGCTATCGC"

}

facial_shape = {
    "square": "GCCACGG",
    "round": "ACCACAA",
    "oval": "AGGCCTCA"
}

eye_color = {
    "blue": "TTGTGGTGGC",
    "green": "GGGAGGTGGC",
    "brown": "AAGTAGTGAC"
}

gender = {
    "female": " TGAAGGACCTTC",
    "male": "TGCAGGAACTTC",
}

race = {
    "white": "AAAACCTCA",
    "black": "CGACTACAG",
    "asian": "CGCGGGCCG"
}

# finding criminal characteristics

def crim_characteristics(char_dict, attribute, dna_code):

    for char in char_dict:
        if char_dict[char] in dna_code:
            return char


# find the criminal hair color



# find the criminal facial shape
#crim_characteristics(facial_shape, "face shape")

# find the criminal eye color
#crim_characteristics(eye_color, "eye color")

# find the criminal gender
#crim_characteristics(gender, "gender")

# find the criminal race
#crim_characteristics(race, "race")


#describing the suspects

eva_char = {
    "gender": "female",
    "race": "white",
    "hair color": "blonde",
    "eye color": "blue",
    "face shape": "oval"
}
larisa_char = {
    "gender": "female",
    "race": "white",
    "hair color": "brown",
    "eye color": "brown",
    "face shape": "oval"
}

matej_char = {
    "gender": "male",
    "race": "white",
    "hair color": "black",
    "eye color": "blue",
    "face shape": "oval"
}

miha_char = {
    "gender": "male",
    "race": "white",
    "hair color": "brown",
    "eye color": "green",
    "face shape": "square"
}

suspects = {
    "Eva": eva_char,
    "Larisa": larisa_char,
    "Matej": matej_char,
    "Miha": miha_char

}


