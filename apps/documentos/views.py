from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Documento


class DocumentCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def form_valid(self, form):
        form.instance.pertence_id = self.kwargs['funcionario_id']
        print(form.is_valid())
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    """
    def get_success_url(self):
        # Substitua 'nome_da_view' pelo nome da view para onde você quer redirecionar
        return reverse_lazy('update_funcionario', kwargs={'funcionario_id': self.kwargs['funcionario_id']})
        """

