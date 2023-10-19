words = [
  '2020184024', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',
  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',
  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',
  'temporize', 'speedboat', 'agenda', 'delusion', 'class04', 'idolize', 'romance', 'overestimate', 'revive', 'smell',
  'modem', 'splat', 'snaky', 'drawn', 'smoke', 'darky', 'lotus', 'mufti', 'pithy', 'jewel', 'nexus',
  'fluff', 'piton', 'finis', 'drake', 'caulk', 'pussy', 'bless', 'weeds', 'realm', 'swoon', 'thorn',
  'plant', 'aorta', 'cupid', 'wafer', 'jewry', 'sinus', 'proud', 'grape', 'cable', 'carer', 'pearl',
  'piece', 'party', 'sleet', 'palmy', 'oiled', 'synod', 'trove', 'voice', 'chest', 'story', 'range',
  'scout', 'sewer', 'lowly', 'usher', 'seine', 'gulch', 'fever', 'frith', 'pylon', 'wager', 'banns',
  'merit', 'cheap', 'booby', 'truss', 'codex', 'sepia', 'totem', 'poult', 'dregs', 'giddy', 'umber',
  'mooch', 'smarm', 'loath', 'spoil', 'drink', 'wrick', 'awake', 'mural', 'glide', 'pinch', 'thine',
  'tawny', 'swede', 'shier', 'satan', 'triad', 'splay', 'tacit',
]

def downHeap(root, size):
  ch = root * 2 + 1
  if ch >= size : return
  if ch+1 < size and words[ch] < words[ch+1]:
    ch = ch + 1
  if words[root] >= words[ch]: return

  words[root], words[ch] = words[ch], words[root]
  downHeap(ch, size)

l_arr = len(words)

for i in range(l_arr // 2 - 1, -1, -1):
  downHeap(i, l_arr)

heapSize = l_arr
for i in range(l_arr - 1, 0, -1):
  heapSize -= 1
  words[0], words[heapSize] = words[heapSize], words[0]
  downHeap(0, heapSize)

print("After Sort: ", words)