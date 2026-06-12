#Chapter 20 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter20.html

import ezgmail, webbrowser, time, subprocess, re
from pathlib import Path
result_threads = ezgmail.search('.torrent')

#use a simple shared secret since emails can be spoofed
with open('emailpassword.txt') as f:
    emailpassword = f.read().strip()

for result in result_threads:
    for message in result.messages:
        executed = False
        body = message.body

        #verify shared secret is in the email before executing
        if emailpassword not in body:
            continue

        #grab the URLs
        links = re.findall(r"https?://\S+", body)
        for link in links:     
            if ".torrent" in link:
                print(link)
                torrent_name = link.split("/")[-1]
                download_directory = Path.home() / 'Downloads' / torrent_name

                #opens the URL link
                #this code is configured to use a direct download link to download the torrent to the user's download folder
                webbrowser.open(link)
                time.sleep(5)
                try:
                    #open torrent program to download
                    qbProcess = subprocess.Popen(['C:\\Program Files\\qBittorrent\\qbittorrent.exe', str(download_directory)])
                    
                    #torrent program is set up to automatically close when the download finishes
                    qbProcess.wait()
                    print(f'Download for "{torrent_name}" has finished.')
                    executed = True
                except Exception as exc:
                    with open('error.txt', 'a') as f:
                        f.write(f'Error: {exc}\n')
                        
        #delete the email so that it doesn't download the same torrent file again
        if executed:
            message.trash()
