# -*- coding: utf-8 -*-
"""
    docxsphinx.testing.util
    ~~~~~~~~~~~~~~~~~~~~~~~

    Docxsphinx test suite utilities

    :license: BSD, see LICENSE for details.
"""

import os
import re
import pytest
from six import StringIO
from docx import Document
from docxsphinx import styles


re_rid = re.compile('r:embed="([^"]*)"')


class InlineShapeInfo:

    def __init__(self, inline_shape):
        self.id = inline_shape._inline.graphic.graphicData.pic.blipFill.blip.embed
        self.name = inline_shape._inline.graphic.graphicData.pic.nvPicPr.cNvPr.name
        self.width = inline_shape.width.emu
        self.height = inline_shape.height.emu


class DocxParser:

    def __init__(self):
        self.stream = None

    def parse(self, path):
        self.stream = StringIO()
        doc = Document(docx=path)
        for p in doc.paragraphs:
            if p.style.name != 'Normal':
                self.stream.write('<%s>' % p.style.name)
            for r in p.runs:
                font_attr = self.__get_font_attributes(r.font)
                if font_attr:
                    self.stream.write('<%s>' % font_attr)
                if r.text:
                    self.stream.write(r.text)
                else:
                    shape_info = self.__get_referenced_inline_shape_info(r)
                    if shape_info:
                        self.stream.write('<%s>' % shape_info.name)
                if font_attr:
                    self.stream.write('</%s>' % font_attr)
            self.stream.write('\n')
        return self.stream.getvalue()

    def __create_inline_shapes_dict(self, doc):
        self.inline_shapes_dict = {}
        for s in doc.inline_shapes:
            shape_info = InlineShapeInfo(s)
            self.inline_shapes_dict[shape_info.id] = shape_info

    def __get_referenced_inline_shape_info(self, run):
        m = re_rid.search(run.element.xml)
        if m:
            return self.inline_shapes_dict.get(m.group(1))

    def __get_font_attributes(self, font):
        attr = []
        if font.italic:
            attr.append('italic')
        if font.bold:
            attr.append('bold')
        if font.name == styles.literal_font:
            attr.append('pre')
        if attr:
            return '|'.join(attr)


def check_parsed_docx(docxfile, expected):
    """
    Check that the result of parsing docxfile is equal to the string expected.
    """
    docxfile = str(docxfile)
    if not os.path.exists(docxfile):
        pytest.fail('Result file missing "%s"' % docxfile)
    parser = DocxParser()
    res = parser.parse(docxfile)
    expected = expected.strip('\n')
    res = res.strip('\n')
    assert res == expected
