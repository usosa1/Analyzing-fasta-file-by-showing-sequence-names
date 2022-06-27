def pick_seq_name(file_path):
    f=open(file_path)
    lines = f.readlines()
    for line in lines:
       if line[0] == ">":
          seqName = line[:-1]
          print(seqName)

print(pick_seq_name('MultiSeq.Afasta'))
