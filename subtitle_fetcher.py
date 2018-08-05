import os
import sys
import hashlib
import urllib.request
import urllib.parse
from msvcrt import getch


extentions=["avi","mp4","mkv","mpg","mpeg","mov","rm","vob","wmv","flv","3gp"]
      
def get_video_format_files():
      my_list=[]
      root = os.getcwd()
      all_files = os.listdir()
      for file in all_files:
            if file.split('.')[-1] in extentions: 
                  my_list.append(os.path.join(root,file))
      return my_list


def check_sub(video):
      ext = video.split('.')[-1]
      video = video.replace(ext,"srt")
      if os.path.exists(video):
            return False
      else:
            return True


      
def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()


def download_sub(key,video):
      try:
            headers = { 'User-Agent' : 'SubDB/1.0 (Movie Subtitle Downloader/1.0; http://instagram.com\imurscherry' }
            url = "http://api.thesubdb.com/?action=download&hash="+key+"&language=en"
            
            request = urllib.request.Request(url, None, headers)
            response = urllib.request.urlopen(request).read()
            return response

      except:
            print("Subtitle {0} not found..! \n ".format(video))

      
def writeSubtitle(sub,video):
      
      print ("Subtile {0} was downloaded!\n".format(video))
      with open(video,'wb') as file:
            file.write(sub)
      return True

      
def main():
      print("\n  Welcome to Subtitle fetcher by Cherry(cherrynamburu@gmail.com) (instagram,Twitter: @imurscherry)\n")
      print("------------------------------------------------------------------------------------------------------------------------")
      print("Starting downloading Subtitle(s)...\n")
      success=0
      videos = get_video_format_files()
      for video in videos:
            ch = check_sub(video)
            if ch:
                  hash = get_hash(video)
                  ext = video.split('.')[-1]
                  sub_file = video.replace(ext,"srt")
                  sub = download_sub(hash,sub_file)
                  if sub != None:
                        writeSubtitle(sub,sub_file)           
                        success+=1

      print ("\nDownloaded {0} subtitles out of {1} Video files.\n".format(success,len(videos)))
      input('                                             ***Happy Watching***                                           ')


if __name__=='__main__':
      main()
