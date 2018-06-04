from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse

line = LINE("EtVBwKukKwVjrFofHLw0.iBuGmRcpaRydqClemgvK8a.AWx9LowE+619a+7Vov2Jjhurz+pw5D2zbPrb2tuRi5I=")
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

ki = LINE("EtXbgMCoppveS7O4i01e.cfU11NWrEakjPSDwvX5qpG.5i2Ns/ZHfHnBXb5u+J+GOJT+fV64KMlv7Tpa/Pqm8iw=")
ki.log("Auth Token : " + str(ki.authToken))
ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

kk = LINE("Ety0rcJrVcvHSCy3369a.1Im09gSpgb9PVQ/agRphwG.0oXJCcdddaJMDFRjRF47D52/UFDCy9hMA3C9n+OlyP0=")
kk.log("Auth Token : " + str(kk.authToken))
kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

kc = LINE("EtFkwCYUQXm3byrsPc05.H0beIntFRNUzLDz1Y+DHLq.eUStXhrSdsGWv2k4Oflj4PkmeBquoDglSF1zLzSWp3A=")
kc.log("Auth Token : " + str(kc.authToken))
kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

ks = LINE("Et62dPrZdq5YJqomu808.NyA+PG8TJV88Pn6FcTZmsa.b4SJM+AG8cbenLrRgU4pgYiJbCR2hucdI965HiYhcb4=")
ks.log("Auth Token : " + str(ks.authToken))
ks.log("Timeline Token : " + str(ks.tl.channelAccessToken))

cl = line
oepoll = OEPoll(cl)
All = [cl,ki,kk,kc,ks]
mid = cl.profile.mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
RABots = [mid,Amid,Bmid,Cmid,Dmid]
RASuper = ["Mid Kamu"]
RAFamily = RASuper + RABots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

