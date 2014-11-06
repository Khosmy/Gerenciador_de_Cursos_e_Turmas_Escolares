#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gerenciador_de_Cursos_e_Turmas_Escolares.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
