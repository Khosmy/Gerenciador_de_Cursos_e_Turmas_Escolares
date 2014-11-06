#coding:utf-8
from django.db import models

# Create your models here.

TIPO_OPCOES = [

	('A','Autorizado'),
	('L','Licenciatura'),
	('E','Especialista'),
	('M','Mestrado'),
	('D','Doutorado')

]


class Professor(models.Model):
	
	
	Tipo = models.CharField('Tipo de Formação Superior',max_length=1,choices=TIPO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=15,blank=True)
	DataFormacao = models.DateField('Data da Ultima Colação de Grau',null=True)

 	 	
 	def __unicode__(self):
		return self.Professor
	
