def hamming_distance(s1,s2):
	cnt=0
	for i in range(len(s1)):
		if(s1[i]!=s2[i]):
			cnt+=1
	return cnt
	

def frequent_words(s,n):
	words=[]
	cnt=0
	for i in range(len(s)-n):
		c=s.count(s[i:i+n])
		if(c>cnt):
			words=[]
			words.append(s[i:i+n])
			cnt=c
		elif(c==cnt and s[i:i+n] not in words):
			words.append(s[i:i+n])
	return words
		
def pattern_matching(s,pat):
	match=[]
	ln=0
	while(s.find(pat) != -1):
		i = s.find(pat)
		match.append(i+ln)
		ln=ln+i+2
		s=s[i+2:]
	return match
	

def patterncount(s,pat):
	cnt=0
	while(s.find(pat) != -1):
		i = s.find(pat)
		s=s[i+1:]
		cnt+=1
	return cnt

