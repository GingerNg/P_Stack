

from xmldiff import main
main.diff_texts("./case3.html",
               "./case4.html")

from xmldiff import formatting
formatter = formatting.DiffFormatter()
print(main.diff_files("../tests/test_data/insert-node.left.html",
                       "../tests/test_data/insert-node.right.html",
                       formatter=formatter))