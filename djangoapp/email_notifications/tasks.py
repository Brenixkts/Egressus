from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Notificacao
from egressus_app.models import EgressoTurma, Turma
from core import settings

# Tarefa assíncrona para enviar notificações agendadas
@shared_task
def enviar_notificacoes_agendadas():
    """Envia notificações agendadas pelo administrador com base no curso especificado."""
    agora = timezone.now()
    # Filtra notificações agendadas cuja data de postagem é menor ou igual ao momento atual
    notificacoes = Notificacao.objects.filter(data_de_postagem__lte=agora)
    for notificacao in notificacoes:
        if notificacao.enviar_para_todos:
            destinatarios = [egresso.user.email for egresso in EgressoTurma.objects.all()]
        else:
            # Obtém os IDs dos egressos associados ao curso alvo da notificação
            egressos_ids = EgressoTurma.objects.filter(turma__curso=notificacao.curso_alvo).values_list('user_id', flat=True)
            # Filtra e-mails dos egressos com base nos IDs obtidos
            destinatarios = [egresso.user.email for egresso in EgressoTurma.objects.filter(user_id__in=egressos_ids)]
        
        send_mail( ## ALterar no futuro para ser senda_mass_mail() e enviar um template html do email @tobias-costa @brenixkts
            notificacao.titulo,
            notificacao.mensagem,
            settings.EMAIL_HOST_USER,
            destinatarios,
        )
        notificacao.delete()  # Remove notificação após o envio

# Tarefa assíncrona para enviar e-mails automáticos
@shared_task
def enviar_notificacoes_automaticas():
    """Envia e-mails automáticos, como aniversários de formatura e aniversários pessoais."""
    hoje = timezone.now().date()

    # Enviar e-mails de aniversário de formatura
    turmas_aniversariantes = Turma.objects.filter(data_formatura=hoje)
    for turma in turmas_aniversariantes:
        # Obtém os egressos associados à turma atual
        egressos = EgressoTurma.objects.filter(turma=turma).select_related('user')
        # Lista os e-mails dos egressos para envio
        destinatarios = [et.user.email for et in egressos]
        send_mail( ## ALterar no futuro para ser senda_mass_mail() e enviar um template html do email @tobias-costa @brenixkts
            'Feliz Aniversário de Formatura!',
            f'Parabéns pela formatura! Hoje comemoramos o aniversário de formatura da turma {turma.nome_turma}.',
            settings.EMAIL_HOST_USER,
            destinatarios,
        )

    # Enviar e-mails de aniversário pessoal
    egressos_aniversariantes = EgressoTurma.objects.filter(user__date_of_birth=hoje)
    for egresso in egressos_aniversariantes:
        # Envia o e-mail de aniversário pessoal para o egresso atual
        send_mail( ## ALterar no futuro para enviar um template html do email @tobias-costa @brenixkts
            'Feliz Aniversário!',
            f'Parabéns, {egresso.user.first_name}! Desejamos a você um ótimo aniversário!',
            settings.EMAIL_HOST_USER,
            [egresso.user.email],
        )
        # Avisar os colegas da turma do aniversariante
        # O comando abaixo obtém os e-mails dos colegas de turma do egresso, excluindo o próprio egresso
        egressos_colegas = EgressoTurma.objects.filter(turma=egresso.turma).exclude(user=egresso.user).values_list('user__email', flat=True)
        if egressos_colegas:
            # Envia um e-mail para os colegas informando sobre o aniversário do egresso
            mensagem_colegas = f"Hoje é aniversário do {egresso.user.first_name} {egresso.user.last_name}!"
            send_mail( ## ALterar no futuro para ser senda_mass_mail() e enviar um template html do email @tobias-costa @brenixkts
                f"Aniversário do colega {egresso.user.first_name}", 
                mensagem_colegas,
                settings.EMAIL_HOST_USER,
                egressos_colegas,
            )