import gender_guesser.detector as gnd
import pandas as pd
# filenames (output written in the same file)
files = ['myfile.xlsx','File2.xlsx']
d = gnd.Detector(case_sensitive=False)

for file in files:
    df = pd.read_excel (file)

    namecol = df['First Name']
    gendercol = [] 
    for name in namecol:
        gender = d.get_gender(name)
        gendercol.append(gender)
    df['Gender'] = gendercol
    with pd.ExcelWriter(file, mode='a') as writer:  
        df.to_excel(writer, sheet_name='output')
