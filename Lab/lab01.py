"""
    Lab 1
    Updated by: Jeron Kuxhausen
    Date: Jan 19th, 2016
    CSCI 110
    This program produces an ascii graphic as an output.
"""
print "Printed with no formatting"

print("  |\_/|   ******************  (\_/)   ")
print(" / @ @ \  *      Lab1      * (='.'=) ")
print("( > 0 < ) *  By: Jeron K.  * (\")_(\")")
print("  >>x<<   *    CSCI 110    * ")
print(" /  0  \  ******************")

print ""
print ("Printed with formatting")

print "{: <2} {:<8} {:*^20} {:<2} {:<8}".format("", "|\_/|", "", "", "(\_/)")
print "{: <1} {:<9} {:^1} {:^16} {:^1} {:<1} {:<9}".format("", "/ @ @ \\", "*", "      Lab1      ", "*", "", "(='.'=)")
print "{: <0} {:<10} {:^1} {:^16} {:^1} {:<1} {:<9}".format("", "( > 0 < )", "*", "  By: Jeron K.  ", "*", "", "(\")_(\")")
print "{: <2} {:<8} {:^1} {:^16} {:^1} {:<2} {:<8}".format("", ">>x<<", "*", "    CSCI 110    ", "*", "", "")
print "{: <1} {:<9} {:*^20} {:<2} {:<8}".format("", "/  0  \\", "", "", "")

print ""
print "More Cats"
print ""
print " _"
print "( \\"
print " ) )"
print "( (  .-\"\"-.  A.-.A"
print " \\ \\/      \\/ , , \\"
print "  \\   \\    =;  t  /"
print "   \\   |\"\".  ',--'"
print "    / //  | ||"
print "   /_,))  |_,))"

print ""
print "      .             *     ,MMM8&&&.            *"
print "                         MMMM88&&&&&    ."
print "                        MMMM88&&&&&&&"
print ".           *           MMM88&&&&&&&&"
print "                        MMM88&&&&&&&&               ."
print "            .           'MMM88&&&&&&'"
print "                          'MMM8&&&'      *"
print ""
print ""
print "          *                                                   "
print "{:<73}".format("                      /^--^\\     /^--^\\     /^--^\\")
print "{:<73}".format("                      \\____/     \\____/     \\____/")
print "{:<73}".format("                     /      \\   /      \\   /      \\")
print "{:<73}".format("                    |        | |        | |        |")
print "{:<73}".format("                     \\__  __/   \\__  __/   \\__  __/")
print "{:<73}".format("|^|^|^|^|^|^|^|^|^|^|^|^\\ \\^|^|^|^/ /^|^|^|^|^\\ \\^|^|^|^|^|^|^|^|^|^|^|^|")
print "{:<73}".format("| | | | | | | | | | | | |\\ \\| | |/ /| | | | | |\\ \\  | | | | | | | | | | |")
print "{:<73}".format("######################## / /#####\\ \\###########/ /#######################")
print "{:<73}".format("| | | | | | | | | | | |  \\/| | | |\\/| | | | | \\/  | | | | | | | | | | | |")
print "{:<73}".format("|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|")