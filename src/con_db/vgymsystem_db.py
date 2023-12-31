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
        data_entrada: str,
        matricula_responsavel: int,
    ) -> None:
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
            data_entrada (str): Data da entrada do aluno.
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
            email,
            data_pagamento,
            valor_pagamento,
            foto,
            data_entrada,
            matricula_responsavel,
        ]
        self._set_aluno(*valores)
        self._set_aluno_tabela_pagamento(matricula_aluno)

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
    ) -> None:
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
        """
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
        self._set_responsavel(*valores)

    def set_novo_professor(
        self,
        matricula_professor: int,
        nome: str,
        data_nascimento: str,
        cpf: str,
        celular: str,
        whatsapp: int,
        email: str,
        cidade: str,
        bairro: str,
        cep: str,
        formacao: str,
        salario: int,
        dia_pagamento: int,
        foto: str,
        data_entrada: str,
    ) -> None:
        """
        Salva um novo professor no banco de dados.
        Args:
            matricula_professor (int): Matrícula.
            nome (str): Nome do professor.
            data_nascimento (str): Data de nascimento.
            cpf (str): CPF.
            celular (str): Número do celular.
            whatsapp (int): Valor (0 | 1) representando um valor booleano.
            email (str): E-mail.
            cidade (str): Cidade.
            bairro (str): Bairro.
            cep (str): CEP.
            formacao (str): Formação acadêmica.
            salario (str): Salário.
            dia_pagamento (str): Dia do pagamento.
            foto (str): Foto.
            data_entrada (str): Data da inscrição.
        """
        valores = [
            matricula_professor,
            nome,
            data_nascimento,
            cpf,
            celular,
            whatsapp,
            email,
            cidade,
            bairro,
            cep,
            formacao,
            salario,
            dia_pagamento,
            foto,
            data_entrada,
        ]
        self._set_professor(*valores)
        self._set_professor_tabela_pagamento(matricula_professor)

    def get_nova_matricula_professor(self) -> int:
        """
        Gera uma matrícula para professor.
        Returns:
            int:  Número da matrícula do professor.
        """
        sql = 'SELECT matricula_professor FROM Professor'
        resultado_pesquisa_professor = self._cursor.execute(sql).fetchall()

        num_matricula_professor = randint(
            self._NUM_MATRICULA_MINIMA, self._NUM_MATRICULA_MAXIMA
        )
        nenhum_dado = 0
        if len(resultado_pesquisa_professor) == nenhum_dado:
            return num_matricula_professor
        else:
            matriculas_existentes_professor = list(
                resultado_pesquisa_professor[0]
            )
            while num_matricula_professor in matriculas_existentes_professor:
                num_matricula_professor = randint(
                    self._NUM_MATRICULA_MINIMA, self._NUM_MATRICULA_MAXIMA
                )

            return num_matricula_professor

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

    def get_professor_por_matricula(self, matricula: str) -> list:
        """
        Busca dados da matrícula informada.
        Args:
            matricula (str): Matrícula do professor.

        Returns:
            list: Lista com os dados do professor.
        """
        if matricula.isnumeric():
            quantidade_num_matricula = 5
            if len(matricula) == quantidade_num_matricula:
                dados = self._get_professor_por_matricula(matricula)
                return dados

    def get_professor_por_cpf(self, cpf: str) -> list:
        """
        Busca dados do CPF informado.
        Args:
            cpf (str): CPF do professor.
        Returns:
            list: Lista com os dados do professor.
        """
        if cpf.isnumeric():
            quantidade_num_cpf = 11
            if len(cpf) == quantidade_num_cpf:
                dados = self._get_aluno_por_cpf(cpf)
                return dados

    def get_usuario(self) -> list:
        """
        Busca os dados do usuário.
        Returns:
            list: Usuário e senha.
        """
        sql = 'SELECT * From Usuario'
        dados_brutos = self._cursor.execute(sql).fetchall()
        dados_filtrados = list(dados_brutos[0])
        return dados_filtrados

    def get_alunos(self) -> list:
        """
        Busca os dados dos alunos.
        Returns:
            list: Dados e pagamentos dos alunos.
        """
        sql = 'SELECT * FROM Aluno'
        dados = self._cursor.execute(sql).fetchall()
        return dados

    def get_professores(self) -> list:
        """
        Busca os dados dos professores.
        Returns:
            list: Dados dos professores.
        """
        sql = 'SELECT * FROM Professor'
        dados = self._cursor.execute(sql).fetchall()
        return dados

    def get_pagamentos_alunos(self) -> list:
        """
        Busca os pagamentos dos alunos.
        Returns:
            list: Pagamentos dos alunos.
        """
        sql = 'SELECT * FROM PagamentoAluno'
        dados = self._cursor.execute(sql).fetchall()
        return dados

    def get_pagamentos_professores(self):
        """
        Busca os pagamentos dos professores.
        Returns:
            list: Pagamentos dos professores.
        """
        sql = 'SELECT * FROM PagamentoProfessor'
        dados = self._cursor.execute(sql).fetchall()
        return dados

    def excluir_professor(self, matricula: str) -> None:
        """
        Exclui dados do professor.
        Args:
            matricula (str): Matrícula do professor
        """
        if matricula.isnumeric():
            self._excluir_professor(matricula)

    def excluir_aluno(self, matricula: str) -> None:
        """
        Exclui dados do aluno, se o aluno é independente a matrícula é do aluno.
        Args:
            matricula (str): Matrícula do responsável
        """
        if matricula.isnumeric():
            self._excluir_aluno(matricula)

    def set_novo_pagamento_aluno(
        self, matricula: str, data_pagamento: str
    ) -> bool:
        """
        Adiciona a data que foi pago a pendência do aluno.
        Args:
            matricula (str): Matrícula do aluno.
            data_pagamento (str): Formato %m/%y.
        Returns:
            bool: Se a transação foi realizada com sucesso.
        """
        if matricula.isnumeric():
            data_pagamento_formatada = '\x20' + data_pagamento
            resultado_transacao = self._set_pagamento_aluno(
                matricula, data_pagamento_formatada
            )
            return resultado_transacao
        else:
            return False

    def set_novo_pagamento_professor(
        self, matricula: str, data_pagamento: str
    ) -> bool:
        """
        Adiciona a data que foi pago o salário do professor.
        Args:
            matricula (str): Matrícula do professor.
            data_pagamento (str): Formato %m/%y.
        Returns:
            bool: Se a transação foi realizada com sucesso.
        """
        if matricula.isnumeric():
            data_pagamento_formatada = '\x20' + data_pagamento
            resultado_transacao = self._set_pagamento_professor(
                matricula, data_pagamento_formatada
            )
            return resultado_transacao
        else:
            return False

    def _set_pagamento_professor(
        self, matricula: str, data_pagamento: str
    ) -> bool:
        """
        Acrescenta a data de pagamento com o formato \x20%m%y.
        Args:
            matricula (str): Matrícula do professor.
            data_pagamento (str): Formato %m/%y.
        Returns:
            bool: Se a transação foi realizada com sucesso.
        """
        try:
            sql = f"""
                update 'PagamentoProfessor' 
                set mes_ano_pago = mes_ano_pago || '{data_pagamento}' 
                where matricula_professor == '{matricula}'
                """
            self._cursor.execute(sql)
            self._con.commit()
            return True
        except sqlite3.OperationalError:
            return False

    def _set_pagamento_aluno(
        self, matricula: str, data_pagamento: str
    ) -> bool:
        """
        Acrescenta a data de pagamento com o formato \x20%m%y.
        Args:
            matricula (str): Matrícula do aluno.
            data_pagamento (str): Formato %m/%y.
        Returns:
            bool: Se a transação foi realizada com sucesso.
        """
        try:
            sql = f"""
                update 'PagamentoAluno' 
                set mes_ano_pago = mes_ano_pago || '{data_pagamento}' 
                where matricula_aluno == '{matricula}'
                """
            self._cursor.execute(sql)
            self._con.commit()
            return True
        except sqlite3.OperationalError:
            return False

    def _set_professor_tabela_pagamento(self, matricula: int) -> None:
        """
        Salva a matrícula do professor na tabela PagamentoProfessor.
        Args:
            matricula (int): Matrícula do professor.
        """
        try:
            sql = 'INSERT INTO PagamentoProfessor VALUES (?, ?)'
            self._cursor.execute(sql, (matricula, ' '))
            self._con.commit()
        except sqlite3.IntegrityError as erro:
            raise erro

    def _set_aluno_tabela_pagamento(self, matricula: int) -> None:
        """
        Salva a matrícula do aluno na tabela PagamentoAluno.
        Args:
            matricula (int): Matrícula do aluno.
        """
        try:
            sql = 'INSERT INTO PagamentoAluno VALUES (?, ?)'
            self._cursor.execute(sql, (matricula, ' '))
            self._con.commit()
        except sqlite3.IntegrityError as erro:
            raise erro

    def _set_aluno(self, *args: list) -> None:
        """
        Salva dados dum aluno.
        Args:
            args (list): Dados ao aluno.
        """
        try:
            sql = 'INSERT INTO Aluno VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            self._cursor.execute(sql, args)
            self._con.commit()
        except sqlite3.IntegrityError as erro:
            raise erro

    def _set_responsavel(self, *args: list) -> None:
        """
        Salva dados dum responsável.
        Args:
            args (list): Dados do responsável.
        """
        try:
            sql = 'INSERT INTO Responsavel VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            self._cursor.execute(sql, args)
            self._con.commit()
        except sqlite3.IntegrityError as erro:
            raise erro

    def _set_professor(self, *args: list) -> None:
        """
        Salva dados dum professor.
        Args:
            args (list): Dados do professor.
        """
        try:
            sql = 'INSERT INTO Professor VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            self._cursor.execute(sql, args)
            self._con.commit()
        except sqlite3.IntegrityError as erro:
            raise erro

    def _get_aluno_por_matricula(self, matricula: str) -> list:
        """
        Busca os dados da matrícula informada.
        Args:
            matricula (str): Matrícula do aluno.
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

    def _get_professor_por_matricula(self, matricula: str) -> list:
        """
        Busca os dados da matrícula informada.
        Args:
            matricula (str): Matrícula do professor.
        Returns:
            list: Lista com os dados do professor.
        """
        sql = f'SELECT * FROM Professor WHERE matricula_professor == "{matricula}"'
        dados_brutos = self._cursor.execute(sql).fetchall()
        dados_filtrados = list(dados_brutos[0])
        return dados_filtrados

    def _get_professor_por_cpf(self, cpf: str) -> list:
        """
        Busca os dados do CPF informada.
        Args:
            cpf (str): CPF do professor.
        Returns:
            list: Lista com os dados do professor.
        """
        sql = f'SELECT * FROM Professor WHERE cpf == "{cpf}"'
        dados_brutos = self._cursor.execute(sql).fetchall()
        dados_filtrados = list(dados_brutos[0])
        return dados_filtrados

    def _excluir_professor(self, matricula: str) -> None:
        """
        Exclui os dados do professor.
        Args:
            matricula (str): Matrícula do professor.
        """
        sql = (
            f'DELETE FROM Professor WHERE matricula_professor == "{matricula}"'
        )
        self._cursor.execute(sql)
        self._con.commit()

    def _excluir_aluno(self, matricula: str) -> None:
        """
        Exclui  os dados do aluno.
        Args:
            matricula (str): Matrícula do responsável pelo o aluno.
        """
        # Busca a matrícula do aluno.
        sql_matricula_aluno = f'SELECT matricula_aluno FROM Aluno WHERE matricula_aluno == "{matricula}"'
        matricula_aluno = self._cursor.execute(sql_matricula_aluno).fetchall()

        # Se tiver algum valor a matrícula pertence ao aluno.
        if matricula_aluno:

            # A exclusão do aluno exclui também da tabela PagamentoAluno.
            sql_aluno = (
                f'DELETE FROM Aluno WHERE matricula_aluno == "{matricula}"'
            )
            self._cursor.execute(sql_aluno)
            self._con.commit()

        # A matrícula pertence a um responsável.
        else:

            # A matrícula do aluno é a chave estrangeira da tabela PagamentoAluno.
            sql_matricula_pagamento = f'SELECT matricula_aluno FROM Aluno WHERE matricula_responsavel == "{matricula}"'
            matricula_pagamento = self._cursor.execute(
                sql_matricula_pagamento
            ).fetchall()[0][0]

            # A exclusão de um dos dois exclui o aluno da tabela Aluno.
            sql_responsavel = f'DELETE FROM Responsavel WHERE matricula_responsavel == "{matricula}"'
            sql_pagamentos = f'DELETE FROM PagamentoAluno WHERE matricula_aluno == "{matricula_pagamento}"'
            self._cursor.execute(sql_responsavel)
            self._cursor.execute(sql_pagamentos)
            self._con.commit()

    def fechar_db(self):
        """
        Encerra a conexão com o VGymSystem.db
        """
        self._con.close()
