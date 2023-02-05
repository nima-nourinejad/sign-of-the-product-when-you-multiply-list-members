def sp (l):
  sign=1
  for i in l:
    sign=i*sign
  if sign>0:
    sign=1
  elif sign<0:
    sign=-1
  return sign
