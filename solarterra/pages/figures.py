import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


COMMON_MARGIN = {"l": 85, "r": 30, "t": 25, "b": 60}
COMMON_X_DOMAIN = [0.0, 0.86]


def apply_common_time_axis(fig, plot):
    fig.update_xaxes(
        range=[plot.t_start, plot.t_stop],
        domain=COMMON_X_DOMAIN,
        automargin=False,
    )
    fig.update_yaxes(automargin=False)
    fig.update_layout(
        margin=COMMON_MARGIN,
        margin_autoexpand=False,
    )


def scatter(plot):

    if len(plot.y_arrays) == 0 or len(plot.y_arrays[0]) == 0:
        return "<div>No significant data for this period.</div>"

    fig = go.Figure()

    x, y = plot.get_values(0)

    fig.add_trace(go.Scatter(
        x=x, y=y, connectgaps=False, mode="lines+markers"))

    fig.update_traces(connectgaps=False, marker=dict(size=4))
    fig.update_layout(
        yaxis_title=plot.variable.get_axis_label(),
    )
    apply_common_time_axis(fig, plot)


    fig.update_yaxes(type=plot.variable.scaletyp)

    config = {'displayModeBar': False}

    plot_div = fig.to_html(config=config, full_html=False,
                           div_id=f"plot_div_{plot.variable.id}", default_width="100%")
    return plot_div


def n_trace(plot):

    fields = plot.y_fields
    
    if len(plot.y_arrays) == 0:
        return "<div>No significant data for this period.</div>"

    fig = make_subplots(rows=len(fields), cols=1,
                        shared_xaxes=True, vertical_spacing=0.05)
    for index, field in enumerate(fields):
        x, y = plot.get_values(index)
        fig.add_trace(go.Scatter(
            x=plot.x_field_array,
            y=plot.y_arrays[index],
            connectgaps=False,
            mode="lines+markers",
        ),
            row=index + 1,
            col=1
        )
        fig['layout'][f"yaxis{index+1}"]['title'] = plot.variable.get_axis_label(index)
        fig['layout'][f"xaxis{index+1}"]['range'] = [plot.t_start, plot.t_stop]

    fig.update_traces(marker=dict(size=4))
    

    fig.update_layout(
        height=700,
        #xaxis_range=[ts[0], ts[1]],
        showlegend=False,
    )
    apply_common_time_axis(fig, plot)

    config = {'displayModeBar': False}
    plot_div = fig.to_html(config=config, full_html=False,
                           div_id=f"plot_div_{plot.variable.id}", default_width="100%")

    return plot_div


def spectrogram(plot):
    if plot.z_array is None or plot.y_axis_array is None or plot.x_field_array is None:
        return "<div>No significant data for this period.</div>"

    if len(plot.x_field_array) == 0 or len(plot.y_axis_array) == 0:
        return "<div>No significant data for this period.</div>"

    raw_z = np.array(plot.z_array, dtype=float)
    if raw_z.size == 0:
        return "<div>No significant data for this period.</div>"

    pos_mask = raw_z > 0
    color_z = np.full(raw_z.shape, np.nan, dtype=float)
    if pos_mask.any():
        color_z[pos_mask] = np.log10(raw_z[pos_mask])

    finite_raw = raw_z[np.isfinite(raw_z) & (raw_z > 0)]
    if finite_raw.size > 0:
        min_pow = int(np.floor(np.log10(finite_raw.min())))
        max_pow = int(np.ceil(np.log10(finite_raw.max())))
        tickvals = list(range(min_pow, max_pow + 1))
        ticktext = [f"1×10<sup>{p}</sup>" for p in tickvals]
    else:
        tickvals = None
        ticktext = None

    z_title = plot.variable.name
    z_unit = plot.variable.get_unit_label()
    if z_unit:
        z_title = f"{z_title}, {z_unit}"

    fig = go.Figure(
        data=go.Heatmap(
            x=plot.x_field_array,
            y=plot.y_axis_array,
            z=color_z.T,
            customdata=raw_z.T,
            colorscale="Rainbow",
            connectgaps=False,
            colorbar={
                "title": z_title,
                "tickvals": tickvals,
                "ticktext": ticktext,
                "x": 0.9,
                "xanchor": "left",
                "thickness": 18,
            },
            hovertemplate="x=%{x}<br>y=%{y}<br>z=%{customdata:.3e}<extra></extra>",
        )
    )

    y_title = plot.variable.get_axis_label()
    if plot.variable.depend_1 is not None:
        dep1_var = plot.variable.dataset.variables.get_or_none(name=plot.variable.depend_1)
        if dep1_var is not None:
            y_title = dep1_var.get_axis_label()

    fig.update_layout(
        yaxis_title=y_title,
    )
    apply_common_time_axis(fig, plot)

    config = {"displayModeBar": False}
    plot_div = fig.to_html(
        config=config,
        full_html=False,
        div_id=f"plot_div_{plot.variable.id}",
        default_width="100%",
    )
    return plot_div