def bot(op):
    try:
        if op.type == 5:
            if Setmain["RAautoadd"] == True:
                cl.sendMessageWithMention(op.param1, op.param1,"Hai","\nsalam kenal ya\n\n{}".format(str(Setmain["RAmessage"])))
                
        if op.type == 22:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    cl.leaveRoom(op.param1)
                    ki.leaveRoom(op.param1)
                    kk.leaveRoom(op.param1) 
                    kc.leaveRoom(op.param1) 
                    ks.leaveRoom(op.param1) 
                    
        # Jika tidak bisa autojoin, silahkan cek letter sealing akun bot di setting -> privasi
        # udah dites pakai akun bot yg sudah berteman & letter sealing dinonaktifkan
        if op.type == 13:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            ra = cl.getGroup(op.param1)
                            cl.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ra = cl.getGroup(op.param1)
                            cl.sendMessageWithMention(op.param1, ra.creator.mid,"hallo","\nsalken group creator...")
                            
            if Amid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = ki.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            ki.acceptGroupInvitation(op.param1)
                            ra = ki.getGroup(op.param1)
                            ki.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            ki.leaveGroup(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                            ra = ki.getGroup(op.param1)
                            ki.sendMessageWithMention(op.param1, ra.creator.mid,"hallo","\nsalken group creator...")
                            
            if Bmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = kk.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            kk.acceptGroupInvitation(op.param1)
                            ra = kk.getGroup(op.param1)
                            kk.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            kk.leaveGroup(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                            ra = kk.getGroup(op.param1)
                            kk.sendMessageWithMention(op.param1, ra.creator.mid,"hallo","\nsalken group creator...")
                            
            if Cmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = kc.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            kc.acceptGroupInvitation(op.param1)
                            ra = kc.getGroup(op.param1)
                            kc.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            kc.leaveGroup(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                            ra = kc.getGroup(op.param1)
                            kc.sendMessageWithMention(op.param1, ra.creator.mid,"hallo","\nsalken group creator...")
                            
            if Dmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = ks.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            ks.acceptGroupInvitation(op.param1)
                            ra = ks.getGroup(op.param1)
                            ks.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            ks.leaveGroup(op.param1)
                        else:
                            ks.acceptGroupInvitation(op.param1)
                            ra = ks.getGroup(op.param1)
                            ks.sendMessageWithMention(op.param1, ra.creator.mid,"hallo","\nsalken group creator...")
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            cl.reissueGroupTicket(op.param1)
                                            X = cl.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            cl.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ki.reissueGroupTicket(op.param1)
                                                X = ki.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass                            
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    Setmain["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in Setmain["blacklist"]:
                        	kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in Setmain["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in Setmain["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in Setmain["blacklist"]:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
      

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    Setmain["blacklist"][op.param2] = True
                    random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    Setmain["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in Setmain["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in Setmain["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in Setmain["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in Setmain["blacklist"]:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in Setmain["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in Setmain["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    Setmain["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    Setmain["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    Setmain["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    Setmain["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    Setmain["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    Setmain["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                pass    
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass                            
        if op.type == 46:
            if op.param2 in RABots:
                cl.removeAllMessages()
                ki.removeAllMessages()
                kk.removeAllMessages()
                kc.removeAllMessages()
                ks.removeAllMessages() 
                
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
                    if Setmain["RAautoscan"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["mid"])
                        
                elif msg.contentType == 0:
                    if Setmain["RAautoread"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                        ks.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:
                        
            #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "menu":
                            md = "Anarchy Menu\n\n"
                            md += "[01] .cek「@」\n"
                            md += "[02] .gid\n"
                            md += "[03] .yid\n"
                            md += "[04] .me\n"
                            md += "[05] .spbot\n"
                            md += "[06] .pengaturan\n"
                            md += "[07] .restart\n"
                            md += "[08] .removechat\n"
                            md += "[09] .cekmid 「on/off」\n"
                            md += "[10] .autoread 「on/off」\n"
                            md += "[11] .join\n"
                            md += "[12] .bye\n"
                            md += "[13] .listbl\n"
                            md += "[14] .kick「@」\n"
                            cl.sendText(msg.to, md)
                            
                        elif text.lower() == ".pengaturan":
                            if msg._from in RASuper:
                                md = "Anarchy Settings\n\n"
                                if Setmain["RAautoscan"] == True: md+="✅ Cekmid\n"
                                else: md+="❎ Cekmid\n"
                                if Setmain["RAautoread"] == True: md+="✅ Autoread\n"
                                else: md+="❎ Autoread\n"
                                cl.sendText(msg.to, md)
                                
            #---------------------- On/Off Command -------------------# 
            
                        elif text.lower() == ".autoread on":
                            if msg._from in RASuper:
                                if Setmain["RAautoread"] == False:
                                    Setmain["RAautoread"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".autoread off":
                            if msg._from in RASuper:
                                if Setmain["RAautoread"] == True:
                                    Setmain["RAautoread"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")
                                    
                        elif text.lower() == ".cekmid on":
                            if msg._from in RASuper:
                                if Setmain["RAautoscan"] == False:
                                    Setmain["RAautoscan"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Cekmid diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".cekmid off":
                            if msg._from in RASuper:
                                if Setmain["RAautoscan"] == True:
                                    Setmain["RAautoscan"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Cekmid dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")            
                            
            #---------------- Fungsi Command ------------------#
            
                        elif ".cek" in text.lower():
                            key = eval(msg.contentMetadata["MENTION"])
                            keys = key["MENTIONEES"][0]["M"]
                            ra = cl.getContact(keys)
                            try:
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/{}".format(str(ra.pictureStatus)))
                                cl.sendMessageWithMention(msg.to,ra.mid,"[Nama]\n","\n\n[Bio]\n{}".format(str(ra.statusMessage)))
                            except:
                                pass
                            
                        elif text.lower() == ".gid":
                            cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            cl.sendText(msg.to,msg.to)
                            
                        elif text.lower() == ".yid":
                            cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            cl.sendText(msg.to,msg._from)
                        
                        elif text.lower() == ".me":
                            cl.sendMessageWithMention(msg.to,msg._from,"Hay","\nsilahkan ketik menu untuk melihat command")
                            
                        elif text.lower() == ".spbot":
                            start = time.time()
                            cl.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start
                            cl.sendText(msg.to, "%s " % (elapsed_time))
                            
                            start2 = time.time()
                            ki.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start2
                            ki.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start3 = time.time()
                            kk.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start3
                            kk.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start4 = time.time()
                            kc.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start4
                            kc.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start5 = time.time()
                            ks.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start5
                            ks.sendText(msg.to, "%s" % (elapsed_time))
                                
                        elif text.lower() == ".restart":
                            if msg._from in RASuper:
                                cl.sendMessageWithMention(msg.to,msg._from,"","Tunggu Sebentar..")
                                python3 = sys.executable
                                os.execl(python3, python3, *sys.argv)
                                
                        elif text.lower() == ".removechat":
                            if msg._from in RASuper:
                                try:
                                    cl.removeAllMessages(op.param2)
                                    ki.removeAllMessages(op.param2)
                                    kk.removeAllMessages(op.param2)
                                    kc.removeAllMessages(op.param2)
                                    ks.removeAllMessages(op.param2)
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Chat bersih...")
                                except:
                                    pass        
                            
                        elif text.lower() == ".join":
                            if msg._from in RASuper:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                G.preventedJoinByTicket(G)
                                cl.updateGroup(G)
                        
                        elif text.lower() == ".bye":
                            if msg._from in RASuper:
                                ra = cl.getGroup(msg.to)
                                cl.sendMessageWithMention(msg.to,ra.creator.mid,"Maaf","\naku keluar dulu ya..")
                                cl.leaveGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ks.leaveGroup(msg.to)
                                
                        elif text.lower() == ".listbl":
                            if msg._from in RASuper:
                                if Setmain["RAblacklist"] == {}:
                                    cl.sendMessageWithMention(msg.to, msg._from,"Maaf","\nblacklist kosong")
                                else:
                                    no = 0
                                    hasil = "User\n"
                                    for a in cl.getContacts(Setmain["RAblacklist"]):
                                        no += 1
                                        hasil += "\n" + str(no) + ". " + str(a.displayName)
                                    hasil += "\n\nTotal {} blacklist".format(str(len(cl.getContacts(Setmain["RAblacklist"]))))
                                    cl.sendText(msg.to,hasil)
                                    
                        elif ".kick" in text.lower():
                            if msg._from in RASuper:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in RAFamily:
                                        pass
                                    else:
                                        try:
                                            cl.sendMessageWithMention(msg.to,target,"Maaf","aku kick")
                                            klist = [ki,kk,kc,ks]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                        except:
                                            pass        
                                
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in RASuper:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["RAautojoin"] == True:
                                        ra = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ki.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kk.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kc.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ks.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
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
