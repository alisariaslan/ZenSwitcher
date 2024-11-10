# ________   _______ .__   __.         _______.____    __    ____  __  .___________.  ______  __    __   _______ .______      
#|       /  |   ____||  \ |  |        /       |\   \  /  \  /   / |  | |           | /      ||  |  |  | |   ____||   _  \     
#`---/  /   |  |__   |   \|  |       |   (----` \   \/    \/   /  |  | `---|  |----`|  ,----'|  |__|  | |  |__   |  |_)  |    
#   /  /    |   __|  |  . `  |        \   \      \            /   |  |     |  |     |  |     |   __   | |   __|  |      /     
#  /  /----.|  |____ |  |\   |    .----)   |      \    /\    /    |  |     |  |     |  `----.|  |  |  | |  |____ |  |\  \----.
# /________||_______||__| \__|    |_______/        \__/  \__/     |__|     |__|      \______||__|  |__| |_______|| _| `._____|
#                                                                                                                             

# Kütüphaneler
from pathlib import Path
from xml.dom import minidom
from datetime import datetime
import os
import platform
import xml.etree.ElementTree as ET
import uuid
import easygui

# Çevre değişkenleri ve uyarıların manipülasyonu
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Bazı temel değişkenler
appName = "Zen Switcher"
appVersion = 1
appVersionStr = "1.0.0"
mac = "Darwin"
win = "Windows"
git_path = "https://github.com/alisariaslan/ZenSwitcher"
root_folder_name = "ZenSwitcher"
projects_folder_name = "ZenProjects"
profiles_folder_name = "ZenProfiles"
commands_folder_name = "ZenCommands"
search_file_name = "search.txt"
replace_file_name = "replace.txt"
project_settings_file_name = "ProjectSettings.xml"
profile_settings_file_name = "ProfileSettings.xml"
home_path = Path.home()
root_folder = Path(home_path,root_folder_name)
projects_folder = Path(root_folder,projects_folder_name)
selected_project = None
selected_profile = None
depth = 0

# Tanıtım
ascii_art = f"""
 _______ _  _   ___        _ _      _            
|_  / __| \| | / __|_ __ _(_) |_ __| |_  ___ _ _ 
 / /| _|| .` | \__ \ V  V / |  _/ _| ' \/ -_) '_|
/___|___|_|\_| |___/\_/\_/|_|\__\__|_||_\___|_|       {appVersionStr}
                                                 
"""
print(ascii_art)
print("\nHoşgeldiniz. Bu mini-program projelerde hızlıca birden fazla profil değiştirmek için tasarlanmıştır.")
print(f"\nProfillerinizin kaydedileceği konum: {root_folder}")

# Komutları listeler
def ListAllCommands():
    print("\nGeçerli Komutlar:")
    print("\t* h/help: Mevcut kullanabileceğiniz komutları listeler.")
    print("\t* exit/stop/close: Programı sonlandırır.")
    print("\t* git/github: Programın kaynak kodunun ve eğitiminin bulunduğu adresi gösterir.")
    if depth == 0:
        print("\t* n/new: Yeni proje oluşturmak için kullanılır.")
        print("\t* l/list: Tüm projeleri listeler. Mevcut öğe varsa seçim yapılır.")
    elif depth == 1:
        print("\t* n/new: Yeni profil oluşturmak için kullanılır.")
        print("\t* l/list: Tüm profilleri listeler.")
        print("\t* c/cancel: Seçili projenin seçimini kaldırır.")
        print("\t* b/back: Seçili projenin seçimini kaldırır. Ve projeleri listeler.")

# Terminal ekranını temizler
def ClearTerminal():
    if platform.system() == win:
        os.system("cls")
    elif platform.system() == mac:
        os.system("clear")

# Derinliği sıfırlar
def BackToZeroDepth():
    global depth
    depth = 0
    print("\nMevcut proje seçimi iptal edildi.")

# Klasör seçimi
def SelectFolder():
    target_folder_select_title = "Hedef proje klasörünü seçin"
    target= easygui.diropenbox(target_folder_select_title)
    if target:
        print(f"\nHedef klasör seçimi başarılı: {target}")
    return target

