import dash_webcam
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    dash_webcam.WebcamComponent(
        id='webcam',
        audio=False,
        screenshotFormat="image/jpeg",
        width=1000,
        height=750
    ),

    html.Button('Click me', id='button'),

    html.Div(id='output')
])


@app.callback(Output('output', 'children'),
              [Input('button', 'n_clicks')],
              [State('webcam', 'width')])
def func(_, width):
    return width


if __name__ == '__main__':
    app.run_server(debug=True)
