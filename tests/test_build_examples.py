import os
from subprocess import Popen
import shlex
import shutil
import pytest


def check_result(app, docxfile):
    __tracebackhide__ = True
    if not (app.outdir / docxfile).exists():
        pytest.fail('Result file missing')
    if app._warning.getvalue():
        pytest.fail('Failed because warnings were detected during generation')


@pytest.mark.sphinx('docx', testroot='sample-1')
def test_sample_1(app):
    app.builder.build_all()
    check_result(app, 'example-0.1.docx')


@pytest.mark.sphinx('docx', testroot='sample-2')
def test_sample_2(app):
    app.builder.build_all()
    check_result(app, 'my_foo_project-0.0.0.docx')


@pytest.mark.sphinx('docx', testroot='sample-3')
def test_sample_3(app):
    app.builder.build_all()
    check_result(app, 'my_foo_project-0.0.0.docx')


@pytest.mark.sphinx('docx', testroot='sample-4')
def test_sample_4(app):
    app.builder.build_all()
    check_result(app, 'my_foo_project-0.0.0.docx')


@pytest.mark.sphinx('docx', testroot='sample-5')
def test_sample_5(app):
    app.builder.build_all()
    check_result(app, 'my_foo_project-0.0.0.docx')
