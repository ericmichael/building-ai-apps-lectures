from IPython.core.magic import register_cell_magic

@register_cell_magic
def mermaid(line, cell):
    import base64
    from IPython.display import Image, display
    import matplotlib.pyplot as plt

    graphbytes = cell.encode("utf8")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    display(Image(url="https://mermaid.ink/img/" + base64_string))