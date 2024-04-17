class Professor:
    def __init__(self, matricula, nome, titulacao, telefone, email, salario):
        self.__matricula = int(matricula)
        self.__nome = str(nome)
        self.__titulacao = str(titulacao)
        self.__telefone = str(telefone)
        self.__email = str(email)
        self.__salario = double(salario)

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = int(matricula)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = str(nome)

    def get_titulacao(self):
        return self.__titulacao

    def set_titulacao(self, titulacao):
        self.__titulacao = str(titulacao)

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = tr(telefone)

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = str(email)

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = double(salario)


    def imprime(self):
        print(f"Matrícula: {self.__matricula}")
        print(f"Nome: {self.__nome}")
        print(f"Titulação: {self.__titulacao}")
        print(f"Telefone: {self.__telefone}")
        print(f"E-mail: {self.__email}")
        print(f"Salário: {self.__salario}")


class Departamento:
    def __init__(self, nome, telefone, email):
        self.__nome = str(nome)
        self.__telefone = str(telefone)
        self.__email = str(email)
        self.__lista_professores = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = str(nome)

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = str(telefone)

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email =str(email)

    def adicionar_professor(self, professor):
        self.__lista_professores.append(professor)

    def excluir_professor(self, matricula):
        for professor in self.__lista_professores:
            if professor.get_matricula() == matricula:
                self.__lista_professores.remove(professor)
                return True
        return False

    def busca_professor(self, matricula):
        for professor in self.__lista_professores:
            if professor.get_matricula() == matricula:
                return True
        return False

    def imprime(self):
        print(f"Departamento: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
        print(f"E-mail: {self.__email}")
        print("Professores no departamento:")
        for professor in self.__lista_professores:
            professor.imprime()
            print("\n")
