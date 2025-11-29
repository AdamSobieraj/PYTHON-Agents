from SearchKnowledgebase import SearchKnowledgebase
from ShopAssistant import ShopAssistant
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

knowledgebase = [
    "Smartfon Apple iPhone 15 Pro z ekranem OLED 6.1 cala, procesorem A17 Pro i aparatem 48 MP.",
    "Smartfon Samsung Galaxy S24 Ultra z wyświetlaczem 6.8 cala QHD+ i zoomem optycznym 10x.",
    "Smartfon Xiaomi 14 z szybkim ładowaniem 120W i baterią 5000 mAh.",
    "Smartfon Google Pixel 8 Pro z czystym Androidem i aparatem fotograficznym wspieranym AI.",
    "Smartfon OnePlus 12 z ekranem AMOLED 120Hz i ładowaniem bezprzewodowym 50W.",
    "Laptop Apple MacBook Air M3 13 cali, 8 GB RAM i dysk SSD 256 GB.",
    "Laptop Dell XPS 13 z procesorem Intel Core i7, 16 GB RAM i ekranem InfinityEdge.",
    "Laptop Lenovo ThinkPad X1 Carbon 11th Gen z ekranem 14 cali i systemem Windows 11 Pro.",
    "Laptop HP Spectre x360 14 – ultrabook z ekranem dotykowym OLED i procesorem i7.",
    "Laptop ASUS ROG Zephyrus G14 z kartą graficzną RTX 4060 i procesorem AMD Ryzen 9.",
    "Telewizor LG OLED C4 55 cali 4K UHD z systemem webOS i Dolby Vision.",
    "Telewizor Samsung QLED 65 cali Neo QLED z procesorem Quantum 4K.",
    "Telewizor Sony Bravia XR 75 cali z technologią Cognitive Processor XR i Google TV.",
    "Telewizor Philips Ambilight 55 cali z podświetleniem LED i obsługą HDR10+.",
    "Telewizor TCL 43 cali 4K Smart TV z systemem Google TV i Wi-Fi.",
    "Słuchawki Apple AirPods Pro 2 z aktywną redukcją szumów i etui MagSafe.",
    "Słuchawki Sony WH-1000XM5 z redukcją hałasu i czasem pracy 30 godzin.",
    "Słuchawki Bose QuietComfort Ultra z dźwiękiem przestrzennym i Bluetooth 5.3.",
    "Słuchawki JBL Tune 770NC z mikrofonem i trybem ambient.",
    "Słuchawki gamingowe SteelSeries Arctis Nova 7 Wireless z dźwiękiem 3D i mikrofonem.",
    "Smartwatch Apple Watch Series 10 z ekranem Retina Always-On i czujnikiem EKG.",
    "Smartwatch Samsung Galaxy Watch6 Classic z ramką obrotową i monitorowaniem snu.",
    "Smartwatch Garmin Fenix 8 z GPS, pulsoksymetrem i trybem treningowym.",
    "Smartwatch Huawei Watch GT 5 z baterią na 10 dni i pomiarem tętna.",
    "Smartwatch Amazfit GTR 4 z obsługą rozmów Bluetooth i GPS.",
    "Monitor Dell UltraSharp 27 cali 4K UHD z panelem IPS i pokryciem sRGB 99%.",
    "Monitor LG UltraGear 32 cali QHD 165Hz dla graczy.",
    "Monitor Samsung Odyssey G9 49 cali z zakrzywionym ekranem QLED 240Hz.",
    "Monitor ASUS ProArt 27 cali 4K dla grafików i projektantów.",
    "Monitor Philips 24 cali Full HD z cienkimi ramkami i trybem LowBlue.",
    "Aparat Sony Alpha 7 IV bezlusterkowiec z matrycą 33 MP i nagrywaniem 4K.",
    "Aparat Canon EOS R6 Mark II z szybkim autofocusem i stabilizacją obrazu.",
    "Aparat Nikon Z6 II z matrycą 24.5 MP i dwoma slotami na karty pamięci.",
    "Aparat Fujifilm X-T5 z matrycą APS-C 40 MP i trybem filmowania 6.2K.",
    "Aparat Panasonic Lumix GH6 z matrycą Micro Four Thirds i 10-bitowym zapisem.",
    "Odkurzacz Dyson V15 Detect z laserem wykrywającym kurz i filtrem HEPA.",
    "Odkurzacz Xiaomi Mi Vacuum Cleaner G10 z silnikiem 125 000 rpm i ekranem LCD.",
    "Odkurzacz robot iRobot Roomba j7+ z automatycznym opróżnianiem pojemnika.",
    "Odkurzacz Samsung Jet 90 Complete z baterią 60 min i stojakiem do ładowania.",
    "Odkurzacz Philips SpeedPro Max Aqua z funkcją mopowania i LED.",
    "Lodówka Samsung Bespoke RB38 z podwójnym obiegiem chłodzenia i wyświetlaczem.",
    "Lodówka LG InstaView Door-in-Door z szybą dotykową i Wi-Fi.",
    "Lodówka Bosch Serie 6 No Frost z pojemnością 366 litrów i klasą A++.",
    "Lodówka Whirlpool W7 z funkcją Total No Frost i trybem Eco.",
    "Lodówka Beko HarvestFresh z technologią światła imitującego cykl dobowy.",
    "Pralka Samsung AddWash 8 kg z funkcją EcoBubble i panelem AI Control.",
    "Pralka LG AI DD 9 kg z automatycznym doborem ruchów piorących.",
    "Pralka Bosch Serie 6 VarioPerfect z silnikiem EcoSilence Drive.",
    "Pralka Electrolux PerfectCare 700 z funkcją SteamCare i czujnikiem wagowym.",
    "Pralka Whirlpool FreshCare+ z parą i programem szybkim 30 minut.",
    "Konsola Sony PlayStation 5 Slim z dyskiem SSD 1 TB i kontrolerem DualSense.",
    "Konsola Microsoft Xbox Series X z obsługą gier 4K i dyskiem 1 TB SSD."
]


def init_openai():
    API_KEY = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=API_KEY)

client = init_openai()

search_service = SearchKnowledgebase(client, knowledgebase)
assistant = ShopAssistant(client, search_service.search)

print("Asystent sklepu gotowy! Wpisz 'exit' aby zakończyć.\n")

while True:
    q = input("Zadaj pytanie: ")

    if q.lower() in ["exit", "quit", "wyjdz", "koniec"]:
        break

    assistant.handle_query(q)
