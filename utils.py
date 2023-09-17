def prepare_xpath(*args, **kwargs) -> str:
    # import pdb; pdb.set_trace()
    if bool(kwargs):
        attribs = kwargs
    else:
        attribs = args[0]
    if 'type' not in attribs.keys():
        print(f'type not supplied')
        return ''
    type = attribs.pop('type')
    props = []
    for k, v in attribs.items():
        if k=='_class': k='class'
        attr_name = 'text()' if k == 'text' else f'@{k}'
        part_xpath = f"contains({attr_name}, '{v}')"
        props.append(part_xpath)
    prop_clause = ' and '.join(props)
    return f'//{type}[{prop_clause}]'


# print(prepare_xpath({'class': 'button', 'text': 'Download PP', 'type': 'a', 'href': 'amd64'}))

print(prepare_xpath(_class = 'button', type='button', text='Download Python'))
