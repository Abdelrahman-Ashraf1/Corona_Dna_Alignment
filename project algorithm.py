files = ["case_consq_edited.txt", "ref_consq_edited.txt"]
with open(files[0], 'r') as f:
    case_cons = f.read()
with open(files[1], 'r') as f:
     ref_cons= f.read()
print(len(ref_cons),len(case_cons))
mismatch_array = []
for index in range(len(ref_cons)):
    if ref_cons[index] != case_cons[index] :
        print(f"At Column {index + 1} , There is a mismatch")
        mismatch_array.append(index+1)
print(f"Number of Mismatches: {len(mismatch_array)}")
