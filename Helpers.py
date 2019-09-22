import os,sys
class Helpers(object):
    ''' 
    Input a list of which the first element is the helpers name
    Args are helper specific and start from the second element in de list

    'Me',          # Main router
    '_cml',        # [helper]-command line execution
    '_flickr',     # [helper]-flickr scrape with gallery-dl
    '_globx',      # [helper]-file globber collects file paths recursive
    '_mkd',        # [helper]-makes folders from a list and root path
    '_vdir',       # [helper]-command on libraries to get optional methods back
    '_GitGo',      # [helper]-pulls git repositories and more!!       
    'args',        # all input args
    'method',      # method selected
    'method_args', # methods argument list
    'no_action'    # if a empty command list is fed to the class

    Mininal Usage :      
                    from pathlib import Path
                    lib_file=Path('/content/lib/Helpers.py')
                    if not lib_file.is_file():
                        import os
                        os.system('mkdir -p /content/lib')
                        os.chdir('/content/lib')
                        os.system('wget https://raw.githubusercontent.com/bxck75/A1_Colabs/master/Helpers.py')
                        os.system('wget https://raw.githubusercontent.com/bxck75/A1_Colabs/master/myrepcol.py')
                        os.chdir('/content/')

                    from lib.Helpers import Helpers
                    from lib.myrepcol import reps
                    import seaborn as sns
                    import numpy as np
                    import pandas as pd

                    import google
                    from google.colab import drive
                    drive.mount('/content/drive', force_remount=True)

                    # Init
                    H=Helpers()
                    #  remove sample_data
                    H.Me(['cml','rm -r /content/sample_data'])

                    def get_gdrive_dataset(pack):
                        os.chdir('/content/drive/My Drive')
                        H.Me(['mkd',['dataset'],'/content/'])
                        H.Me(['cml','cp -r '+pack+' /content/dataset/'])
                        os.chdir('/content/dataset')
                        H.Me(['cml','unzip -q '+pack])
                        H.Me(['cml','rm -r '+pack])
                        os.chdir('/content')

                    def MethHelp(libs):
                        os_help=H.Me(['vdir',libs])
                        #make a list containing libs values of os_help
                        listOfLibs = [x[0] for x in os_help]
                        #make a list containing libs method values of os_help
                        listOfMethods= [x[1] for x in os_help]
                        # Create a zipped list of tuples from above lists
                        zippedList =  list(zip(listOfLibs, listOfMethods[0:5]))
                        zippedList
                        # request help on method from list
                        return zippedList

    Usage in colab :
                    from pathlib import Path
                    my_file=Path('/content/lib/Helpers.py')
                    if not my_file.is_file():
                        os.system('mkdir -p /content/lib')
                        os.system('cd /content/lib')
                        os.system('wget https://raw.githubusercontent.com/bxck75/A1_Colabs/master/Helpers.py')
                        os.system('wget https://raw.githubusercontent.com/bxck75/A1_Colabs/master/myrepcol.py')
                        os.system('cd /content/')

                    from lib.Helpers import Helpers
                    from lib.myrepcol import reps
                    # print(reps)

                    # list command snippets
                    vdir_self=        ['vdir']
                    vdir_helpers=         ['vdir',[Helpers]]
                    gal_extr=         ['cml','gallery-dl --list-extractors |grep ','flickr']
                    gal_help=         ['cml','gallery-dl -h']
                    fl_scrp=          ['flickr','abstract','/content/custom_images',5]
                    flickr_scrape=    ['flickr','portrait','/content/custom_images',10]
                    col_gdrive=       ['cml','cd "/content/drive/My Drive/Colab Notebooks"']
                    makefolders=      ['mkd',['custom_images'],'/content']
                    cmd_line=         ['cml','ls -l',True]
                    pip_install_all=  ['cml',"pip install -e . |grep 'succes'",True]
                    globber=          ['globx','/content/installed_repos','*.jpg']
                    gitgo=            ['inst_reps',['bxck75/pytorch-CycleGAN-and-pix2pix'],'/content/installed_repos',False,True]
                    gitgo_colab=      ['inst_reps',[reps[17],reps[18],reps[21]],'/content/installed_repos',False,True]
                    pip_install=      ['pip',['fnmatch','gallery-dl']]
                    pip_install_setup=['pip',["-e . |grep 'succes'"]]

                    # Init
                    H=Helpers()

                    # Calls
                    # show repositories in the reps list
                    print(str(len(reps)) + ' repos in the list')
                    for i in range(len(reps)-1):
                        print('[' + str(i) + '] '+reps[i])
                    # choose reps to install
                    gitgo[1]=[reps[17],reps[18],reps[21]]  
                    # see command
                    print(gitgo)
                    # install reps
                    H.Me(gitgo)

                    H.Me(globber)
                    H.Me(makefolders)

                    # remove sample dir
                    cmd_line[1],cmd_line[2] = 'rm -r /content/sample_data', False
                    H.Me(cmd_line)

                    H_list = H.Me(vdir_self) # have all helper functions in a list
                    print(H_list)
                    # Output from above
                    # ['Me', '_cml', '_flickr', '_globx', '_inst_reps', '_mkd', '_pip', '_vdir', 'args',
                    # 'custom_reps_setup', 'get_other_reps', 'method', 'method_args', 'no_action', 'root_path']

                    # flickrscrape
                    flir=H.Me(fl_scrp)
                    print(flir)

                    # change only the command in the snippet list
                    cmd_line[1],cmd_line[2]='ls -l',True
                    print(H.Me(cmd_line))
                    cmd_line[1]='rm -r sample_data'
                    H.Me(cmd_line)

                    # H=Helpers()
                    # H.repo_list=reps
                    # H.git_install_root='/content/installed_repos'
                    # H.GUSER = 'bxck75'
                    # H.path = H.git_install_root+'/'+H.GUSER
                    # H.get_other_reps()
    '''
    # Main method router
    def Me(self, args):
        os.system('sudo pip install gallery-dl')
        os.system('sudo pip install fnmatch')
        """Dispatch method"""
        # glob the args
        self.root_path='/content/'
