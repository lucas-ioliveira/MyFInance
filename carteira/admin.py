from django.contrib import admin
from carteira.models import Category, AccountsReceivable, AccountsPayable


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title', 'is_active')


@admin.register(AccountsReceivable)
class AccountsReceivableAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'amount_received', 'due_date', 'category', 'status')
    list_display_links = ('title',)
    search_fields = ('title', 'status')
    exclude = ('owner', 'is_active')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)
    
    def save_model(self, request, obj, form, change):
        if not change:  
            obj.owner = request.user
        super().save_model(request, obj, form, change)


@admin.register(AccountsPayable)
class AccountsPayableAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'amount_paid', 'due_date', 'category', 'status')
    list_display_links = ('title',)
    search_fields = ('title', 'status')
    exclude = ('owner', 'is_active')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)
    
    def save_model(self, request, obj, form, change):
        if not change:  
            obj.owner = request.user
        super().save_model(request, obj, form, change)
