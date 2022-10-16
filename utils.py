def remove_redundant_in_list(source_list: list) -> list:
    sorted_list = []
    for item in source_list:
        if item not in sorted_list:
            sorted_list.append(item)
    return sorted_list
