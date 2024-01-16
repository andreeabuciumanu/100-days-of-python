import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:

for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")

new_nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}


# print(new_nato_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_text = input("Please insert a name: ").upper()
    try:
        phonetic_list = [new_nato_dict[letter] for letter in user_text]
    except KeyError:
        print("Sorry, only letter in the alphabet, please!")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()
