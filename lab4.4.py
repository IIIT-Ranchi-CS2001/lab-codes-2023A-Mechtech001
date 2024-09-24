singers_list = list(str(input("Enter the name of singers (separated by spaces): ")).split())
dancers_list = list(str(input("Enter the name of dancers (separated by spaces): ")).split())

singers = {singer for singer in singers_list}
dancers = {dancer for dancer in dancers_list}

all_artists = singers | dancers 
allrounders = singers & dancers
dancers_not_singers = dancers - singers
singers_not_dancers = singers - dancers
symmetric_diff = singers ^ dancers

print("\nAll artists:", all_artists)
print("\nAll rounders:", allrounders)
print("\nDancers but not singers:", dancers_not_singers)
print("\nSingers but not dancers:", singers_not_dancers)
print("\nDancers but not singers cum Singers but not dancers:", symmetric_diff)