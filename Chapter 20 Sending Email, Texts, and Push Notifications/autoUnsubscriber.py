#Chapter 20 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter20.html

#this doesn't use Beautiful Soup like the assignment says because from my experiments the unsubscribe link doesn't always appear in the body
#instead this looks directly at the messageObj for each email and accesses the "List-Unsubscribe" key instead

import ezgmail, webbrowser
result_threads = ezgmail.search('unsubscribe', maxResults=50)


for result in result_threads:
    for message in result.messages:
        headers = message.messageObj['payload']['headers']
        for header in headers:
            if header['name'] == 'List-Unsubscribe':
                #skip youtube links, optional
                if 'youtube' in header['value']:
                    continue

                #header['value'] looks something like this so we split the string because it can appear in either order:
                #<mailto:unsubscribe@example.net?subject=unsubscribe>, <https://example.com/page/common/unsubscribe>
                unsubscribe = header['value'].split(",")

                for links in unsubscribe:
                    #ignore the mailto part of the unsubscribe methods
                    if 'mailto' in links:
                        continue
                    #remove the <> brackets
                    link = links.strip()[1:-1]
                    webbrowser.open(link)