#         print(self.root_path)
        self.args = args
        print('[Running-->]'+str(self.args))
        self.method= self.args[0]
        self.method_args= self.args[1:]
        method_args = self.method_args
        method_name = '_' + str(self.method)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: self.no_action())
        # Call the method as its returned
        return method()

    # HELPER FUNCTIONS 
    
    # Folder globber
    def _globx(self):
        import fnmatch,os
#         print(self.args)
        treeroot=self.method_args[0]
        pattern=self.method_args[1]
        Sheisterhaufen = []
        for base, dirs, files in os.walk(treeroot):
            goodfiles = fnmatch.filter(files, pattern)
            Sheisterhaufen.extend(os.path.join(base, f) for f in goodfiles)
        return Sheisterhaufen

    # CMD-LINE subprocess spawner
    def _cml(self): 
        Sheisterhaufen =[]
        cmd=self.method_args[0]
        if len(self.method_args) > 1:
            fi=self.method_args[1]
        else: # only False needs to be fed
            fi=True
        nepopso = os.popen(cmd)
        try: # Yeah try that u popo!!!
            for line in nepopso:
#                 line.encode("utf-8") Mightbe on older python
                if fi == True:
                    Sheisterhaufen.append(line.replace('\n',''))
        finally: # yeah finally done pooping!!!!!
            nepopso.close()
        return Sheisterhaufen
    
    # Flickr scraper
    # TODO: make this the main gallery-dl wrapper class and include it 
    # I can then us the API to it full sambal power and scrape 200+ galleries!!!
    def _flickr(self):
