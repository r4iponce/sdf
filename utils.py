def remove_redundant_in_list(source_list: list[str]) -> list[str]:
    sorted_list = []
    for item in source_list:
        if item not in sorted_list:
            sorted_list.append(item)

    return sorted_list


def print_list(printed_list) -> None:
    for item in printed_list:
        print(item)
