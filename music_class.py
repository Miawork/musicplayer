import random
import pygame
#import the pygame module so we can use mp3

a=True
pygame.mixer.init()
class Music:
    
    def __init__(self,pl=[],n=''):
        self.__singletoloop=''
        self.__playlist=pl
        self.music_name=n
        self.__filename = ''
        self.__lyric = ''
        #insert all the songs to the list
        self.__playlist.append('年深几许.mp3')
        self.__playlist.append('不必回望.mp3')
        self.__playlist.append('你爱着的.mp3')
        self.__playlist.append('林下漏月光.mp3')
        self.__playlist.append('说情长.mp3')
        self.__playlist.append('船客与执灯人.mp3')

    def allsongs_name(self):
        global i
        for i in range(len(self.__playlist)):
            if self.__playlist[i]==self.music_name:
                return i
            else:
                pass

    def get_playlist(self):
        #the playlist will be showed on the shell
        #this is the fastest funtion in this program
        print(set(self.__playlist))

    def play_music(self):
        #test if there is a song displaying
        #or play the list as start
        if pygame.mixer.music.get_busy() == 1:
            pygame.mixer.music.unpause()
        else:
            self.listtoloop_music()

    def pause_music(self):
        #pause the music
        pygame.mixer.music.pause()
     
    def stop_music(self):
        #stop the music
        pygame.mixer.music.stop()

    def next_music(self):
        if self.music_name==self.__playlist[-1]:
            pygame.mixer.music.load(self.__playlist[0])
            self.music_nameself.__playlist[0]
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load(self.__playlist[self.allsongs_name()+1])
            self.music_name=self.__playlist[self.allsongs_name()+1]
            pygame.mixer.music.play()

    def previous_music(self):
        #play previous song
        #if the first song is playing, play the last one instead
        if self.music_name==self.__playlist[0]:
            pygame.mixer.music.load(self.__playlist[-1])
            self.music_name=self.__playlist[-1]
            pygame.mixer.music.play()

        else:
            pygame.mixer.music.load(self.__playlist[self.allsongs_name()-1])
            self.music_name=self.__playlist[self.allsongs_name()-1]
            pygame.mixer.music.play()

    def listtoloop_music(self,list_num=0):
        #play songs follow the list 
        if list_num<len(self.__playlist):
            list_num+=1
            if list_num==len(self.__playlist):
                list_num=0
#should be while here
#python was loading for ten minutes which is too ling
        pygame.mixer.music.load(self.__playlist[list_num])
        self.music_name=self.__playlist[list_num]
        pygame.mixer.music.play()
        
    def singletoloop_music(self,single_n=''):
        #the methonds to play one song all the time
        self.__playlist=[]
        #to input the name of song
        #pls add .mp3 in the end
        single_n=input('The filename of song for single loop:')
        self.__playlist.append(single_n)
        self.music_name=single_n
        #should be while here
        #python was loading for ten minutes which is too ling
        pygame.mixer.music.load(self.__playlist[0])
        self.music_name=self.__playlist[0]
        pygame.mixer.music.play()

    def playatrandom_music(self):
        #play the song randomly
        self.len=len(self.__playlist)
        ran=random.randint(0,self.len)
        #get a random number
        pygame.mixer.music.load(self.__playlist[ran])
        self.music_name=self.__playlist[ran]
        pygame.mixer.music.play()

    #to get the name of lyric file
    def set_filename(self,f):
        self.__filename = f

    def read_file(self):
        #to read the lyric file
        if self.__filename != '':
            try:
                f = open(self.__filename, 'r')
                self.__lyric = f.read()
                f.close()
            except:
                self.__lyric = 'Waiting for the supplement'

    def save_lyric(self):
        if self.__filname != '':
            f = open(self.__filname, 'w')
            f.write(self.__lyric)
            f.close()

    def get_lyric(self):
        #get the text
        return self.__lyric
    

    
    
