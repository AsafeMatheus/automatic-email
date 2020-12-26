from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

sended = []

dictionary_with_people = {
    'pessoa1': 'pessoa1@outlook.com',
}

option = Options()
option.headless = True

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=option)
driver.get("https://outlook.live.com/mail/0/inbox")
sleep(2)
print('1) entrei no site')

entrar1 = driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a')
entrar1.click()
sleep(2)
print('2) entrei no site página de login')

email = driver.find_element_by_name('loginfmt')
sleep(1)
email.send_keys('email para entrar na sua conta')
sleep(5)
print('3) digitei o email')

entrar2 = driver.find_element_by_id('idSIButton9')
entrar2.click()
sleep(5)

senha = driver.find_element_by_name('passwd')
senha.send_keys('senha para entrar na sua conta')
sleep(2)
print('4) digitei a senha')

entrar3 = driver.find_element_by_id('idSIButton9')
entrar3.click()
sleep(10)

for k, v in dictionary_with_people.items():
    nova_mensagem = driver.find_element_by_id('id__5')
    nova_mensagem.click()
    sleep(8)

    enviar_parai = driver.find_element_by_id('ReadingPaneContainerId')
    sleep(1)
    enviar_para = enviar_parai.find_element_by_xpath('//*[@id="ReadingPaneContainerId"]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input')
    enviar_para.send_keys(v)
    sleep(10)
    print('5) digitei o destino')

    assuntoi = driver.find_element_by_xpath('//*[@id="ReadingPaneContainerId"]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div')
    assunto = assuntoi.find_element_by_tag_name('input')
    assunto.send_keys('invitation') #assunto
    sleep(3)
    print('6) digitei o assunto')

    texto = driver.find_element_by_xpath('//*[@id="ReadingPaneContainerId"]/div/div/div/div[1]/div[2]/div[1]')
    texto.send_keys(f'''
    Hi {k}! I hope to see you at my party tomorrow.
    ''') #texto
    sleep(10)
    print('7) digitei o texto')

    enviar = driver.find_element_by_xpath('//*[@id="ReadingPaneContainerId"]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]')
    enviar.click()
    print('8) eviei o email')
    sended.append(v)
    print('**************** ENVIADOS ****************')
    for p in sended:
        print(f'{sended.index(p) + 1} --> {p}')
    print('==========================================')

driver.quit()
print('=== TERMINEI ===')