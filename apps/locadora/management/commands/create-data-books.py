from django.core.management.base import BaseCommand
from apps.locadora.models import Livro
from datetime import date


class Command(BaseCommand):
    help = 'Cria e adiciona dados na tabela de livros.'

    def handle(self, *args, **options):
        livros = [

            Livro(
                titulo="Livro01", 
                ano=date(2020, 5, 17), preco=130.50, 
                quantidade=20, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),
            Livro(
                titulo="Livro02", 
                ano=date(2023, 5, 17), preco=135.50, 
                quantidade=20, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),
            Livro(
                titulo="Livro03", 
                ano=date(2022, 5, 17), preco=30.50, 
                quantidade=5, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),
            Livro(
                titulo="Livro04", 
                ano=date(2021, 5, 17), preco=100.50, 
                quantidade=10, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),
              Livro(
                titulo="Livro05", 
                ano=date(2005, 5, 18), preco=100.50, 
                quantidade=10, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),
              Livro(
                titulo="Livro06", 
                ano=date(2021, 8, 27), preco=180.50, 
                quantidade=10, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),
              Livro(
                titulo="Livro07", 
                ano=date(2023, 5, 17), preco=100.50, 
                quantidade=10, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),
              Livro(
                titulo="Livro08", 
                ano=date(2021, 5, 17), preco=20.50, 
                quantidade=2, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),
              Livro(
                titulo="Livro09", 
                ano=date(2018, 5, 17), preco=100.50, 
                quantidade=10, 
                descricao="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy."
            ),

 
        ]
        Livro.objects.bulk_create(livros)

        