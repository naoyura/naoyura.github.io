#!/usr/bin/env python

if __name__ == '__main__':
  import os, sys, glob
  
  if len(sys.argv) is not 5:
    print 'Usage: $ python %s dir_name from_num to_num' % sys.argv[0]
    quit()
  
  dir         = sys.argv[1]
  from_num    = int(sys.argv[2])
  to_num      = int(sys.argv[3])
  gallery_num = sys.argv[4]
  
  # collect filenames
  lst = []
  for fn in glob.glob(os.path.join(dir, '*_thumb.jpg')):
    num = int(os.path.basename(fn)[4:8])
    if from_num <= num and num <= to_num:
      lst.append(fn)
  
  # fancybox gallery output
  print('<div class="gallery">')
  for im in lst:
    thumb = im[1:]
    orig  = thumb.replace('thumb', 'small')
    print('\t<a rel="gallery%s" href="http://naoyura.github.io/photos%s" class="fancybox"><img src="http://naoyura.github.io/photos%s"></a>' % (gallery_num, orig, thumb))
  print('\t<div class="clear"></div>')
  print('</div>')