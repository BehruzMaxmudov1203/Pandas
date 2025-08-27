"""
Refine legends to an axis object
"""
from typing import Dict
import matplotlib.pyplot
from .extract_legend_handles_labels import extract_legend_handles_labels


def refine_legend(obj_axis, handle_label_pairs, legend_params):
    # type: (object, Dict) -> obj_axis
    """Refine legends to an axis object

    Args:
        obj_axis (object): a matplotlib axis object
        handle_label_pairs (list): a list of [handle, label] pairs
        legend_params (dict): a dictionary with legend property specifications

    Returns:
        the input axis object
    """
    p = legend_params
    handles, labels = extract_legend_handles_labels(handle_label_pairs)
    if len(labels) == 0:
        return obj_axis
    else:
        obj_legend = obj_axis.legend(
            handles, labels,
            fancybox=legend_params['box']['rounded'],
            loc=p['anchor']['corner'],
            bbox_to_anchor=p['anchor']['coordinate'],
            frameon=p['frame']['show'],
            framealpha=p['frame']['opacity'],
            ncol=p['number_of_columns'],
            fontsize=p['font']['size'],
            markerscale=p['marker']['scale'],
            numpoints=p['marker']['number_of_points'],
            handlelength=p['handle_length'],
            borderpad=p['border_padding'],
            labelspacing=p['vertical_spacing'],
            handletextpad=p['padding_between_handle_and_text'],
            borderaxespad=p['padding_between_border_and_axes'],
            columnspacing=p['column_spacing'],
            )
        # obj_legend = matplotlib.pyplot.gca().get_legend()
        # get all the lines.Line2D instance from the legend
        obj_legend_lines = obj_legend.get_lines()
        # get all the text.Text instance from the legend
        obj_legend_text = obj_legend.get_texts()
        matplotlib.pyplot.setp(obj_legend_lines, linewidth=p['line']['width'])
        matplotlib.pyplot.setp(obj_legend_text, fontweight=p['font']['weight'])

        # get the patch.Rectangle instance surrounding the legend
        obj_legend_frame = obj_legend.get_frame()
        # Change legend face color
        obj_legend_frame.set_facecolor(p['face']['color'])
        # Change legend edge color
        obj_legend_frame.set_edgecolor(p['edge']['color'])

        return obj_axis
