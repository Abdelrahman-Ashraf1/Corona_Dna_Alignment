files = ["ref_consq", "case_consq"]
for file in files:
    # first get all lines from file
    with open(file+".txt", 'r') as f:
        lines = f.readlines()

    # remove spaces
    lines = [line.replace(' ', '') for line in lines]
    lines = [line.replace('\n', '') for line in lines]

    # finally, write lines in the file
    with open(file+"_edited.txt", 'w') as f:
        f.writelines(lines)