file = open("new_prismDb.psql","r")
file_to_str = file.read()
splitlines_list = file_to_str.splitlines()

new_line_list = []

# import pdb;pdb.set_trace()

for line_no, line in enumerate(splitlines_list, start=1):
    if line.startswith("SELECT setval("):
        line2 = line.replace(',', ', (SELECT ')
        right_br_index = line2.rfind(')')
        line3 = line2[:right_br_index] + line2[right_br_index+1:]
        line4 = line3.replace(';', '));')
        
        # ask = input("line no:{},\nLine: {}\nConverted: {}".format(line_no, line, line4))
        # if ask.lower() == 'y':
        #     line_final = line4
        # else:
        #     line_final = line

        line_final = line4
        new_line_list.append(line_final)
    else:
        new_line_list.append(line)

with open('new_db.psql', 'w') as new_fp:
    sss = '\n'.join(new_line_list)
    new_fp.write(sss)
