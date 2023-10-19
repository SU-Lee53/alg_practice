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

# 1. MergeSort

def merge(start, mid, end):
	merged = []
	l, r = start, mid + 1
	while l <= mid and r <= end:
		if words[l] <= words[r]:
			merged.append(words[l])
			l += 1
		else:
			merged.append(words[r])
			r += 1

	if l <= mid:
		merged += words[l:mid+1]
		words[start:end+1] = merged
	else:
		words[start:r] = merged


def mergeSort(start, end):
	if start >= end: return

	mid = (start + end) // 2
	mergeSort(start, mid)
	mergeSort(mid+1, end)
	merge(start, mid, end)



l_arr = len(words)
mergeSort(0, l_arr-1)
print("After Sorted:", words)