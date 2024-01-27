s = open('24_11241.txt').readline()

#ABYKMLLKJOBSDJKKLAl
#  YKMLLKJO S JKKL l
#['', 'YKMLLKJO', S, JKKL, L]
s = s.replace('A', ' ')
s = s.replace('B', ' ')
s = s.replace('C', ' ')
s = s.replace('D', ' ')

cepochki = s.split()
dlini_cepochek = [len(podstroka) for podstroka in cepochki]
print(max(dlini_cepochek))