from django.contrib import admin
from carteira.models import Category, AccountsReceivable, AccountsPayable
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title', 'is_active')


class AccountsReceivableResources(resources.ModelResource):
    class Meta:
        model = AccountsReceivable


@admin.register(AccountsReceivable)
class AccountsReceivableAdmin(ImportExportActionModelAdmin):
    resource_classes = [AccountsReceivableResources]
    list_display = ('title', 'description', 'amount_received', 'date_receipt')
    list_display_links = ('title',)
    search_fields = list_display_links
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


class AccountsPayableResources(resources.ModelResource):
    class Meta:
        model = AccountsPayable

@admin.register(AccountsPayable)
class AccountsPayableAdmin(ImportExportActionModelAdmin):
    resource_classes = [AccountsPayableResources]
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
