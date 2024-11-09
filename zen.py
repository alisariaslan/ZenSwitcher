# Kütüphaneler
import os
import platform
from pathlib import Path

# Bazı temel değişkenler
mac = "Darwin"
win = "Windows"
git_path = "https://github.com/alisariaslan/ZenSwitcher"
home_path = Path.home()
main_folder_name = "ZenSwitcher"
main_folder_path = Path(home_path,main_folder_name)
projects_folder_name = "ZenProjects"
projects_folder_path = Path(main_folder_path,projects_folder_name)
profiles_folder_name = "ZenProfiles"
commands_folder_name = "ZenCommands"
depth = 0
selected_project = None
selected_project_profiles_path = None
selected_project_commands_path = None

# Tanıtım
print("\n_____Zen Switcher 1.0.0_____")
print("\nHoşgeldiniz. Bu mini-program projelerde hızlıca birden fazla profil değiştirmek için tasarlanmıştır.")
print(f"\n({git_path})")
print(f"\nProfillerinizin kaydedileceği konum: {main_folder_path}")

# Komutları listeler
def ListAllCommands():
    print("\nGeçerli Komutlar:")
    print("\t* h/help: Mevcut kullanabileceğiniz komutları listeler.")
    print("\t* exit/stop/close: Programı sonlandırır.")
    print("\t* git/github: Programın kaynak kodunun bulunduğu adresi gösterir.")
    if depth is 0:
        print("\t* n/new: Yeni proje oluşturmak için kullanılır.")
        print("\t* l/list: Tüm projeleri listeler. Mevcut öğe varsa seçim yapılır.")
    elif depth is 1:
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

# Klasörleri oluştur
def CreateDefaults():
    global selected_project,profiles_folder_name, commands_folder_name,selected_project_profiles_path,selected_project_commands_path
    main_folder_path.mkdir(exist_ok=True)
    projects_folder_path.mkdir(exist_ok=True)
    if not selected_project == None:
        selected_project_profiles_path = Path(selected_project.resolve(), profiles_folder_name)
        selected_project_commands_path = Path(selected_project.resolve(), commands_folder_name)
        selected_project_profiles_path.mkdir(exist_ok=True)
        selected_project_commands_path.mkdir(exist_ok=True)

# Proje klasörlerini listeleme
def ListProjects():
    global selected_project, depth 
    projects = [item for item in projects_folder_path.iterdir() if item.is_dir()]
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
            # Sayısal girişleri kontrol et
            try:
                selected_index = int(selected_input)
                if 1 <= selected_index <= folder_count:
                    selected_project = projects[selected_index - 1]
                    print(f"\nSeçilen proje: {selected_project.name}")
                    CreateDefaults()
                    depth = 1
                    ListProfiles()
                    break
                else: raise ValueError
            except ValueError:
                print("\nGeçersiz bir değer girdiniz. Lütfen tekrar deneyin.")
    else:
        print("\nGörünüşe göre hiç proje klasörünüz yok.")

# Proje klasörlerini listeleme
def ListProfiles():
    profiles = [item for item in selected_project_profiles_path.iterdir() if item.is_dir()]
    folder_count = len(profiles)
    if folder_count > 0:
        print(f"\nProfiller ({folder_count}):")
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
            # Sayısal girişleri kontrol et
            try:
                selected_index = int(selected_input)
                if 1 <= selected_index <= folder_count:
                    selected_profile = profiles[selected_index - 1]
                    print(f"\nProfil uygulanıyor: {selected_profile.name}")
                    # TO-DO: Profili uygulama işlemleri buraya gelecek
                    break
                else: raise ValueError
            except ValueError:
                print("\nGeçersiz bir değer girdiniz. Lütfen tekrar deneyin.")
    else:
        print("\nGörünüşe göre hiç profiliniz yok.")

# Yeni proje oluşturulacak yolu uygun platformda açar.
def NewProject():
        print("\nOluşturmak istediğiniz yeni projeleri klasörler halinde şimdi açılacak olan klasöre oluşturun." )
        print("Projeleri oluşturduktan sonra, tekrar listeleme yapıp projeler arasından seçim yapabilirsiniz..." )
        if platform.system() == mac:
            os.system(f"open {projects_folder_path}")
        elif platform.system() == win:
            os.system(f"explorer {projects_folder_path}")

# Yeni profil oluşturulacak yolu uygun platformda açar.
def NewProfile():
        print("\nOluşturmak istediğiniz yeni profilleri klasörler halinde şimdi açılacak olan mevcut proje klasörünüze oluşturun." )
        print("Profilleri oluşturduktan sonra, tekrar listeleme yapıp profiller arasından geçiş yapabilirsiniz..." )
        if platform.system() == mac:
            os.system(f"open {selected_project_profiles_path}")
        elif platform.system() == win:
            os.system(f"explorer {selected_project_profiles_path}")

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
    elif (cmd =="n" or cmd =="new") and depth == 0:
        NewProject()
    elif (cmd =="n" or cmd =="new") and depth == 1:
        NewProfile()
    elif (cmd == "l" or cmd =="list") and depth == 0:
        ListProjects()
    elif (cmd == "l" or cmd =="list") and depth == 1:
        ListProfiles()
    elif (cmd == "c" or cmd == "cancel") and depth == 1:
        BackToZeroDepth()
    elif (cmd == "b" or cmd == "back") and depth == 1:
        BackToZeroDepth()
        ListProjects()
    else:
        print("\nGeçersiz komut!")

print("\nProgram sonlandı. Kullanımınız için teşekkür ederiz...\n")

