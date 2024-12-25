def tabulate(contents: list[dict[str, str]] = [],
             headers: list[str] = [],
             rows: list[list[any]] = []) -> None:

    if contents:
        headers = list(contents[0].keys())
        rows = [list(activity.values()) for activity in contents]
    max_column_widths = []
    table_width = 0
    if headers:
        max_column_widths = [max([len(str(row[idx])) for row in rows] + [len(headers[idx])]) for idx in range(len(headers))]
        table_width = sum(max_column_widths) + 4 * len(headers)
    elif rows:
        max_column_widths = [max([len(str(row[idx])) for row in rows]) for idx in range(len(rows[0]))]
        table_width = sum(max_column_widths) + 4 * len(rows[0])

    def display_border(edge='+') -> None: print(f"{edge}{'-'*table_width}{edge}")

    def display_row(row) -> None: 
        nonlocal max_column_widths
        for idx, cell in enumerate(row):
            print(f"| {' ' * (max_column_widths[idx] - len(str(cell)))} {cell}", end=" ")
        print(" |")

    display_border()
    def display_headers() -> None: 
        nonlocal headers
        if headers:
            display_row(headers)
            display_border()
        
    def display_rows(row: list[any]) -> None: 
        nonlocal rows
        n = len(rows)
        for idx, row in enumerate(rows):
            display_row(row)  
            if idx != n - 1: display_border(edge='-')

    display_headers()
    display_rows(rows)
    if rows: display_border()