# Dosya seçimi
def SelectFile():
    target_file_select_title = "Hedef dosya seçin"
    if platform.system() == win:
        target_file = easygui.fileopenbox(target_file_select_title)
    elif platform.system() == mac:
        target_file = easygui.fileopenbox(
            msg=target_file_select_title,
            filetypes=["*.txt", "*.py", "*.java", "*.c", "*.cpp", "*.cs", "*.html", "*.css",
            "*.js", "*.json", "*.xml", "*.yaml", "*.yml", "*.md", "*.ini",
            "*.php", "*.rb", "*.swift", "*.go", "*.r", "*.sh", "*.bat",
            "*.sql", "*.pl", "*.vb", "*.scala", "*.lua","*.csproj"]
        )
    if target_file:
        print(f"\nHedef dosya seçimi başarılı: {target_file}")
    return target_file

# Klasörleri oluştur
def CreateDefaults():
    root_folder.mkdir(exist_ok=True)
    projects_folder.mkdir(exist_ok=True)
    if not selected_project == None:
        selected_project_settings_file = selected_project / project_settings_file_name
        if not Path.exists(selected_project_settings_file):
            print(f"\nAçılacak olan seçim penceresini kullanarak bu projenin hedefleyeceği, hedef proje klasörünü seçin.\n")
            target_project_folder = SelectFolder()
            if not target_project_folder:
                print(f"\nHedef proje klasörü seçimi iptal edildiği için gerekli dosyalar {selected_project} klasörü altına oluşturulamadı!")
                return
            root = ET.Element("zen-project")
            ET.SubElement(root, "project-id").text = str(uuid.uuid4())
            ET.SubElement(root, "target-project-path").text = target_project_folder
            ET.SubElement(root, "creation-date").text = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            ET.SubElement(root, "compatible-version").text = f"{appVersionStr}"
            ET.SubElement(root, "search-tags-mode").text = "false"
            paths = ET.SubElement(root, "user-based-project-paths",)
            ET.SubElement(paths, "default").text="Bu alan daha sonraki sürümlerde kullanılacaktır"
            raw_xml = ET.tostring(root, encoding='utf-8')
            parsed_xml = minidom.parseString(raw_xml)
            pretty_xml = parsed_xml.toprettyxml(indent="  ")
            with open(selected_project_settings_file, 'w', encoding='utf-8') as f:
                f.write(pretty_xml)   
            selected_project_profiles_folder = selected_project / profiles_folder_name
            selected_project_commands_folder = selected_project / commands_folder_name
            selected_project_profiles_folder.mkdir(exist_ok=True)
            selected_project_commands_folder.mkdir(exist_ok=True)
            print(f"\nGerekli dosyalar {selected_project} altına oluşturuldu.")

# Proje klasörlerini listeleme
def ListProjects():
    global depth, selected_project
    projects = [item for item in projects_folder.iterdir() if item.is_dir()]
    folder_count = len(projects)
    if folder_count > 0:
        print(f"\nProjeler ({folder_count}):")
        for index, project in enumerate(projects, start=1):
            print(f"\t{index}. {project.name}")
        print(f"\tC. İptal")
        while True:
            selected_input = input("\nBir proje seçmek için numara girin: ").strip().lower()
            if selected_input == "c":
                print("\nSeçim iptal edildi.")
                break
            try:
                selected_index = int(selected_input)
                if 1 <= selected_index <= folder_count:
                    selected_project = projects[selected_index - 1]
                    print(f"\nSeçilen proje: {selected_project.name}")
                    CreateDefaults()
                    project_settings = selected_project / project_settings_file_name
                    if not Path.exists(project_settings):
                        break
                    try:
                        tree = ET.parse(project_settings)
                        root = tree.getroot()
                        cv = root.find("compatible-version")
                        if not cv.text == appVersionStr:
                            print(f"\nUyumsuz sürüm! {project_settings.name} adlı dosyanın sürümü kullandığınız uygulama sürümü ile uyuşmuyor.\nLütfen dosyalarınıza uygun sürüm kullanın. Bu önlem veri kayıplarını önlemek için alınmıştır.\nDosya konumu: {project_settings}")
                            break
                    except ET.ParseError:
                        print(f"\nOkuma hatası! {project_settings.name} adlı dosya okunamadı. Dosya içerisinde önemli bilgiler içeriyorsa kopyalayıp, projeyi yeniden oluşturun.\nDosya konumu: {project_settings}")
                        break
                    depth = 1
                    ListProfiles(selected_project)
                    break
                else: raise ValueError
            except ValueError:
                print("\nGeçersiz bir değer girdiniz. Lütfen tekrar deneyin.")
    else:
        print("\nGörünüşe göre hiç proje klasörünüz yok. Yeni projelerinizi 'n' komutu ile oluşturabilirsiniz.")

