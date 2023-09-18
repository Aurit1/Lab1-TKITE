import wordfreq as wf
import sys,urllib.request

def main():
    stopwords = open(sys.argv[1], encoding='utf-8').read().splitlines()
    amount = int(sys.argv[3])
    lines = []
    if sys.argv[2].startswith('https://') or sys.argv[2].startswith('http://'):
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
        wf.printTopMost(wf.countWords(wf.tokenize(lines), stopwords), amount)
    else:
        lines = open(sys.argv[2], encoding='utf-8').readlines()
        wf.printTopMost(wf.countWords(wf.tokenize(lines), stopwords), amount)
main()