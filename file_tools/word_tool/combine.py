
from docx import Document
from docxcompose.composer import Composer


def combine(save_paths, target):
    composer = Composer(Document())
    for i in range(0, len(save_paths)):
        composer.append(Document(save_paths[i]))
    print("合并结束.....开始保存，保存路径: %s" % target)
    composer.save(target)


if __name__ == "__main__":
    save_paths = [
        "/home/ginger/Projects/Learning/P_Stack/file_tools/word_tool/20200416134916/机器预填【部分】.docx",
        "/home/ginger/Projects/Learning/P_Stack/file_tools/word_tool/20200416134916/公司股份结构.docx",
    ]
    combine(save_paths, target="./combined.docx")
