from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

enviados = []
lista_de_emails = [
    'exemplo123@outlook.com'
]

option = Options()
option.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=option)
driver.get("https://outlook.live.com/mail/0/inbox")
sleep(5)
print('1) entrei no site passo 1')

entrar1 = driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a')
entrar1.click()
sleep(5)
print('2) entrei na página de login')

email = driver.find_element_by_name('loginfmt')
sleep(1)
email.send_keys('seu email para entrar na sua conta')
sleep(3)
print('3) digitei o email')

entrar2 = driver.find_element_by_id('idSIButton9')
entrar2.click()
sleep(3)

senha = driver.find_element_by_name('passwd')
senha.send_keys('sua senha para entrar na sua conta')
sleep(5)
print('4) digitei a senha')

entrar3 = driver.find_element_by_id('idSIButton9')
entrar3.click()
sleep(10)

for pessoa in lista_de_emails:
    nova_mensagem = driver.find_element_by_id('id__5')
    nova_mensagem.click()
    sleep(12)

    enviar_parai = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]')
    enviar_para = enviar_parai.find_element_by_tag_name('input')
    enviar_para.send_keys(pessoa)
    sleep(8)
    print('5) digitei o destino')

    assuntoi = enviar_parai.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div')
    assunto = assuntoi.find_element_by_tag_name('input')
    assunto.send_keys('aqui fica o assunto do email a ser enviado')
    sleep(3)
    print('6) digitei o assunto')

    texto = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div[1]/div')
    texto.send_keys('''
    aqui fica o texto do email a ser enviado 
    ''')
    sleep(10)
    print('7) digitei o texto')

    enviar = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]/span')
    enviar.click()
    print('8) eviei o email')
    enviados.append(pessoa)
    for p in enviados:
        print(f'--> {p}')
    print('==========================================')

driver.quit()
print('=== TERMINEI ===')