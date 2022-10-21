from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import HomePageView
from apps.product.urls import product_patterns
from apps.supplier.urls import supplier_patterns
from apps.product_input.urls import product_input_patterns
from apps.product_output.urls import product_output_patterns
from apps.product_loan.urls import product_loan_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('', include(supplier_patterns)),
    path('product/', include(product_patterns)),
    path('input/', include(product_input_patterns)),
    path('output/', include(product_output_patterns)),
    path('loan/', include(product_loan_patterns)),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