# Proje klasörlerini listeleme
def ListProfiles(project: Path):
    global selected_project, selected_profile
    profiles_folder = project/profiles_folder_name
    if not Path.exists(profiles_folder):
        print(f"\nKlasör bulunamadı! Profillerin listeleneceği klasöre ulaşılamadı. Konum: {profiles_folder}")
        return
    profiles = [item for item in profiles_folder.iterdir() if item.is_dir()]
    folder_count = len(profiles)
    if folder_count > 0:
        print(f"\n{project.name} - Profiller ({folder_count}):")
        for index, profile in enumerate(profiles, start=1):
            print(f"\t{index}. {profile.name}")
        print(f"\tB. Geri")
        print(f"\tC. İptal")
        while True:
            selected_input = input("\nBir profili uygulamak için numara girin: ").strip().lower()
            if selected_input == "b":
                print("\nGeri gidiliyor...")
                BackToZeroDepth()
                ListProjects()
                break
            elif selected_input == "c":
                print("\nSeçim iptal edildi.")
                break
            try:
                selected_index = int(selected_input)
                if 1 <= selected_index <= folder_count:
                    selected_profile = profiles[selected_index - 1]
                    ApplyProfile(selected_project, selected_profile)
                    break
                else: raise ValueError
            except ValueError:
                print("\nGeçersiz bir değer girdiniz. Lütfen tekrar deneyin.")
    else:
        print("\nGörünüşe göre hiç profiliniz yok. Yeni profilleri 'n' komutu ile oluşturabilirsiniz.")

# Platform bağımsız gui ile klasör açma
def OpenFolder(folder: Path):
     if platform.system() == mac:
            os.system(f"open {folder}")
     elif platform.system() == win:
            os.system(f"explorer {folder}")

# Yeni proje oluşturulacak yolu uygun platformda açar.
def NewProject():
        if not Path.exists(projects_folder):
            print(f"\nKlasör bulunamadı! Projelerin listeleneceği klasöre ulaşılamadı. Konum: {projects_folder}")
            return
        print("\nOluşturmak istediğiniz yeni projeleri klasörler halinde şimdi açılacak olan kök klasörünüze oluşturun.\nKlasör adları aynı zamanda proje adlarınız olacaktır.\nProjeleri oluşturduktan sonra, 'l' komutu ile tekrar listeleme yapıp projeler arasında seçim yapabilirsiniz." )
        OpenFolder(projects_folder)

# Yeni profil oluşturulacak yolu uygun platformda açar.
def NewProfile(project_profiles_root: Path):
        if not Path.exists(project_profiles_root):
            print(f"\nKlasör bulunamadı! Profillerin listeleneceği klasöre ulaşılamadı. Konum: {project_profiles_root}")
            return
        print("\nOluşturmak istediğiniz yeni profilleri klasörler halinde şimdi açılacak olan proje klasörünüze oluşturun.\nKlasör adları aynı zamanda profil adlarınız olacaktır.\nKlasörleri oluşturduktan sonra, 'l' komutu ile tekrar listeleme yapıp profiller arasında seçim yapabilirsiniz." )
        OpenFolder(project_profiles_root)

# Profil düzenleme
def EditProfile(profile_root: Path):
        if not Path.exists(profile_root):
            print(f"\nKlasör bulunamadı! Profile ait klasöre ulaşılamadı. Konum: {profile_root}")
            return
        print("\nProfili düzenlemek için lütfen oluşturulan dosyaları doldurun. Gerekli ayarlamaları yaptıktan sonra profili tekrar uygulayın." )
        OpenFolder(profile_root)

