# -*- coding: utf-8 -*-
import sqlite3
from pathlib import Path
from numpy.random import randint


class VGymSystemDB:
    """
    Classe responsável por modifica e manipular do banco de dados.
    """

    def __init__(self):
        _caminho_db = str(Path('./Banco de dados/VGymSystem.db'))
        self._con = sqlite3.connect(_caminho_db)
        self._cursor = self._con.cursor()
        _habilita_chaves_estrangeiras = 'PRAGMA foreign_keys=ON'
        self._cursor.execute(_habilita_chaves_estrangeiras)
        self._NUM_MATRICULA_MINIMA = 11111
        self._NUM_MATRICULA_MAXIMA = 99999

    def set_novo_aluno(
        self,
        matricula_aluno: int,
        nome_aluno: str,
        data_nascimento: str,
        cpf: str,
        celular: str,
        whatsapp: int,
        bairro: str,
        cep: str,
        cidade: str,
        email: str,
        data_pagamento: int,
        valor_pagamento: int,
        foto: str,
        matricula_responsavel: int,
    ) -> bool:
        """
        Salva um novo aluno dependente no banco de dados
        Args:
            matricula_aluno (int): Número da matrícula única do aluno.
            nome_aluno (str): Nome completo do aluno.
            data_nascimento (str): Data de nascimento do aluno.
            cpf (str): CPF do aluno.
            celular (str): Número de celular do aluno.
            whatsapp (int): Valor (0 | 1) representando um valor booleano.
            bairro (str): Bairro do aluno.
            cep (str): CEP do aluno.
            cidade (str): Cidade do aluno.
            email (str): E-mail do aluno.
            data_pagamento (int): Data do pagamento.
            valor_pagamento (int): Valor do pagamento.
            foto (str): É uma string contendo o binário da foto do aluno.
            matricula_responsavel (int): Número da matrícula única do responsável.
        Returns:
            bool: Retorna True se a transação foi realizada e False se acontecer algum erro.
        """
        if nome_aluno == '':
            return False
        else:
            valores = [
                matricula_aluno,
                nome_aluno,
                data_nascimento,
                cpf,
                celular,
                whatsapp,
                bairro,
                cep,
                cidade,
                email,
                data_pagamento,
                valor_pagamento,
                foto,
                matricula_responsavel,
            ]
            self._set_novo_aluno(*valores)
            return True

    def set_novo_responsavel(
        self,
        matricula_responsavel: int,
        nome: str,
        data_nascimento: str,
        cpf: str,
        celular: str,
        whatsapp: int,
        bairro: str,
        cep: str,
        cidade: str,
        email: str,
        foto: str,
    ) -> bool:
        """
        Salva um novo responsável no banco de dados
        Args:
            matricula_responsavel (int): Número da matrícula única do responsável.
            nome (str): Nome completo do responsável.
            data_nascimento (str): Data de nascimento do responsável.
            cpf (str): CPF do responsável.
            celular (str): Número de celular do responsável.
            whatsapp (int): Valor (0 | 1) representando um valor booleano.
            bairro (str): Bairro do responsável.
            cep (str): CEP do responsável.
            cidade (str): Cidade do responsável.
            email (str): E-mail do responsável.
            foto (str): É uma string contendo o binário da foto do responsável.
        Returns:
            bool: Retorna True se a transação foi realizada e False se acontecer algum erro.
        """
        if nome == '':
            return False
        else:
            valores = [
                matricula_responsavel,
                nome,
                data_nascimento,
                cpf,
                celular,
                whatsapp,
                bairro,
                cep,
                cidade,
                email,
                foto,
            ]
            self._set_novo_responsavel(*valores)
            return True

    def get_nova_matricula_aluno(self) -> int:
        """
        Gera uma matrícula para aluno.
        Returns:
            int:  Número da matrícula do aluno.
        """
        sql = 'SELECT matricula_aluno FROM Aluno'
        # resultado da consulta no banco de dados
        resultado_pesquisa_aluno = self._cursor.execute(sql).fetchall()
        # nova matrícula gerada
        num_matricula_aluno = randint(
            self._NUM_MATRICULA_MINIMA, self._NUM_MATRICULA_MAXIMA
        )
        nenhum_dado = 0
        if len(resultado_pesquisa_aluno) == nenhum_dado:
            return num_matricula_aluno
        else:
            # resultado filtrado de matrículas existentes
            matriculas_existentes_alunos = list(resultado_pesquisa_aluno[0])
            # se a matrícula gerada já exitir, é gerada uma nova.
            while num_matricula_aluno in matriculas_existentes_alunos:
                num_matricula_aluno = randint(
                    self._NUM_MATRICULA_MINIMA, self._NUM_MATRICULA_MAXIMA
                )
            return num_matricula_aluno

    def get_nova_matricula_responsavel(self) -> int:
        """
        Gera uma matrícula para responsável.
        Returns:
            int:  Número da matrícula do responsável.
        """
        # resultado da consulta no banco de dados
        sql = 'SELECT matricula_responsavel FROM Aluno'

        resultado_pesquisa_responsavel = self._cursor.execute(sql).fetchall()
        # nova matrícula gerada
        num_matricula_responsavel = randint(
            self._NUM_MATRICULA_MINIMA, self._NUM_MATRICULA_MAXIMA
        )
        nenhum_dado = 0
        if len(resultado_pesquisa_responsavel) == nenhum_dado:
            return num_matricula_responsavel
        else:
            # resultado filtrado de matrículas existentes
            matriculas_existentes_responsaveis = list(
                resultado_pesquisa_responsavel[0]
            )
            # se a matrícula gerada já exitir, é gerada uma nova.
            while (
                num_matricula_responsavel in matriculas_existentes_responsaveis
            ):
                num_matricula_responsavel = randint(
                    self._NUM_MATRICULA_MINIMA, self._NUM_MATRICULA_MAXIMA
                )
            return num_matricula_responsavel

    def get_aluno_por_matricula(self, matricula: str) -> list:
        """
        Busca dados da matrícula informada.
        Args:
            matricula (str): Matrícula do aluno.

        Returns:
            list: Lista com os dados do aluno.
        """
        if matricula.isnumeric():
            quantidade_num_matricula = 5
            if len(matricula) == quantidade_num_matricula:
                dados = self._get_aluno_por_matricula(matricula)
                return dados

    def get_aluno_por_cpf(self, cpf: str) -> list:
        """
        Busca dados do CPF informado.
        Args:
            cpf (str): CPF do aluno.
        Returns:
            list: Lista com os dados do aluno.
        """
        if cpf.isnumeric():
            quantidade_num_cpf = 11
            if len(cpf) == quantidade_num_cpf:
                dados = self._get_aluno_por_cpf(cpf)
                return dados

    def excluir_aluno(self, matricula: str) -> None:
        """
        Excluí dados do aluno, se o aluno é independente a matrícula é do aluno.
        Args:
            matricula (str): Matrícula do responsável
        """
        self._excluir_aluno(matricula)

    def _set_novo_aluno(self, *args: list) -> None:
        """
        Salva dados de um novo aluno.
        Args:
            args (list): Dados ao aluno.
        """
        try:
            sql = 'INSERT INTO Aluno VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            self._cursor.execute(sql, args)
            self._con.commit()
        except sqlite3.IntegrityError as erro:
            raise erro

    def _set_novo_responsavel(self, *args: list) -> None:
        """
        Salva dados de um novo responsável.
        Args:
            args (list): Dados do responsável.
        """
        try:
            sql = 'INSERT INTO Responsavel VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            self._cursor.execute(sql, args)
            self._con.commit()
        except sqlite3.IntegrityError as erro:
            raise erro

    def _get_aluno_por_matricula(self, matricula: str) -> list:
        """
        Busca os dados da matrícula informada.
        Args:
            matricula (str): Lista com os dados.
        Returns:
            list: Lista com os dados do aluno.
        """
        sql = f'SELECT * FROM Aluno WHERE matricula_aluno == "{matricula}"'
        dados_brutos = self._cursor.execute(sql).fetchall()
        dados_filtrados = list(dados_brutos[0])
        return dados_filtrados

    def _get_aluno_por_cpf(self, cpf: str) -> list:
        """
        Busca dados do CPF informado.
        Args:
            cpf (str): CPF do aluno.
        Returns:
            list: Lista com os dados do aluno.
        """
        sql = f'SELECT * FROM Aluno WHERE cpf == "{cpf}"'
        dados_brutos = self._cursor.execute(sql).fetchall()
        dados_filtrados = list(dados_brutos[0])
        return dados_filtrados

    def _excluir_aluno(self, matricula) -> None:
        """
        Excluí  os dados do aluno.
        Args:
            matricula (str): Matrícula do responsável
        """
        sql = f'DELETE FROM Aluno WHERE matricula_responsavel == "{matricula}"'
        self._cursor.execute(sql)
        self._con.commit()

    def fechar_db(self):
        """
        Encerra a conexão com o VGymSystem.db
        """
        self._con.close()
