import os
import time
import unittest
import threading
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# definindo porta para rodar o servidor web temporario dos testes
PORTA_SERVIDOR = 8000
ENDERECO_SERVIDOR = f"http://localhost:{PORTA_SERVIDOR}"

class ServidorWebThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        # vamos rodar a partir do diretorio src
        os.chdir(os.path.join(os.path.dirname(__file__), "src"))
        self.httpd = TCPServer(("", PORTA_SERVIDOR), SimpleHTTPRequestHandler)

    def run(self):
        # inicia o servidor na thread em background
        self.httpd.serve_forever()

    def parar(self):
        # fecha o servidor de forma limpa
        self.httpd.shutdown()
        self.httpd.server_close()

class TesteSistemaCafeteria(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # inicializa o servidor de arquivos estaticos na thread secundaria
        cls.servidor = ServidorWebThread()
        cls.servidor.start()

        # configurando o chrome para rodar sem interface grafica
        opcoes = Options()
        opcoes.add_argument("--headless")
        opcoes.add_argument("--disable-gpu")
        opcoes.add_argument("--no-sandbox")
        cls.driver = webdriver.Chrome(options=opcoes)
        cls.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        # fecha o navegador no fim dos testes
        cls.driver.quit()
        # finaliza o servidor http local
        cls.servidor.parar()

    def setUp(self):
        # recarrega a pagina principal no inicio de cada teste para resetar o estado
        self.driver.get(f"{ENDERECO_SERVIDOR}/index.html")

    def test_operacao_com_sucesso(self):
        # preenche o formulario de pedido com todas as informacoes corretas
        self.driver.find_element(By.ID, "cliente").send_keys("Carlos")
        self.driver.find_element(By.ID, "produto").send_keys("Cappuccino")
        self.driver.find_element(By.ID, "quantidade").send_keys("2")
        
        # clica no botao principal de envio
        self.driver.find_element(By.ID, "btn-enviar").click()
        
        # busca as linhas da tabela de pedidos cadastrados
        linhas = self.driver.find_elements(By.XPATH, "//tbody[@id='lista-pedidos']/tr")
        
        # garante que o pedido inserido agora esta na tabela
        self.assertTrue(len(linhas) > 0)
        self.assertIn("Carlos", linhas[0].text)

    def test_campo_obrigatorio_vazio(self):
        # deixa o cliente vazio e preenche os outros campos
        self.driver.find_element(By.ID, "produto").send_keys("Espresso")
        self.driver.find_element(By.ID, "quantidade").send_keys("1")
        
        # tenta enviar o pedido com informacao faltando
        self.driver.find_element(By.ID, "btn-enviar").click()
        
        # garante que a tabela continua limpa sem nenhum registro inserido
        linhas = self.driver.find_elements(By.XPATH, "//tbody[@id='lista-pedidos']/tr")
        self.assertEqual(len(linhas), 0)

    def test_mensagem_sucesso(self):
        # envia um pedido valido para a cafeteria
        self.driver.find_element(By.ID, "cliente").send_keys("Mariana")
        self.driver.find_element(By.ID, "produto").send_keys("Espresso")
        self.driver.find_element(By.ID, "quantidade").send_keys("3")
        self.driver.find_element(By.ID, "btn-enviar").click()
        
        # encontra o elemento que exibe os avisos na tela
        mensagem = self.driver.find_element(By.ID, "mensagem")
        
        # valida se a mensagem correta foi mostrada em verde
        self.assertEqual(mensagem.text, "Pedido realizado com sucesso!")
        self.assertIn("green", mensagem.get_attribute("style"))

    def test_mensagem_erro(self):
        # clica em enviar logo de cara com todos os inputs vazios
        self.driver.find_element(By.ID, "btn-enviar").click()
        
        # captura o paragrafo de retorno
        mensagem = self.driver.find_element(By.ID, "mensagem")
        
        # checa se o erro e exibido e se a cor da fonte e vermelha
        self.assertEqual(mensagem.text, "Erro: Todos os campos são obrigatórios!")
        self.assertIn("red", mensagem.get_attribute("style"))

    def test_ordem_e_quantidade_itens(self):
        # insere o primeiro pedido na fila
        self.driver.find_element(By.ID, "cliente").send_keys("Lucas")
        self.driver.find_element(By.ID, "produto").send_keys("Latte")
        self.driver.find_element(By.ID, "quantidade").send_keys("1")
        self.driver.find_element(By.ID, "btn-enviar").click()
        
        # insere o segundo pedido na fila
        self.driver.find_element(By.ID, "cliente").send_keys("Beatriz")
        self.driver.find_element(By.ID, "produto").send_keys("Pão de Queijo")
        self.driver.find_element(By.ID, "quantidade").send_keys("4")
        self.driver.find_element(By.ID, "btn-enviar").click()
        
        # busca as linhas criadas dinamicamente
        linhas = self.driver.find_elements(By.XPATH, "//tbody[@id='lista-pedidos']/tr")
        
        # garante que existem exatamente dois pedidos na lista
        self.assertEqual(len(linhas), 2)
        
        # valida se a ordem de insercao foi mantida certinha
        self.assertIn("Lucas", linhas[0].text)
        self.assertIn("Beatriz", linhas[1].text)

    def test_navegacao_entre_paginas(self):
        # localiza e clica no link para ir para a pagina do cardapio
        self.driver.find_element(By.ID, "link-Cardapio").click()
        
        # valida se navegou com sucesso checando o titulo da nova aba
        self.assertEqual(self.driver.title, "Cafeteria - Cardápio")
        
        # encontra o botao de retornar para a tela inicial
        self.driver.find_element(By.ID, "link-voltar").click()
        
        # valida se retornou corretamente para a pagina de pedidos
        self.assertEqual(self.driver.title, "Cafeteria - Fazer Pedido")

if __name__ == "__main__":
    unittest.main()
