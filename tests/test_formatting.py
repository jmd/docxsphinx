import pytest
from docxsphinx.testing.util import check_parsed_docx


simple_formatting_result = '''
Some <italic>italic text</italic>, some <bold>bold text</bold> and some <pre>literal</pre> and back to normal.'''

@pytest.mark.sphinx('docx', testroot='simple-formatting')
def test_simple_formatting(app):
    app.builder.build_all()
    check_parsed_docx(app.outdir / 'simple-formatting-1.0.docx', simple_formatting_result)
