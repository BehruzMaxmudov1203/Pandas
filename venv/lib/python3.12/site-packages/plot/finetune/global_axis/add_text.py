"""
Add text annotation to each panel
"""
import matplotlib


def add_text(params: dict) -> dict:
    for t in params['global']['text']:
        if t['content'] is not None:
            matplotlib.pyplot.figtext(
                t["x"],
                t["y"],
                t["content"],
                alpha=t['font']["opacity"],
                fontsize=t["font"]["size"],
                color=t["font"]["color"],
                rotation=t["rotation"],
                bbox=dict(
                    facecolor=t['background']['color'],
                    alpha=t['background']['opacity']),
                horizontalalignment=t["alignment"]["horizontal"],
                verticalalignment=t["alignment"]["vertical"],
                )
    return params
