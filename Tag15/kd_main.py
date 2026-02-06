# Main

# Datei mit Implementierung der Funktionalität einbinden
from kd_start import init_inventory
from kd_bedienung import user_input
from kd_funktion import show_inventory

if __name__ == '__main__':
    inventory = init_inventory()
    user_input(inventory)
    print('\nFinaler Stand:')
    show_inventory(inventory)