counter = 0
while counter <= 15:
    print(f'Hello {counter}')
    counter += 1
    if counter == 12:
        break

# # in:

# def very_important_function(template: str, *variables, file: os.PathLike, engine: str, header: bool = True, debug: bool = False):
#     """Applies `variables` to the `template` and writes to `file`."""
#     with open(file, 'w') as f: