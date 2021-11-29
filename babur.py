import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction

extension_info = {
    "title": "Babur Tool",
    "description": "made in tr/abzon :komutlar'i inceleyebilirsiniz.",
    "version": "0.4",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv)
ext.start()


on = False


def speech(message):
    global on

    text = message.packet.read_string()

    if text == ':sc':
        message.is_blocked = True
        if  on:
             ext.send_to_client('{in:YouArePlayingGame}{b:false}')
             on = False
             print('False')
        else:
             ext.send_to_client('{in:YouArePlayingGame}{b:true}')
             on = True
             print('True')


    if text == ':komutlar':
        message.is_blocked = True
        if  on:
             ext.send_to_client('{in:Whisper}{i:133}{s:"Su anlik kullanabiliceginiz komutlar= :sc (oyun modu) , :q (odadan çıkmak) , :s (spam atmak) , :se (sansur engelleyici) , :bc (babur chat (bosluklu yazmaya yarar.) ) not: ilk yazısınızda komutları iki kez deneyiniz. "}{i:0}{i:34}{i:0}{i:-1}{i:133}')
             on = False
             print('False')
        else:
             ext.send_to_client('{in:Whisper}{i:133}{s:"Su anlik kullanabiliceginiz komutlar= :sc (oyun modu) , :q (odadan çıkmak) , :s (spam atmak) , :se (sansur engelleyici) , :bc (babur chat (bosluklu yazmaya yarar.) ) not: ilk yazısınızda komutları iki kez deneyiniz. "}{i:0}{i:34}{i:0}{i:-1}{i:133}')
             on = True
             print('True')

    if text == ':q':
        message.is_blocked = True
        if on:
            ext.send_to_server('{out:Quit}')
            on = True
            print('False')
        else:
            ext.send_to_client('{out:Quit}')
            on = True
            print('True')


    if text == ':s':
        message.is_blocked = True
        if on:
            ext.send_to_server('{out:Chat}{s:"¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬"}{i:0}{i:0}')
            ext.send_to_server('{out:Chat}{s:"¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬"}{i:0}{i:0}')
            on = True
            print('True')
        else:
            ext.send_to_client('{out:Chat}{s:"¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬"}{i:0}{i:0}')
            on = True
            print('True')




    if text == ':hc':
        message.is_blocked = True
        if on:
            ext.send_to_server('{out:NewUserExperienceGetGifts}{i:1}{i:1}{i:1}')
            on = True
            print('True')
        else:
            ext.send_to_client('{out:NewUserExperienceGetGifts}{i:1}{i:1}{i:1}')
            on = True
            print('True')





ext.intercept(Direction.TO_SERVER, speech, 'Chat')

# {in:YouArePlayingGame}{b:true}

# {in:Whisper}{i:133}{s:" Su anlik kullanabiliceginiz komutlar: !sc (oyun modu) , !q (odadan cıkma) "}{i:0}{i:34}{i:0}{i:-1}{i:133}

#{in:Whisper}{i:133}{s:"anlik olarak odadan ciktiniz. "}{i:0}{i:34}{i:0}{i:-1}{i:133}

# {out:Quit}

#{out:Chat}{s:"¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬"}{i:0}{i:0}

#{out:CancelTyping}