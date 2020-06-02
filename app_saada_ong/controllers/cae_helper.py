# !url/bin/env/python
# -*- encoding: utf-8 -*-


# import unicode


def clean_backslash(string):
    import re

    regex = re.compile(r'(\\){3,}')

    return regex.sub('\\\\', string)



def new_clean_string(input_str=None, change_encode=False):
    """
    Remove all the dirt from string (CRLF, escape, quotes)
    """

    # Default values
    if not input_str:
        return ''

    if change_encode:
        input_str = input_str.encode('ASCII', 'ignore')

    clean_str = input_str.strip().replace('\\.','') \
                        .replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t') \
                        .replace(':', '').replace("'", "").replace('"', '').replace('|', '')

    '''
    if isinstance(clean_str, unicode):
        clean_str = clean_str.replace(u'\u0093', '').replace(u'\u0094', '') \
                            .replace(u'\u0095', '').replace(u'\u0096', '') \
                            .replace(u'\u0080', '').replace(u'\u0099', '') \
                            .replace(u'\u200b', '').replace(u'\u0303', '') \
                            .replace(u'\u0327', '').replace(u'\u0335', '') \
                            .replace(u'\u0337', '').replace(u'\u2013', '')

    '''
    return clean_backslash(clean_str)
