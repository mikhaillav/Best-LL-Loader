#Best LL-Loader by Fundi1330
#original LL-Loader by mikhaillav

import urllib.request
import os
import zipfile
import subprocess

pth=os.getcwd()

print('██████╗░███████╗░██████╗████████╗  ██╗░░░░░██╗░░░░░░░░░░░██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░')
print('██╔══██╗██╔════╝██╔════╝╚══██╔══╝  ██║░░░░░██║░░░░░░░░░░░██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗')
print('██████╦╝█████╗░░╚█████╗░░░░██║░░░  ██║░░░░░██║░░░░░█████╗██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝')
print('██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░  ██║░░░░░██║░░░░░╚════╝██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗')
print('██████╦╝███████╗██████╔╝░░░██║░░░  ███████╗███████╗░░░░░░███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║')
print('╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░  ╚══════╝╚══════╝░░░░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝\n')

print('write down which versions you want to use(use full name of version, example 1.2.4 and 1.17.34.02)')
LL = input('what version of LL you need?: ')
BDS = input('what version of BDS you need?: ')

print('Beginning downloading files...') 
bds = 'https://minecraft.azureedge.net/bin-win/bedrock-server-'+ BDS +'.zip'
ll = 'https://github.com/LiteLDev/LiteLoaderBDS/releases/download/'+ LL +'/LiteLoader-' + LL + '.zip'

urllib.request.urlretrieve(bds, 'bedrock_server.zip') 
urllib.request.urlretrieve(ll, 'LiteLoader.zip')
print('Success!')

print('Starting extract files')
fantasy_zip = zipfile.ZipFile(pth + '\\bedrock_server.zip')
fantasy_zip.extractall(pth)
fantasy_zip = zipfile.ZipFile(pth + '\\LiteLoader.zip')
fantasy_zip.extractall(pth)
fantasy_zip.close()

print('All file extracted! Starting generate server')

os.remove(pth + '\\LiteLoader.zip')
os.remove(pth + '\\bedrock_server.zip')

os.system(pth + '\\SymDB2.exe')

for i in range( 0, 0 ):
    subprocess.call(('SymDB2.exe', str(i)))

os.system(pth + '\\bedrock_server_mod.exe')
