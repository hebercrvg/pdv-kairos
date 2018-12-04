from model.DTO.ProdutoDTO import ProdutoDTO
from model.DAO.ProdutoDAO import ProdutoDAO
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QIcon

class ProdutoCTR:


    def Get_codprod_por_descricao(descricao):
        produtoDAO = ProdutoDAO
        result = produtoDAO.get_cod_produto_por_descricao(descricao)
        return result

    def Get_preco_produto(codprod):
        produtoDAO = ProdutoDAO
        Codprod = int(codprod)
        result = produtoDAO.get_preco_produto(codprod)
        return result

    def Cadastrar_Produto(descricao, tipo, preco):
        produtoDTO = ProdutoDTO
        produtoDAO = ProdutoDAO
        produtoDTO.descricao = descricao
        produtoDTO.tipo = tipo
        produtoDTO.preco = preco
        aux = 0
        if (produtoDTO.descricao == ''):
            aux += 1
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Erro")
            dlg.setIcon(QMessageBox.Critical)
            dlg.setWindowIcon(QtGui.QIcon("error.png"))
            text = ("Informe a descrição do produto.")
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.setText(text)
            dlg.exec_()

        if (produtoDTO.preco <= 0.0):
            aux += 1
            dlg = QMessageBox(None)
            dlg.setIcon(QMessageBox.Critical)
            dlg.setWindowTitle("Erro")
            dlg.setWindowIcon(QIcon("error.png"))
            dlg.setText("Por favor, informe um preço válido.")
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.exec_()

        if (aux==0):
            produtoDAO.cadastrar_produto(produtoDTO.descricao, produtoDTO.tipo, produtoDTO.preco)
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Sucesso")
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowIcon(QtGui.QIcon("greencheck.png"))
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.setText("Produto cadastrado com sucesso.")
            dlg.exec_()

    def Alterar_Produto(codprod, descricao, tipo, preco):
        produtoDTO = ProdutoDTO
        produtoDAO = ProdutoDAO
        produtoDTO.descricao = descricao
        produtoDTO.tipo = tipo
        produtoDTO.preco = preco
        Codprod = codprod
        aux = 0

        if (produtoDTO.descricao == ''):
            aux += 1
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Erro")
            dlg.setIcon(QMessageBox.Critical)
            dlg.setWindowIcon(QtGui.QIcon("error.png"))
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            text = ("Informe a descrição do produto.")
            dlg.setText(text)
            dlg.exec_()

        if (produtoDTO.preco <= 0.0):
            aux += 1
            dlg = QMessageBox(None)
            dlg.setIcon(QMessageBox.Critical)
            dlg.setWindowTitle("Erro")
            dlg.setWindowIcon(QtGui.QIcon("error.png"))
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.setText("Por favor, informe um preço válido.")
            dlg.exec_()

        if (aux==0):
            produtoDAO.alterar_produto(Codprod, produtoDTO.descricao, produtoDTO.tipo, produtoDTO.preco)
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Sucesso")
            dlg.setIcon(QMessageBox.Information)
            dlg.setWindowIcon(QIcon("greencheck.png"))
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(15)
            dlg.setFont(font)
            dlg.setText("Produto alterado com sucesso.")
            dlg.exec_()

    def Excluir_Produto(codprod):
        Codprod = codprod
        produtoDAO = ProdutoDAO
        produtoDAO.excluir_produto(Codprod)

        dlg = QMessageBox(None)
        dlg.setWindowTitle("Sucesso")
        dlg.setIcon(QMessageBox.Information)
        dlg.setWindowIcon(QtGui.QIcon("greencheck.png"))
        dlg.setText("Produto excluido com sucesso!")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        dlg.setFont(font)
        dlg.exec_()

    def Pesquisar_Produto(descricao):
        produtoDAO = ProdutoDAO
        result = produtoDAO.pesquisar_produto(descricao)
        return result
    def Pesquisar_Todos_Produtos():
        produtoDAO = ProdutoDAO
        return produtoDAO.pesquisar_todos_produtos()
