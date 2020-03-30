import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1('Это сайт Ани Чечениной'),

    html.Div("Попробую написать здесь какую-то информацию")

])

if __name__ == 'Bananya':
    app.run_server(debug=True)
                
