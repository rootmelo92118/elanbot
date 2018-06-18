from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse

line = LINE()
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))


cl = line
oepoll = OEPoll(cl)
All = [cl]
mid = cl.profile.mid
RASuper = ["u7537bd0d2a8380e1b3a0b1852a6bbbda","u640fc4e52553be8a0a55394712a52296","u9ab020b116f35afbdb3398f2bfe247c5","u8b206423cd23b08a2c233f02582f9c8a","u90ca582842fdd187224f3d61b8f0eba6","u8d59223cc63fe9167f33d5499cef78ec"]
RAStaff = ["ua1b1326288657deb35461cce7f28a2d5","u1de2fe12c2814774acbe099ea030c01f"]
RAFa = RASuper + RAStaff
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot) 

def bot(op):
    try:
        if op.type == 5:
            if Setmain["autoadd"] == True:
                cl.sendMessageWithMention(op.param1, op.param1,"Hai","\nsalam kenal ya\n\n{}".format(str(Setmain["RAmessage"])))
                

        if op.type == 13:
            if mid in op.param3:
              if op.param2 in RASuper:                    
                if Setmain["autojoin"] == True:                 
                    cl.acceptGroupInvitation(op.param1)

        if op.type == 11:
           if Setmain["protectqr"] == True:
               if op.param2 not in RAFa:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
                   Setmain["blacklist"][op.param2] = True
        if op.type == 13:
           if Setmain["protectguest"] == True:
               if op.param2 not in RAFa:
                  cl.cancelGroupInvitation(op.param1,[op.param3])
                  cl.kickoutFromGroup(op.param1,[op.param2]) 
                  Setmain["blacklist"][op.param2] = True
        if op.type == 13:
            if op.param3 in Setmain["blacklist"]:
                cl.cancelGroupInvitation(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op,param2])
            else:
                pass                
        if op.type == 17:
            if op.param2 in Setmain["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
        if op.type == 32:
           if Setmain["cancel"] == True:
               if op.param2 not in RAFa:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  Setmain["blacklist"][op.param2] = True            
        if op.type == 19:
           if Setmain["protect"] == True:
               if op.param2 not in RASuper:
                  cl.kickoutFromGroup(op.param1,[op.param2]) 
                  Setmain["blacklist"][op.param2] = True                
        if op.type == 19:
           if op.param3 in RASuper:
              cl.kickoutFromGroup(op.param1,[op.param2])
              cl.inviteIntoGroup(op.param1,RASuper)
              Setmain["blacklist"][op.param2] = True
           else:
               pass
                    
        if op.type == 46:
            if op.param2 in mid:
                cl.removeAllMessages() 
        if op.type == 28:
           if Setmain["larangan"] == True:
               if op.param2 not in RASuper:
                  cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 19:
            if mid in op.param3:
               Setmain["blacklist"][op.param2] = True                
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                    
                if msg.contentType == 13:
                    if Setmain["autoscan"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["mid"])
                        
                elif msg.contentType == 0:
                    if Setmain["autoread"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:
                        
            #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "menux":
                          if msg._from in RASuper:                        
                              md = " 🔎²  αя вσтѕ 🔎²\n\n"
                              md += "🔎² .cek「@」\n"
                              md += "🔎² .gid\n"
                              md += "🔎² .yid\n"
                              md += "🔎² .me\n"                            
                              md += "🔎² .spbot\n"
                              md += "🔎² .pengaturan\n"
                              md += "🔎² .restart\n"
                              md += "🔎² .removechat\n"
                              md += "🔎² .cekmid 「on/off」\n"
                              md += "🔎² .autoread 「on/off」\n"
                              md += "🔎² .bye\n"
                              cl.sendText(msg.to, md)
                            
                        if text.lower() == "ar menux":
                          if msg._from in RASuper:                        
                              md = " 🔎²  αя вσтѕ 🔎²\n\n"
                              md += "🔎² .protect on/off\n"
                              md += "🔎² .qr on/of\n"
                              md += "🔎² .invite on/off\n"
                              md += "🔎² .larangan on/off\n"                            
                              md += "🔎² .hust\n"                            
                              md += "🔎² .spbot\n"
                              cl.sendText(msg.to, md)                            
                            
                        elif text.lower() == ".setx":
                            if msg._from in RASuper:
                                ginfo = cl.getGroup(msg.to)                               
                                md = "🔎² αя вσтѕ 🔎²\n\npengaturan di group\n " +str(ginfo.name) + "\n\n"
                                if Setmain["autoscan"] == True: md+="✅ cekmid\n"
                                else: md+="❎ cekmid\n"
                                if Setmain["autoread"] == True: md+="✅ autoread\n"
                                else: md+="❎ autoread\n"
                                if Setmain["protect"] == True: md+="✅ protect\n"
                                else: md+="❎ protect\n"
                                if Setmain["protectqr"] == True: md+="✅ qr\n"
                                else: md+="❎ qr\n"
                                if Setmain["protectguest"] == True: md+="✅ invite\n"
                                else: md+="❎ invite\n"
                                if Setmain["autojoin"] == True: md+="✅ autojoin\n"
                                else: md+="❎ autojoin\n" 
                                if Setmain["larangan"] == True: md+="✅ larangan\n"
                                else: md+="❎ larangan\n"                                     
                                cl.sendText(msg.to, md)
                                
            #---------------------- On/Off Command -------------------# 
            
                        elif text.lower() == ".autoread on":
                            if msg._from in RASuper:
                                if Setmain["autoread"] == False:
                                    Setmain["autoread"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".autoread off":
                            if msg._from in RASuper:
                                if Setmain["autoread"] == True:
                                    Setmain["autoread"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")

                        elif text.lower() == ".re on":
                            if msg._from in RASuper:
                                if Setmain["cancel"] == False:
                                    Setmain["cancel"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".re off":
                            if msg._from in RASuper:
                                if Setmain["cancel"] == True:
                                    Setmain["cancel"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","di nonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")
                                                
                        elif text.lower() == ".protect on":
                            if msg._from in RASuper:
                                if Setmain["protect"] == False:
                                    Setmain["protect"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","protect group diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".protect off":
                            if msg._from in RASuper:
                                if Setmain["protect"] == True:
                                    Setmain["protect"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","protect group dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","sudah off")

                        elif text.lower() == ".larangan on":
                            if msg._from in RASuper:
                                if Setmain["larangan"] == False:
                                    Setmain["larangan"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","larangan group diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".larangan off":
                            if msg._from in RASuper:
                                if Setmain["larangan"] == True:
                                    Setmain["larangan"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","larangan group dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","sudah off")                                    

                        elif text.lower() == ".join on":
                            if msg._from in RASuper:
                                if Setmain["autojoin"] == False:
                                    Setmain["autojoin"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","already on")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".join off":
                            if msg._from in RASuper:
                                if Setmain["autojoin"] == True:
                                    Setmain["autojoin"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","already off")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","sudah off")                                    
                                    
                                    
                        elif text.lower() == ".invite on":
                            if msg._from in RASuper:
                                if Setmain["protectguest"] == False:
                                    Setmain["protectguest"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","protect invite diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".invite off":
                            if msg._from in RASuper:
                                if Setmain["protectguest"] == True:
                                    Setmain["protectguest"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","protect invite dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","sudah off")                                    
                                    
            
                        elif text.lower() == ".qr on":
                            if msg._from in RASuper:
                                if Setmain["protectqr"] == False:
                                    Setmain["protectqr"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","protect Qr diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".qr off":
                            if msg._from in RASuper:
                                if Setmain["protectqr"] == True:
                                    Setmain["protectqr"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","protect Qr dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")                                   
                                    
                        elif text.lower() == ".cekmid on":
                            if msg._from in RASuper:
                                if Setmain["autoscan"] == False:
                                    Setmain["autoscan"] = True
                                    ginfo = cl.getGroup(msg.to)
                                    msgs = "cekmid diaktifkan\nDi Group  " +str(ginfo.name)
                                    cl.sendText(msg.to, msgs)                                    
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".cekmid off":
                            if msg._from in RASuper:
                                if Setmain["autoscan"] == True:
                                    Setmain["autoscan"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Cekmid dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")            
                            
            #---------------- Fungsi Command ------------------#
                        
                                                                       
                        elif ".cek1" in text.lower():
                            if msg._from in RASuper:                    
                                key = eval(msg.contentMetadata["MENTION"])
                                keys = key["MENTIONEES"][0]["M"]
                                ra = cl.getContact(keys)
                                try:
                                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/{}".format(str(ra.pictureStatus)))
                                    cl.sendMessageWithMention(msg.to,ra.mid,"[Nama]\n","\n\n[Bio]\n{}".format(str(ra.statusMessage)))
                                except:
                                    pass
                            
                        elif text.lower() == ".gid":
                            if msg._from in RASuper:                            
                                cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                                cl.sendText(msg.to,msg.to)
                            
                        elif text.lower() == ".yid":
                            if msg._from in RASuper:                            
                                cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                                cl.sendText(msg.to,msg._from)
                        
                        elif text.lower() == ".respon":
                            if msg._from in RASuper:                            
                                cl.sendMessageWithMention(msg.to,msg._from,"","\nsiap ")
                            
                        elif text.lower() == ".spbot":
                            if msg._from in RASuper:                            
                                start = time.time()
                                cl.sendText(msg.to, "eror...")
                                elapsed_time = time.time() - start
                                cl.sendText(msg.to, "%s " % (elapsed_time))
                          
                        elif text.lower() == ".restart":
                            if msg._from in RASuper:
                                cl.sendMessageWithMention(msg.to,msg._from,"","Tunggu Sebentar..")
                                python3 = sys.executable
                                os.execl(python3, python3, *sys.argv)
                                
                        elif text.lower() == ".removechat":
                            if msg._from in RASuper:
                                try:
                                    cl.removeAllMessages(op.param2)
                                    cl.sendMessageWithMention(msg.to,msg._from,"","chat bersih...")
                                except:
                                    pass        
                                                    
                        elif text.lower() == ".bye":
                            if msg._from in RASuper:
                                ra = cl.getGroup(msg.to)
                               # cl.sendMessageWithMention(msg.to,ra.creator.mid,"Maaf pemilik group","\naku keluar dulu ya..")
                                cl.leaveGroup(msg.to)
                        elif text.lower() ==".clearban":
                            if msg._from in RASuper:                                
                                Setmain["blacklist"] = {}
                                cl.sendMessageWithMention(msg.to,msg._from,"","blacklist di kosongkan.")                                 

                        elif text.lower() == ".listgroup1":
                            if msg._from in RASuper:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendText(msg.to,"╔══[ ℓιsт gяσυρ ]\n║\n"+ma+"║\n╚══[ тσтαℓ「"+str(len(gid))+"」gяσυρ ]")                                
                                
                        elif text.lower() == ".listbl1":
                            if msg._from in RASuper:
                                if Setmain["blacklist"] == {}:
                                    cl.sendMessageWithMention(msg.to, msg._from,"Maaf","blacklist kosong")
                                else:
                                    no = 0
                                    hasil = "🔎² αя вσтѕ 🔎²\n"
                                    for a in cl.getContacts(Setmain["blacklist"]):
                                        no += 1
                                        hasil += "\n" + str(no) + ". " + str(a.displayName)
                                    hasil += "\n\nтσтαℓ {} вℓα¢ℓιsт".format(str(len(cl.getContacts(Setmain["blacklist"]))))
                                    cl.sendText(msg.to,hasil)

                                    
                        elif ".hust1" in text.lower():
                            if msg._from in RASuper:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in RAFa:
                                        pass
                                    else:
                                        try:
                                           # cl.sendMessageWithMention(msg.to,target,"Maaf","aku kick")
                                            klist = [cl]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                        except:
                                            pass                                 
                        elif "kick @α я" in text.lower():
                            if Setmain["larangan"] == True:                            
                                cl.sendMessageWithMention(msg.to, msg._from,"wooiiii","mau kick bosku ya")
                                cl.kickoutFromGroup(msg.to, [msg._from])
                        elif "dor @α я" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooiii","mau kick bosku ya")
                                cl.kickoutFromGroup(msg.to, [msg._from])                            
                            
                        elif "!kick @α я" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooii","mau kick bosku ya")
                                cl.kickoutFromGroup(msg.to, [msg._from]) 
                            
                        elif ".kick @α я" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooii","mau kick bosku ya")
                                cl.kickoutFromGroup(msg.to, [msg._from])  
                        elif "!hust @α я" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau kick bosku ya")
                                cl.kickoutFromGroup(msg.to, [msg._from]) 
                        elif "kickal" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from])   
                        elif "kickall" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from]) 
                        elif ".kickal" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from]) 
                        elif "!kickal" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from]) 
                        elif ".hay" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from]) 
                        elif "!hai" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from]) 
                        elif "nuke" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from]) 
                        elif ".nuke" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")   
                        elif "!nuke" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")   
                        elif "kick" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")                                
                        elif "kibar" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from])  
                        elif "crash" in text.lower():
                            if Setmain["larangan"] == True:                             
                                cl.sendMessageWithMention(msg.to, msg._from,"wooyyyy","mau ngpin lu")
                                cl.kickoutFromGroup(msg.to, [msg._from])                             
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in RASuper:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["autojoin"] == True:
                                        ra = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
                                    else:    
                                        cl.sendMessageWithMention(msg.to,msg._from,"Maaf","\naktifkan auotojoin dulu")

    except Exception as error:
        print (error)
        
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
