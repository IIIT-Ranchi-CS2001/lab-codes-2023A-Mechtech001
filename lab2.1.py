# String Manipulation 1st Question (Mera Bharat)
S1 = "Maha Bharat"

s1_case_swapped = S1[0].lower() + S1[1:5].upper() + ' ' + S1[5].lower() + S1[6:].upper()

s1_bharat = S1.split()[1]

s1_bharat_repeated = s1_bharat * 3

s1_mera_bharat = "Mera " + S1[len("Maha "):]

s1_mera_bharat_mahan = s1_mera_bharat + " Mahan"

# Output
print(s1_case_swapped)
print(s1_bharat)
print(s1_bharat_repeated)
print(s1_mera_bharat)
print(s1_mera_bharat_mahan)