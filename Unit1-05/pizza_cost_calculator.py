import ui

def calculateCost(sender):
	diameter = float(view['diameterInput'].text)
	cost = 0.75 + 1 + (0.5*diameter)
	view['costOutput'].text = 'cost: $' + str(cost)
	

view = ui.load_view()
view.present('sheet')
