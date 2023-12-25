
import os
pdb_path = '1bga.pdb'
helix_data = []
with open(pdb_path, 'r') as f:
    for line in f:
        if line.startswith('HELIX'):
            serial_number = line[7:10].strip()
            helix_id = line[11:14].strip()
            start_residue = line[15:18].strip()
            start_residue_chain = line[19]
            end_residue = line[21:24].strip()
            end_residue_chain = line[25]
            helix_class = line[39:41].strip()
            comment = line[40:70].strip()
            helix_data.append((serial_number, helix_id, start_residue, start_residue_chain, end_residue, end_residue_chain, helix_class, comment))
output_filename = 'helix_data.SS'
with open(output_filename, 'w') as outfile:
     # outfile.write('Serial Number,Helix ID,Start Residue,Start Residue Chain,End Residue,End Residue Chain,Helix Class,Comment\n')
     for record in helix_data:
         outfile.write(f"{record[0]},{record[1]},{record[2]},{record[3]},{record[4]},{record[5]},{record[6]},{record[7]}\n")