#         self.Me(['cml','pip install gallery-dl'])
        self.flickr_query = self.method_args[0]
        print(self.method_args)
        self.flickr_dest = self.method_args[1]
        self.flickr_qty = int(self.method_args[2])
        if isinstance(self.flickr_query, list):
            for s in self.flickr_query:
                keyword=s.replace(' ', '+')
                self.Me(['cml','gallery-dl --range 1-'+str(self.flickr_qty)+' -d '+self.flickr_dest+' https://flickr.com/search/?text='+keyword])
        else: 
            keyword=str(self.flickr_query.replace(' ', '+'))
            self.Me(['cml','gallery-dl --range 1-'+str(self.flickr_qty)+' -d '+self.flickr_dest+' https://flickr.com/search/?text='+keyword])
    
    # Method discloser
    def _vdir(self):
        if len(self.method_args)==0:
            return [x for x in dir(self) if not x.startswith('__')]
        else:
            if isinstance(self.method_args[0], list):
                elem=[]
                for m in self.method_args[0]:
                    elem.append([m.__name__,[x for x in dir(m) if not x.startswith('__')]])
                return elem 
            else:   
                return [x for x in dir(self.method_args[0]) if not x.startswith('__')]
    
    # Pip installer
    def _pip(self):
        import os
        print()
        self.pip_install_list = self.method_args[0]
        
        if isinstance(self.pip_install_list, list):
            spaced_list=''
            for s in self.pip_install_list:
                spaced_list += str( s + ' ' )
            # install the space separated list
            print('Installing ' + spaced_list)
            self.Me(['cml','pip install ' + spaced_list])
        else: 
            # install the single pip lib
            print('Installing ' + self.pip_install_list)
            self.Me(['cml','pip install ' + self.pip_install_list])
            
    # Folder spawner
    def _mkd(self):
        import os
        if isinstance(self.method_args[0], list):
            for x in self.method_args[0]:
                os.makedirs(self.method_args[1] + '/' + str(x), exist_ok = True)
        else:
            os.makedirs(self.method_args[1]+'/'+self.method_args[0], exist_ok = True)
            
    # Pull all selected reps  
    def _inst_reps(self):
        
        self.repo_list=self.method_args[0]      
        self.git_install_root=self.method_args[1]
        self.sub_repos=self.method_args[2]
        self.chadir=self.method_args[3]
        self.Me(['cml','mkdir -p '+self.git_install_root])
#         print(self.git_install_root)
        for rep in self.repo_list:
            self.rep=rep.split('/')
            # change folder check
            if self.chadir == True:
                #Switch to path
                os.chdir(self.git_install_root)
                # pull the git repo
                self.Me(['cml','git clone https://github.com/'+self.rep[0]+'/'+self.rep[1]+'.git'])
                # Set the return value for rep rootpath
                self.path=self.git_install_root+self.rep[1]
        # show imported files
        self.Me(['cml','ls ' +self.path])
        # run custom setups and get other reps
        self.custom_reps_setup()
#         if self.sub_repos == True:
#             self.get_other_reps()
            
        def __repr__(self):
            return self.path
        
    # get GPU Capabilities    
    def _get_gpu(self):
    #     check gpu
        import tensorflow as tf
        tf.test.gpu_device_name()
        self.Me(['cml','ln -sf /opt/bin/nvidia-smi /usr/bin/nvidia-smi'])
        self.Me(['cml','pip install gputil'])
        self.Me(['cml','pip install psutil'])
        self.Me(['cml','pip install humanize'])
        import psutil
        import humanize
        import os
        import GPUtil as GPU
        GPUs = GPU.getGPUs()
        # XXX: only one GPU on Colab and isn’t guaranteed
        gpu = GPUs[0]
        def printm():
         process = psutil.Process(os.getpid())
         print("Gen RAM Free: " + humanize.naturalsize( psutil.virtual_memory().available ), " I Proc size: " + humanize.naturalsize( process.memory_info().rss))
         print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))
        printm()






        
    #--repository required dependancies setup
    def custom_reps_setup(self):
        # custom stuff for CartoonGAN-tensorflow and keras-team/keras-contrib
        if 'keras-team/keras-contrib' in self.repo_list:
            os.chdir(self.path+'/keras-contrib')
            self.Me(['cml','python convert_to_tf_keras.py'])
            self.Me(['cml','USE_TF_KERAS=1'])
            self.Me(['cml','python setup.py install'])
            import tensorflow as tf
            tf.__version__     
        # custom setup stuff for gallery-dl repo
        if 'mikf/gallery-dl' in self.repo_list:
            os.chdir(self.git_install_root+'/gallery-dl')
            self.Me(['cml',"pip install -e . |grep 'succes'",True])
        # custom setup stuff for youtube-dl repo
        if 'ytdl-org/youtube-dl' in self.repo_list:
            os.chdir(self.git_install_root+'/youtube-dl') 
            self.Me(['cml',"pip install -e . |grep 'succes'",True])      
        # switch backt to root
        os.chdir(self.git_install_root)   

        
    #   --grab the username if a repos is installed
    #   --generate a txt file of all other reps of the user    
    def get_other_reps(self):          
        for r in self.repo_list:
            self.GitUsers=[]
            self.sub_repo_list=[]
            self.GUSER=r.split('/')[0]
            self.repo_name=r.split('/')[1]
            self.GitUsers.append(self.GUSER)
            h=Helpers()

            CURL_CMD="curl https://api.github.com/users/{self.GUSER}/repos?per_page=100 | grep -o '"
            CURL_CMD+='git@[^"]*' + ' > '+self.git_install_root+'/info.txt'
            result=self.Me(['cml',CURL_CMD])
            print(result)
            self.Me(['cml','cat '+self.git_install_root+"/info.txt |awk -F ':' '{print $2}'|awk -F '.' '{print $1}' > "+self.path+"/"+self.GUSER+"_repositories.txt"])
            with open(self.git_install_root+'/info.txt','r') as f:
                for line in f:
                    cline=line.split(':')[1].split('.')[0]
                    self.sub_repo_list.append(cline),

        print(self.sub_repo_list)

    # END OF HELPER FUNCTIONS
  
    def no_action(self):
        return self._vdir()
    
    
    # # Install repo and import images