# Profil ana dosyasını oluştur
def NewProfileFile(project: Path, profile: Path):
    profile_file = profile / profile_settings_file_name
    print(f"\nAçılacak olan seçim penceresini kullanarak bu profilin hedefleyeceği, hedef dosyayı seçin.\n(Search edilip, replace atılacak dosya)\n")
    target_file = SelectFile()
    if not target_file:
        print(f"\nHedef dosya seçimi iptal edildiği için gerekli dosyalar {profile} klasörü altına oluşturulamadı!")
        return
    root = ET.Element("zen-profile")
    try:
        parent_tree = ET.parse(project/project_settings_file_name)
        parent_root = parent_tree.getroot()
        project_id = parent_root.find("project-id")
        if project_id is None or project_id.text is None:
            raise ET.ParseError
    except ET.ParseError:
        print(f"\nOkuma hatası! {project_settings_file_name} adlı dosya okunamadı. Dosya içerisinde önemli bilgiler içeriyorsa kopyalayıp, projeyi yeniden oluşturun.\nDosya konumu: {selected_project/project_settings_file_name}")
        return
    ET.SubElement(root, "project-id").text = f"{project_id.text}"
    ET.SubElement(root, "profile-id").text = str(uuid.uuid4())
    ET.SubElement(root, "target-profile-path").text = target_file
    ET.SubElement(root, "creation-date").text = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    ET.SubElement(root, "last-applied-date").text = ""
    ET.SubElement(root, "compatible-version").text = f"{appVersionStr}"
    ET.SubElement(root, "search-tags-mode").text = "parent"
    paths = ET.SubElement(root, "user-based-project-paths",)
    ET.SubElement(paths, "default").text="Bu alan daha sonraki sürümlerde kullanılacaktır"
    ET.SubElement(root, "search-file").text = f"{search_file_name}"
    ET.SubElement(root, "replace-file").text = f"{replace_file_name}"
    raw_xml = ET.tostring(root, encoding='utf-8')
    parsed_xml = minidom.parseString(raw_xml)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    with open(profile_file, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    search_file = profile / search_file_name
    with open(search_file, 'w', encoding='utf-8') as f:
        f.write("#Aramak istediğiniz metni aşağıya ekleyin. Varyasyonlarını alt alta ekleyin.\n#Birden fazla metin için ise arada mutlaka boş bir yeni satır olsun.")
    replace_file = profile / replace_file_name
    with open(replace_file, 'w', encoding='utf-8') as f:
        f.write("#Değiştirmek istediğiniz metni aşağıya ekleyin.\n#Arama dosyasındaki satır sırasına dikkat ederek ekleme işlemini gerçekleştirin.")
    print(f"\nGerekli dosyalar {profile} altına oluşturuldu.")
    EditProfile(profile)

def ReadSearchFile(profile: Path, file_name):
    try:
        with open(profile/file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        result = []
        current_item = None  # Geçerli öğe
        current_variations = []  # Geçerli öğenin varyasyonları
        for line in lines:
            line = line.strip()  # Başlangıç ve sonundaki boşlukları temizle
            if line.startswith('#'):  # Eğer satır # ile başlıyorsa, atla
                continue
            if line:  # Boş olmayan satırlarla işlem yap
                if current_item is None:
                    # Eğer geçerli öğe yoksa, bu satır yeni bir öğe olarak kabul edilir
                    current_item = line
                else:
                    # Eğer geçerli öğe varsa, bu satır bir varyasyon olarak kabul edilir
                    current_variations.append(line)
            else:
                # Boş satırla karşılaştığımızda, mevcut öğeyi kaydet
                if current_item:
                    result.append({'item': current_item, 'variations': current_variations})
                    current_item = None
                    current_variations = []
        if current_item:
            result.append({'item': current_item, 'variations': current_variations})
        return result
    except FileNotFoundError:
        print(f"{file_name} adlı dosya bulunamadı! Bulunması gereken dosya konumu: {profile/file_name}")
        return None

def ReadReplaceFile(profile: Path, file_name):
    try:
        with open(profile/file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        result = []
        for line in lines:
            line = line.strip()  # Remove leading/trailing spaces
            if line.startswith('#'):  # Eğer satır # ile başlıyorsa, atla
                continue
            if line:  # Only add non-empty lines to the result list
                result.append(line)
        return result
    except FileNotFoundError:
        print(f"{file_name} adlı dosya bulunamadı! Bulunması gereken dosya konumu: {profile/file_name}")
        return None

def ReplaceValues(profile,search_terms, replace_terms):
    try:
        tree = ET.parse(profile/profile_settings_file_name)
        root = tree.getroot()
        target_file = root.find("target-profile-path")
        if target_file is None or target_file.text is None:
            raise ET.ParseError
        target_file = Path(target_file.text.strip())
        if not Path.exists(target_file):
            raise FileNotFoundError
        with open(target_file, 'r', encoding='utf-8') as file:
            content = file.readlines()
        for index, line in enumerate(content):
            isReplacedAlready = False  # Her satır için işlem yapılmış mı kontrolü
            for term in search_terms:
                original = term['item']  # Orijinal terim
                variations = term['variations']  # Varyasyonlar
                if not isReplacedAlready and original in line:
                    line = line.replace(original, replace_terms[search_terms.index(term)], 1)  # İlk bulunanla değiştir
                    isReplacedAlready = True  # İşlem yapıldı olarak işaretle
                if not isReplacedAlready:  # Eğer orijinal terim bulunmadıysa
                    for variation in variations:
                        if variation in line:
                            line = line.replace(variation, replace_terms[search_terms.index(term)], 1)  # Varyasyonu da değiştir
                            isReplacedAlready = True  # İşlem yapıldı olarak işaretle
                            break  # İlk bulunan varyasyonu değiştirdikten sonra durdur
            content[index] = line
        with open(target_file, 'w', encoding='utf-8') as file:
            file.writelines(content)
        print(f"\nProfil başarıyla uygulandı. Değiştirilen dosya yolu: {target_file}\nIDE ortamınızı güncel değilse güncellemeyi unutmayın!")
        root.find("last-applied-date").text = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        tree.write(profile/profile_settings_file_name)
    except FileNotFoundError:
        print(f"\nHedef dosya bulunamadı: {target_file}")
    except ET.ParseError:
        print(f"\nOkuma hatası! {profile_settings_file_name} adlı dosya okunamadı. Dosya içerisinde önemli bilgiler içeriyorsa kopyalayıp, dosyayı yeniden oluşturun.\nDosya konumu: {profile/profile_settings_file_name}")

# Seçilen proje altındaki profili uygula.
def ApplyProfile(project: Path, profile: Path):
    print(f"\nProfil kontrol ediliyor... ({project.name} -> {profile.name})")
    profile_settings = profile/profile_settings_file_name
    if not Path(profile_settings).exists():
        print(f"\n{profile_settings.name} dosyası mevcut değil. İçerik oluşturuluyor...")
        NewProfileFile(project,profile)
        return
    try:
        tree = ET.parse(profile_settings)
        root = tree.getroot()
        cv = root.find("compatible-version")
        if not cv.text == appVersionStr:
            print(f"\nUyumsuz sürüm! {profile_settings.name} adlı dosyanın sürümü kullandığınız uygulama sürümü ile uyuşmuyor.\nLütfen dosyalarınıza uygun sürüm kullanın. Bu önlem veri kayıplarını önlemek için alınmıştır.\nDosya konumu: {profile_settings}")
            return
    except ET.ParseError:
        print(f"\nOkuma hatası! {profile_settings.name} adlı dosya okunamadı. Dosya içerisinde önemli bilgiler içeriyorsa kopyalayıp, projeyi yeniden oluşturun.\nDosya konumu: {profile_settings}")
        return
    print(f"\nProfil uygulanıyor... ({project.name} -> {profile.name})")
    search_terms = ReadSearchFile(selected_profile,search_file_name)
    replace_terms = ReadReplaceFile(selected_profile,replace_file_name)
    if (search_terms is None or replace_terms is None) or (len(search_terms) == 0 or len(replace_terms) == 0):
        print(f"\nProfil içerisindeki arama veya değişim dosyası boş gibi gözüküyor.\nLütfen kontrol edin. Profil konumu: {selected_profile}")
        return
    ReplaceValues(selected_profile,search_terms,replace_terms)

def ShowLastAppliedProfile():
    profiles_folder = selected_project / profiles_folder_name
    if not profiles_folder.exists() or not profiles_folder.is_dir():
        print(f"Profillerin bulunduğu klasör mevcut değil: Bulunması gereken konum: {profiles_folder}")
        return
    last_applied_profile = None
    last_applied_date = None

    for profile_folder in profiles_folder.iterdir():
        if profile_folder.is_dir():  # Check if it's a directory (a profile)
            profile_settings = profile_folder / profile_settings_file_name
            if profile_settings.exists():
                try:
                    tree = ET.parse(profile_settings)
                    root = tree.getroot()
                    profile_last_applied_date = root.find("last-applied-date").text if root.find("last-applied-date") is not None else None
                    if profile_last_applied_date:
                        try:
                            profile_date = datetime.strptime(profile_last_applied_date, '%d-%m-%Y %H:%M:%S')
                            if last_applied_date is None or profile_date > last_applied_date:
                                last_applied_date = profile_date
                                last_applied_profile = profile_folder.name
                        except ValueError:
                            print(f"\nGeçersiz tarih formatı! {profile_last_applied_date} değeri {profile_settings.name} dosyasındaki 'last-applied-date' etiketi için.")
                except ET.ParseError as e:
                    print(f"\nOkuma hatası! {profile_settings.name} adlı dosya okunamadı. Devam ediliyor.\nDosya konumu: {profile_settings}")
    if last_applied_profile:
        print(f"\n{selected_project.name} için son uygulanan profil: {last_applied_profile} ({last_applied_date.strftime('%d-%m-%Y %H:%M:%S')})")
    else:
        print(f"\n{selected_project.name} için son uygulanan herhangi bir profil bulunamadı.")

CreateDefaults()
ListProjects()

# Komut girişi
while True:
    if depth == 0:
        cmdStr = "\nZen - Komut girin (h/help): "
    elif depth == 1:
        cmdStr = f"\nZen - {selected_project.name} - Komut girin (h/help): "
    cmd = input(cmdStr).strip().lower()
    if cmd == "h" or cmd =="help":
        ListAllCommands()
    elif cmd == "exit" or cmd =="stop" or cmd =="close":
        break
    elif cmd == "cls" or cmd =="clear":
        ClearTerminal()
    elif cmd == "git" or cmd =="github":
        print(f"\nProgramın kaynak koduna aşşağıdaki adresten ulaşabilirsiniz:\n{git_path}")
    elif cmd == "root":
        OpenFolder(root_folder)
    elif (cmd =="n" or cmd =="new") and depth == 0:
        NewProject()
    elif (cmd =="n" or cmd =="new") and depth == 1:
        NewProfile(selected_project/profiles_folder_name)
    elif (cmd == "l" or cmd =="list") and depth == 0:
        ListProjects()
    elif (cmd == "last") and depth == 1:
        ShowLastAppliedProfile()
    elif (cmd == "l" or cmd =="list") and depth == 1:
        ListProfiles(selected_project)
    elif (cmd == "c" or cmd == "cancel") and depth == 1:
        BackToZeroDepth()
    elif (cmd == "b" or cmd == "back") and depth == 1:
        BackToZeroDepth()
        ListProjects()
    else:
        print("\nGeçersiz komut!")

print("\nProgram sonlandı. Kullanımınız için teşekkür ederiz...\n")

# LICENSED BY:
#                                                                                                                                
#              ,--,                                                                               ,--,                           
#            ,--.'|     ,--,                                     ,--,                           ,--.'|                           
#            |  | :   ,--.'|                            __  ,-.,--.'|                           |  | :                     ,---, 
#            :  : '   |  |,      .--.--.              ,' ,'/ /||  |,                  .--.--.   :  : '                 ,-+-. /  |
#   ,--.--.  |  ' |   `--'_     /  /    '    ,--.--.  '  | |' |`--'_      ,--.--.    /  /    '  |  ' |     ,--.--.    ,--.'|'   |
#  /       \ '  | |   ,' ,'|   |  :  /`./   /       \ |  |   ,',' ,'|    /       \  |  :  /`./  '  | |    /       \  |   |  ,"' |
# .--.  .-. ||  | :   '  | |   |  :  ;_    .--.  .-. |'  :  /  '  | |   .--.  .-. | |  :  ;_    |  | :   .--.  .-. | |   | /  | |
#  \__\/: . .'  : |__ |  | :    \  \    `.  \__\/: . .|  | '   |  | :    \__\/: . .  \  \    `. '  : |__  \__\/: . . |   | |  | |
#  ," .--.; ||  | '.'|'  : |__   `----.   \ ," .--.; |;  : |   '  : |__  ," .--.; |   `----.   \|  | '.'| ," .--.; | |   | |  |/ 
# /  /  ,.  |;  :    ;|  | '.'| /  /`--'  //  /  ,.  ||  , ;   |  | '.'|/  /  ,.  |  /  /`--'  /;  :    ;/  /  ,.  | |   | |--'  
#;  :   .'   \  ,   / ;  :    ;'--'.     /;  :   .'   \---'    ;  :    ;  :   .'   \'--'.     / |  ,   /;  :   .'   \|   |/      
#|  ,     .-./---`-'  |  ,   /   `--'---' |  ,     .-./        |  ,   /|  ,     .-./  `--'---'   ---`-' |  ,     .-./'---'       
# `--`---'             ---`-'              `--`---'             ---`-'  `--`---'                         `--`---'                
#                                                                                                                                
