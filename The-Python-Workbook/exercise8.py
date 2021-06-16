# An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number of widgets and the number of gizmos from the user. Then your program should compute and display the total weight of the parts.

widget = input('Insert number widget: ')
gizmos = input('Insert number gizmos: ')

widget_weighs = 75
gizmos_weighs = 112

total_widget_weighs = float(widget) * float(widget_weighs)
total_gizmos_weighs = float(gizmos) * float(gizmos_weighs)
print('Total widget :' + widget)
print('Total gizmos :' + gizmos)

print('Total widget weight ' + str(total_widget_weighs) + ' grams')
print('Total gizmos weight ' + str(total_gizmos_weighs) + ' grams')
