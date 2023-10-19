import plotly as px





xArray = [1,2,3,1]
yArray = [1,1,2,2]

fig = px.graph_objs.Figure()
fig.add_trace(px.graph_objs.Scatter(x= xArray, y= yArray ))
sizeMultiplier = 300


fig.update_layout(
    autosize=False,
    width=max(xArray)*sizeMultiplier,
    height=max(yArray)*sizeMultiplier,
    margin=dict(
        l=100,
        r=100,
        b=100,
        t=100,
        pad=4
    )
)

fig.show()