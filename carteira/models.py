from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Base(models.Model):
    is_active = models.BooleanField(verbose_name='Ativo', default=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        abstract = True
       


class Category(Base):
    title = models.CharField(verbose_name='Título', max_length=200)
    description = models.CharField(verbose_name='Descrição', max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-id']
        
    
    def __str__(self):
        return self.title



class StatusChoices(models.TextChoices):
    PAID = 'PG', 'Paga'
    PENDING = 'PD', 'Pendente'


class AccountsReceivable(Base):
    owner = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Título', max_length=200)
    description = models.CharField(verbose_name='Descrição', max_length=200)
    amount_received = models.FloatField(verbose_name='Valor recebido')
    due_date = models.DateField(verbose_name='Data de vencimento', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Status', max_length=2,  choices=StatusChoices.choices,
                              default=StatusChoices.PENDING,)

    class Meta:
        verbose_name = 'Conta a Receber'
        verbose_name_plural = 'Contas a Receber'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['due_date']),
        ]
    
    def __str__(self):
        return self.title
    
    @property
    def get_total_amount_received(self):
        total = AccountsReceivable.objects.aggregate(total_received=Sum('amount_received'))['total_received']
        return total if total is not None else 0
    

class AccountsPayable(Base):
    owner = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Título', max_length=200)
    description = models.CharField(verbose_name='Descrição', max_length=200)
    amount_paid = models.FloatField(verbose_name='Valor pago')
    due_date = models.DateField(verbose_name='Data de vencimento', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Status', max_length=2,  choices=StatusChoices.choices,
                              default=StatusChoices.PENDING,)
    
    class Meta:
        verbose_name = 'Conta a Pagar'
        verbose_name_plural = 'Contas a Pagar'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['due_date']),
        ]
    
    def __str__(self):
        return self.title
    
    @property
    def get_total_amount_paid(self):
        total = AccountsPayable.objects.aggregate(total_paid=Sum('amount_paid'))['total_paid']
        return total if total is not None else 0
