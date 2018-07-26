import dash_webcam
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div(className='row', children=[
        html.P('Original Footage:'),

        dash_webcam.WebcamComponent(
            id='webcam',
            audio=False,
            screenshotFormat="image/jpeg",
            width=500,
            height=300
        )
    ]),

    html.Div(className='row', children=[
        html.P('Returned Footage:'),
        html.Img(id='output')
    ])

])


@app.callback(Output('output', 'src'),
              [Input('webcam', 'screenshot')])
def show_screenshot_image(screenshot):
    return screenshot


if __name__ == '__main__':
    app.run_server(debug=True)
