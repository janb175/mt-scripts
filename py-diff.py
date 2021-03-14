#############################
## py-diff
## 
## Line by line visual comparison script
## Store results in HTML pretty diff
## Using Google Diff_match_patch library
##
## USAGE
##
## py-diff.py <file_old_version> <file_new_version> [compare.html]
##
## writes compare html as output into same directory
##
########################################


import diff_match_patch
import sys, os


html_start = """
<html><body><table border=0>
     <tr>
       <th>Source</th>
       <th>Target</th>
       <th>Diff</th>

     </tr>"""
html_end = """     
</table></body></html>
"""

#open TXT files provided as parameters
try:
    in_file1 =  open(sys.argv[1], 'r')
except IOError:
    print("Could not open ", sys.argv[1], "\nExiting ...")
    sys.exit(1)

try:
    in_file2 =  open(sys.argv[2], 'r')
except IOError:
    print("Could not open ",sys.argv[2], "\nExiting ...")
    sys.exit(1)

print("Starting to compare files: ",sys.argv[1],sys.argv[2])
#open HTML file for copmaring, write starting part of HTML file 
htmlFile =  open('compare.html', 'w')
htmlFile.write(html_start)


#read first string pair 
try:
    string1 = in_file1.readline()
except IOError:
    print("Could not read ",string1)
    sys.exit(1)

try:
    string2 = in_file2.readline()
except IOError:
    print("Could not read ",string2)
    sys.exit(1)

while string1:
    diff_obj = diff_match_patch.diff_match_patch()
    diffs = diff_obj.diff_main(string1, string2)
    diff_obj.diff_cleanupSemantic(diffs)
    html_diff = diff_obj.diff_prettyHtml(diffs)
    htmlFile.write("<tr><td>"+string1+"</td><td>"+string2+"</td><td>"+html_diff+"</td><td>")
    string1 = in_file1.readline()
    string2 = in_file2.readline()

htmlFile.write(html_end)


htmlFile.close()
in_file1.close()
in_file2.close()

print ("Compare done. ")

