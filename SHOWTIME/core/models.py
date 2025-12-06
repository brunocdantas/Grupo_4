from django.db import models

# Create your models here.

# Modelo de Artista
class Artist(models.Model):
    id = models.AutoField(primary_key=True)

    # Informações básicas
     
    
    name = models.CharField(max_length=255, db_column='NAME')
    image = models.ImageField(upload_to='artists/', blank=True, null=True,db_column='IMAGE')
    biography = models.TextField(db_column='BIOGRAPHY', blank=True)

    # Informações musicais
    top_musics = models.TextField(
        db_column='TOP_MUSICS',
        help_text="Lista de músicas em formato texto (ex.: separadas por vírgula)"
    )

    # Informações sobre shows
    upcoming_shows = models.TextField(
        db_column='UPCOMING_SHOWS',
        help_text="Shows futuros; pode ser JSON, texto ou lista formatada"
    )

    # Dados extras importantes
    genre = models.CharField(max_length=100, db_column='GENRE', blank=True)
    country = models.CharField(max_length=100, db_column='COUNTRY', blank=True)
    followers = models.TextField(db_column='FOLLOWERS')
    social_links = models.TextField(
        db_column='SOCIAL_LINKS',
        blank=True,
        help_text="Links de redes sociais em formato texto ou JSON"
    )

    class Meta:
        managed = True
        db_table = 'Artist'
        ordering = ['id']

    def __str__(self):
        return f"Artista: {self.name}"
