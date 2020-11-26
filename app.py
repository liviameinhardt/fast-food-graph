# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:23:57 2020

@author: livia
"""

import dash
import dash_cytoscape as cyto
import dash_html_components as html
import json

with open('grafo.txt') as json_file:
    grafo = json.load(json_file)
    

app = dash.Dash(__name__)

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        layout={
                'name': 'cose',
                'idealEdgeLength': 100,
                'nodeOverlap': 20,
                'refresh': 20,
                'fit': True,
                'padding': 30,
                'randomize': False,
                'componentSpacing': 100,
                'nodeRepulsion': 400000,
                'edgeElasticity': 100,
                'nestingFactor': 5,
                'gravity': 80,
                'numIter': 1000,
                'initialTemp': 200,
                'coolingFactor': 0.95,
                'minTemp': 1.0
            },
        style={
        'position': 'absolute',
        'width': '100%',
        'height': '100%',
        'z-index': 999
    },
        elements=grafo
    )
])



@app.callback(Output('cytoscape', 'responsive'), [Input('toggle-button', 'n_clicks')])
def toggle_responsive(n_clicks):
    n_clicks = 2 if n_clicks is None else n_clicks
    toggle_on = n_clicks % 2 == 0
    return toggle_on


@app.callback(Output('toggle-text', 'children'), [Input('cytoscape', 'responsive')])
def update_toggle_text(responsive):
    return '\t' + 'Responsive ' + ('On' if responsive else 'Off')


if __name__ == '__main__':
    app.run_server(debug=False)    