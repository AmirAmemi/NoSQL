import json
with open('TP1Q4.json') as f:
    file = json.load(f)
print(json.dumps(file, indent=4))
msgs = sorted(file['messages'], key=lambda k: k['date'])
for message in msgs:
    print(message['date'], message['objet'], message['expediteur'], message['destinataire'], message['contenu'])