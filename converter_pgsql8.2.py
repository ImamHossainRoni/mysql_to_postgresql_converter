file = open("myfile.psql","r")
file_to_str = file.read()
splitlines_list = file_to_str.splitlines()

new_line_list = []

for line_no, line in enumerate(splitlines_list, start=1):
    if line.startswith("CREATE INDEX ON"):
        left_br_index = line.rfind('" (')
        end_br = line.rfind('");')
        start_br = line.rfind('("')
        get_id = line[start_br:end_br+2]
        index_on_index = line.rfind('CREATE INDEX ON')
        query_started = 'CREATE INDEX '
        table_name = line[17 :left_br_index]
        index_name = table_name + '_index' 
        final_query = query_started + '"'+index_name + '"' +' '+ 'ON'+' ' +'"'+ table_name +'"' +' '+get_id
        new_line_list.append(final_query)
        
# print(get_id)
# print(final_query)
with open('roni_db.psql', 'w') as new_fp:
    sss = '\n'.join(new_line_list)
    new_fp.write(sss)
