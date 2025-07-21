from ..src.nb_html_export import convert_notebook_to_html_string, _generate_table_of_contents
import pytest


# Creating a temporary notebook file for testing
@pytest.fixture
def temp_notebook(tmp_path):

    nb_content = r"""

            {
            "cells": [
            {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Example heading level 1 (this should not be included as the function captures from heading level 2-6)"
            ]
            },
            {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Example heading level 2\n",
                "\n",
                "Author : *Population Health Management Analytical Team: phm.data@snee.nhs.uk*\n",
                "<br>\n",
                "Published on : * *\n",
                "\n",
                "### Example heading level 3\n",
                "\n",
                "\n",
                "some content\n",
                "\n",
                "\n",
                "\n",
                "#### Example heading level 4\n"
            ]
            },
            {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "##### Example heading level 5\n",
                "\n",
                "\n",
                "some extra content"
            ]
            },
            {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "###### Example heading level 6"
            ]
            }
            ],
            "metadata": {
            "language_info": {
            "name": "python"
            }
            },
            "nbformat": 4,
            "nbformat_minor": 2
            }

    """
    temp_file = tmp_path / "test_notebook.ipynb"
    temp_file.write_text(nb_content)

    return temp_file

# Testing convert_notebook_to_html function

def test_convert_notebook_to_html(temp_notebook):
    # output html does not return anything  
    output_html = convert_notebook_to_html_string(temp_notebook)
    assert isinstance(output_html, str)  # checking if output is a string
    assert r"toc" in output_html       # checking if html is generated


def test_convert_notebook_to_html_no_toc(temp_notebook):
    # output html does not return anything  
    output_html = convert_notebook_to_html_string(temp_notebook, make_table_of_contents=False)
    assert isinstance(output_html, str)  # checking if output is a string
    assert r"<div id = 'toc'>" not in output_html       # checking if html is generated

# Testing generate_toc function

def test_generate_toc(temp_notebook):
    toc = _generate_table_of_contents(temp_notebook)
    assert isinstance(toc, str)  # Check if output is a string
    assert "Example heading level 1 (this should not be included as the function captures from heading level 2-6)" not in toc # Excluded heading level 1 to be titles of reports
    assert "Example heading level 2" in toc
    assert "Example heading level 3" in toc
    assert "Example heading level 4" in toc
    assert "Example heading level 5" in toc
    assert "Example heading level 6" in toc

