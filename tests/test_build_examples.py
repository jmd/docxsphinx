import os
from subprocess import Popen
import shlex
import shutil
import pytest


@pytest.mark.sphinx('docx', testroot='sample-1')
def test_sample_1(app):
    app.builder.build_all()
    assert (app.outdir / 'example-0.1.docx').exists()


@pytest.mark.sphinx('docx', testroot='sample-2')
def test_sample_2(app):
    app.builder.build_all()
    assert (app.outdir / 'my_foo_project-0.0.0.docx').exists()


@pytest.mark.sphinx('docx', testroot='sample-3')
def test_sample_3(app):
    app.builder.build_all()
    assert (app.outdir / 'my_foo_project-0.0.0.docx').exists()


@pytest.mark.sphinx('docx', testroot='sample-4')
def test_sample_4(app):
    app.builder.build_all()
    assert (app.outdir / 'my_foo_project-0.0.0.docx').exists()


@pytest.mark.sphinx('docx', testroot='sample-5')
def test_sample_5(app):
    app.builder.build_all()
    assert (app.outdir / 'my_foo_project-0.0.0.docx').exists()
