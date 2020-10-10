from django.urls import path
from product.views import createBrand,brandEdit,brandDelete,createMobile,index,mobileView,order,mobileEdit,mobileDelete,viewOrders,orderDetails,register,loginPage,logOutPage

urlpatterns = [
    path('createbrand/', createBrand, name="brandcreate"),
    path('brandedit/<int:pk>', brandEdit, name="editbrand"),
    path('branddelete/<int:pk>',brandDelete,name="deletebrand"),
    path('createmobile/',createMobile,name="mobilecreate"),
    path('editmobile/<int:pk>',mobileEdit,name="mobileedit"),
    path('mobileview/<int:pk>', mobileView, name="mobileview"),
    path('mobiledelete/<int:pk>',mobileDelete,name="mobiledelete"),
    path('index',index,name="index"),
    path('order/<int:pk>',order,name="order"),
    path('vieworders/',viewOrders,name='viewoders'),
    path('orderdetail/<int:pk>',orderDetails,name="orderdetail"),
    path('register',register,name="register"),
    path('logoutpage',logOutPage,name="logoutpage")

]