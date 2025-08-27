"""
Set color bar tick label font size
"""


def set_tick_label_font_size(obj_color_bar, font_size):
    """Set color bar tick label font size
    Args:
        obj_color_bar (object): a ``matplotlib.colorbar.Colorbar`` object
        font_size (int): font size
    """
    for tick in obj_color_bar.ax.get_yticklabels():
        tick.set_fontsize(font_size)
    return
