#!/usr/bin/env python

from PIL import Image
from PIL.ExifTags import TAGS
import os

def get_exif(im):
  ret  = {}
  exif = im._getexif()
  
  if not exif:
    print(os.path.basename(fn) + ' has no exif and skipped.')
    return ret
    
  for tag, value in exif.items():
    decoded = TAGS.get(tag, tag)
    ret[decoded] = value
	
  return ret


if __name__ == '__main__':
  import sys, glob
  
  if len(sys.argv) is not 2:
    print 'Usage: $ python %s dir_name' % sys.argv[0]
    quit()
  
  dir = sys.argv[1]
  
  # make a list of already processed photos
  skip = [f[:-10] for f in glob.glob(os.path.join(dir, '*.jpg'))]
  
  for fn in glob.glob(os.path.join(dir, '*.JPG')):
    name, ext = os.path.splitext(fn)
    
    if name in skip:
      print(name + ' is already processed and skipped.')
      continue
    
    print('processing ' + fn + '...'),
    im   = Image.open(fn)
    exif = get_exif(im)
    if len(exif) is not 0:
      if exif['Orientation'] is 1:
        im = im.resize((600, 450), Image.ANTIALIAS)
      elif exif['Orientation'] is 3:
        im = im.rotate(180).resize((600, 450), Image.ANTIALIAS)
      elif exif['Orientation'] is 6:
        im = im.rotate(-90).resize((600, 800), Image.ANTIALIAS)
      
      out = name + "_small" + ext.lower()
      im.save(out, quality=100)
    print('finished.')    