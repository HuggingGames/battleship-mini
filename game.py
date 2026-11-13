"""Mini-game by CAN YILDIRIM · Hugging Games."""
import random
import math

def reply(state, message):
    return state, message

def finish(state, message):
    state["done"] = True
    return state, message + "\n🏁 Oyun bitti. Yeniden başlat ile tekrar oyna."

def _view(s):
    return '\n'.join(' '.join(('X' if 5*y+x in s['hits'] else 'o' if 5*y+x in s['miss'] else '·') for x in range(5)) for y in range(5))
def new_game():
    positions=random.sample(range(25),5);s={'ships':positions,'hits':[],'miss':[],'done':False};return s,'5x5 denizde 5 gizli gemi noktası. Satır sütun yaz (1-5).\n'+_view(s)
def play(s,action):
    if s['done']:return reply(s,'Yeni oyun başlat.')
    try:y,x=[int(z)-1 for z in action.replace(',',' ').split()]
    except ValueError:return reply(s,'Örnek: 3 5')
    if not (0<=x<5 and 0<=y<5):return reply(s,'1-5 arasında koordinat yaz.')
    i=5*y+x
    if i in s['hits']+s['miss']:return reply(s,'Bu noktayı zaten denedin.')
    if i in s['ships']:s['hits'].append(i);msg='💥 İsabet!'
    else:s['miss'].append(i);msg='🌊 Iska.'
    msg+=f" {len(s['hits'])}/5 gemi bulundu.\n"+_view(s)
    return finish(s,msg) if len(s['hits'])==5 else reply(s,msg)
