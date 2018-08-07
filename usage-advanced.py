"""
Note: audio and screenshotWidth can't be updated after it is set.
"""

import dash_webcam
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash('')
server = app.server

app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div(className='row', children=[
        html.P('Original Footage on the left, screenshot on the right'),

        dash_webcam.WebcamComponent(
            id='webcam',
            audio=True,
            screenshotFormat="image/jpeg",
            width=1280,
            height=720,
            screenshotWidth=700
        ),

        html.Img(id='output')
    ]),

    html.Div(className='row', style={'width': '50%'}, children=[
        html.P('Screenshot format:', style={'margin-top': '15px'}),
        dcc.RadioItems(
            id='radio-screenshot-format',
            options=[{'label': val.upper(), 'value': val} for val in [
                'webp',
                'jpeg',
                'png',
                'gif'
            ]],
            value='jpeg'
        ),

        html.P("Screenshot quality:", style={'margin-top': '30px'}),
        dcc.Slider(
            id='slider-screenshot-quality',
            min=0,
            max=1,
            step=0.1,
            value=0.8,
            updatemode='drag',
            marks={0: '0%', 1: '100%'}
        ),

        html.P("Update Interval for screenshots:",
               style={'margin-top': '30px'}),
        dcc.Slider(
            id='slider-interval-screenshot',
            min=40,
            max=1000,
            step=None,
            updatemode='drag',
            marks={i: str(i) for i in [40, 100, 200, 500, 1000]},
            value=100
        ),
    ])
])


@app.callback(Output('output', 'src'),
              [Input('webcam', 'screenshot')])
def show_screenshot_image(screenshot):
    return screenshot



@app.callback(Output('webcam', 'screenshotQuality'),
              [Input('slider-screenshot-quality', 'value')])
def update_screenshot_quality(value):
    return value


@app.callback(Output('webcam', 'screenshotInterval'),
              [Input('slider-interval-screenshot', 'value')])
def update_screenshot_interval(value):
    return value


@app.callback(Output('webcam', 'screenshotFormat'),
              [Input('radio-screenshot-format', 'value')])
def update_screenshot_format(value):
    return 'image/' + value


if __name__ == '__main__':
    app.run_server(debug=True)
