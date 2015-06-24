import glob  
import shutil 
import xlwt
import xlrd

base_dir = "/Users/kareemwahid/Documents/statistics/" #insert correct directories here, move files from base to dest
dest_dir = "/Users/kareemwahid/Desktop/output_1/"

workbook = xlrd.open_workbook('pfam_tm_no_structure_set.xlsx') #insert correct spreadsheet here
sheet = workbook.sheet_by_index(0)

protein_id_list = [sheet.cell_value(row, 3) for row in range(2,sheet.nrows)] # skips first 2 rows and targets 4th column

for protein_id in protein_id_list:
    if entry == '': #ignores any blank excel cells in column
        continue 
    else:
        print "Uniprot ID to process: {}".format(protein_id)
        pattern_ = base_dir+"*"+str(protein_id)+"*"
        print pattern_
        files = glob.glob(pattern_) # matches ANY files in statistics folder with protein IDs 
        if files != []:
            for file_ in files:
                print "ID match found"
                print str(file_)
                shutil.copy(file_, dest_dir)
                print "{} copied".format(file_)
        else:
            print "No ID match found"
