#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/1/19 1:25 AM
# @Author  : lixintang - (xintang.li@fir.ai)
# @Site    :
# @File    : word_extract_catalogues_1.py
import os
import shutil
import time
from copy import deepcopy
from xml.dom.minidom import parse
import xml.dom.minidom
import re

# from handlers.word_handlers import logger
# from tools import zip_utils

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from docx import Document
from docxcompose.utils import xpath
from docx.oxml.section import CT_SectPr
from docxcompose.composer import REFERENCED_PARTS_IGNORED_RELTYPES
from docxcompose.utils import NS
from docx.oxml.text.paragraph import CT_P
from docx.oxml.xmlchemy import BaseOxmlElement


class DocContent(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.doc = Document(file_path)
        self.all_catalogues = []
        self.all_indexes = []
        self.s_doc = Document()

    def extract_catalogues(self):
        i = 0
        for element in self.doc.element.body:
            if isinstance(element, CT_SectPr):
                continue
            bookmarks_start = xpath(element, './/w:bookmarkStart')
            if bookmarks_start:
                catalogue = {
                    "w:name": xpath(bookmarks_start[0], '@w:name'),
                    "element": element,
                    "index": i
                }
                self.all_catalogues.append(catalogue)
            i += 1

        for catalogue in self.all_catalogues:
            print(catalogue)

    def add_element(self, element, index, doc):
        element = deepcopy(element)
        self.doc.element.body.insert(index, element)
        self.add_referenced_parts(doc.part, self.doc.part, element)
        self.add_styles(doc, element)
        self.add_numberings(self.doc, element)
        self.restart_first_numbering(self.doc, element)
        self.add_images(self.doc, element)
        self.add_shapes(self.doc, element)
        self.add_footnotes(self.doc, element)
        self.remove_header_and_footer_references(self.doc, element)
        self.renumber_bookmarks()
        self.renumber_docpr_ids()

    def save(self, filename):
        self.s_doc.save(filename)

    def add_referenced_parts(self, src_part, dst_part, element):
        rid_elements = xpath(element, './/*[@r:id]')
        for rid_element in rid_elements:
            rid = rid_element.get('{%s}id' % NS['r'])
            rel = src_part.rels[rid]
            if rel.reltype in REFERENCED_PARTS_IGNORED_RELTYPES:
                continue
            new_rel = self.add_relationship(src_part, dst_part, rel)
            rid_element.set('{%s}id' % NS['r'], new_rel.rId)


if __name__ == '__main__':

    file_path = '/home/ginger/Projects/Learning/P_Stack/file_tools/word_tool/20200416134916/机器预填【部分】.docx'
    doc_parse = DocContent(file_path=file_path)
    doc_parse.extract_catalogues()
    # modify_document_xml("1-1_科创版招股说明书撰写模板")
