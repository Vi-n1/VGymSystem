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

    def set_novo_aluno_dependente(
        self,
        matricula_aluno: int,
        nome_aluno: str,
        data_nascimento: str,
        cpf: int,
        celular: int,
        whatsapp: int,
        bairro: str,
        cep: int,
        cidade: str,
        foto: str,
        matricula_responsavel: int,
    ) -> None:
        """
        Salva um novo aluno dependente no banco de dados
        Args:
            matricula_aluno (int): Número da matrícula única do aluno.
            nome_aluno (str): Nome completo do aluno.
            data_nascimento (str): Data de nascimento do aluno.
            cpf (int): CPF do aluno.
            celular (int): Número de celular do aluno.
            whatsapp (int): Valor entre (0, 1) representando um valor booleano.
            bairro (str): Bairro do aluno.
            cep (int): CEP do aluno.
            cidade (str): Cidade do aluno.
            foto (str): É uma string contendo o binário da foto do aluno.
            matricula_responsavel (int): Número da matrícula única do responsável.
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
            foto,
            matricula_responsavel,
        ]
        self._set_novo_aluno_dependente(valores)

    def _set_novo_aluno_dependente(self, *args: list) -> None:
        """
        Salva dados de um novo aluno.
        Args:
            args (list): Dados ao aluno.
        """
        sql = 'INSERT INTO Aluno VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self._cursor.execute(sql, *args)
        self._con.commit()

    def get_nova_matricula(self) -> list[int, int]:
        """Gera matrícula única

        Returns:
            list[int, int]: primeira matrícula é do aluno, segunda matrícula é do responsável.
        """
        num_matricula_minima = 00000
        num_matricula_maxima = 99999
        resultado_responsavel = self._cursor.execute(
            'SELECT matricula_responsavel FROM Responsavel'
        ).fetchall()
        resultado_aluno = self._cursor.execute(
            'SELECT matricula_aluno FROM Aluno'
        ).fetchall()
        matriculas_existentes_alunos = [
            resultado_aluno[index][0]
            for index in range(0, len(resultado_aluno))
        ]
        matriculas_existentes_responsaveis = [
            resultado_responsavel[index][0]
            for index in range(0, len(resultado_responsavel))
        ]
        num_matricula_aluno = randint(
            num_matricula_minima, num_matricula_maxima
        )
        num_matricula_responsavel = randint(
            num_matricula_minima, num_matricula_maxima
        )
        while (
            num_matricula_responsavel in matriculas_existentes_responsaveis
            and num_matricula_aluno in matriculas_existentes_alunos
        ):
            num_matricula_aluno = randint(
                num_matricula_minima, num_matricula_maxima
            )
            num_matricula_responsavel = randint(
                num_matricula_minima, num_matricula_maxima
            )

        return [num_matricula_aluno, num_matricula_responsavel]

    def fechar_db(self):
        """
        Encerra a conexão com o VGymSystem.db
        """
        self._con.close()
