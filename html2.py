# -*- coding: utf-8 -*-
import dash
import json
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F0FFF0',
    'text': '#2F4F4F'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children="Welcome! Это сайт Чечениной Анны",
        style={
            'textAlign': 'center',
            'color': colors['text']
            }),

    html.Div(children="Поcмотрите это прекрасное видео, оно очень милое :)", style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.Iframe(width="560", height="315", src="https://www.youtube.com/embed/bIyl9bCp6W4"),

    dcc.Tabs([
        dcc.Tab(label='Обо мне', children=[
            html.Div(children=["Привет! Я учусь на первом курсе ОП 'Клеточная и молекулярная биотехнология' в НИУ ВШЭ. В свободное время люблю путешествовать и заниматься всеми возможными видами спорта. Состою в Зеленой Вышке и в Добровольных Лесных Пожарных, где мы всеми силами стараемся сделать наш мир чуточку лучше!"])
        ]),
        dcc.Tab(label='Фоточка', children=[
           html.Img(src="https://1.downloader.disk.yandex.ua/preview/ef11a2f7d9c26a6e28009e88a2c696597749a4b18e9ef52e66031d5215f2291e/inf/75ok4E5a-7lP5V9PRoRYb_SV1dl7-2YIr0Wm0I69cis6XDifpsOpuGOPkyAsKQVaiXMjGYfe1GPEeLG476EEFQ%3D%3D?uid=163562962&filename=gus.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=163562962&tknv=v2&size=2158x1296", style={'width':'40%', 'margin-left':450, 'margin-top':25})
         ]),
        dcc.Tab(label="Опрос", children=[
            html.Div(children="Тут опрос о том, как вы наливаете соус на сосиску! Он на английском, т.к русский не поддерживается :(", style={
            'textAlign': 'center',
            'color': colors['text']
        }),
            html.Button('I pour it all over the sausage at once', id='I pour it all over the sausage at once'),
    html.Button('I pour it next to the sausage, then dip the pieces in it', id='I pour it next to the sausage, then dip the pieces in it'),
    html.Button('I get my energy from the Holy spirit', id='I get my energy from the Holy spirit'),
    html.Div(id='container')            
        ]),
            dcc.Tab(label='Контакты', children=[
            dcc.Markdown('''
                 **Моя телега: @sleepingann **''',style={
        'textAlign': 'center',
        'color': colors['text']}),
            dcc.Markdown('''
                 **Для важных сообщений используйте почту:  [написать Ане](mailto:che4enina.a@yandex.ru)**''',style={
        'textAlign': 'center',
        'color': colors['text']}),
            dcc.Markdown('''
                 **Мой вк:  [http://vk.com/annnnche](http://vk.com/annnnche)**''',style={
        'textAlign': 'center',
        'color': colors['text']
        })
        ])
    ])
])

@app.callback(Output('container', 'children'),
              [Input('I pour it all over the sausage at once', 'n_clicks'),
               Input('I pour it next to the sausage, then dip the pieces in it', 'n_clicks'),
               Input('I get my energy from the Holy spirit', 'n_clicks')])
def display(btn1, btn2, btn3):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)

    return html.Div([
        html.Table([
            html.Tr([html.Th('First'),
                     html.Th('Second'),
                     html.Th('Third'),
                     html.Th('Most Recent Click')]),
            html.Tr([html.Td(btn1 or 0),
                     html.Td(btn2 or 0),
                     html.Td(btn3 or 0),
                     html.Td(button_id)])
        ])
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
