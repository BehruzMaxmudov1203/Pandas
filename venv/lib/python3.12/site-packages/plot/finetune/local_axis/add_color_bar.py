"""
Add color bar
"""
from ...tk.matplotlibTK import color_bar
from typing import Dict
from .make_color_bar_axis import make_color_bar_axis


def add_color_bar(params):
    # type: (Dict) -> Dict
    """Refine legend properties

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    p_panel = params['internal']['panel']
    fig = params['internal']['canvas']['figure']
    axes = params['internal']['canvas']['axes2D'].ravel().tolist()
    for panel_id in p_panel['color_bar']:
        if panel_id in params['local']:
            p = params['local'][panel_id]['color_bar']
        else:
            p = params['internal']['default']['local']['color_bar']

        if p['global'] is True:
            ax = axes
            cax = None
        else:
            ax = None
            obj_axis = params['internal']['canvas']['axes'][panel_id]
            cax = make_color_bar_axis(obj_axis, p)

        for handles_labels in p_panel['color_bar'][panel_id]:
            handle, label = handles_labels
            obj_color_bar = color_bar.add_color_bar(
                handle,
                ax=ax,
                cax=cax,
                bar_label=label,
                bar_tick_label_font_size=p['tick_label']['font']['size'],
                bar_tick_label_color=p['tick_label']['color'],
                bar_tick_label_padding=p['padding']['label_and_tick'],
                bar_ticks=p['tick']['set'],
                bar_tick_width=p['tick']['width'],
                bar_tick_length=p['tick']['length'],
                bar_tick_color=p['tick']['color'],
                bar_padding=p['padding']['color_bar_and_panel'],
                orientation=p['orientation'],
                fraction=p['fraction'],
                shrink=p['shrink'],
                aspect=p['aspect'],
                anchor=p['anchor'],
                parent_anchor=p['parent_anchor'],
                tick_label_format=p['tick_label']['format'],
                color_edges=p['color']['show_edges'],
                color_spacing=p['color']['spacing'],
                color_segment_boundaries=p['color']['segment']['boundaries'],
                color_segment_values=p['color']['segment']['values']
                )

    return params
