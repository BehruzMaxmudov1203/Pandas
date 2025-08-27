"""
Set tick parameters
"""
from typing import Dict


def set_tick_params(params):
    # type: (Dict) -> Dict
    """Set the tick parameters

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for panel_id, p in params['local'].items():
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for k in ['x', 'y']:
            for m in ['major', 'minor']:
                if m is 'major':
                    obj_axis.ticklabel_format(
                        axis=k,
                        style=p['tick_label'][m]['format']['style'][k],
                        scilimits=(0,0),
                        useMathText=True)
                    getattr(obj_axis, "{}axis".format(k)).offsetText.set_fontsize(
                        p['tick_label'][m]['format']['sci_font_size'][k])
                obj_axis.tick_params(
                    axis=k,
                    which=m,
                    labelsize=p['tick_label'][m]['font']['size'][k],
                    width=p['tick'][m]['width'][k])

    return params
