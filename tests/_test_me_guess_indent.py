import re

# I can't import 'pdf-toc' (it has a dash '-').


class Parser(object):

    indent = 4

    def guessIndent(self, indent, title):
        if indent == '':
            m = re.match(r'\d+((\.\d+)+)\.?(\s|$)', title)
            if m:
                inc = len(m.group(1).split('.')) - 1
                indent = ' ' * self.indent * inc
        return indent, title


def test_indent():
    lines = (
        ('1',                   0),

        ('1 xxx',               0),
        ('1. xxx',              0),
        ('1.1 xxx',             1),
        ('1.1. xxx',            1),
        ('1.1.1 xxx',           2),
        ('1.1.1. xxx',          2),

        ('32.32 xxx',           1),
        ('32.32. xxx',          1),
    )
    parser = Parser()
    for line in lines:
        title, expected = line
        indent, _ = parser.guessIndent('', title)
        error_msg = 'title: %r, indent: %r' % (title, indent)
        assert indent == ' ' * 4 * expected, error_msg


test_indent()
