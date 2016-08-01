from rolepermissions.roles import AbstractUserRole

class Professor(AbstractUserRole):
    available_permissions = {
        'criar_modulos': True,
        'criar_cursos':True,
        'ver_modulos':True,
        'ver_cursos':True,
        'editar_modulos':True,
        'editar_cursos':True,
    }

class Aluno(AbstractUserRole):
    available_permissions = {
        'ver_modulos':True,
        'ver_cursos':True,
        'editar_modulos':False,
        'editar_cursos':False,
        'criar_modulos': False,
        'criar_cursos':False,
    }
