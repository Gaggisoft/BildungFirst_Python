# Main

# Datei mit Implementierung der Funktionalität einbinden
from kd_start import start_inventar
from kd_bedienung import user_input
from kd_funktion import show_inventory

# leeres Dictionary erstellen
inventar = start_inventar()
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