import os
#для работы с терминалом
from mnemonic import Mnemonic
#https://github.com/trezor/python-mnemonic  генератор мнемоники BIP39
import time
#время
from selenium import webdriver
#работа с сайтом
def startChiaDemon():
    os.system("cd ~/chia-blockchain; . ./activate; chia start wallet-only; deactivate")
    time.sleep(2)
#запуск Chia
def stopChiaDemon():
    os.system("cd ~/chia-blockchain; . ./activate; chia stop all; deactivate")
#остановка Chia
def generationMnemonics():
    mnemo = Mnemonic("english")
    wordMnemo = mnemo.generate(strength=256)
    mnemo = wordMnemo.split()
    word = '"'+mnemo[0]+'","'+mnemo[1]+'","'+mnemo[2]+'","'+mnemo[3]+'","'+mnemo[4]+'","'+mnemo[5]+'","'+mnemo[6]+'","'+mnemo[7]+'","'+mnemo[8]+'","'+mnemo[9]+'","'+mnemo[10]+'","'+mnemo[11]+'","'+mnemo[12]+'","'+mnemo[13]+'","'+mnemo[14]+'","'+mnemo[15]+'","'+mnemo[16]+'","'+mnemo[17]+'","'+mnemo[18]+'","'+mnemo[19]+'","'+mnemo[20]+'","'+mnemo[21]+'","'+mnemo[22]+'","'+mnemo[23]+'"'
    return (word)
#генерация мнемоники
def keyInput(word):
    os.system("""curl --insecure --cert ~/.chia/mainnet/config/ssl/wallet/private_wallet.crt --key ~/.chia/mainnet/config/ssl/wallet/private_wallet.key -d '{"mnemonic":["""+word+"""], "type": "new_wallet"}' -H "Content-Type: application/json" -X POST https://localhost:9256/add_key""")
#ввод нового ключа
def clearKeys():
    os.system("cd ~/chia-blockchain; . ./activate; chia keys delete_all; deactivate")
    time.sleep(1)
    os.system("rm ~/.chia/mainnet/wallet/db/*")
#удаление всех ключей
def walletKey():
    n = os.popen("cd ~/chia-blockchain; . ./activate; chia keys show; deactivate").read()
    return(n)
#информация о ключе
def web (wallet):
    chromedriver = '/usr/lib/chromium-browser/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    browser.get('https://xchscan.com/address/'+wallet)
    time.sleep(2)
    requiredHtml = browser.page_source
    testWord = 'class="bg-404'
    if testWord in requiredHtml:
        return("not_working")
    else:
        return("working")
#проверка кошелька

def allLog(mnemonic,wallet,valid):
    log_file = open('logChiaHak.txt', 'a')
    log_file.write('\n' + mnemonic + '\n' + wallet + '\n' + valid)
    log_file.close()
    if valid == "working":
        log_file = open('validWallet.txt', 'a')
        log_file.write('\n' + mnemonic + '\n' + wallet + '\n' + valid)
        log_file.close()
#запись всех логов

def workHackChia():
    mnemonicWord = generationMnemonics()
    print("generated mnemonics \n"+mnemonicWord)
    keyInput(mnemonicWord)
    wallet = walletKey().split()[29]
    print("\nwallet\n" + wallet)
    valid = web(wallet)
    print(valid)
    allLog(mnemonicWord, wallet, valid)
    clearKeys()
#работа

startChiaDemon()
time.sleep(2)
clearKeys()
while True:
	workHackChia()






