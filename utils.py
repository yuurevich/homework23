def build_query(cmd, val, file_list):
    if cmd == 'filter':
        res = filter(lambda x: val in x, file_list)
        return res
    if cmd == 'map':
        val = int(val)
        res = [x.split()[int(val)] for x in file_list]
        return res
    if cmd == 'unique':
        res = list(set(file_list))
        return res
    if cmd == 'sort':
        reverse = val == "desc"
        res = sorted(file_list, reverse=reverse)
        return res
