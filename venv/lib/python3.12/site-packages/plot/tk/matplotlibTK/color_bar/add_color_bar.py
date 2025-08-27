"""
Add a color bar
"""
from typing import List, AnyStr
import matplotlib.ticker
import matplotlib.pyplot
import mpl_toolkits.axes_grid1 as MplTkAxes
from .add_label import add_label
from .set_tick_label_font_size import set_tick_label_font_size


def add_color_bar(
        obj_matshow,                                     # type: object
        ax=None,                                         # type: List
        cax=None,                                        # type: List
        bar_label=None,                                  # type: AnyStr
        bar_tick_label_font_size=20,                     # type: int
        bar_tick_label_color="k",                        # type: AnyStr
        bar_tick_label_padding=5,                        # type: int
        bar_ticks=None,                                  # type: List
        bar_tick_width=2,                                # type: int
        bar_tick_length=7,                               # type: int
        bar_tick_color="k",                              # type: AnyStr
        bar_padding=0.01,                                # type: float
        orientation='vertical',                          # type: AnyStr
        fraction=0.1,                                    # type: float
        shrink=1.0,                                      # type: float
        aspect=20,                                       # type: int
        anchor=[0, 0.5],                                 # type: List
        parent_anchor=[1.0, 0.5],                        # type: List
        tick_label_format=None,                          # type: AnyStr
        color_edges=False,                               # type: bool
        color_spacing='uniform',                         # type: AnyStr
        color_segment_boundaries=None,                   # type: List
        color_segment_values=None                        # type: List
        ):
    # type: (...) -> object
    """Add color bar to an axis object

    Args:
        obj_matshow (object): a ``matplotlib.image.AxesImage`` object
        ax=None (list): a list of subplots axes objects
        cax=None (object): matplotlib axis object
            where the color bar will be plotted
        bar_label=None (str): label for the color bar
        bar_tick_label_font_size (int): color bar tick label font size
        bar_tick_label_color='k' (str): color for tick labels
        bar_ticks (list): a list/tuple of tick locations, e.g. (0, 0.5, 1.0)
            (default: None, i.e. use matplotlib default)
        bar_tick_width (int): width of the color bar ticks
        bar_tick_length (int): length of the color bar ticks
        bar_tick_color (str): color of the color bar ticks
        padding (int): padding between ticks and tick labels
        orientation='vertical' (str):  orientation of the color bar
        fraction=0.1 (float): fraction of the original axes to use
            for color bar
        shrink=1.0 (float): fraction to shrink
        aspect=20 (int): ratio between the long to short color bar axis
        anchor=[0, 0.5] (list): anchor point for the color bar axes
        parent_anchor=[1.0, 0.5] (list): anchor point for the parent axes
        tick_label_format=None (str): formating string for the tick labels
        color_edges=False (bool): draw edges between neighboring colors
        color_spacing='uniform' (str): 'uniform' or 'proportional'
        color_segment_boundaries=None (list): boundaries for the colors
        color_segment_values=None (list): values to be
            mapped to the regions defined by boundaries
            must be of length one less than boundaries

    Returns:
        a ``matplotlib.colorbar.Colorbar`` object
    """
    if ax is None:
        obj_color_bar = matplotlib.pyplot.colorbar(
            obj_matshow,
            ax=ax,
            cax=cax,
            orientation=orientation,
            spacing=color_spacing,
            ticks=bar_ticks,
            format=tick_label_format,
            drawedges=color_edges,
            boundaries=color_segment_boundaries,
            values=color_segment_values
            )
    else:
        obj_color_bar = matplotlib.pyplot.colorbar(
            obj_matshow,
            ax=ax,
            cax=cax,
            orientation=orientation,
            fraction=fraction,
            pad=bar_padding,
            shrink=shrink,
            aspect=aspect,
            anchor=anchor,
            panchor=parent_anchor,
            spacing=color_spacing,
            ticks=bar_ticks,
            format=tick_label_format,
            drawedges=color_edges,
            boundaries=color_segment_boundaries,
            values=color_segment_values
            )

    # add color bar label
    add_label(obj_color_bar, bar_label)

    # change tick label font size
    set_tick_label_font_size(obj_color_bar, bar_tick_label_font_size)

    # set tick label color
    obj_color_bar.ax.yaxis.set_tick_params(labelcolor=bar_tick_label_color)

    # set ticks color
    obj_color_bar.ax.yaxis.set_tick_params(color=bar_tick_color)

    # set tick width
    obj_color_bar.ax.yaxis.set_tick_params(width=bar_tick_width)

    # set tick length
    obj_color_bar.ax.yaxis.set_tick_params(length=bar_tick_length)

    # set padding between ticks and tick labels
    obj_color_bar.ax.yaxis.set_tick_params(pad=bar_tick_label_padding)

    return obj_color_bar
