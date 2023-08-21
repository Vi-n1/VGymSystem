# -*- coding: utf-8 -*-
import sqlite3
from pathlib import Path
from numpy.random import randint


class VGymSystemDB:
    """
    Classe responsável pela a modificação e manipulação do banco de dados.
    """

    def __init__(self):
        _caminho_db = str(Path('./Banco de dados/VGymSystem.db'))
        self._con = sqlite3.connect(_caminho_db)
        self._cursor = self._con.cursor()

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
            foto (str): É uma string contendo o binário da foto do aluno.
            matricula_responsavel (int): Número da matrícula única do responsável.
        Returns:
            bool: Retorna True se a transação foi realizada e False se acontecer algum erro.
        """
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
            foto,
            matricula_responsavel,
        ]
        if nome_aluno == '':
            return False
        elif data_nascimento == '':
            return False
        elif whatsapp < 0 or whatsapp > 1:
            return False
        else:
            self._set_novo_aluno(*valores)
            return True

    def _set_novo_aluno(self, *args: list) -> None:
        """
        Salva dados de um novo aluno.
        Args:
            args (list): Dados ao aluno.
        """
        sql = 'INSERT INTO Aluno VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self._cursor.execute(sql, args)
        self._con.commit()

    def get_nova_matricula(self, dependente: bool) -> int | list[int, int]:
        """Gera uma matrícula para aluno Independente ou duas matrícula para aluno dependente.

        Args:
            dependente (bool): Se o aluno é dependente ou não
        Returns:
            int | list[int, int]: Primeira matrícula é do aluno, segunda matrícula é do responsável.
        """
        # números da matrícula deve ser entre 00000 e 99999
        num_matricula_minima = 00000
        num_matricula_maxima = 99999

        # resultado da consulta no banco de dados
        resultado_pesquisa_aluno = self._cursor.execute(
            'SELECT matricula_aluno FROM Aluno'
        ).fetchall()

        # resultado filtrado de matrículas existentes
        matriculas_existentes_alunos = [
            resultado_pesquisa_aluno[index][0]
            for index in range(0, len(resultado_pesquisa_aluno))
        ]

        # nova matrícula gerada
        num_matricula_aluno = randint(
            num_matricula_minima, num_matricula_maxima
        )
        while num_matricula_aluno in matriculas_existentes_alunos:
            num_matricula_aluno = randint(
                num_matricula_minima, num_matricula_maxima
            )

        # se dependente for verdadeiro, é gerado uma matrícula para o responsável
        if dependente:
            # resultado da consulta no banco de dados
            resultado_pesquisa_responsavel = self._cursor.execute(
                'SELECT matricula_responsavel FROM Responsavel'
            ).fetchall()

            # resultado filtrado de matrículas existentes
            matriculas_existentes_responsaveis = [
                resultado_pesquisa_responsavel[index][0]
                for index in range(0, len(resultado_pesquisa_responsavel))
            ]
            # nova matrícula gerada
            num_matricula_responsavel = randint(
                num_matricula_minima, num_matricula_maxima
            )
            # se a matrícula gerada já exitir, é gerada uma nova.
            while (
                num_matricula_responsavel in matriculas_existentes_responsaveis
            ):
                num_matricula_responsavel = randint(
                    num_matricula_minima, num_matricula_maxima
                )
            return [num_matricula_aluno, num_matricula_responsavel]

        return num_matricula_aluno

    def fechar_db(self):
        """
        Encerra a conexão com o VGymSystem.db
        """
        self._con.close()
