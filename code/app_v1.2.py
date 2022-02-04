# -*- coding: utf-8 -*-
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc
from dash import html
import pandas as pd

import plotly.graph_objs as go
from datetime import datetime
from dash.dependencies import Input, Output
from Data import Analyzer

import app_bollingerband as ab
import app_candlechart as ac
import app_prediction as ap

mk = Analyzer.MarketDB()
daily = mk.get_daily_table()

# 드롭 아웃 라벨
codes = list(mk.codes.keys())
company = list(mk.codes.values())
drop_label = list()
predict = list()
for i in range(0, len(codes)) :
    drop_label.append(f'{codes[i]}_{company[i]}')

def make_table(df, code):
    predict = ap.predict_stock(code)
    return html.Table(
        children=[
            html.Thead(
                style={"display": "block", "marginBottom": 10, "marginLeft": 30},
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(3, 1fr)",
                            "fontWeight": "600",
                            "fontSize": 16,
                        },
                        children=[
                            html.Th(column_name.replace("_", " ")) for column_name in df.columns
                        ]
                    )
                ]
            ),
            html.Tbody(
                style={"minHeight" : "40vh",
                       "maxHeight": "40vh",
                       "display": "block", "overflow": "scroll",
                       "marginLeft": 30},
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(3, 1fr)",
                            "borderTop": "1px solid black",
                            "padding": "15px 0px",
                        },
                        children=[
                            html.Td(
                                value_column,
                                style={"textAlign": "center"}
                            ) for value_column in value
                        ]
                    ) for value in df.values
                ]
            ),
            html.Thead(
                style={"display": "block", "marginTop":20, "marginBottom": 10, "marginLeft": 30},
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(2, 1fr)",
                            "fontWeight": "600",
                            "fontSize": 16,
                        },
                        children=[
                            html.Th(column_name.replace("_", " ")) for column_name in ['Company', 'Predict_Close']
                        ]
                    )
                ]
            ),
            html.Tbody(
                style={"minHeight" : "10vh",
                       "maxHeight": "10vh",
                       "display": "block",
                       "marginLeft": 30},
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(2, 1fr)",
                            "borderTop": "1px solid black",
                            "padding": "15px 0px",
                        },
                        children=[
                            html.Td(
                                value_column,
                                style={"textAlign": "center"}
                            ) for value_column in predict
                        ]
                    )
                ]
            )
        ]
    )

stylesheet = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Roboto&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        #"backgroundColor": "#121212",
        #"color": "#C8D6E5",
        "fontFamily": "Roboto, sans-serif"
    },
    children=[
        html.Header(
            style={
                "textAlign": "center",
                "paddingTop": "50px",
                "marginBottom": 50
            },
            children=[html.H1("주식 분석 시스템",
                              style={"fontSize": 50})]
        ),
        html.Div(
            style={"marginLeft": 30,"marginBottum":20},
            children=
                dcc.Dropdown(style={
                    "width": 300,
                    "color": "#111111",
                },
                id="test_drop",
                options=[
                    {'label': company, 'value': company[:company.index('_')]} for company in drop_label],
                value='000020',
                clearable=False
        )),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(10, 1fr)",
                "marginTop" : 20,
                "maxHeight": "50vh",
            },
            children=[
                html.Div(
                    style={"gridColumn": "span 2", },
                    id = 'predict'),
                html.Div(
                    style={"gridColumn": "span 4", },
                    children=[
                        dcc.Graph(
                            id='candle',
                            #figure=plotly_fig
                        )
                    ]),
                html.Div(
                    style={"gridColumn": "span 4", },
                    children=[
                        dcc.Graph(
                            id='bollinger',
                            #figure=plotly2_fig
                        )
                ])
        ]),

    ])

@app.callback([
    Output('candle', 'figure'),
    Output('bollinger', 'figure'),
    Output('predict', 'children'),
], [Input('test_drop', 'value')])
def update_drop(value):
    #r1 = 'candle chart "{}"'.format(value)
    #r2 = 'bollinger chart "{}"'.format(value)
    #r3 = 'predict value "{}"'.format(value)
    return ac.candlechart(value), ab.trendfollowing(value), make_table(daily, value)


if __name__ == '__main__':
    app.run_server(debug=True)