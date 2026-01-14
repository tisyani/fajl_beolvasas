
with open('./file.txt', 'r', encoding='utf-8') as forrasfajl, \
        open('./adatok/file_masolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            print(sor.strip(), file=celfajl)
  