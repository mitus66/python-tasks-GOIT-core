import sys
from pathlib import Path
from colorama import Fore, Style, init
import os

def visualize_directory_structure(directory_path):
    """
    Візуалізує структуру директорії, виводячи імена піддиректорій та файлів
    з використанням кольорів.

    Args:
        directory_path (str): Шлях до директорії.
    """
    init(autoreset=True)  # Ініціалізація colorama для автоматичного скидання кольору

    path = Path(directory_path)

    if not path.exists():
        print(Fore.RED + f"Помилка: Директорія '{directory_path}' не існує.")
        return

    if not path.is_dir():
        print(Fore.RED + f"Помилка: '{directory_path}' не є директорією.")
        return

    print(Fore.CYAN + f"Структура директорії: {directory_path}")

    def _visualize(current_path, indent=""):
        items = sorted(current_path.iterdir())
        total = len(items)
        for index, item in enumerate(items):
            prefix = "├── " if index < total - 1 else "└── "
            if item.is_dir():
                print(indent + Fore.BLUE + prefix + item.name)
                _visualize(item, indent + "│   " if index < total - 1 else indent + "    ")
            else:
                print(indent + Fore.GREEN + prefix + item.name)

    _visualize(path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python hw03.py <шлях_до_директорії>")
    else:
        directory_to_visualize = sys.argv[1]
        visualize_directory_structure(directory_to_visualize)

# input - python task_4_bot.py C:\DUBLES\YACHTING
# output - Структура директорії: C:\DUBLES\YACHTING
# ├── 29m_tender
# │   ├── 29m_1 hull panels.pdf
# │   ├── 29m_2 hull construction, sail.pdf
# │   ├── 29m_3 daggerboard, rudder, fittings.pdf
# │   └── thank you.pdf
# ├── 29m_tender.zip
# ├── 31m_tender
# │   ├── 31m_1 hull panels.pdf
# │   ├── 31m_2 hull construction.pdf
# │   ├── 31m_3 sails and spars.pdf
# │   ├── 31m_4 daggerboard and rudder.pdf
# │   └── thank you.pdf
# ├── 31m_tender.zip
# ├── 36m_solo_canoe
# │   ├── 36m_1 hull panels, paddle.pdf
# │   ├── 36m_2 hull construction.pdf
# │   └── thank you.pdf
# ├── 36m_solo_canoe.zip
# ├── 40m_dayboat (mast_step)
# │   ├── 40m_1 lines.pdf
# │   ├── 40m_2 hull panels, oars.pdf
# │   ├── 40m_3 hull construction.pdf
# │   ├── 40m_4 sail and spars, oarlock.pdf
# │   ├── 40m_5 daggerboard and rudder.pdf
# │   └── thank you.pdf
# ├── 40m_dayboat (mast_step).zip
# ├── 40m_dayboat (tabernacle)
# │   ├── 40m_1 lines.pdf
# │   ├── 40m_2 hull panels, paddle.pdf
# │   ├── 40m_3 hull construction.pdf
# │   ├── 40m_4 sail and spars.pdf
# │   ├── 40m_5 daggerboard and rudder.pdf
# │   └── thank you.pdf
# ├── 40m_dayboat (tabernacle).zip
# ├── 45m_dinghy
# │   ├── 45m_1 lines.pdf
# │   ├── 45m_2 hull panels.pdf
# │   ├── 45m_3 hull construction.pdf
# │   ├── 45m_4 sails and spars.pdf
# │   ├── 45m_5 centreboard and rudder.pdf
# │   ├── 45m_6 spar and hull fittings.pdf
# │   └── thank you.pdf
# ├── 45m_dinghy.zip
# ├── 46m_canoe
# │   ├── 46m_1 hull panels, paddle, yoke.pdf
# │   ├── 46m_2 hull construction.pdf
# │   └── thank you.pdf
# ├── 46m_canoe.zip
# ├── ArchimedesMB, Carene2008, Freeship 3.30+, NavalDesigner - Софт для судостроения.mhtml
# ├── FREEship_version_2.3_win32_executable.zip
# ├── FSplus3_13.zip
# ├── FSplus3_43+.zip
# ├── vy.pdf
# ├── Yachting
# │   ├── 95-101.pdf
# │   ├── Boat_Building_Manual.pdf
# │   ├── Bob_Bond_SPRAVOChNIK_YaKhTSMENA.pdf
# │   ├── Building Strip-Planked Boats.pdf
# │   ├── CGCbrochure3.pdf
# │   ├── dedekam.pdf
# │   ├── DniproEcoMarathon_презентация_спорт.pptx
# │   ├── ferro-1.pdf
# │   ├── ferro-2.pdf
# │   ├── ferro-3.pdf
# │   ├── gl_i-3-3_e.pdf
# │   ├── GougeonBook 061205.pdf
# │   ├── Gulbrandsen_Fishing_Boat_Designs.pdf
# │   ├── IMG_5185 - копия.jpg
# │   ├── IMG_5187 - копия.jpg
# │   ├── IMG_5187.jpg
# │   ├── IMG_5271 - копия.jpg
# │   ├── Intro Pages.pdf
# │   ├── J.Toghil_Yachting.pdf
# │   ├── Leontyev_rulevoy.pdf
# │   ├── mal_flot_svoimi_rukami.pdf
# │   ├── pionerskaya_sudoverf.pdf
# │   ├── Sponsor Pakage - Dnipro Eco_Marathon - Парусная регата  2016.xls
# │   ├── vybor-proektov-analogov-pri-razrabotke-uchebnogo-parusnogo-sudna-dlya-vnutrennih-vodnyh-putey.pdf
# │   ├── xclassconstruction.pdf
# │   ├── Курбатов Д.А. - 15 проектов судов для любительской постройки (1974)
# │   │   ├── 1.pdf
# │   │   ├── 2.pdf
# │   │   ├── 3.pdf
# │   │   ├── 4.pdf
# │   │   ├── 5.pdf
# │   │   ├── 6.pdf
# │   │   ├── 7.pdf
# │   │   ├── 8.pdf
# │   │   └── 9.pdf
# │   ├── Рангоут и такелаж судов - Ф.Л.Миддендорф 1905.pdf
# │   └── Стив Слейт - Все о парусном спорте. Новое полное руководство [2006, 448, DjVu].djvu
# ├── как_.mhtml
# ├── креслення яхт
# │   ├── 26m_pram.zip
# │   ├── 29m_tender.zip
# │   ├── 30m_tender.zip
# │   ├── 31m_tender.zip
# │   ├── 35m_dinghy.zip
# │   ├── 37m_dinghy.zip
# │   ├── 38m_dinghy.zip
# │   ├── 40m_dayboat (mast_step).zip
# │   ├── 40m_dayboat (tabernacle).zip
# │   ├── 42m_skiff.zip
# │   ├── 45m_1 lines.pdf
# │   ├── 45m_2 hull panels.pdf
# │   ├── 45m_3 hull construction.pdf
# │   ├── 45m_4 sails and spars.pdf
# │   ├── 45m_5 centreboard and rudder.pdf
# │   ├── 45m_6 spar and hull fittings.pdf
# │   ├── 45m_dinghy.zip
# │   ├── 48m_dinghy.zip
# │   ├── 50m_yawl
# │   │   ├── 50m_1 lines.pdf
# │   │   ├── 50m_2 hull panels.pdf
# │   │   ├── 50m_3 hull construction.pdf
# │   │   ├── 50m_4 sails and spars.pdf
# │   │   ├── 50m_5 centreboard and rudder.pdf
# │   │   └── thank you.pdf
# │   └── 50m_yawl.zip
# ├── Ордана
# │   ├── Razmery.doc
# │   └── upholster_list.doc
# ├── Проект 3-метровой парусно-гребной лодки динги. Построить самодельную лодку из фанеры.html
# ├── Проект 3-метровой парусно-гребной лодки динги. Построить самодельную лодку из фанеры_files
# │   ├── 1s.jpg
# │   ├── 2s.jpg
# │   ├── 3s.jpg
# │   ├── 4s(1).jpg
# │   ├── 4s.jpg
# │   ├── 5s.jpg
# │   ├── 99s.jpg
# │   ├── background_general_NEW1.gif
# │   ├── code.js
# │   ├── count.js
# │   ├── counter
# │   ├── deck_gears.gif
# │   ├── frame_1.gif
# │   ├── frame_2.gif
# │   ├── frame_3.gif
# │   ├── frame_stem.gif
# │   ├── frame_transom.gif
# │   ├── fw_menu(1).js
# │   ├── fw_menu.js
# │   ├── hull_plywood_1.gif
# │   ├── linesplan.gif
# │   ├── mast1.gif
# │   ├── mast2.gif
# │   ├── menu.css
# │   ├── midsection.gif
# │   ├── plywood_1.jpg
# │   ├── plywood_2.gif
# │   ├── plywood_cockpit.gif
# │   ├── plywood_details.jpg
# │   ├── plywood_loft_shell.gif
# │   ├── rudder1.gif
# │   ├── rudder2.gif
# │   ├── sail.gif
# │   ├── sailplan.gif
# │   ├── saved_resource
# │   ├── SD-11-1s.jpg
# │   ├── show_ads.js
# │   ├── spacer.gif
# │   ├── spaser1x1.gif
# │   ├── srtplan.gif
# │   ├── strprofile.gif
# │   ├── top100.jcn
# │   ├── top_banner_ru_design.gif
# │   ├── top_nav_ru_r1_c1.gif
# │   ├── top_nav_ru_r2_c1.gif
# │   ├── top_nav_ru_r2_c10.gif
# │   ├── top_nav_ru_r2_c11.gif
# │   ├── top_nav_ru_r2_c12.gif
# │   ├── top_nav_ru_r2_c13.gif
# │   ├── top_nav_ru_r2_c14.gif
# │   ├── top_nav_ru_r2_c15.gif
# │   ├── top_nav_ru_r2_c16.gif
# │   ├── top_nav_ru_r2_c17.gif
# │   ├── top_nav_ru_r2_c18.gif
# │   ├── top_nav_ru_r2_c19.gif
# │   ├── top_nav_ru_r2_c2.gif
# │   ├── top_nav_ru_r2_c20.gif
# │   ├── top_nav_ru_r2_c21.gif
# │   ├── top_nav_ru_r2_c3.gif
# │   ├── top_nav_ru_r2_c4.gif
# │   ├── top_nav_ru_r2_c5.gif
# │   ├── top_nav_ru_r2_c6.gif
# │   ├── top_nav_ru_r2_c7.gif
# │   ├── top_nav_ru_r2_c8.gif
# │   ├── top_nav_ru_r2_c9.gif
# │   ├── trunk.gif
# │   ├── tutor.gif
# │   └── urchin.js
# └── Яхтинг законы
#     ├── 116380_1.gif
#     ├── 116380_2.gif
#     ├── 5618149225.jpg
#     ├── 5618149225_1.jpg
#     ├── f400913n360.doc
#     ├── f400913n362.doc
#     ├── f400913n363.doc
#     ├── f400913n364.doc
#     ├── f431926n197.doc
#     ├── f431926n198.doc
#     ├── f431926n207.doc
#     ├── f431926n214.doc
#     ├── IMG_0481_800.jpg
#     ├── IMG_0482_800.jpg
#     ├── Prava_2013.jpg
#     ├── Prava_2014.jpg
#     ├── Про внесення змін до Положення про порядок видачі пос...   від 26.08.2014 № 413 (Текст для друку).mht
#     ├── Про затвердження Положення про порядок видачі посвідч...   від 07.05.2013 № 283 (Текст для друку)(новий).mht
#     └── Про затвердження Положення про порядок видачі посвідч...   від 07.05.2013 № 283 (Текст для друку).mht