# Lets use the repo made by carpedm20, a tensorflow implementation to Dgans
# H.Me(['inst_reps',['sinanatra/DCGAN-Art-Tensorflow'], '/content/installed_repos', False, True])
# cd /content/installed_repos/DCGAN-Art-Tensorflow
# # install the necessary libraries
# !pip install tqdm
# !pip install -U -q PyDrive
# !pip install googledrivedownloader
# Import from your Google Drive your dataset -* never upload with the files.upload(), it crashes if file is too big*
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from google.colab import auth
# from oauth2client.client import GoogleCredentials
# # 1. Authenticate and create the PyDrive client.
# auth.authenticate_user()
# gauth = GoogleAuth()
# gauth.credentials = GoogleCredentials.get_application_default()
# drive = GoogleDrive(gauth)
# print("all right")
# # Import Dataset
# Some of the dataset i'm using, not sure they will work on other computers, just check or else upload a folder with the same img size and colors (RGB, not RGBA) to your drive. Make it a sharable link and copy the last part like this: drive.google.com/open?id=**1LWolfUnkoAwHnxmyOz3PnI1gWsQI-oUc**
# #link_name ="1XKrAkCV4dzVNegPk2tYJ2SxBsDATufnG" #flowers
# link_name ="1A3fVxHiH9OlGVIN5ciAixr8YEn3lBAdR" #naked
# #link_name = "1xuuqhbE0OH0SEPC-pymbnzoffYubkH6t" #portrait
# #link_name ="1nv7WmFpz6TPwerNG4srjz-COfVgpe2Sy" #calligraphy
# #link_name ="1yHSggsUgtW4OV6k6lfaJmJMdEwnMaCmU"
# #link_name="174dn8Ts6pyRwU1vNu0-0eNKZBEkbautj"
# #link_name ="1aPcBcuDt4fAKemSMwhLNiFgHC8-APRe4" # nurse
# create dirs to place dataset
# mkdir data
# mkdir data/naked
# #rm -R data
# import from drive and unzip the  file to *dest*
# dest ="/content/installed_repos/DCGAN-Art-Tensorflow/data/"+ link_name+".zip"
# print(dest)
# from google_drive_downloader import GoogleDriveDownloader as gdd
# gdd.download_file_from_google_drive(file_id=link_name,
#                                     dest_path=dest,
#                                     unzip=True)
    
 
    # check gpu
# import tensorflow as tf
# tf.test.gpu_device_name()
# !ln -sf /opt/bin/nvidia-smi /usr/bin/nvidia-smi
# !pip install gputil
# !pip install psutil
# !pip install humanize
# import psutil
# import humanize
# import os
# import GPUtil as GPU
# GPUs = GPU.getGPUs()
# # XXX: only one GPU on Colab and isn’t guaranteed
# gpu = GPUs[0]
# def printm():
#  process = psutil.Process(os.getpid())
#  print("Gen RAM Free: " + humanize.naturalsize( psutil.virtual_memory().available ), " I Proc size: " + humanize.naturalsize( process.memory_info().rss))
#  print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))
# printm()
    
    
    

