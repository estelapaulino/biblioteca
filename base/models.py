from django.db import models

# Create your models here.

class Biblioteca(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)

    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'

    def __str__(self):
        return self.nome

class Titulo(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    categoria = models.CharField(verbose_name='Categoria', choices=[['LIVRO', 'Livro'], ['REVISTA', 'Revista']], max_length=50)
    imagem = models.ImageField(verbose_name='Imagem', upload_to='titulos')

    class Meta:
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'

    def __str__(self):
        return self.nome


class Exemplar(models.Model):
    data_aquisicao = models.DateField(verbose_name='Data de aquisição')
    titulo = models.ForeignKey(Titulo, verbose_name='Título', on_delete=models.CASCADE)
    ativo = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        verbose_name = 'Exemplar'
        verbose_name_plural = 'Exemplares'

    def __str__(self):
        return '{} - {}'.format(self.id, self.titulo)