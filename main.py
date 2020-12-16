from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

#Lista com os emails que ja foram enviados
enviados = []

# Lista com os emails de destino
lista_de_emails = [
    'exemplo123@outlook.com'
]

for pessoa in lista_de_emails:
    sleep(10)
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.get("https://outlook.live.com/mail/0/inbox")
    sleep(5)
    print('1) entrei no site passo 1')

    entrar1 = driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a')
    entrar1.click()
    sleep(5)
    print('2) entrei na página de login')

    email = driver.find_element_by_name('loginfmt')
    sleep(1)
    email.send_keys('seu email para entrar na conta')
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
    sleep(15)

    nova_mensagem = driver.find_element_by_id('id__5')
    nova_mensagem.click()
    sleep(12)

    enviar_parai = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]')
    enviar_para = enviar_parai.find_element_by_tag_name('input')
    enviar_para.send_keys(pessoa)
    sleep(8)
    print('5) digitei o destino')

    #assunto = driver.find_element_by_id('TextField1003')
    assuntoi = enviar_parai.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div')
    assunto = assuntoi.find_element_by_tag_name('input')
    assunto.send_keys('Assunto que você deseja')
    sleep(3)
    print('6) digitei o assunto')

    texto = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div[1]/div')
    texto.send_keys('''
    O texto que você deseja enviar
    ''')
    sleep(10)
    print('7) digitei o texto')

    enviar = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]/span')
    enviar.click()
    print('eviei o email')
    enviados.append(pessoa)
    print(enviados)
    print('==========================================')
    driver.quit()