from difflib import SequenceMatcher

with open('file1.txt') as first_file , open('file2.txt') as second_file:

    data_file1=first_file.read()

    data_file2=second_file.read()

    Match_Plagarism=SequenceMatcher(None,data_file1,data_file2).ratio()

    print(f"The plagiarized data is {Match_Plagarism*100}%")


    