# My original GitGoi class onwards
    
# # GitGo helper class
# class GitGo(object):
#     '''
#     * pulls git rep and shows files \
#     * returns root path for the repository \
#     * Function needs repository <user>/<repository name> combination\
#     * Switch chdir and define the rootpath for the repository\
#     * Use : GitGo(<list of reps to install>, sub_repos=<True/False, chdir=<True/False>, path=<root path>)\  
#     '''
#     def __init__(self,repos,sub_repos=False,chdir=True,path='/content/'):
#         self.sub_repo_list = []
#         self.GitUsers = []
#         self.sub_repos = sub_repos
#         self.repos = repos
#         self.chdir = chdir
#         self.path = path
#         self.H = Helpers()
#         print(dir(self.H))
#         os.makedirs(self.path, exist_ok = True)
#         if 'help' in self.repos:
#             self.help()
#         self.install_reps()

        
#     def help(self):
#         return "under construction"
    
#     #   -pull al selected reps  
#     def install_reps(self):    
#         for rep in self.repos:
#             self.rep=rep.split('/')
#             # change folder check
#             if self.chdir ==True:
#                 #Switch to path
#                 os.chdir(self.path)
#                 # pull the git repo
#                 import Helpers
#                 self.H=Helpers()
#                 self.H.Me(['cml','git clone https://github.com/'+self.rep[0]+'/'+self.rep[1]+'.git'])
#                 # Set the return value for rep rootpath
#                 self.PATH=self.path+self.rep[1]
#         # show imported files
#         self.H.Me(['cml','ls ' + root])
#         # run custom setups and get other reps
#         self.custom_reps_setup()
#         if self.sub_repos == True:
#             self.get_other_reps()

#     #   --repository required dependancies setup
#     def custom_reps_setup(self):
#         # custom stuff for CartoonGAN-tensorflow and keras-team/keras-contrib
#         if 'keras-team/keras-contrib' in self.repos:
#             os.chdir(self.path+'/keras-contrib')
#             self.H.Me(['cml','python convert_to_tf_keras.py'])
#             self.H.Me(['cml','USE_TF_KERAS=1'])
#             self.H.Me(['cml','python setup.py install'])
#             import tensorflow as tf
#             tf.__version__     
#         # custom setup stuff for gallery-dl repo
#         if 'mikf/gallery-dl' in self.repos:
#             os.chdir(root+'/gallery-dl')
#             self.H.Me(['cml',"pip install -e . |grep 'succes'",True])
#         # custom setup stuff for youtube-dl repo
#         if 'ytdl-org/youtube-dl' in self.repos:
#             os.chdir(root+'/youtube-dl') 
#             self.H.Me(['cml',"pip install -e . |grep 'succes'",True])      
#         # switch backt to root
#         os.chdir(self.path)

#     #   --grab the username if a repos is installed
#     #   --generate a txt file of all other reps of the user    
#     def get_other_reps(self):          
#         for r in self.repos:
#             self.GUSER=r.split('/')[0]
#             self.repo_name=r.split('/')[1]
#             self.GitUsers.append(self.GUSER)
#             h=Helpers()
#             CURL_CMD='git@[^"]*'+' > {root}/info.txt'
#             print(CURL_CMD)
#             CURL_CMD+='curl https://api.github.com/users/{self.GUSER}/repos?per_page=100 | grep -o ' # git@[^"]*' > {root}/info.txt
#             print(CURL_CMD)
#             exit
#             self.H.Me(['cml','cat '+root+"/info.txt |awk -F ':' '{print $2}'|awk -F '.' '{print $1}' > "+self.path+"/"+self.GUSER+"_repositories.txt"])
#             with open(root+'/info.txt','r') as f:
#                 for line in f:
#                     cline=line.split(':')[1].split('.')[0]
#                     self.sub_repo_list.append(cline),

#         print(self.sub_repo_list)

#     def __repr__(self):
#         return self.PATH
    
