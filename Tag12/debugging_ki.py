def berechne_durchschnitt(werte):
    return sum(werte) / len(werte)

# GitHub Copilot
def berechne_durchschnitt(werte):
    if len(werte) == 0:
        return None
    return sum(werte) / len(werte)

# ChatGPT / Microsoft Copilot
def berechne_durchschnitt(werte):
    if not werte:
        return None
    return sum(werte) / len(werte)


zahlen = []
durchschnitt = berechne_durchschnitt(zahlen)
print('Durchschnitt ist', durchschnitt)