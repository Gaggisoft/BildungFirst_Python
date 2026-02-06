# Main

# Datei mit Implementierung der Funktionalität einbinden
from kd_start import init_inventory
from kd_bedienung import user_input
from kd_funktion import show_inventory

# leeres Dictionary erstellen
inventar = init_inventory()
# Nutzereingabe
user_input(inventar)


# TESTS
#beispiel_inventar = {'milch': 3,
#                     'apfel': 1}
#kd_funktion.show_inventory(beispiel_inventar)
#kd_funktion.add_item(beispiel_inventar, 'Birne')
#kd_funktion.show_inventory(beispiel_inventar)
#kd_funktion.remove_item(beispiel_inventar, 'Milch', 2)
#kd_funktion.remove_item(beispiel_inventar, 'Apfel')
#kd_funktion.show_inventory(beispiel_inventar)